Languages: [English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)
PDF: [English](ai-capital-pressure-v3.en.pdf) | [简体中文](ai-capital-pressure-v3.zh-CN.pdf) | [日本語](ai-capital-pressure-v3.ja.pdf)
(PDFs are v3 archives; v3.1 and v3.2 revisions are in Markdown.)

# AI Capital Pressure

With the old capital-stock assumption held fixed, updated revenue lowers the calculated annual capital pressure relative to revenue. It remains above the mature-industry benchmarks. Revenue disclosure has improved, but the capital stock has not been remeasured, so this does not establish a fall in actual industry-wide pressure.

Cross-industry and historical comparison; dda, 2026-11-09, v3.2. Research stress test, not investment advice. B=billion USD; T=trillion USD.

## Data verification and version notes

v3.2 (2026-11-09): updates the available official/reported Anthropic and OpenAI revenues, four cloud companies’ calendar-year capex guidance, Oracle FY27 guidance, GDP and latest company results. Adds SpaceX’s consolidation of xAI and company-level CoreWeave, Nebius and IREN disclosures. Anthropic recognizes marketplace sales gross; the unverified residual Bedrock/Vertex amount is excluded from strict revenue. The old model-company total cannot be split to isolate xAI, so it is not counted; no allocation is invented. Wide/strict EPR changes from 1.66x/2.81x to 1.40x/2.70x; the geometric midpoint falls from 2.16x to 1.95x, within the shale-oil reference range. The conditional result remains above normal-industry benchmarks. K remains an old assumption. See the source ledger for unverified items. The method and existing scenario parameters are unchanged, apart from the revenue starting point.

**v3.1 (2026-06-10) revision note**: After external review, five measurement-basis issues were corrected; all numbers can be recomputed from repo `epr.py` + `data/inputs.json` (the script includes consistency assertions). (1) Strict R_T now uses Anthropic's official $30B ($40B reported figure only enters the wide basis), deducts application-layer resale paid to model APIs (about $6-8B), and removes the previous $147B→$160B upward rounding: strict EPR is revised from 2.28x to 2.81x; wide basis after the same resale deduction is 1.66x. (2) Historical cases add opex-calibration sensitivity: after calibrating 1846 UK railways to the period operating ratio (45-55%), EPR is only about 1.0-1.9x, so "AI below the 1846 peak" is no longer a headline conclusion. (3) Big-5 2026 capex is unified at $755-805B (consistent with the §3.2 company table). (4) R_T is explicitly a point-in-time run-rate, with a TTM reference basis (about 2.6x). (5) The sensitivity table adds a "construction in progress not depreciated" row. The direction of the central conclusion is unchanged; the magnitude changes are below.

The review cutoff is 2026-11-09, not a common measurement date for every input. The [source ledger](data/sources_2026-11.md) lists old/new values, sources, publication dates and reasons for retaining inputs. Strict/wide retain the paper’s basket names; both still contain labelled legacy estimates and are not audited industry statistics.

