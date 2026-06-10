#!/usr/bin/env python3
"""Reproducible EPR calculations for the AI capital pressure paper (v3.1).

Every number in the paper's quantitative spine is computed here from
data/inputs.json, so internal inconsistencies (mismatched table sums,
asymmetric rounding) get caught mechanically instead of by readers.

Run: python3 epr.py
"""
import json
from pathlib import Path

I = json.loads((Path(__file__).parent / "data" / "inputs.json").read_text())


def fmt(x, nd=2):
    return f"{x:.{nd}f}"


def section(title):
    print(f"\n=== {title} ===")


core = I["core"]
K = core["K_trillion"] * 1000  # $B
dep = K * core["blended_depreciation_rate"]
opex = K * core["opex_over_K"]
interest = K * core["debt_rate"] * core["debt_share"]
P = dep + opex + interest

section("P (annual capital service pressure, $B)")
print(f"depreciation {dep:.0f} + opex {opex:.0f} + interest {interest:.1f} = P {P:.0f}")
assert abs(P - 364) < 2, P

section("R_T bottom-up ($B)")
strict_items = I["r_t_strict_billion"]
wide_items = I["r_t_wide_billion"]
strict_sum = sum(strict_items.values())
wide_sum = sum(wide_items.values())
R_strict = round(strict_sum / 5) * 5   # symmetric rounding to nearest 5
R_wide = round(wide_sum / 5) * 5
print(f"strict sum {strict_sum} -> R_T strict {R_strict}")
print(f"wide   sum {wide_sum} -> R_T wide {R_wide}")
assert R_strict == 130 and R_wide == 220, (R_strict, R_wide)

section("EPR")
epr_wide = P / R_wide
epr_strict = P / R_strict
mid = (epr_wide * epr_strict) ** 0.5
print(f"EPR wide {epr_wide:.2f}x | strict {epr_strict:.2f}x | geometric mid {mid:.2f}x")
ttm = I["r_t_ttm_wide_billion"]
print(f"EPR on TTM wide R_T (${ttm}B): {P/ttm:.2f}x  (R_T above is point-in-time run-rate)")

section("Required revenue at terminal gross margin")
R_req = P / core["terminal_gross_margin"]
print(f"R_req {R_req:.0f} | gap wide {R_req - R_wide:.0f} | gap strict {R_req - R_strict:.0f}")

section("Construction-in-progress sensitivity")
lo, hi = core["cip_share_of_K"]
print(f"if CIP ({lo:.0%}-{hi:.0%} of K) accrues no depreciation: "
      f"D&A falls {dep*lo:.0f}-{dep*hi:.0f} -> EPR wide "
      f"{(P-dep*hi)/R_wide:.2f}-{(P-dep*lo)/R_wide:.2f}x")

section("2026 Big-5 capex ($B)")
cx = I["capex_2026_billion"]
big5_lo = sum(v[0] for k, v in cx.items() if isinstance(v, list) and k != "neocloud")
big5_hi = sum(v[1] for k, v in cx.items() if isinstance(v, list) and k != "neocloud")
ai_share = cx["ai_share_of_hyperscaler"]
ai_lo, ai_hi = big5_lo * ai_share, big5_hi * ai_share
print(f"Big-5 total {big5_lo}-{big5_hi} | AI share ~{ai_share:.0%} -> {ai_lo:.0f}-{ai_hi:.0f}")
gdp = I["us_gdp_trillion"] * 1000
industry_ai = (ai_lo + ai_hi) / 2 + sum(cx["neocloud"]) / 2
print(f"AI capex / US GDP: Big-5 {((ai_lo+ai_hi)/2)/gdp:.1%} | industry ~{industry_ai/gdp:.1%}")

section("Sensitivity grid (P=base unless noted, denominator = wide R_T)")
s = I["sensitivity"]
for r in s["r_t_levels"]:
    print(f"R_T -> {r}: EPR {P/r:.2f}x")
