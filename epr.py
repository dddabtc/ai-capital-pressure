#!/usr/bin/env python3
"""Reproducible EPR calculations for the AI capital pressure paper (v3.2).

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
assert abs(P - 364.65) < 0.01, P

section("R_T bottom-up ($B)")
strict_items = I["r_t_strict_billion"]
wide_items = I["r_t_wide_billion"]
strict_sum = sum(strict_items.values())
wide_sum = sum(wide_items.values())
R_strict = round(strict_sum / 5) * 5   # symmetric rounding to nearest 5
R_wide = round(wide_sum / 5) * 5
print(f"strict sum {strict_sum} -> R_T strict {R_strict}")
print(f"wide   sum {wide_sum} -> R_T wide {R_wide}")
assert R_strict == 165 and R_wide == 270, (R_strict, R_wide)

section("EPR")
epr_wide = P / R_wide
epr_strict = P / R_strict
mid = (epr_wide * epr_strict) ** 0.5
print(f"EPR wide {epr_wide:.2f}x | strict {epr_strict:.2f}x | geometric mid {mid:.2f}x")
ttm = I["r_t_ttm_wide_billion"]
print(f"EPR on TTM wide R_T (${ttm}B): {P/ttm:.2f}x  (R_T mixes disclosed annualization bases; see notes)")

section("Capital date alignment: actual Q3 flows only ($B)")
kr = I["k_rollforward"]
cash_q3 = sum(kr["cash_ppe_q3_billion"].values())
reported_q3 = sum(kr["company_reported_capex_q3_billion"].values())
ai_q3 = cash_q3 * I["capex_2026_billion"]["ai_share_of_hyperscaler"]
quarter_dep = core["blended_depreciation_rate"] / 4
assert abs(cash_q3 - 201.923) < 0.000001, cash_q3
assert abs(ai_q3 - 151.44225) < 0.000001, ai_q3
assert abs(reported_q3 - 207.384) < 0.000001, reported_q3
assert kr["base_as_of"] is None and kr["aligned_k_trillion"] is None
print(f"Q3 actual cash PP&E subtotal {cash_q3:.3f}; AI at assumed 75% {ai_q3:.5f}")
print(f"Company-reported Q3 capex subtotal {reported_q3:.3f}; lease definitions and Amazon netting differ, not used as new asset additions.")
print(f"Partial roll identity: K_0930 = {1-quarter_dep:.3f} * K_0630 + {ai_q3:.5f} + unmeasured net additions ($B).")
print(f"Annual P = {P/K:.4f} * K_0930; EPR strict = P/{R_strict}; wide = P/{R_wide}; mid = sqrt(strict*wide).")
print("Aligned 2026-09-30 K/P/EPR: unavailable; base measurement date is not established.")
print("Oracle June-August is unmatched; neocloud/other flows and noncash asset additions are incomplete. No guidance substituted for actuals.")

section("Required revenue at terminal gross margin")
R_req = P / core["terminal_gross_margin"]
print(f"R_req {R_req:.0f} | gap wide {R_req - R_wide:.0f} | gap strict {R_req - R_strict:.0f}")

section("Construction-in-progress sensitivity")
lo, hi = core["cip_share_of_K"]
print(f"if CIP ({lo:.0%}-{hi:.0%} of K) accrues no depreciation: "
      f"D&A falls {dep*lo:.0f}-{dep*hi:.0f} -> EPR wide "
      f"{(P-dep*hi)/R_wide:.2f}-{(P-dep*lo)/R_wide:.2f}x")

section("Annual capex guidance ($B; Oracle FY27, other Big-5 CY2026)")
cx = I["capex_2026_billion"]
big5 = [cx[k] for k in ("microsoft", "alphabet", "amazon", "meta", "oracle")]
big5_lo = sum(v[0] for v in big5)
big5_hi = sum(v[1] for v in big5)
assert (big5_lo, big5_hi) == (810, 835), (big5_lo, big5_hi)
ai_share = cx["ai_share_of_hyperscaler"]
ai_lo, ai_hi = big5_lo * ai_share, big5_hi * ai_share
print(f"Big-5 total {big5_lo}-{big5_hi} | assumed AI share {ai_share:.0%} -> {ai_lo:.1f}-{ai_hi:.2f}")
nc = cx["neocloud"]
nc_lo = nc["coreweave"][0] + nc["nebius"][0]
nc_hi = nc["coreweave"][1] + nc["nebius"][1]
assert (nc_lo, nc_hi) == (57, 64), (nc_lo, nc_hi)
print(f"CoreWeave {nc['coreweave']} + Nebius {nc['nebius']} -> listed neocloud guidance {nc_lo}-{nc_hi}")
print("Oracle and Nebius annual amounts remain supplementary third-party transcripts, not primary-verified guidance.")
gdp = I["us_gdp_trillion"] * 1000
industry_ai = (ai_lo + ai_hi + nc_lo + nc_hi) / 2
assert abs(industry_ai - 677.375) < 1e-9
assert round(industry_ai / gdp * 100, 1) == 2.1
print(f"Annual-guidance scale / US GDP (${gdp/1000:.6f}T SAAR): Big-5 AI {((ai_lo+ai_hi)/2)/gdp:.1%} | plus listed neocloud {industry_ai/gdp:.1%}")
print("Mixed periods and definitions; not US domestic investment or a complete industry total.")
sp = I["disclosed_billion"]["spacex"]
print(f"SpaceX SI: Q3 actual capex {sp['si_capex_q3']:.3f}; 9M actual {sp['si_capex_9m']:.3f}; full-year AI guidance not separately disclosed.")
print(f"IREN: remaining FY27 capex {I['disclosed_billion']['iren']['remaining_fy2027_capex']}; CY2026 capex not verified. Other neocloud estimate: unavailable, not counted.")

section("Latest company disclosures ($B; not additional terminal revenue)")
d = I["disclosed_billion"]
an = d["anthropic"]
an_q = [an[f"gaap_2026_q{x}"] for x in (1, 2, 3)]
print(f"Anthropic GAAP Q1/Q2/Q3: {an_q}; 9M {sum(an_q):.3f}; TTM {sum(an_q)+an['gaap_2025_q4']:.3f}")
an_annualized = round(an["gaap_2026_q3"] * 4, 1)
assert an_annualized == strict_items["anthropic_q3_gaap_annualized"] == wide_items["anthropic_q3_gaap_annualized"]
print(f"Anthropic Q3 GAAP annualized {an_annualized:.1f}; not company-defined Run-Rate Revenue; commitments/annualization {an['committed_spend']/an_annualized:.1f}x")
print(f"Anthropic marketplace share {an['marketplace_share_2026_9m']:.0%}; sales recognized gross, not added again in strict Bedrock/Vertex.")
print(f"Anthropic commitments {an['committed_spend']}; due next 12M {an['commitments_due_next_12m']}")
sp = d["spacex"]
print(f"SpaceX SI Q3 revenue {sp['si_revenue_q3']:.3f}; solutions/infrastructure {sp['si_solutions_infrastructure_revenue_q3']:.3f}; pure terminal AI run-rate not separately disclosed.")
orcl = d["oracle"]
print(f"Oracle FY27 Q1 capex {orcl['capex_quarter']:.3f}; net cash capex {orcl['net_cash_capex_quarter']:.3f}; RPO {orcl['rpo']}; OCI revenue {orcl['oci_revenue_quarter']}")
ytd = orcl['historical_cash_capex_ytd']
quarters = orcl['historical_cash_capex_quarters']
for quarter, derived in (
    ('fy2024_q3', ytd['fy2024_9m'] - ytd['fy2024_h1']),
    ('fy2024_q4', ytd['fy2024_full_year'] - ytd['fy2024_9m']),
    ('fy2025_q1', ytd['fy2025_q1']),
    ('fy2025_q2', ytd['fy2025_h1'] - ytd['fy2025_q1']),
    ('fy2025_q3', ytd['fy2025_9m'] - ytd['fy2025_h1']),
    ('fy2025_q4', ytd['fy2025_full_year'] - ytd['fy2025_9m']),
    ('fy2026_q1', ytd['fy2026_q1']),
    ('fy2026_q2', ytd['fy2026_h1'] - ytd['fy2026_q1']),
):
    assert abs(quarters[quarter] - derived) < 1e-9, quarter
near_2024 = sum(quarters[q] for q in ('fy2024_q3', 'fy2024_q4', 'fy2025_q1', 'fy2025_q2'))
near_2025 = sum(quarters[q] for q in ('fy2025_q3', 'fy2025_q4', 'fy2026_q1', 'fy2026_q2'))
assert abs(near_2024 - orcl['capex_near_calendar_2024']) < 1e-9
assert abs(near_2025 - orcl['capex_near_calendar_2025']) < 1e-9
ms = d['microsoft']
ms_ytd = ms['historical_cash_capex_ytd']
ms_quarters = ms['historical_cash_capex_quarters']
for quarter, derived in (
    ('cy2024_q1', ms_ytd['fy2024_9m'] - ms_ytd['fy2024_h1']),
    ('cy2024_q2', ms_ytd['fy2024_full_year'] - ms_ytd['fy2024_9m']),
    ('cy2024_q3', ms_ytd['fy2025_q1']),
    ('cy2024_q4', ms_ytd['fy2025_h1'] - ms_ytd['fy2025_q1']),
    ('cy2025_q1', ms_ytd['fy2025_9m'] - ms_ytd['fy2025_h1']),
    ('cy2025_q2', ms_ytd['fy2025_full_year'] - ms_ytd['fy2025_9m']),
    ('cy2025_q3', ms_ytd['fy2026_q1']),
    ('cy2025_q4', ms_ytd['fy2026_h1'] - ms_ytd['fy2026_q1']),
):
    assert abs(ms_quarters[quarter] - derived) < 1e-9, quarter
for year in (2024, 2025):
    assert abs(sum(ms_quarters[f'cy{year}_q{q}'] for q in range(1, 5)) - ms[f'capex_calendar_{year}']) < 1e-9
historical_big5_2024 = sum(d[n]['capex_calendar_2024'] for n in ('microsoft', 'alphabet', 'amazon', 'meta')) + near_2024
historical_big5_2025 = sum(d[n]['capex_calendar_2025'] for n in ('microsoft', 'alphabet', 'amazon', 'meta')) + near_2025
assert abs(historical_big5_2024 - 239.087) < 1e-9
assert abs(historical_big5_2025 - 411.528) < 1e-9
print(f"Oracle near-calendar cash capex: 2024 {near_2024:.3f}; 2025 {near_2025:.3f}; both shifted one month earlier.")
print(f"Historical Big-5 cash-purchase totals: 2024 {historical_big5_2024:.3f}; 2025 {historical_big5_2025:.3f}; Oracle shifted one month, other four calendar-year actuals.")
cw = d["coreweave"]
print(f"CoreWeave Q3 revenue {cw['revenue_quarter']:.3f}; 9M revenue {cw['revenue_ytd']:.3f}; backlog {cw['backlog']}; RPO approximately {cw['remaining_performance_obligations_approx']}; backlog/quarter revenue {cw['backlog']/cw['revenue_quarter']:.1f}x; backlog/FY26 revenue-guidance midpoint {cw['backlog']/(sum(cw['revenue_guidance_2026'])/2):.1f}x")
assert cw['capex_2026'] == nc['coreweave'] == [37, 39]
assert cw['capex_guidance_q4_2026'] is None and cw['revenue_guidance_q4_2026'] is None
assert abs(cw['backlog'] - cw['remaining_performance_obligations_approx'] - cw['backlog_other_estimated_future_revenue_approx']) < 1e-9
for period in ('quarter', 'ytd'):
    assert abs(cw[f'reported_capex_{period}'] - cw[f'gross_ppe_increase_{period}'] + cw[f'construction_in_progress_change_{period}']) < 1e-9
assert abs(cw['total_debt'] - sum(cw['debt_components'].values())) < 1e-9
lease_leverage = (cw['total_debt'] + cw['finance_lease_liabilities'] + cw['operating_lease_liabilities']) / (cw['revenue_quarter'] * 4)
assert round(lease_leverage, 1) == cw['debt_including_leases_to_annualized_quarter_revenue'] == 4.5
print(f"CoreWeave company-defined capex Q3 {cw['reported_capex_quarter']:.3f}; 9M {cw['reported_capex_ytd']:.3f}; lease-inclusive debt / annualized-quarter revenue {lease_leverage:.1f}x. Cash purchases are separate.")
nb = d["nebius"]
print(f"Nebius Q2 revenue {nb['revenue_quarter']}; AI cloud {nb['ai_cloud_revenue_quarter']}; customer commitments >{nb['customer_commitments_lower_bound']} (not comparable backlog)")
ir = d["iren"]
print(f"IREN FY27 Q1 revenue {ir['revenue_quarter']:.3f}; AI cloud {ir['ai_cloud_revenue_quarter']:.3f}; backlog {ir['backlog']}")

section("Oracle and neocloud cash spending / balance-sheet checks ($B)")
assert orcl['annual_guidance_primary_verified'] is False
assert nb['annual_guidance_primary_verified'] is False
assert cw['annual_guidance_primary_verified'] is True
assert cw['latest_results_date'] == '2026-11-10' and cw['next_results_date'] is None
assert nb['next_results_date'] == '2026-11-12'
assert abs(orcl['operating_cash_flow_quarter'] - orcl['capex_quarter']
           - orcl['free_cash_flow_quarter']) < 1e-9
assert abs(orcl['capex_quarter'] - orcl['short_term_capex_financing_net_cash_flow']
           - orcl['customer_prepayments_with_financing_component_quarter']
           - orcl['net_cash_capex_quarter']) < 1e-9
assert abs(ir['capex_quarter'] - (2.131 + 2.693)) < 1e-9
for name in ('alphabet', 'amazon', 'meta', 'spacex', 'anthropic', 'coreweave', 'cipher_digital', 'terawulf', 'core_scientific', 'hut8'):
    row = d[name]
    assert abs(row['capex_quarter'] - (row['capex_ytd'] - row['capex_h1'])) < 1e-9, name
assert abs(d['nvidia']['capex_quarter'] - (d['nvidia']['capex_ytd'] - d['nvidia']['capex_fy_q1'])) < 1e-9
for name in ('microsoft', 'alphabet', 'amazon', 'meta', 'nvidia', 'spacex', 'anthropic', 'openai', 'oracle', 'coreweave', 'nebius', 'iren', *d['other_neocloud']['members']):
    row = d[name]
    print(f"{name}: {row['period']}; cash capex Q {row['capex_quarter']}, "
          f"YTD {row['capex_ytd']}; PP&E net {row['ppe_net']}; debt {row['total_debt']}; finance leases {row['finance_lease_liabilities']}")
    if row['capex_quarter'] is not None and row['capex_ytd'] is not None:
        assert 0 <= row['capex_quarter'] <= row['capex_ytd'], name
assert d['galaxy_digital']['capex_quarter'] is None
assert d['nscale']['revenue_quarter'] is None
for name in ('microsoft', 'alphabet', 'meta'):
    row = d[name]
    assert abs(row['total_debt'] - row['debt_current'] - row['debt_noncurrent']) < 1e-9, name
amzn = d['amazon']
assert abs(amzn['total_debt'] - amzn['debt_current'] - amzn['debt_noncurrent'] - amzn['other_short_term_borrowings']) < 1e-9
for period in ('quarter', 'ytd'):
    assert abs(amzn[f'reported_capex_{period}'] - amzn[f'capex_{period}'] + amzn[f'ppe_disposal_proceeds_and_incentives_{period}']) < 1e-9
    assert abs(d['meta'][f'reported_capex_{period}'] - d['meta'][f'capex_{period}'] - d['meta'][f'finance_lease_principal_payments_{period}']) < 1e-9
assert abs(d['iren']['total_debt'] + d['iren']['finance_lease_liabilities'] - d['iren']['company_reported_debt_including_finance_leases']) < 1e-9
print("Cash-spending identities passed. Periods, noncash assets, project announcements and order definitions remain separate.")
for name in ('microsoft', 'alphabet', 'amazon', 'meta', 'oracle'):
    row = d[name]
    print(f"{name}: latest-quarter cash purchases / revenue {100 * row['capex_quarter'] / row['revenue_quarter']:.2f}%")

nv = d["nvidia"]
print(f"NVIDIA FY27 Q2 revenue {nv['revenue_quarter']}; DC {nv['data_center_revenue_quarter']}; Q3 guidance {nv['revenue_guidance_next_quarter']}; supply/capacity commitments {nv['supply_capacity_commitments']}")

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

section("Time path (legacy illustrative capex $600B/yr, dep at blended rate)")
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

print("\nAll assertions passed - paper numbers are reproducible from data/inputs.json")