| Item | This edition | Source and period |
|---|---|---|
| Anthropic | Official run-rate >47; reported >65 | [Company](https://www.anthropic.com/news/series-h) (2026-05-28); [Reuters](https://www.investing.com/news/stock-market-news/anthropic-revenue-run-rate-tops-65-billion-source-says-4864031) (2026-08-17) |
| OpenAI | Official monthly ~2, times 12=24; reported almost 50 | [Company](https://openai.com/index/accelerating-the-next-phase-ai/) (2026-03-31); [Reuters](https://www.investing.com/news/stock-market-news/openais-annualized-revenue-20-billion-less-than-previously-signaled-ft-reports-4939854) (2026-10-08, updated 10-09) |
| Microsoft AI | Official 37 (older); net 27/30 remains an unupdated estimate | [FY26 Q3](https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3) (2026-04-29) |
| NVIDIA | FY27 Q2 revenue 96.2, DC 89.0; Q3 guidance 108±2% | [IR](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx) (2026-08-26) |
| CoreWeave | Q2 revenue 2.575, backlog 104.2; 2026 capex 35–39 | [IR](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/default.aspx) (2026-08-11); [Outlook](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf) (2026-08-11) |
| US GDP | 2026Q3 nominal SAAR 33.010036T | [BEA](https://apps.bea.gov/national/Release/XLS/Survey/Section1All_xls.xlsx) (2026-10-29) |

NVIDIA’s latest released quarter is FY27 Q2. Its official FY27 Q3 release is scheduled for 2026-11-17, after the cutoff; no Q3 actuals are used. [IR](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/) (2026-10-28)

## Central conclusion

EPR divides annual depreciation, cash operating costs and interest by estimated terminal revenue to measure capital-service pressure. Holding the old K=$1.3T and other assumptions fixed gives 1.40x wide, 2.70x strict and a geometric midpoint of 1.95x. The unchanged normal-industry range is 0.65–0.95x; the midpoint is about 2.4 times its representative 0.80x value.

The midpoint falls from 2.16x to 1.95x, entering the 2014 shale-oil range of 1.5–2x; the old claim that it is above that range no longer applies. It remains above the 1873 aggregate rail estimate of 1.08–1.21x and below the approximately 3x new-build telecom estimate for 2000. No stable ranking against 1846 rail is made: its opex assumptions produce 1.8–3.6x or 1.0–1.9x. Strict EPR of 2.70x remains within the paper’s 2.0–4.0x high-pressure band; the midpoint’s ranking does not describe the whole range.

This edition cannot update the industry’s deployed capital stock or establish a complete comparable terminal-revenue census. The result is a stress test under the old K, not evidence that actual risk has improved. Higher capex guidance or quarterly spending cannot be treated directly as current K. Housing and Japanese asset-price bubbles have different mechanisms; EPR does not rank every type of bubble.

## **1. EPR Framework: What it is and what it is not**

## **1.1 Definition**

P = K/L + o × K + r × d × K

EPR_cash = P/R_T

Among them, K = deployed capital stock, L = weighted average economic life, o = cash operation and maintenance / K, r = average debt financing interest rate, d = debt financing proportion, R_T = verifiable terminal revenue. 

## **1.2 Framework traceability (not a new invention)**

Strictly speaking, EPR is not a new metric. It is essentially a combination of several existing concepts:

- Economic level: Jorgenson (1963) Capital Service Cost Theory. Capital service price c = (i + δ - π) × p_K, where δ is the economic depreciation rate, i is the interest rate, and π is the asset price change. This is modern productivity accounting

   - Basics of (BEA, BLS, KLEMS).

- Regulatory Economics: Utility revenue requirement formula. rate base × (depreciation rate + return on capital + O&M) = income that must be recovered. Standard practice in regulating ROE models for 60+ years. 

- Real estate valuation: The reciprocal of cap rate (NOI / property value) is a similar indicator, 1930s already exists. 

- Enterprise valuation: Equivalent to "implied required revenue to justify capex" analysis, which Damodaran and others have repeatedly used in the hyperscaler AI business. 

The contribution of this article does not lie in the framework itself, but in applying it to the AI ​​cycle + making a horizontal comparison with the current normal industry + with the four major infrastructure cycles in history. EPR is a convenient nomenclature adopted for the discussion in this article. 

## **1.3 What is EPR**

- EPR is capital service pressure ratio. Compress the capital-related costs (depreciation + cash operation and maintenance + interest) that the industry must absorb from terminal revenue every year into a single number. 

- EPR is more information dense than Debt/Revenue or Capex/Revenue because it also incorporates existing capital pressure, operating pressure and financing costs. 

- EPR can be used for cross-industry and cross-period comparisons within the same framework (although differences in historical accounting standards are inevitable). 

## **1.4 What EPR is not**

- EPR is not a traditional leverage ratio. It is not Debt/Equity, Debt/EBITDA, Assets/Equity, Net Debt/Revenue. Calling EPR "leverage" will make readers mistakenly think that it measures debt risk, but many of the core risks of AI are not debt, but equity dilution, depreciation eating up profits, cloud contract renegotiation, capex deceleration leading to valuation compression, and GPU residual value revisions. 

- EPR is not a complete profit margin indicator. In this article, P only includes depreciation + opex + interest at the infrastructure layer, and does not include R&D, SG&A, sales, customer service, equity incentives, data procurement, promotion subsidies, and taxes at the model company and application layer. Real industry profit pressure is higher than the EPR suggests. 

- EPR > 1 is not directly equivalent to "the industry is not profitable". But the terminal revenue is not enough to cover the annual infrastructure pressure defined in this article. 

- EPR_cash defaults to cash interest (r × d × K), without charge equity capital opportunity cost. If WACC is used instead, the EPR increases significantly (see sensitivity analysis). 

- Historical EPR is an approximate estimate of the same frame, not a precise measurement of "the same basis". All historical EPR numbers have low-medium confidence. 

## **Interpretation interval of 1.5 EPR**

|**EPR_cash area**<br>**room**|**Interpretation**|**Typical examples**|
|---|---|---|
|< 0.6x|Low capital pressure, steady industry profitability|Consumer goods, Internet platforms, light asset services|
|0.6–1.0x|Medium capital pressure, most normal industries |Utilities, telecommunications, SaaS, automobiles, aviation|
|1.0–2.0x|High capital pressure, demand extrapolation or cycle high|Peak shale oil period, current AI wide basis, 1873U.S.<br>U.S. rail aggregation|
|2.0–4.0x|Infrastructure bubble magnitude, capitalize future needs in advance|Current AI strict basis, 2000 new telecom optical fiber section, 1840s railway (unified o basis)|
|> 4.0x|Extreme situations, usually appearing in the last stage before a crash|A few extreme cases|

## 2. Conditional AI capital-pressure test

## 2.1 Inputs

| Parameter | Value | Status |
|---|---|---|
| K | $1.3T | Carried from v3.1; not updated |
| L / blended depreciation rate | 6.1 / 16.4% | Legacy assumption |
| o / r / d | 10% / 5.5% / 30% | Legacy assumptions |
| R_T wide/strict | $260B / $135B | Components in 2.3 |
| m_T | 50% | Legacy gross-margin assumption |
| CIP share of K | 15–20% | Legacy sensitivity assumption |

The old K breakdown is hyperscalers 780–880B, neoclouds 90–130B and others 200–300B, totalling 1.07–1.31T and using the upper 1.3T. These components lack comparable November updates. Oracle appeared in both Big-5 and “other” descriptions, creating possible overlap; the old breakdown cannot establish a new stock value. K is retained only for conditional comparison.

## 2.2 Recalculated results

| Item | Formula or denominator | Result |
|---|---|---|
| Depreciation | 1300 × 16.4% | $213.2B |
| Cash opex | 1300 × 10% | $130B |
| Cash interest | 1300 × 5.5% × 30% | $21.45B |
| P | 213.2 + 130 + 21.45 | $364.65B (~$365B) |
| EPR wide | 364.65 / 260 | 1.40x |
| EPR strict | 364.65 / 135 | 2.70x |
| Geometric midpoint | sqrt(EPR_wide × EPR_strict) | 1.95x |
| R_req | P / 50% | $729B |
| Revenue gap: wide/strict | R_req − R_T | $469B / $594B |
| Old TTM-wide reference | 364.65 / 140 | 2.60x |

TTM means the trailing twelve months. Industry TTM-wide revenue of 140B is carried from v3.1, unupdated/unverified, so 2.60x is only an old reference. Anthropic’s filing supports its own TTM of 35.282B, not a revised industry TTM. Official run-rates, quarterly GAAP revenue and future guidance are kept separate.

## 2.3 Terminal-revenue components

| Category, $B | Strict | Wide | Basis |
|---|---|---|---|
| Anthropic | 47 | 65 | Official May floor / reported July floor |
| OpenAI | 24 | 50 | Official March monthly annualization / reported September approximation |
| Microsoft AI net | 27 | 30 | Carried; overlap deduction unverified |
| SpaceX/xAI terminal-only | 0 | 0 | Not separately disclosed, not counted; not zero revenue |
| Mistral/Cohere/other models | 0 | 0 | Old combined 5/8 cannot be allocated; not counted |
| Google Gemini/Workspace AI | 5 | 8 | Legacy estimate, unverified |
| AI SaaS net (including Cursor) | 9 | 12 | Legacy gross 15/20 less API resale 6/8, unverified |
| Traditional SaaS AI increment | 10 | 15 | Legacy estimate, unverified |
| China AI | 10 | 15 | Legacy estimate, unverified |
| Bedrock/Vertex net | 0 | 10 | Strict excluded; wide retains an unverified legacy estimate excluding all model resale |
| Internal AI attribution | 0 | 35 | Wide estimate, unverified |
| Consulting/productivity savings | 0 | 10 | Wide estimate, unverified |
| Long tail | 5 | 8 | Legacy estimate, unverified |
| Sum → nearest 5B | 137 → 135 | 258 → 260 | Rounding unchanged |

Anthropic’s S-1/A p161 gives Q1/Q2/Q3 revenue of 4.731/11.555/16.956B and nine-month revenue of 33.242B. Page 58 and Note 2 state that 44% of nine-month sales went through cloud marketplaces and were recognized gross. Those sales cannot be added again in Bedrock/Vertex, and 44% cannot be deducted mechanically from Microsoft’s whole AI business. The latest October-end run-rate field is blank; strict retains the official 47B floor rather than treating quarter-times-four as an exit run-rate. [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm) (2026-11-02)

xAI is consolidated into SpaceX, whose SI segment also contains ads, cloud capacity, Grok and Cursor. Terminal-only run-rate is not separately disclosed; the entire 7.560B quarterly segment revenue cannot be annualized into R_T. The old 5/8B model-company bucket cannot reliably isolate xAI, so that old bucket is not counted. New zero rows mean excluded, not no revenue. The application net estimate of 9/12B retains Cursor; SpaceX segment revenue is not added again. [10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm) (2026-10-22)

## 3. Capital stock, annual spending and commitments

K is the stock of deployed or in-construction assets; capex is asset purchases during a period; commitments are future contractual obligations or announcements. They cannot be added together. Annual capex and commitments do not directly enter this edition’s P, which still uses the old K.

## 3.1 Retaining K

There is insufficient primary data to rebuild company-level AI net assets and construction in progress. K=$1.3T is carried from v3.1 and is not described as November’s actual stock; the old ±20% is an estimate, not a statistical error bound. Added company disclosures show why the stock needs rebuilding but do not justify inventing a new K.

## 3.2 Company capex and latest quarters

| Company | Annual capex guidance, $B | Period and source |
|---|---|---|
| Microsoft | 170 | CY2026; [IR](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1) (2026-10-28) |
| Alphabet | 195–205 | CY2026; [IR](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx) (2026-10-28) |
| Amazon | 220 | CY2026; [IR](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf) (2026-10-29) |
| Meta | 135–145 | CY2026; [IR](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx) (2026-10-21) |
| Oracle | 90–95 | FY2027 (2026-06 to 2027-05); [Call transcript](https://www.roic.ai/quote/ORCL/transcripts/2027-year/1-quarter) (2026-09-10, call date) |
| Big-5 | 810–835 | Four calendar years plus one fiscal year; periods differ |
| Big-5 assumed AI portion | 607.5–626.25 | 75% × (810–835) |
| CoreWeave | 35–39 | CY2026; [IR](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf) (2026-08-11) |
| Nebius | 20–25 | CY2026; [Call transcript](https://www.fool.com/earnings/call-transcripts/2026/08/19/nebius-nbis-q2-2026-earnings-call-transcript/) (2026-08-19, call 08-12) |
| Two listed neoclouds | 55–64 | Not an industry total |
| IREN | CY2026 unverified; remaining FY27 is 15 | [IR](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results) (2026-11-05) |
| SpaceX SI | Full-year AI not separately disclosed; 9M actual 39.995 | [10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm) (2026-10-22) |
| Other (estimate): Lambda, Crusoe, etc. | Amount unverified; no estimate invented or counted | Financing/project announcements are not annual capex |

Oracle and Nebius annual guidance uses public transcriptions of management’s earnings-call words; the audio was not replay-checked. This limitation is retained in the ledger. The old neocloud 60–70B lacks a company-level allocation: it cannot be added on top of CoreWeave and Nebius or turned into an invented residual for other companies. SpaceX and IREN partial-period amounts do not enter the annual-guidance sum.

| Company/quarter | Latest quarterly revenue, $B | Backlog or RPO, $B | Additional disclosure |
|---|---|---|---|
| Oracle FY27 Q1 | OCI ~7.4 | RPO 664 | Capex 28.499; net cash 17.966 |
| CoreWeave Q2 2026 | 2.575 | 104.2 | Annual revenue guidance 12.4–13.2 |
| Nebius Q2 2026 | 0.5823 (AI cloud 0.5749) | Customer commitments >40; not comparable backlog | Q2 capex ~5.7 |
| IREN FY27 Q1 | 0.228 (AI cloud 0.200) | 20.3 | Remaining fiscal-year capex 15 |
| SpaceX SI Q3 2026 | 7.560 (Solutions & Infrastructure 7.022) | No terminal-AI backlog used here | Q3 capex 16.444; 9M revenue 10.939 |

SpaceX’s Q3 10-Q Note 1 (pp10–11) confirms that xAI is wholly owned; Notes 3 (p12) and 18 (pp32–33) disclose revenue and capex. GPU purchases, data-center capex and full-year pure-AI guidance are not separately disclosed. Neocloud order metrics have different definitions and are not directly summed; their entire revenues are not added to terminal AI revenue either. [10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm) (2026-10-22); [Oracle](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx) (2026-09-10); [Nebius](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf) (2026-08-12); [IREN](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results) (2026-11-05)

Microsoft’s 170B versus its old guidance cannot directly establish a smaller project programme: lease recognition and delivery timing affect reported capex. Microsoft said FY27 second-half spending would accelerate; Alphabet said 2027 spending would increase significantly; Meta said its 2027 budget was still being developed and it intended to keep investing aggressively, without a full-year amount. Amazon’s release supplied no comparable full-year 2027 capex number, so none is entered. These are published management statements, not new forecasts by this paper. [Microsoft](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1), [Alphabet](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx), [Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx), [Amazon](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf)

SpaceX’s latest S-1/A is dated 2026-06-03. Its “AI Capital Expenditures” paragraph reports 7.723B of AI capex in 2026 Q1, driven by construction, equipment and supporting terrestrial data-center infrastructure. The final prospectus dated 2026-06-12 carries this disclosure forward. Current values here use the later Q3 10-Q rather than the pre-listing quarter. [S-1/A](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm), [424B4](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm)

## 3.3 Commitments and revenue

OpenAI’s old nominal total of 1.4T lacks a verified current comprehensive primary-source schedule. It is retained as historical context, not used to rank current risk. The old rows Oracle 300, Stargate 500 (400+ planned), AMD 90, NVIDIA up to 100, Azure 250, CoreWeave 22.4 and Broadcom 50–100B remain unupdated: their natures and terms differ and overlap, so they cannot be summed as debt or K. The AWS update is verified: an additional 100B over 8 years on top of the original 38B multi-year agreement, nominally 138B across differing terms. [OpenAI](https://openai.com/index/amazon-partnership/) (2026-02-27)

Anthropic’s S-1/A discloses 895.4B of aggregate commitments, including long-term purchases, short-term and subsequent commitments, and uncommenced leases; 69.8B is due over the following twelve months. This replaces the old 200–300+B. Old partner rows mix financing, compute capacity and analyst estimates and are not summed. Against official 47B or reported 65B run-rate revenue, the ratios are approximately 19.1x or 13.8x; the old “only 5–7.5x, relatively restrained commitments” conclusion is no longer supported. [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm) (2026-11-02)

Simply dividing OpenAI’s old 1.4T by the 24B official annualization or reported 50B gives 58.3x or 28.0x. These are conditional comparisons across different dates, not comparable current risk ratios. Multi-year commitments divided by a current revenue run-rate are not financial leverage.

## **4. Normal industry EPR benchmark (rough estimate, non-audit industry model)**

The normal industry EPR range serves as the benchmark. All figures are based on industry average estimates based on 2024-2025 public financial reports, with a medium confidence level. Warning: Industry aggregate data is rough. Company income, D&A, opex, and interest come from different companies and accounting standards, and it is impossible to have the same basis. These numbers are order of magnitude benchmarks, not exact comparisons. 

|**Industry**|**Estimated EPR_cash**|**Asset life characteristics**|**Risk characteristics**|
|---|---|---|---|
|Mature SaaS|0.69x|Short (3–5y)|Light asset, opex adjustable|
|Traditional telecommunications (post-2002)|0.76x|Medium long (10–15y)|Steady-state industries|
|Utilities (regulated)|0.80x|Long (30+y)|High debt + stable returns|
|Aviation|0.90x|Medium (15–25y)|Close to the equilibrium line|
|Automotive OEM|0.92x|Short to medium (5–10y products)|Close to balance line|

|**Industry**|**Estimated EPR_cash**|**Asset life characteristics**|**Risk characteristics**|
|---|---|---|---|
|AI (v3.2 wide basis)|1.40x|Hybrid (4–15y) |Far beyond normal baseline|
|AI (v3.2 strict basis)|2.70x|Same as above|Far beyond the normal baseline|

The unchanged representative normal-industry EPR is 0.80x. AI’s conditional EPR is about 1.8–3.4 times that value. These are approximate benchmarks, not current audited industry averages.

Mature-industry figures in this section are carried from v3.1, unupdated/not reverified, and serve only as fixed benchmarks.

## **5. Approximate estimation of historical bubbles in the same framework**

Use the same formula to construct approximate EPR estimates for four historical bubbles. All figures are based on published academic research and economic history, accounting and - statistical basis are different from modern times, confidence level is low - medium. Only for order of magnitude positioning. 

## **5.1 1844-1847 British Railmania**

background. Rail capex accounted for 7-8% of UK GDP in 1847 (Mitchell historical statistics) and twice as much as military spending. 1844-1846 Railroad stock index doubled before crashing, 1847-49 shares fell 50%+. 

|**Item**|**Estimate**|**Description**|
|---|---|---|
|Cumulative rail capital commitments1844-1847|£170M|Odlyzko estimate|
|UK GDP 1846|£550-600M|Mitchell historical statistics|
|1847<br>Railway capex/GDP|7-8%|Tandfonline (2022) Historical Research|
|Years D&A (L=30y on £170MDepartment<br>Department)|£5.7M|Long life of railway assets|
|year opex (unified basis: K<br>10-15%)|£17-25.5M|Same assumption as AI, not industry calibrated|
|year opex (calibrated basis: operating ratio 45-55%)|£4.5-8.2M|Railway working expenses in the period were about 45-55% of revenue (≈K's 2.6-4.9%)|
|Annual interest (d=60%, r=4.5-5%)|£4.6-5.1M||
|P_cash|Unified £27-36M / calibrated £15-19M||
|1846Railway operating income|£10-15M||
|Estimated EPR_cash|Unified 1.8-3.6x (median 2.5-3x) / calibrated about 1.0-1.9x|Extremely sensitive to the o assumption|

Interpretation. Under a unified opex basis, the 1840s UK rail EPR estimate is 2.5-3x; after calibrating opex to the period's actual operating ratio, it is only about 1.0-1.9x. Both basiss are shown (v3.1): the difference shows this anchor is not stable enough, and together with the asymmetry that K uses committed capital (while AI uses deployed capital), this article no longer uses "AI below the 1846 peak" as a ranking conclusion. Mechanistically it remains very similar to AI: real technology + real future demand + capital market extrapolation in advance + reflexive financing. Result: 1847 Bank of England Interest rate hikes and banking crisis trigger collapse. Railroad stocks fell 1847-1850 50-80%. But the rail network was eventually built and produced ongoing returns—investors lost money and society gained.

## **5.2 1865-1873 US Railroad Expansion**

background. 1865-1873 U.S. rail mileage doubled from 35,000 to 70,000 miles. In September 1873, the bankruptcy of Jay Cooke triggered the Panic of 1873. 1873-1879 Long Depression, 89 railroads (about 25%) went bankrupt. 

|**Item**|**Estimate**|**Description**|
|---|---|---|
|Accumulated railroad capital1865-1873|$2.7B|historical estimates|
|US GDP 1873|approximately $7B|Williamson historical|

|**Item**|**Estimate**|**Description**|
|---|---|---|
|Cumulative capex/GDP|About 38%|Extremely high|
|Year D&A (L=30y)|$90M||
|year opex (unified basis: K<br>15%)|$405M||
|year opex (calibrated basis: 1872 operating ratio ~65%)|$338M (≈K's 12.5%)||
|Annual interest (d=70%, r=7%)|$132M|High leverage and high interest rate|
|P_cash|Unified $627M / calibrated $560M||
|Annual Railway Operating Revenue1872|Approximately$520M|Census/ICC historical|
|Estimated EPR_cash (aggregated)|Approximately 1.1-1.2x|Unified 1.21x / calibrated 1.08x|

Interpretation. Overall rail EPR approximately 1.1-1.2x. Profits on old mature lines masked extreme pressure on new speculative lines. Crash Mechanism: Jay Cooke Fundraising Failure → Credit Crunch → Overall Railroad Bond Price Collapse → Bank Failures → 6 Years of Long Depression.

## **5.3 1996-2001 US Telecom Fiber Optic Foam**

background. WorldCom CEO claims that Internet traffic doubles every 100 days (actually about 2x per year). In 1996-2001, U.S. telecommunications companies issued $500B+ of new debt and laid 80M miles of optical fiber. Global Crossing 2002 Bankruptcy leaves $12.4B debt. WorldCom 2002 Bankruptcy, largest U.S. accounting fraud. 2002 Only 2.7% US fiber is "lit". 2004 Long-distance wholesale prices fell 55% year-on-year. 

|**Item**|**Estimate**|**Description**|
|---|---|---|
|Accumulated US telecom capex 1996-<br>2001|About $500B|Industry aggregation|
|Peak year capex (2000)|$120B|BEA|
|US GDP 2000|$10.25T|BEA|
|Peak capex/GDP|About 1.2%||
|Year D&A (L=15y on $500BDepartment<br>Department)|$33B||
|year opex(K<br>10-12%)|$50-60B||
|Annual interest (d=60%, r=8%)|$24B||
|P_cash|$107-117B||
|2001 IP/data terminal revenue|$30-50B|Split from total telecom revenue|
|Estimated EPR_cash<br>(IP/data new<br>segment only)|About 2.5-4x|Median 3x|
|Industry-wide (including voice steady-state) EPR|About 0.5-0.8x|Steady-state business covers the pressure of new IP|

Interpretation. Excluding steady-state voice services gives about 3x for the new IP/data segment. The comparison shows how mature revenue can mask pressure in newly built infrastructure. It does not establish healthy current cash flow at every cloud company; this edition compares capital pressure only through the conditional calculations above.

## **5.4 2005-2008 American Housing (Contrast Case)**

|**Item**|**Estimate**|**Description**|
|---|---|---|
|Home Mortgage Debt/GDP 2007|97%|FRED|
|Total value of housing stock2007Q3|Approximately$24T||
|Home Mortgage Debt2007Q3|Approx.$10T|FRED HHMSDODNS|
|Year D&A<br>(Housing2%Depreciation)|$480B||
|Annual cash opex|$700B|3% of about K<br>|
|Annual interest|$600B||
|P_cash|about$1.78T||
|Annual rental income (actual + imputed)|Approx. $1.7-2T|BEA|
|Estimated housing EPR_cash|0.9-1.1x||

Interpretation. Housing EPR is about 1.0x, not extreme. The core of the housing bubble is not in EPR, but in three different dimensions: (1) price/income ratio rising from 3x to 5x; (2) credit quality (NINJA loans, option ARM); (3) securitization deregulation and rating fraud. Important conclusions. EPR is not a be-all and end-all indicator for all bubbles. The housing bubble is a three-layer structure of "price + credit quality + securitization", and the railway/telecom/AI is a "capital front + demand extrapolation + short asset life" structure. 

## **5.5 Other historical cases (short list)**

|**Case**|**Period**|**EPR estimate**|**Main rupture mechanism**|
|---|---|---|---|
|Japanese asset bubble|1985-1990|n/a (price bubble)|The stock market fell 60%<br>, land prices fell 80%, 30 years of deflation|
|China’s steel surplus|2010-2016|About 0.5-0.7x|Price falls70%, supply-side reform and integration|
| U.S. shale oil | 2011-2016 | About 1.5-2x | Oil prices collapse 75%, ~100<br>E&Ps bankrupt<br>|
|Cryptocurrency<br>(2017/2021<br>)|2017, 2021|n/a (narrative bubble) |Bitcoin fell 80% multiple times|

Historical inputs in this section are carried from v3.1; original archives were not reverified. The two rail opex cases are recalculated by epr.py.

## 6. Updated historical position

| Reference | EPR | Interpretation |
|---|---|---|
| Normal industries | 0.65–0.95x | Old benchmark |
| 1873 US rail | 1.08–1.21x | Aggregate |
| 2014 shale oil | 1.5–2x | Midpoint 1.95x lies in this range |
| AI v3.2 wide/strict | 1.40x / 2.70x | Conditional on old K |
| 1846 UK rail | 1.8–3.6x / 1.0–1.9x | Uniform/calibrated; no stable ranking |
| 2000 new-build telecom | ~3x | Old high-pressure reference |

The updated result remains above normal industries, while its geometric midpoint is now within the shale range. Higher revenue lowers the ratio with a fixed numerator, but K is unremeasured and strict revenue still contains old estimates. This conditional improvement does not establish lower industry risk or a reduced probability of a broad collapse.

## 7. Capex and GDP

## 7.1 Scale comparison

For a scale comparison, the midpoint of the Big-5 assumed AI portion is 616.875B / US nominal GDP SAAR of 33.010036T, about 1.9%. Adding the two listed neoclouds’ guidance midpoint of 59.5B gives about 2.0%. Oracle uses a different fiscal year, 75% is a legacy AI-share assumption, and company activity is global. This is neither US domestic AI investment as a share of GDP nor a complete industry total. SpaceX’s 9M 39.995B and IREN’s remaining-fiscal-year 15B are separate and not added to this annual figure.

Goldman’s 2026-08-07 research estimates global AI investment of about 1000B, including 581B in the US, with US/GDP of 1.8% and global/GDP of 0.9%. This replaces the old 0.8% claim but remains a research estimate with a different method and geography; it is not substituted into the paper’s 75% calculation. Historical references remain the old 7–8% for 1847 rail, about 1.2% for 2000 telecom and about 6.3% for 2005–2006 housing investment, not reverified. [Goldman](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026) (2026-08-07)

## 7.2 Contribution to GDP growth

The St. Louis Fed’s 39% refers to AI-related investment categories’ share of real GDP growth over the first three quarters of 2025. Q3 alone was 11%, or 0.48 percentage points. The old single-quarter attribution and a reference to nominal growth are corrected. The study covers software, R&D, information equipment and data centers; these are not all pure AI investment. [St. Louis Fed](https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth) (2026-01-12)

Furman’s 92%, Goldman’s 1.5 percentage points and net 0.1–0.2 percentage points, the old net range of 0.1–0.5 percentage points and the 70%+ import share were not verified or updated and no longer support current conclusions. Contribution shares and percentage points are different units and cannot be described directly as differing by 100 or 1000 times. Global company capex/GDP also cannot establish US GDP growth contributions.

## 8. Sensitivity and existing time scenarios

## 8.1 One-input sensitivities

| Change | Condition | EPR wide |
|---|---|---|
| R_T → $300B | P = $364.65B | 1.22x |
| R_T → $400B | P = $364.65B | 0.91x |
| R_T → $180B | P = $364.65B | 2.03x |
| R_T → $135B | Strict baseline | 2.70x |
| K → $1.7T | P = $477B (+$112B) | 1.83x |
| K → $2.0T | P = $561B (+$196B) | 2.16x |
| GPU life 4→3 years | Legacy extra depreciation 43B | 1.57x |
| o 10% → 15% | +$65B | 1.65x |
| r×d → WACC 8% | Legacy approximate +80B, replacing r×d | 1.71x |
| No depreciation on CIP | D&A −$32–43B | 1.24–1.28x |

These are one-input assumption changes, not statistical confidence intervals. The old “90% credible interval” lacks a reproducible probability model and is not presented as an updated interval.

## 8.2 Time paths (existing scenarios; updated revenue start only)

Annual capex of 600B, blended depreciation of 16.4% and revenue CAGR of 50%/25%/10% retain the old scenarios; they are not current company guidance or new forecasts. Starting K is 1.3T and revenue is synchronized from 220B to 260B. Steady-state K=600×6.1=3.66T remains a scenario calculation.

| Year | K ($T) | P ($B) | R@50% ($B) / EPR | R@25% ($B) / EPR | R@10% ($B) / EPR |
|---|---|---|---|---|---|
| 2026 | 1.3 | 365 | 260 / 1.40x | 260 / 1.40x | 260 / 1.40x |
| 2027 | 1.7 | 473 | 390 / 1.21x | 325 / 1.46x | 286 / 1.65x |
| 2028 | 2.0 | 564 | 585 / 0.96x | 406 / 1.39x | 315 / 1.79x |
| 2029 | 2.3 | 640 | 878 / 0.73x | 508 / 1.26x | 346 / 1.85x |
| 2030 | 2.5 | 703 | 1316 / 0.53x | 635 / 1.11x | 381 / 1.85x |
| 2031 | 2.7 | 756 | 1974 / 0.38x | 793 / 0.95x | 419 / 1.81x |
| 2032 | 2.9 | 800 | 2962 / 0.27x | 992 / 0.81x | 461 / 1.74x |

The 50% case is about 0.96x in 2028; the 25% case is about 1.46x in 2027 and 0.95x in 2031; the 10% case is about 1.85x in 2029–2030. The old claims that 25% reaches 0.95x only in 2032 and 10% stays at 2x no longer hold after the starting-point change. These scenarios do not establish the most likely dates.

## 9. Implications of company disclosures

NVIDIA FY27 Q2 data-center revenue is 89B, up 117% year over year. Quarter-times-four is about 356B, a quarterly annualization rather than terminal AI revenue. Supply and capacity commitments update from 95.2B to 279B. Its 10-Q also lists 99B of equity investments and 25B of future equity commitments; these are not a combined annual new-investment flow and cannot be conflated with supply commitments as a single circular-investment measure. [IR](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx) (2026-08-26); [10-Q](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf) (2026-08-26)

CoreWeave’s backlog of 104.2B is about 40.5x quarterly revenue of 2.575B, or 8.1x its full-year revenue-guidance midpoint of 12.8B. These use different denominators. Its backlog and IREN’s 20.3B depend on delivery conditions; Nebius’s >40B customer commitments likewise cannot be called realized revenue.

The old claims of four-company free cash flow of 300+B, CoreWeave lease leverage of 4.2x, Copilot penetration of 3.3–4.4% and 400M seats, 10–30-fold inference-cost declines, 18–24-month hardware cycles and 24-month GPU value changes were not updated or verified and do not support current conclusions. Microsoft explicitly did not update its Copilot count this quarter. These figures cannot guarantee that a class of companies will avoid bankruptcy or identify a certain weakest company. [IR](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1) (2026-10-28)

## 10. Existing monitoring items

Continue observing model-company terminal revenue, capex guidance, asset-life policies, contract delivery and financing costs. NVIDIA supply commitments are now 279B, CoreWeave backlog 104.2B and Anthropic aggregate commitments 895.4B. New disclosures and old assumptions must retain their dates; guidance is not completed spending.

Old watch thresholds such as H100 at $3/hour, B200 at $5/hour and monthly growth of 10% are unverified and are not presented as current quotes or validated turning-point rules. Announced funding valuations are Anthropic 965B and OpenAI 852B. Relative to official 47B/reported 65B, Anthropic’s ratios are about 20.5x/14.8x; against 24B/reported 50B, OpenAI’s are 35.5x/17.0x. Dates differ, so these are not directly comparable rankings.

## 11. Final assessment

Using information available by 2026-11-09, with K=$1.3T and the original cost parameters unchanged, strict/wide R_T is 135B/260B, strict/wide EPR is 2.70x/1.40x and the geometric midpoint is 1.95x. The conditional result remains above normal industries; the midpoint is now within shale oil’s 1.5–2x range, replacing the old above-range positioning. The ranking against 1846 rail remains unstable.

There is primary evidence of growing company revenue and larger commitments, but incomplete capital-stock data and estimated overlap deductions between models, clouds and applications limit risk conclusions. This edition does not retain categorical claims that Anthropic’s commitments are restrained, adjustment is most likely by a particular year, or a class of firms cannot fail. Conditional recalculation is not measured industry-wide improvement.

## 12. Limitations

EPR is not financial leverage and excludes model/application R&D, sales, administration, tax and equity opportunity costs. R_T combines different measurement dates; wide revenue includes reports and internal attribution, and strict still includes labelled old estimates. Excluding unmeasurable items understates the denominator. K and industry TTM are unupdated; capex periods and lease accounting differ. Historical and mature-industry comparisons are old approximations, and sensitivities are not statistical intervals.

Anthropic’s marketplace gross sales and SpaceX consolidated revenue create particular overlap risks. Anthropic model resale is not added twice; the entire SpaceX SI or neocloud revenue is not treated as terminal revenue. Microsoft’s net estimate and application API deductions still lack complete detail, so all double counting cannot be claimed to have been eliminated.

## 13. Reproducible calculations

```bash
python3 epr.py
```

inputs.json stores inputs and added disclosures. epr.py recomputes P, R_T totals, EPR, capex, sensitivities, time scenarios and rail comparisons. Assertions check the paper’s baseline P=364.65, strict/wide revenue 135/260 and mixed-period Big-5 totals 810/835. The ledger distinguishes assumptions, reports, official disclosures and public earnings-call transcriptions.

## 14. Sources

The complete update ledger and handling of old values are in [data/sources_2026-11.md](data/sources_2026-11.md). Company disclosures, statistics and reports have different dates; retained inputs are not called current measurements. The original historical and methodological references below are retained without claiming that they were reverified.

## Historical bubble:

- Andrew Odlyzko, "Collective Hallucinations and Inefficient Markets: The British Railway Mania of the 1840s" (2010)

- Andrew Odlyzko, "The Railway Mania of the 1860s"

- Mitchell, B.R., British Historical Statistics

- Williamson, J.G., American Growth and the Balance of Payments 1820-1913

- "Dark Fiber—an Archeology of the Dot-Com Bubble" (Technostatecraft, 2025)

- "Lessons from History: The Rise and Fall of the Telecom Bubble" (Fabricated Knowledge, 2023)

- Global Crossing bankruptcy filings (2002)

- WorldCom Form 10-K 2001 (SEC EDGAR)

- FRED HHMSDODNS, DPI (US housing leverage)

- Federal Reserve History: "The Great Recession and Its Aftermath"

## Framework and methodology:

- Jorgenson, D.W. (1963), "Capital Theory and Investment Behavior"

- Public utility revenue requirement framework (standard regulatory economics)

- Damodaran, A. (2024-2025), "Implied required revenue to justify AI capex" blog series