for k_t in s["k_levels_trillion"]:
    P_k = P * (k_t * 1000 / K)
    print(f"K -> {k_t}T: P {P_k:.0f} (+{P_k-P:.0f}) EPR {P_k/R_wide:.2f}x")
print(f"GPU life 4->3y: EPR {(P+s['gpu_life_extra_dep_billion'])/R_wide:.2f}x")
print(f"o 10->15%: EPR {(P+s['opex_15pct_extra_billion'])/R_wide:.2f}x")
print(f"WACC 8% replacing r*d: EPR {(P+s['wacc_extra_billion'])/R_wide:.2f}x")

section("Time path (capex $600B/yr, dep at blended rate)")
tp = I["time_path"]
k_path = [K]
for _ in tp["years"][1:]:
    k_next = k_path[-1] + tp["annual_capex_billion"] - k_path[-1] * core["blended_depreciation_rate"]
    k_path.append(k_next)
print("year  K($T)  P($B) | " + " | ".join(f"R@{int(c*100)}% -> EPR" for c in tp["cagr_scenarios"]))
for i, yr in enumerate(tp["years"]):
    k_b = k_path[i]
    p_b = k_b * (P / K)
    cells = []
    for c in tp["cagr_scenarios"]:
        r = tp["r_t_start_billion"] * (1 + c) ** i
        cells.append(f"{r:7.0f} -> {p_b/r:.2f}x")
    print(f"{yr}  {k_b/1000:.1f}  {p_b:5.0f} | " + " | ".join(cells))
print(f"steady-state K = 600 x {core['L_years']} = {600*core['L_years']/1000:.2f}T")

section("Historical: UK railways 1846 (per-assumption)")
uk = I["historical"]["uk_rail_1846"]
Kr = uk["K_committed_mGBP"]
dep_r = Kr / uk["L_years"]
int_lo = Kr * uk["debt_share"] * uk["debt_rate"][0]
int_hi = Kr * uk["debt_share"] * uk["debt_rate"][1]
rev_lo, rev_hi = uk["revenue_mGBP"]
ou_lo, ou_hi = [Kr * x for x in uk["opex_uniform_over_K"]]
P_u_lo, P_u_hi = dep_r + ou_lo + int_lo, dep_r + ou_hi + int_hi
print(f"uniform o (paper's AI-like 10-15% of K): P {P_u_lo:.0f}-{P_u_hi:.0f} -> "
      f"EPR {P_u_lo/rev_hi:.1f}-{P_u_hi/rev_lo:.1f}x")
oc_lo = rev_lo * uk["operating_ratio_calibrated"][0]
oc_hi = rev_hi * uk["operating_ratio_calibrated"][1]
P_c_lo, P_c_hi = dep_r + oc_lo + int_lo, dep_r + oc_hi + int_hi
print(f"calibrated o (operating ratio 45-55% of revenue = {oc_lo:.1f}-{oc_hi:.1f}M "
      f"= {oc_lo/Kr:.1%}-{oc_hi/Kr:.1%} of K): P {P_c_lo:.0f}-{P_c_hi:.0f} -> "
      f"EPR {P_c_lo/rev_hi:.1f}-{P_c_hi/rev_lo:.1f}x")

section("Historical: US railroads 1873")
us = I["historical"]["us_rail_1873"]
Ku = us["K_busd"] * 1000
dep_u = Ku / us["L_years"]
int_u = Ku * us["debt_share"] * us["debt_rate"]
rev_u = us["revenue_busd"] * 1000
P_uni = dep_u + Ku * us["opex_uniform_over_K"] + int_u
P_cal = dep_u + rev_u * us["operating_ratio_calibrated"] + int_u
print(f"uniform o 15%: P {P_uni:.0f} -> EPR {P_uni/rev_u:.2f}x")
print(f"calibrated (op ratio 65%): P {P_cal:.0f} -> EPR {P_cal/rev_u:.2f}x")

print("\nAll assertions passed — paper numbers are reproducible from data/inputs.json")
