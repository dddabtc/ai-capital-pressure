Languages: [English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)
PDF: [English](ai-capital-pressure-v3.en.pdf) | [简体中文](ai-capital-pressure-v3.zh-CN.pdf) | [日本語](ai-capital-pressure-v3.ja.pdf)
(PDFs are v3 archives; v3.1 and v3.2 revisions are maintained in Markdown.)

# AI Capital Pressure

## **Cross-industry and historical comparison of annual capital pressure in the AI industry chain**

Stress testing under the EPR framework: comparison with normal industries and the same framework with the four historical infrastructure cycles _dda | 2026-05-25 (v3.1 revised 2026-06-10; v3.2 2026-11-09) |_Non-investment advice_ | Data verified through2026-11-09; unupdated items labelled

## **Data Verification and Version Notes**


v3.2 (2026-11-09) revision note: The original structure, judgments and forecasts are retained; only data and directly affected facts are updated. Both Anthropic baskets use 67.8B annualized Q3 2026 GAAP revenue; the legacy model-company estimates of 5/8B remain, while the strict Bedrock/Vertex residual is excluded. Strict/wide R_T is 165/270B, EPR is 2.21/1.35x and the geometric midpoint is 1.73x. Company capex, SpaceX consolidation of xAI, Oracle and Anthropic filings are added. The date of K=1.3T cannot be established, so a complete September-end stock roll is not claimed; actual flows and limits are in 3.1. Notes qualify the author’s judgments instead of deleting them. See the [source ledger](data/sources_2026-11.md).
**v3.1 (2026-06-10) revision note**: After external review, five measurement-basis issues were corrected; all numbers can be recomputed from repo `epr.py` + `data/inputs.json` (the script includes consistency assertions). (1) Strict R_T now uses Anthropic's official $30B ($40B reported figure only enters the wide basis), deducts application-layer resale paid to model APIs (about $6-8B), and removes the previous $147B→$160B upward rounding: strict EPR is revised from 2.28x to 2.81x; wide basis after the same resale deduction is 1.66x. (2) Historical cases add opex-calibration sensitivity: after calibrating 1846 UK railways to the period operating ratio (45-55%), EPR is only about 1.0-1.9x, so "AI below the 1846 peak" is no longer a headline conclusion. (3) Big-5 2026 capex is unified at $755-805B (consistent with the §3.2 company table). (4) R_T is explicitly a point-in-time run-rate, with a TTM reference basis (about 2.6x). (5) The sensitivity table adds a "construction in progress not depreciated" row. The direction of the central conclusion is unchanged; the magnitude changes are below.


Key data are checked against public sources available by November 9, 2026. Comparable figures are updated; other old numbers remain marked “v3.2 unupdated.” Major updates from earlier estimates:

|**Key Data**|**Updated Value**|**Source (Confidence)**|
|---|---|---|
|Anthropic 2026Q3 GAAP revenue annualized|$67.8B (16.956×4≈67.8)|S-1/A 2026-11-02, p161; not company-defined Run-Rate Revenue|
|OpenAI annualized revenue|Official $24B; reported nearly $50B|Company monthly revenue about 2×12, 2026-03-31; Reuters 2026-10-08, reported figure wide only|
|Microsoft AI ARR|$37B (FY26 Q3) |MSFT official conference call disclosure (high) (v3.2 unupdated) (v3.2 note: Microsoft37 is April disclosure; comparable net revenue is unupdated)|
|OpenAI<br>Total commitments|About $1.4 trillion (5+ years cumulative nominal) |Sam Altman publicly confirmed (medium) (v3.2 unupdated)|
|Big-5 annual capex guidance|$810–835B|Four CY2026 plus Oracle FY27; mixed periods, AI75% remains an assumption|
|CoreWeave quarterly revenue|$2.575B (Q2 2026)|Company disclosure 2026-08-11|
|CoreWeave<br>Revenue backlog|~$104B (vs<br>Early$30B+)|CRWV Q2 2026 Disclosure (High)|
|CoreWeave 2026 capex guide|$35–39B|CRWV guide (high)|
|NVDA Q2 FY27 Total Revenue | $96.2B (DC: $89.0B) | NVDA 8-K (High) |
|NVDA Q3 FY27 Guidelines|$108B (±2%)|NVDA Guidelines (High)|
|NVDA supply commitments|$279B (FY27 Q2)|NVDA FY27 Q2 10-Q Note10 (2026-08-26)|
|Anthropic valuation/financing|$965B valuation, $65B raised|Company Series H 2026-05-28; replaces old expectation|
|OpenAI Valuation/Financing|$852B (March 2026 close<br>$122B round)|Official Financing Announcement (High)|
|Goldman 2026 AI capex<br>baseline|$1000B|Goldman Sachs Research 2026-08-07 (High)|

Of all the updates, the ones that have the biggest impact on the conclusion are Anthropic ARR jumping from $8-10B to $40B, Microsoft AI ARR disclosure $37B, and OpenAI commitments stack accumulating to $1.4T. This significantly changes the specific numbers of R_T terminal revenue and commitments/revenue ratio, but the overall conclusion direction of the EPR framework remains unchanged. (v3.2 unupdated)

## **Central Conclusion**

Conclusion first. This article uses the unified indicator EPR (Economic Pressure Ratio) = annual capital service pressure / verifiable terminal income to compare the AI ​​industry chain with normal industries and historical bubbles under the same framework. 

Let’s first define it clearly: EPR is not a traditional “leverage ratio” (not Debt/Equity, not Debt/EBITDA), but a capital service pressure ratio—a measure of how much capital-related costs (depreciation + cash operations + interest) must be absorbed from terminal revenue each year. This metric is essentially a simplified form of Jorgenson's (1963) capital service cost theory and utility revenue requirement model, applied to AI cycle analysis. EPR is a nomenclature adopted for the convenience of discussion in this article; the framework itself is not new. 

Under the assumptions of this article (K=$1.3T, weighted asset life 6.1 years, o=10%, r=5.5%, d=30%), the current EPR_cash of the AI ​​industry chain is in the 1.35x–2.21x range (wide/strict basis), with a median of about 1.73x. These are stress test results based on explicit assumptions and are not precise industry measurements.

Put it into the benchmark and see:

   - Normal industries (Utilities, Telecommunications, Mature SaaS, Automotive, Aviation) EPR approximately 0.65–0.95x. AI’s current EPR is 2–3 times higher than normal industry benchmarks. 

   - Approximate estimation of historical infrastructure cycle peak EPR with the same framework: 1840s British Railways 2.5–3x, 1996–2001 U.S. telecommunications optical fiber (stripping out steady-state voice services, only looking at new IP/data segments) is about 3x, 1873 U.S. Railways is about 1.2x (aggregated basis), 2014 U.S. shale oil is about 1.5–2x. 2007 US housing 0.9–1.1x, but housing is a price + credit quality + securitization structural bubble, and EPR is not a suitable indicator. 

- AI's current EPR is clearly above the 1873 US railroad aggregate basis (about 1.1-1.2x), at the upper edge of or slightly above 2014 US shale oil (1.5-2x), and below the 2000 new telecom segment (about 3x, this article's most reliable high historical reference). Ranking against 1846 UK rail is not robust: under a unified opex basis, 1846 is about 2.5-3x, but after calibration to the period operating ratio it is only about 1.0-1.9x (see 5.1), so this article does not make a ranking conclusion. It is lower than the median EPR I estimated in mid-2025 2.5-3.0x - this reflects the surge in Anthropic ARR in the first half of 2026 ($9B→$40B), Microsoft AI ARR ($13B→$37B), and the substantial expansion of R_T driven by the rapid growth of OpenAI.  (v3.2 note: At old K, midpoint1.73x is within shale’s1.5–2x range; strict2.21x remains above it. The midpoint does not describe the full range) (v3.2 unupdated)

- Warning required: EPR Center 1.73x remains well above normal industry benchmarks and remains in "infrastructure bubble magnitude" territory. AI has clearly crossed the 1873 railroad aggregate position; its relative position to 1846 rail depends on historical opex calibration, so a hard conclusion is not appropriate.  (v3.2 note: Midpoint1.73x lies in the1–2x band and strict2.21x in2–4x; the author’s judgment is retained)

- AI does not come close to 2007 US housing patterns. Housing is a "price + credit quality + securitization" structure, which is a different failure mode than AI's "capex front-loading + short asset life". 

Capex to GDP (strictly distinguishing between level and growth contribution):

- AI capex level/GDP (stock basis): Goldman estimates that AI capex currently accounts for about 1.8% of GDP. 2026 The total capex of Big-5 hyperscalers in the United States is $810-835B (of which ~75% is AI related ≈ $607.5-626.25B), accounting for about 1.9% of U.S. GDP (~$33.010036T) (including the industry-wide AI capex of about 2.0%). UK Rail capex to GDP in 1847 7-8%. U.S. telecom capex accounted for approximately 1.2% of GDP in 1999-2000. AI's current level is slightly above peak 2000 telecoms and well below 1840s railroads.  (v3.2 note: Goldman estimates US1.8% and global0.9%; this paper’s global-company guidance/USGDP is only a scale comparison, not domestic investment. Big-5 mixes years; adding two known neoclouds is not an industry total)

- AI capex contribution to GDP growth (incremental basis, much more sensitive than horizontal basis): St. Louis Fed estimates 2025 first three quarters AI-related investment accounts for 39% of real GDP growth. Jason Furman estimates that investment in information processing equipment and software accounts for 92% of H1 2025 GDP growth. But Goldman Sachs (Jan Hatzius) countered: After deducting imported capital goods, the net contribution of AI capex to GDP growth is only 0.1–0.2 percentage points. The difference between the two basiss is more than 100 times. This article uses the St Louis Fed figures as a reference, but acknowledges that Goldman's imported capital goods adjustment is an important methodological correction.  (v3.2 note: The Fed’s39% covers the first three quarters of2025; Q3 alone11%,0.48pp, all real growth. Shares and percentage points do not support a100-fold comparison; other old estimates unupdated)

Confidence. "AI EPR far exceeds normal industry benchmarks": High. "AI EPR Median 1.73x": Medium (strongly relies on R_T basis assumptions; the greatest uncertainty in R_T estimates is that internal AI usage attribution and private placement ARR numbers are not audited). "AI above 1873 railroad aggregate, below the 2000 new telecom segment": Medium. "Ranking against 1846 rail": Low (extremely sensitive to historical opex calibration). "AI is likely to follow a digestion-like path rather than a complete collapse": Medium-High. "Specific clearing time point": low. All historical EPR numbers have low-medium confidence.

v3.2 capital-date comparison: The old-K=1.3T midpoint is1.73x; a complete roll to2026-09-30 is unavailable. The original measurement date is unspecified. Four firms’ Q3 cash spending is201.923B, with151.44225B at assumed75%AI, but Oracle’s period differs and other flows are incomplete. There is no new matched-dateK/P/EPR number directly comparable to1.73x and the difference cannot be quantified; only the partial identity in3.1 is given. Updating revenue mechanically lowers fixed-K EPR and does not establish lower matched-date capital risk.

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

## **2. Current EPR (data update) of the AI industry chain**

## **2.1 Input parameters (update)**

|**Parameter**|**Value (update)**|**Change from earlier estimate**|
|---|---|---|
|K (deployed +<br>AI capex<br>stock under construction)|$1.3 trillion|Upgraded 8% from $1.2T<br>(capex acceleration)|
|L (asset-weighted average economic life)|6.1 years|unchanged|
|o<br>(Cash opex/K)|10%|No change|
|r (average debt financing interest rate)|5.5%|unchanged|
|d (proportion of debt financing)|30%|unchanged|
|R_T wide (mixed annualization bases)|$270B|v3.1 was220; Anthropic uses Q3 GAAP annualized, other definitions in2.3|
|R_T strict (mixed annualization bases)|$165B|v3.1 was130; Q3 GAAP annualized, marketplace duplicate excluded, old model estimate retained|
|m_T<br>(Terminal AI gross profit margin)|50%|Unchanged|

Reason for K increase: 2025 hyperscaler AI capex about $260B + 2026 H1 deployment ~$260B + Neocloud + other cumulative deployments of subjects + construction in progress. (v3.2 unupdated)

Core reasons for the significant R_T upgrade: Anthropic ARR rose from $9B at the end of 2025 to ~$40B at 2026 May (increased 4.4x); Microsoft AI ARR disclosed $37B; OpenAI maintained ~$25B but continued to grow rapidly. The rapid realization of AI terminal revenue is the most important variable for EPR improvement. (v3.2 unupdated)  (v3.2 note: Microsoft37 is April disclosure; comparable net revenue is unupdated)

## **2.2 EPR Calculation (Updated)**

|**Project**|**Formula**|**Results (updated)**|
|---|---|---|
|Annual depreciation (stratified sum)|ΣK_i/L_i = $1.3T ×<br>16.4%|$213B|
|Annual cash opex|o × K|$130B|
|Annual cash interest|r × d × K|$21.5B|
|Annualized Economic Pressure P_cash|Subtotal|$365B|
|EPR_cash wide diameter|P/R_T(wide $270B)|1.35x|
|EPR_cash strict basis|P/R_T(strict $165B)|2.21x|
|EPR_cash median estimate||about 1.73x|
|EPR_cash (TTM reference basis)|P / TTM wide R_T(~$140B)|about 2.6x (R_T is point-in-time run-rate, TTM basis is more conservative) (v3.2 unupdated)|
|R_req|P/m_T|$729B|
|Current gap (width)|R_req − R_T|About $459B|
|Current gap (strict)|R_req − R_T|About $564B|

Interpretation. EPR is 1.35x in wide aperture and 2.21x in strict aperture. Median estimate is about 1.73x. This is lower than the mid-year 2025 estimate of 2.5-3.0x, but the decline is smaller than the 1.6-2.3x stated in the first v3 draft - the first draft's strict basis mixed upward rounding and unaudited numbers, which v3.1 corrects. Note that R_T is point-in-time run-rate (exit ARR) while P is annualized pressure: during a phase when revenue doubles in half a year, TTM-basis EPR is about 2.6x, so the point-in-time basis is naturally optimistic.  (v3.2 note: The original draft comparison is retained; v3.2 midpoint1.73x. Anthropic now uses quarterly GAAP annualization; industry TTM140B is unupdated, so the basket is not entirely exit run-rate. Capital timing in3.1)

What has changed? R_T expanded significantly. This is the entire driver of EPR improvement. From mid-year 2025 to May 2026, AI terminal revenue roughly doubled, while P (capital pressure) only increased by about 8% (K rose from $1.2T to $1.3T). R_T growth rate >> P growth rate → EPR decreases. (v3.2 unupdated)

What hasn't changed? All buffering and amplification factors are still present. OpenAI's total commitments have increased to $1.4T, CoreWeave backlog has increased to ~$104B, NVDA's recurring investment scale >$40B, and hyperscaler 2026 capex guidance is still being revised upward. The AI ​​cycle is accelerating in two directions at the same time: revenue is chasing, and capex is also chasing. EPR is the difference between the two races. (v3.2 unupdated)

## **2.3 R_T bottom-up decomposition (core update table)**

R_T is the most sensitive input of the EPR framework. The table below gives the item-by-item breakdown of 2026-11-09's strict and wide apertures.

|**Category**|**Strict Caliber**|**Wide Caliber**|**Confidence/Explanation**|
|---|---|---|---|
|Anthropic (Claude API +<br>Subscription<br>+ Claude Code)|$67.8B|$67.8B|2026Q3 GAAP16.956×4≈67.8; not company Run-Rate Revenue; exceeds older reported65|
|OpenAI (API + ChatGPT Subscription)|$24B|$50B|Reuters reports /<br>Sacra (Medium-High) (v3.2 note: 24 is official monthly revenue about2×12; nearly50 is reported, wide only)|
|Microsoft AI Net($37B less|$27B|$30B|MSFT FY26 Q3<br>Disclosure (v3.2 unupdated)|

|**Category**|**Strict Caliber**|**Wide Caliber**|**Confidence/Explanation**|
|---|---|---|---|
|~$10B Azure-OpenAI resale)|||$37B<br>; This article deducts<br>Azure-OpenAI resale<br> points (v3.2 unupdated)|
|xAI(SpaceX)/Mistral/Cohere/other (v3.1 legacy estimate, unupdated)|$5B|$8B|SpaceX SI disclosures are background only, not added toR_T|
|Google Gemini Advanced +<br>Workspace AI|$5B|$8B|Medium-Low (not separately<br>disclosed by GOOG) (v3.2 unupdated)|
|Dedicated AI<br>SaaS (Cursor, Glean, Harve<br>y, Perplexity, Cognition, Sie<br>rra), net|$9B|$12B|Medium; gross $15B/$20B, less ~$6B/$8B paid to model APIs (already counted in Anthropic/OpenAI ARR) (v3.2 unupdated)|
|AI add-on incremental<br> for traditional SaaS<br>(Salesforce<br>Agentforce, ServiceNow Now<br>Assist)|$10B|$15B|Low-Medium (incremental only) (v3.2 unupdated)|
|China AI commercialization (Baidu, Byte,<br>Alibaba,<br>Zhipu, DeepSeek, Moonshot)|$10B|$15B|Low (v3.2 unupdated)|
|AWS Bedrock + GCP Vertex<br>AI<br>Terminal Billing (deduct<br>Anthropic/OpenAI resale)|0|$10B|Medium-Low (v3.2 note: Strict residual is not counted, not zero revenue; wide10 remains the unupdated estimate assuming all model resale excluded)|
|Hyperscaler<br>Internal AI usage attribution<br>(search, advertising, recommendation increment)|0 (not counted)|$35B|Low (not independently verifiable,<br>but the scale is real) (v3.2 unupdated)|
|Consulting/Professional Services/<br>In-house<br>productivity savings|0 (not counted)|$10B|Low (v3.2 unupdated)|
|Long tail (other paid)|$5B|$8B|Low (v3.2 unupdated)|
|Exclusion 1: Azure/AWS/GCP sales<br>Intermediate revenue<br>to OpenAI/Anthropic|Exclusions|Exclusions|Avoid double counting|
|Exclusion 2: NVIDIA GPU Sales<br>Revenue|Exclusion|Exclusion|Upstream Capital Goods Revenue|
|Exclusion 3: application-layer resale paid to model APIs|Exclusion|Exclusion|Avoid model-layer ↔ application-layer double counting (added in v3.1)|
|Total (rounded to nearest $5B)|$162.8B →<br>Take $165B|$268.8B →<br>Take $270B||

The difference between the two basiss. Strictly speaking, only verifiable pure AI product revenue (API, subscription, Claude Code terminal products) will be included. Broadcast joins hyperscaler internal AI usage attribution (search, advertising, recommendation AI delta) and enterprise productivity savings. The main difference between the two is whether the attribution can be trusted.

Source and basis allocation for Anthropic $40B. The company officially disclosed on April 6 that ARR had exceeded $30B. TechCrunch follow-up reported ARR "closer to $40B" per internal source in late April - that figure has not been audited and has not been disclosed in SEC filings. Starting with v3.1, the strict basis (defined as "verifiable") uses only the official $30B, while $40B enters only the wide basis. The trajectory from $14B (Feb) → $19B (March) → $30B (April) → $40B (May) is roughly equivalent to about 10 weeks doubling. (v3.2 unupdated)  (v3.2 note: This paragraph retains v3.1 source history; the current value is Q3 GAAP annualized67.8 below)

Microsoft $37B net $27B split logic. Microsoft Official FY26 Q3 Disclosed AI Business ARR $37B (+123% YoY). But this number includes the portion of Azure OpenAI Service sold to the end customer (already billed at the end customer and can be included in R_T) and the resale portion sold to OpenAI itself (which should be excluded to avoid duplication with OpenAI ARR). This article estimates the overlap to be approximately $10B, netting $27B. Note that Microsoft's official basis explicitly says the $37B "includes all model builders on Azure"; combined overlap from OpenAI and Anthropic (which has committed to buy $30B of Azure) may be greater than $10B, so the split uncertainty is widened to ±$5-10B. (v3.2 unupdated)  (v3.2 note: Microsoft37 is April disclosure; comparable net revenue is unupdated)

v3.2 supplement: Anthropic S-1/A p161 reports2026Q1/Q2/Q3 revenue4.731/11.555/16.956B,9M33.242B and, with2025Q4 2.040B, TTM35.282B. Per rework instruction both baskets use67.8B (16.956×4=67.824, shown to one decimal), named quarterly GAAP revenue annualized, not company-defined Run-Rate Revenue. It exceeds the older reported65B. The October-end amount on p199 remains blank. Quarterly annualization does not itself establish an exit-rate floor without sustained intra-quarter growth. P58 and Note2 disclose44% of9M revenue through cloud marketplaces, recognized gross; strict Bedrock/Vertex cannot add those sales again. Microsoft net27/30 and application net9/12 remain old estimates. [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm) (2026-11-02). xAI is consolidated into SpaceX; SI mixes ads, cloud, Grok and Cursor, with no separate terminal annualization. Legacy5/8 stays; whole-segment sales and Cursor are not added again.

## **Three, K, annual Capex and Commitments are strictly stratified**

## The AI industry chain involves three types of related but essentially different numbers. Mixing up leads to serious double counting or conceptual errors. 

|**Level**|**Definition**|**Accounting Nature**|**Use in this article**|**Typical2026Number**<br>**(Updated)**|
|---|---|---|---|---|
|K<br>: Deployed + Assets Under Construction<br> Capital Stock | Assets on Book NBV + Construction in Progress|Stock | Enter EPR Numerator | Estimate $1.3T|
|Annual Capex|The current year’s PP&E acquisition flow|Flow|Forecast future K<br>; used for<br>capex/GDP level|Big-5 $810-835B;<br>with AI ~$607.5-626.25B|
|Commitments|Contractual obligations not yet fully deployed<br>Obligations/announced|Contractual obligations<br>Obligations/<br>announce<br>d|Future K leading indicators|OpenAI<br>Total stack~$1.4<br>Trillion over 5+ years (v3.2 unupdated)|

## **3.1 K (about $1.3T, updated with disassembly)**

- Hyperscaler AI cumulative capex stock (Big-5 2022-2026 cumulative by AI portion 75%): approx. $780880B (v3.2 unupdated)

- Neocloud AI capex stock (CoreWeave net property and equipment, PP&E, $46.736B at 2026-06-30 + Lambda + Crusoe + Nebius, etc.): approx. $90-130B (v3.2 note: [Q2](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000366/crwv-20260630.htm), 2026-08-12, updates CoreWeave only; the industry stock estimate is not remeasured. Company assets include construction in progress and do not equal deployed pure-AI capital.)

- Others (Oracle AI infra, self-built by enterprises, government/sovereign investment): $200-300B (v3.2 unupdated)

- The total range is about $1.07-1.31T; this article takes the upper end $1.3T (making P higher and EPR more conservative). Note the basis difference when comparing with historical cases: AI's K is deployed basis (excluding $1.4T commitments), while the £170M for 1846 rail is cumulative committed capital - this asymmetry makes the historical anchor higher and AI lower (see 5.1) (v3.2 unupdated)

v3.2 capital-date comparison: Original3.1 provides cumulative2022–2026 amounts but no measurement date forK;2.1 mentions2026H1 deployments. The May25 paper/June10 revision dates do not establish a June30 stock of1.3T. Annual guidance or all Q3 spending cannot simply be added to that old K. Verified July–September cash PP&E purchases are actuals:

| Company | Q3 cash PP&E, $B | Company-reported capex, $B | Primary source |
|---|---|---|---|
| Microsoft | 39.367 | 45.2 | [Cash](https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast), [Call](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1) (2026-10-28) |
| Alphabet | 51.355 | 51.4 | [Cash flow](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm) (2026-10-28) |
| Amazon | 77.259 | 77.259 | [Cash flow, p6](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf) (2026-10-29) |
| Meta | 33.942 | 34.906 | [Cash flow / FCF reconciliation](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx) (2026-10-21) |

Cash subtotal201.923B; applying the unchanged75% AI assumption gives151.44225B, a known flow rather than complete asset additions. Reported capex totals208.765B: Microsoft includes lease recognition, Meta lease principal payments, so these are not equivalent new-asset measures. The paper’s roll method, with16.4% annual depreciation allocated quarterly as4.1%, gives only the partial identity: K_September=0.959×K_June+151.44225B+unmeasured net additions. Oracle28.499B covers June–August, not Q3; neocloud flows, noncash leases and disposals are incomplete. June-endK cannot be determined, so alignedK,P and strict/wide/midpoint EPR are unavailable, not zero. WithK inB, P=0.2805K, strictEPR=P/165, wide=P/270 and midpoint is geometric. This limitation is also stated in the central conclusion and Section11; a denominator-driven decline is not evidence of matched-date risk improvement.

## **3.2 Annual Capex (2026 latest guidance)**

|**Subject**|**2024**|**2025**|**2026Guidelines/Estimates (Updated after Q1**<br>**)**|**AI**<br>**Part (~75%)**|
|---|---|---|---|---|
|Microsoft|~$56B (v3.2 unupdated)|~$95B (v3.2 unupdated)|$170B|$127.5B|
|Alphabet|~$53B (v3.2 unupdated)|~$75B (v3.2 unupdated)|$195–205B|$146.25–153.75B|
|Amazon|~$78B (v3.2 unupdated)|~$105B (v3.2 unupdated)|$220B|$165B|
|Meta|~$37B (v3.2 unupdated)|~$65B (v3.2 unupdated)|$135–145B|$101.25–108.75B|
|Oracle|$6.866B (FY24)|$21.215B (FY25)|$90–95B|$67.5–71.25B (v3.2 note: [FY25](https://s23.q4cdn.com/440135859/files/doc_financials/2025/q4/4q25-pressrelease-June-final.pdf), 2025-06-11; historical columns are fiscal years. FY27 is 2026-06 to 2027-05; annual guidance remains third-party transcript information, not primary-verified)|
|Big-5 Total|~$231B (v3.2 unupdated)|~$361.2B (v3.2 note: Oracle FY25 corrected; other legacy estimates and mixed periods retained)|$810–835B|$607.5–626.25B|

|**Subject**|**2024**|**2025**|**2026Guidelines/Estimates (Updated after Q1**<br>**)**|**AI**<br>**Part (~75%)**|
|---|---|---|---|---|
||||$750B)| (v3.2 unupdated)|
|Neocloud total|~$15B|~$35B|~$60-70B|~$65B (v3.2 unupdated) (v3.2 note: Company rows below replace this aggregate; old60–70 is not added again)|
|Industry AI capex<br>Traffic||~$400B|~$676.375B| (v3.2 note: Big-5 assumed AI guidance midpoint616.875+two listed firms59.5; incomplete industry, mixed periods, not actual spending)|

Sources: SEC 10-Q Public Disclosures, Q1 2026 Earnings Call Guidance, CreditSights/Goldman Sachs/Yahoo Finance Comprehensive (updated after Q1). Four of the Big-5 companies raised their capex guidance after Q1; only Amazon maintained its original plan (because it was already the highest in the industry).  (v3.2 note: Four firms now use October disclosures and Oracle September FY27; Microsoft170 reflects delivery delays, so not every firm raised guidance. Original source description remains unupdated)

Observation: Goldman Sachs latest baseline model estimates 2026 AI capex $1000B, consistent with CreditSights $750B estimates. Goldman predicts AI capex of $1.6T in 2031. Capital expenditures/revenue ratios have exceeded Oracle 86%, Meta 54%, Microsoft 47%, Alphabet 46%, Amazon 25% - historically unimaginable levels.  (v3.2 note: Goldman’s August7 research estimate no longer equals old CreditSights750; the2031 forecast and old capex/revenue ratios remain unupdated)

### 3.2a v3.2: company capex and subsequent quarters

Big-5’s810–835B mixes four CY2026 guides with Oracle FY27 (2026-06 to2027-05). Oracle90–95 and net cash maximum70 remain supplementary third-party transcript figures. Official FY27 Q1 results, the 2026-09-11 10-Q and 2026-10-28 Investor Day materials were checked; the annual capex amounts could not be verified from official text or replay. FY27 Q2 has not ended as of 2026-11-09. The retained aggregate is not wholly primary-verified.

| Company | Annual capex guidance, $B | Period and source |
|---|---|---|
| CoreWeave | 35–39 | CY2026; [IR](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf) (2026-08-11) |
| Nebius | 20–25 | CY2026; [Third-party transcript](https://www.fool.com/earnings/call-transcripts/2026/08/19/nebius-nbis-q2-2026-earnings-call-transcript/) (2026-08-19, call 08-12) |
| Two listed neoclouds | 55–64 | Not an industry total |
| IREN | CY2026 unverified; remaining FY27 is 15 | [IR](https://iren.gcs-web.com/static-files/3217742e-5d79-4681-a7d9-06b934b35937) (2026-11-05) |
| SpaceX SI | Full-year AI not separately disclosed; 9M actual 39.995 | [10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm) (2026-10-22) |
| Applied Digital | Full-year unverified | FY27 Q1 cash capex 2.074698; initial-term contracts ~36 |
| Cipher Digital (formerly Cipher Mining) | Full-year unverified | Q3 cash capex 1.552980; Barber Lake initial-term contract ~9.1 |
| TeraWulf | Full-year unverified | Q3 cash capex 0.852274; Anthropic initial-term contract ~19 |
| Galaxy Digital (Helios) | Full-year unverified | Q3 segment-reported capex 0.757; potential contract value >30 includes renewal options |
| Nscale | Full-year unverified | H1 cash capex 3.2301; September financing 3.36, including 1 expected later |
| Lambda | Not disclosed | Financing facility 1; proposed multiyear Red Clay project 33.1, not CY2026 capex |
| Crusoe | Not disclosed | Initial close of anticipated Series F 3.9; total contracted value >140 |
| Fluidstack | Not disclosed | Series A 0.830 raised in January; company post 2026-07-20 |
| Together AI | Not disclosed | Series C 0.8; company post 2026-07-01 |
| Core Scientific | Full-year unverified | Q3 cash PP&E 0.540735; reported capex 0.9851 includes asset acquisitions |
| Hut 8 | Full-year unverified | Q3 cash PP&E 0.476026; portfolio initial-term contract value ~26.6 |

CoreWeave Q3 results and call are scheduled for 2026-11-10; Nebius for 2026-11-12. Q2 remains the latest reported quarter for both. Oracle and Nebius annual capex amounts still require official-audio verification; Nebius’s official Q2 letter reaffirms guidance without printing the capex amount. Private-company financing and project amounts above are separate announcements. The old neocloud60–70B has no auditable company allocation. SpaceX and IREN partial-period amounts and the added firms are not added to the annual-guidance sum. Definitions, dates, original line items and sources: [ledger](data/sources_2026-11.md#oracle-neocloud-2026-11-09).

Cash capex below is the cash-flow statement measure; Q/YTD periods follow each company’s fiscal year. PP&E is net book value, not cumulative capex. Debt follows each company’s disclosed balance-sheet categories, with finance leases treated as specified in the ledger. Backlog, customer commitments, initial-term contract value and values including renewal options are not comparable or additive. Galaxy’s segment-reported capex is separate from unavailable consolidated cash PP&E; Nscale discloses a half-year rather than a quarter.

| Company/quarter | Latest quarterly revenue, $B | Backlog/RPO or separately defined contract value, $B | Cash capex Q / YTD; PP&E net; debt; other, $B |
|---|---|---|---|
| Oracle FY27 Q1 | 19.345 (OCI ~7.4) | RPO 664 | 28.499 / 28.499; 127.845; 125.337; net cash capex17.966 |
| CoreWeave Q2 2026 | 2.575 | ~104 | 6.422 / 14.117; 46.736; 35.068; FY revenue guide12.4–13.2 |
| Nebius Q2 2026 | 0.5823 (AI cloud 0.5749) | >40 | 5.6574 / 8.1303; 13.0452; 8.5457 |
| IREN FY27 Q1 | 0.228 (AI cloud 0.200) | 20.3 | 4.824 / 4.824; 12.344; 10.208 |
| Applied Digital FY27 Q1 | 0.341875 | ~36 | 2.074698 / 2.074698; 6.330411; 6.376592 |
| Cipher Digital Q3 2026 | 0.026701 (HPC 0.005852) | ~9.1 | 1.552980 / 2.517241; 3.899880; 5.559878 |
| TeraWulf Q3 2026 | 0.076230 (HPC 0.062986) | ~19 | 0.852274 / 2.230788; 4.580681; 5.232310 |
| Galaxy Digital Q3 2026 | 8.688050 (leasing 0.079068) | >30 | null / null; 2.946995; 6.748432 |
| Nscale H1 2026 | H1 0.1406; Q null | >103 | null / 3.2301; 5.7275; 0.1374 |
| Lambda | null | null | null / null; null; null |
| Crusoe | null | >140 | null / null; null; null |
| Fluidstack | null | null | null / null; null; null |
| Together AI | null | null | null / null; null; null |
| Core Scientific Q3 2026 | 0.232866 (HDC 0.215432) | 7.484422 + ~1.8 | 0.540735 / 1.494979; 2.630353; 4.302175 |
| Hut 8 Q3 2026 | 0.071071 | ~26.6 | 0.476026 / 1.092208; 1.861749; 7.628225 |
| SpaceX SI Q3 2026 | 7.560 (Solutions & Infrastructure 7.022) | No terminal-AI backlog used here | Q3 capex 16.444; 9M revenue 10.939 |

SpaceX’s Q3 10-Q Note 1 (pp10–11) confirms that xAI is wholly owned; Notes 3 (p12) and 18 (pp32–33) disclose revenue and capex. GPU purchases, data-center capex and full-year pure-AI guidance are not separately disclosed. Neocloud order metrics have different definitions and are not directly summed; their entire revenues are not added to terminal AI revenue either. [10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm) (2026-10-22); [Oracle](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx) (2026-09-10); [Nebius](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf) (2026-08-12); [IREN](https://iren.gcs-web.com/static-files/3217742e-5d79-4681-a7d9-06b934b35937) (2026-11-05)

Microsoft’s 170B versus its old guidance cannot directly establish a smaller project programme: lease recognition and delivery timing affect reported capex. Microsoft said FY27 second-half spending would accelerate; Alphabet said 2027 spending would increase significantly; Meta said its 2027 budget was still being developed and it intended to keep investing aggressively, without a full-year amount. Amazon’s release supplied no comparable full-year 2027 capex number, so none is entered. These are published management statements, not new forecasts by this paper. [Microsoft](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1), [Alphabet](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx), [Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx), [Amazon](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf)

SpaceX’s latest S-1/A is dated 2026-06-03. Its “AI Capital Expenditures” paragraph reports 7.723B of AI capex in 2026 Q1, driven by construction, equipment and supporting terrestrial data-center infrastructure. The final prospectus dated 2026-06-12 carries this disclosure forward. Current values here use the later Q3 10-Q rather than the pre-listing quarter. [S-1/A](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm), [424B4](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm)

## **3.3 OpenAI Commitments stack (updated to $1.4T)**

Sam Altman publicly confirmed that OpenAI’s total commitments are approximately $1.4  trillion (covering the next 5+ years). This is the largest single point in the industrial chain. The table below is the breakdown. (v3.2 unupdated)

|**Contract/Commitment**|**Nominal Size**|**Time Window**|**Confidence**|
|---|---|---|---|
|Oracle compute deal|About $300B|5 years (2027-<br>2031)|High (Oracle CEO Safra Catz confirmed many times) (v3.2 unupdated)|
| Stargate (OpenAI/<br>SoftBank/Oracle/<br>MGX) | About $500B<br> (<br>announced<br>$400B+<br><br>committed<br>) | 4 years (2025-<br>2028) | Medium (announced<br>, overlapping with Oracle part<br>) (v3.2 unupdated)|
|AMD (6 GW Instinct<br>GPU) | Approximately $90B Cumulative<br>Hardware Revenue | From H2 2026<br>Onwards | Medium (AMD/OpenAI Public Disclosure)  (v3.2 unupdated)|
|NVIDIA investment|up to<br>$100B|Conditional, gradually deployed per<br>GW|Medium (announced strategic cooperation) (v3.2 unupdated)|
|Amazon AWS|Original$38B + additional$100B; nominal$138B|Additional amount8 years; original agreement has different term|OpenAI official2026-02-27|
|Microsoft Azure (after reorganization<br>)|about $250B<br>cloud<br>purchase|many years|medium (reorganization agreement between both parties) (v3.2 unupdated)|
|CoreWeave|Up to approximately $22.4B announced aggregate|Order-specific; latest $6.5B to 2031-05-31| (v3.2 note: [company](https://www.coreweave.com/news/coreweave-expands-agreement-with-openai-by-up-to-6-5b), 2025-09-25, confirms aggregate ceiling; latest Q2 10-Q, 2026-08-12, confirms latest order. Not remaining backlog or a uniform 2032 term)|
|Broadcom<br>Self-developed chips +<br>Others|About $50-<br>100B|Many years|Mid (v3.2 unupdated)|
|Total Notional Stack (Altman Public<br>Numbers) | Approximately $1.4 Trillion | 5+ Years | Mid-High  (v3.2 unupdated)|
|OpenAI 2026-03 official|~$24B|current|medium-high|

|**Contract/Commitment**|**Nominal Size**|**Time Window**|**Confidence**|
|---|---|---|---|
|ARR||||
|Commitments /<br>Revenue Ratio|||About 58.3x|

The OpenAI commitments/revenue ratio rose to 58.3x from an early estimate of 28-36x. This is a level that has not been achieved by any model company or customer/supplier relationship in history. Even if OpenAI ARR grows at 100% CAGR (already extremely optimistic), it still takes about 4 years for the commitments/revenue ratio to drop below 5x ($24B×2⁴=$384B, 1400/384≈3.6x); at a more realistic 50% CAGR, it takes more than 6 years.  (v3.2 note: Total1.4T is unupdated; reported50B gives28.0x, so this does not establish a current risk ranking)

Compare Anthropic commitments stack:

|**Contract/Commitment**|**Nominal Size**|**Description**|
|---|---|---|
|Amazon|$5B<br>Cash +<br>Up to $25B + 5GW<br>Trainium + $100B AWS<br>Procurement<br>(10 years)|Primary Training Partner (v3.2 unupdated)|
|Google|$10B<br>Cash +<br>Up to $40B + 5GW<br>TPU|Announced April 24th (v3.2 unupdated)|
|NVIDIA|Up to $10B + 1GW GPU supply| (v3.2 unupdated)|
|Microsoft|Up to $5B + Anthropic<br>Buy<br>$30B Azure compute| (v3.2 unupdated)|
|Broadcom|$21B AI<br>Revenue (Anthropic 2026<br>estimate)|Mizuho estimates (v3.2 unupdated)|
|U.S. compute infrastructure<br>Investment Commitment|$50B|Nov 2025Public (v3.2 unupdated)|
|Total nominal commitments (S-1/A)|$895.4B|GAAP quarterly annualization$67.8B, ratio13.2x;69.8B due next12months|

Anthropic's commitments/revenue ratio (13.2x) is much lower than OpenAI (58.3x). This reflects two different business models: Anthropic’s revenue is expanding rapidly (doubling in about 10 weeks), and its commitment scale is relatively restrained; OpenAI’s commitment scale is extremely large, and it relies on future revenue to deliver.  (v3.2 note: S-1/A’s895.4B weakens the original “relatively restrained” judgment; OpenAI1.4T is unupdated and from another date, so not a same-date risk ranking. Old partner rows are unupdated and not summed to replace total commitments)

v3.2: Total commitments use[S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm) (2026-11-02), pp174–175 and related disclosures, including short-term, subsequent commitments and uncommenced leases; the319.993B table is not the complete total. AWS update:[OpenAI](https://openai.com/index/amazon-partnership/) (2026-02-27).

## **4. Normal industry EPR benchmark (rough estimate, non-audit industry model)**

The normal industry EPR range serves as the benchmark. All figures are based on industry average estimates based on 2024-2025 public financial reports, with a medium confidence level. Warning: Industry aggregate data is rough. Company income, D&A, opex, and interest come from different companies and accounting standards, and it is impossible to have the same basis. These numbers are order of magnitude benchmarks, not exact comparisons. 

v3.2 note: This section’s normal-industry estimates are unupdated; Section5 historical assumptions and background numbers are also unupdated and retained as reference.

|**Industry**|**Estimated EPR_cash**|**Asset life characteristics**|**Risk characteristics**|
|---|---|---|---|
|Mature SaaS|0.69x|Short (3–5y)|Light asset, opex adjustable|
|Traditional telecommunications (post-2002)|0.76x|Medium long (10–15y)|Steady-state industries|
|Utilities (regulated)|0.80x|Long (30+y)|High debt + stable returns|
|Aviation|0.90x|Medium (15–25y)|Close to the equilibrium line|
|Automotive OEM|0.92x|Short to medium (5–10y products)|Close to balance line|

|**Industry**|**Estimated EPR_cash**|**Asset life characteristics**|**Risk characteristics**|
|---|---|---|---|
|AI (v3.2 wide basis)|1.35x|Hybrid (4–15y) |Far beyond normal baseline|
|AI (v3.2 strict basis)|2.21x|Same as above|Far beyond the normal baseline|

The normal industry median EPR is about 0.80x, and even high capital intensity industries (utilities, automobiles) rarely exceed 1.0x. AI's current EPR is 1.7–2.8 times that of normal industries. Still an order of magnitude away from normal benchmarks.  (v3.2 note: Against representative0.80, wide1.35/strict2.21 are about1.7/2.8x; midpoint about2.2x)

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

Interpretation. After stripping off the steady-state voice service, the EPR of the new IP/data segment is about 3x. This is almost completely parallel to the current situation of AI: Hyperscaler's overall business (search, advertising, e-commerce, Office) is healthy, but the newly built AI infrastructure is under great pressure alone. 

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

## **6. Main comparison table: AI’s position in the leverage spectrum (updated)**

## Put all previous calculations in a table. 

|**Case**|**Period**|**EPR Approximate Estimate**|**Asset Life**|**Terminal Crash Characteristics**|**Similar to AI**<br>** Degree**|
|---|---|---|---|---|---|
|Mature SaaS|Current|0.69x|3-5y|n/a (steady state)|Low|
|Traditional Telecommunications (post-<br>bubble)|Current|0.76x|10-15y|n/a|Low|
|Utilities|Current|0.80x|30+y|n/a|Low|

|**Case**|**Period**|**EPR Approximate Estimate**|**Asset Life**|**Terminal Crash Characteristics**|**Similar to AI**<br>** Degree**|
|---|---|---|---|---|---|
|regulated||||||
|Aviation|Current|0.90x|15-25y|Cyclic Bankruptcy|Low|
|Auto OEM|Current|0.92x|5-10y|Cyclic Bankruptcy|Low|
|China Steel|2015 Peak<br>Value|0.5-0.7x|20+y|Price fell70%|Low|
|US Housing|2007Peak<br>Value|0.9-1.1x|50+y|House prices fall35%, financial<br>crisis|Low (structure<br>different)|
| U.S. Railroads | 1873 Peak<br>Value | Approximately 1.1-1.2x (aggregated) | 50+y | 25% Industry Bankruptcy, 6<br>Long Depression | Mid-High |
|US shale oil|2014peak<br>value|1.5-2x|5-10y|Oil prices drop<br>75%, ~100 bankrupt|mid|
|AI 2026 (Wide<br>Caliber R_T, v3.2)|Current|1.35x|4-15y Mix|?|Baseline|
|AI 2026 (strict<br>basis R_T, v3.2<br>)|current|2.21x|same|?|baseline|
|British Rail|1846 Peak<br>Value|Unified 2.5-3x /<br>calibrated 1.0-1.9x|50+y|Share price down50-80%|High (ranking unstable)|
|US Telecom Optical Fiber (New<br>IP/data)|2000 Peak<br>Value|Approximately 3x|15-20y|$2T Market value evaporates<br>, WorldCom goes bankrupt<br>|High|

Warning: All historical EPRs are approximate estimates of the same frame, not precise measurements of "the same basis". Read several key conclusions from the updated table:

Conclusion 1: The AI position has moved down from the historical bubble peak range, but remains high. Early EPR 2.5-3x estimates put AI looking on par with 1846 railroads and 2000 telecoms. The v3.2 updated 1.35-2.21x puts AI clearly above the 1873 US railroad aggregate (1.1-1.2x), at the upper edge of or slightly above 2014 US shale oil (1.5-2x), and still below the 2000 new telecom segment (about 3x). This article does not rank AI against 1846 rail (its EPR is extremely sensitive to opex calibration: 2.5-3x or 1.0-1.9x).  (v3.2 note: At old K, midpoint1.73x is within shale’s1.5–2x range; strict2.21x remains above it. The midpoint does not describe the full range)

Conclusion 2: AI still far outperforms normal industry benchmarks. Normal industry 0.65-0.95x, AI 1.35-2.21x. Median EPR about 1.73x ≈ 2.2x normal industry benchmark. Still at the "infrastructure bubble level", just no longer at the peak.

Conclusion 3: The direction has not changed, but the degree has slowed down. AI still shows "capital front + demand extrapolation" characteristics. But R_T cashes out faster than expected - this is the most important "escape" path. If Anthropic + Microsoft AI + OpenAI, etc. 2026-2027 continue to expand at the current growth rate, wide-basis EPR may fall below 1.5x in 2027-2028 and enter the same level as the peak of shale oil.  (v3.2 note: New wide1.35x is already below1.5x; the original scenario judgment remains, not an unmet threshold)

Conclusion 4: AI’s comparability with 1846 Railroad and 2000 Telecommunications decreases, and its comparability with 1873 Rail + Shale Oil increases. 1846 Rail and 2000 Telecom are characterized by terminal demand growth that is severely undercapex paced. AI's current situation is different - R_T is expanding at a rate of 100%+. This reduces the probability of the AI ​​heading towards a 1846/2000-like full-blown crash. 

Conclusion 5: But the capex side is still accelerating. Big-5 2026 capex guidance rose to $810-835B from about $620B at the beginning of the year, with Microsoft FY27 hinting at higher. If capex continues to accelerate + R_T growth slows, EPR will rebound. The current 1.35-2.21x is not steady state.  (v3.2 note: Microsoft170 reflects delayed deliveries; an aggregate rise does not imply every company raised guidance. Early-year620 unupdated)

## **7. Capex/GDP dual-basis analysis (updated)**

Strictly distinguish between two completely different concepts: (1) capex level as a share of GDP; (2) capex contribution to GDP growth. Mixing is a common mistake. 

## **7.1 Capex level to GDP**

|**Case**|**Period**|**Capex**<br>**Level/GDP (annual**<br>**Diameter)**|**Description**|
|---|---|---|---|
|British Rail|1847Peak value|7-8%|New capex/GDP for the year|
|US Telecom|2000Peak<br>Value|Approx.1.2%|BEA|
|US Housing (Residential Investment<br>Investment)|2005-<br>2006|About 6.3%|Historical Highs|
|AI USA (Big-5<br>2026)|2026|About 1.9%|$607.5-626.25B AI<br>Part/GDP $33.010036T (v3.2 note: Global companies/USGDP; mixed periods, not US domestic investment)|
|AI<br>USA (all industries<br>2026)|2026|about 2.0%|including neocloud + Oracle + sovereign (v3.2 note: Now Big-5 assumedAI plus CoreWeave/Nebius, not all industry; Oracle already inBig-5, not added again)|
|Goldman<br>Estimated AI<br>capex/GDP|Current|About 1.8% (narrow bore) |Goldman Sachs Research (v3.2 note: Goldman2026-08-07; US / 米国 / 美国)|
|AI<br>Global2026|2026|About0.9%|$700-750B /<br>Global$110T (v3.2 note: New0.9% is Goldman’s global research estimate; old700–750/110T is unupdated and does not calculate the new share)|

AI 2026 US capex/GDP is slightly higher than 2000 telecom peak, and well below 1840s rail. The difference between Goldman's estimate (1.8%) and this article's estimate (~1.9–2.0%) lies in the basis: Goldman uses a more stringent definition of pure AI capex, while this article uses the hyperscaler total capex × 75% AI ratio.  (v3.2 note: The difference also includes geography and period definitions, not onlyAI share)

## **7.2 Capex Contribution to GDP Growth**

This is a completely different metric than the capex/GDP level. GDP growth contribution looks at the year-on-year increase in capex, not the total amount. The latest external estimates differ sharply:

|**Caliber**|**Estimate**|**Source**|
|---|---|---|
|Jason Furman: Information Processing Equipment +<br>Software accounts for H1 2025<br>GDP Growth|92%|X Posts (v3.2 unupdated)|
|St Louis Fed: AI<br>related investment in 2025 Q1–Q3<br>real GDP<br>growth|39%|St Louis Fed On the Economy Jan 2026 (v3.2 note: 39% is first three quarters; Q3 alone11% or0.48pp, real growth)|
|Goldman Sachs: AI capex<br>contribution to GDP growth<br> (capex incremental basis) |1.5 pp nominal |Goldman Sachs Research (v3.2 unupdated)|
|Goldman Sachs: AI capex<br>Net GDP growth contribution|0.1-0.2 pp|Jan Hatzius (v3.2 unupdated)|

|**Caliber**|**Estimate**|**Source**|
|---|---|---|
|(After deducting imported capital goods)|||
|Units and periods differ; percentage points and contribution shares do not imply a nearly1,000-fold difference. Reasons:|||

   - Furman used the NIPA category (Information processing equipment + software). This category H1 2025 has an unusually high contribution to GDP growth due to the surge in AI investment, but the denominator (total GDP growth) is also unusually low. This is the denominator effect. 

- St Louis Fed uses more precise AI-related subcategories, resulting in 39% (more credible, real-growth basis).  (v3.2 note: 39% covers the first three quarters of2025; Q3 alone11%,0.48pp)

- Goldman further deducts imported capital goods (most imports of GPUs, HBMs, servers) to get net 0.1-0.2 pp. GDP measures domestic production and imported goods do not count towards GDP growth. (v3.2 unupdated)

- This article adopts Goldman's methodological revisions. The true AI capex's net contribution to U.S. GDP growth may be only 0.1-0.5 pp, far less than the horizontal share (1.7-2.0%) would lead one to think. This is because AI investments 70%+ are imported capital goods (NVIDIA is made with TSMC, HBM is from SK Hynix and Samsung). But this correction in turn means that if AI capex slows down, the direct drag on GDP growth will be smaller (0.1-0.5 pp reversal). Reflexivity is more reflected in stock market valuation → wealth effect → consumption rather than direct GDP calculation. (v3.2 unupdated)  (v3.2 note: The author’s net-contribution and reflexivity judgments remain;0.1–0.5pp,70%+ and other old estimates are unverified. They are not directly comparable to global-company/USGDP scale ratios)

## **8. Sensitivity analysis**

The EPR center estimate 1.73x appears to be precise, but actually relies on multiple uncertain parameters. The table below shows the impact of changes in key parameters on EPR.

## **8.1 Key Parameter Sensitivity (Updated Baseline)**

|**Assumption changes**|**P change direction**|**Impact on wide-aperture EPR**<br>** (baseline1.35x)**|
|---|---|---|
|R_T<br>raised from $270B<br> to $300B<br> (such as 2027 continues to grow at a high<br> rate)|unchanged|EPR<br>reduces to 1.22x|
|R_T<br>raised from $270B<br> to $400B|unchanged|EPR<br>dropped to 0.91x (close to normal industry)|
|R_T<br>downgraded from $270B<br> to $180B|unchanged|EPR<br>upgraded to 2.03x|
|R_T<br>Downgraded from $270B<br> to $165B (strict basis)|Unchanged|EPR<br>Upgraded to 2.21x|
|K<br>Upgraded from $1.3T<br> to $1.7T (end of 2027)|P<br>Upgraded to approximately $112B|EPR<br>Upgraded to 1.77x|
|K<br>Upgraded from $1.3T<br> to $2.0T (2028)|P<br>Upgraded to approximately $196B|EPR<br>Upgraded to 2.08x|
|GPU/network<br>lifetime dropped from 4<br> years to 3 years|Depreciation increased to approximately $43B|EPR<br>increased to 1.51x|
|o<br>Upgraded from 10%<br> to 15%<br> (high opex) |opex<br>Upgraded to $65B|EPR<br>Upgraded to 1.59x|
|Replace r×d with WACC 8%<br>|P<br>up to about $80B|EPR_wacc<br>about 1.65x|
|Construction in progress (15-20% of K)<br>not depreciated (added in v3.1)|D&A<br>down $32-43B|EPR<br>falls to 1.19-1.23x|
|EPR<br>'s reasonable 90% confidence interval: 1.1x-2.9x (wide basis) / 1.8x-3.8x<br> (strict basis). The point estimate is 1.35x<br> or<br>2.21x, but the actual values ​​are spread over the interval. || (v3.2 note: Original90% ranges retained, not recalibrated and not statistical confidence intervals generated by this update)|

## **8.2 EPR Time Path (Updated)**

The current K=$1.3T is still below steady state. Estimated by annual capex run rate $600B and L=6.1 years, steady state K=$3.66T. K is still expanding upward. The following is a hypothetical trajectory of the third-speed R_T speed increase (wide aperture $270B starting point). Assumption: annual capex remains at $600B (2026 actual guidance level); other parameters remain unchanged.  (v3.2 note: 600B remains a legacy scenario assumption, not this edition’s actual2026 guidance; only start revenue changes to270B)

|**Year**|**K (beginning of the year)**|**P**|**R_T**<br>**50%C**<br>**AGR**|**EPR**|**R_T**<br>**25%C**<br>**AGR**|**EPR**|**R_T**<br>**10%C**<br>**AGR**|**EPR**|
|---|---|---|---|---|---|---|---|---|
|2026|$1.3T|$365B|$270B|1.35x|$270B|1.35x|$270B|1.35x|
|2027|$1.7T|$473B|$405B|1.17x|$338B|1.40x|$297B|1.59x|
|2028|$2.0T|$564B|$608B|0.93x|$422B|1.34x|$327B|1.73x|
|2029|$2.3T|$640B|$911B|0.70x|$527B|1.21x|$359B|1.78x|
|2030|$2.5T|$703B|$1367B|0.51x|$659B|1.07x|$395B|1.78x|
|2031|$2.7T|$756B|$2050B|0.37x|$824B|0.92x|$435B|1.74x|
|2032|$2.9T|$800B|$3075B|0.26x|$1030B|0.78x|$478B|1.67x|

## Interpretation:

- 50% CAGR (close to 2026 actual first half rate): R_T continues to grow at current pace, EPR falls below 1.5x in 2027-2028 (about 0.93x in 2028), and 2030 is close to normal industry benchmarks. Under this path, the AI ​​cycle achieves "rapid digestion".  (v3.2 note: Table now0.93x; the original “near normal by2030” judgment remains, while the scenario enters the normal range in2028)

- 25% CAGR (still very aggressive): EPR peaks in 2027 at about 1.40x, then slowly falls back. 2032 enters the upper edge of the normal industry (0.78x). This is a neutral scenario.  (v3.2 note: Updated scenario peaks1.40x in2027 and reaches0.92x in2031; original scenario judgment retained)

- 10% CAGR (conservative): EPR continues at 2x platform. Requires capex to actively slow down to balance. May cause hyperscaler capex downward revision cycle.  (v3.2 note: At the updated start, the table peaks near1.78x, below2x; original judgment retained)

Note that 50% CAGR is not extreme. Anthropic's trailing 12-month ARR went from $9B → $40B (400%+). OpenAI 2025 changes from $6B → $20B (230%) throughout the year. If the two companies continue to grow at 50-100% for a few years, it is entirely possible that R_T will reach $500-600B in 2028. (v3.2 unupdated)

But of course there are risks. Reasoning price wars, open source model challenges, and enterprise penetration saturation may bring R_T's growth to a sudden halt. If R_T growth falls to 10% CAGR and capex continues to be invested at $600B/year level, EPR will continue at the 2x platform in 2027-2029, similar to the digestion period after the establishment of historical bubbles. (v3.2 unupdated)  (v3.2 note: The10% scenario is1.59/1.73/1.78x in2027–2029; the original2x plateau judgment is weakened by the new starting revenue)

## **9. Key differences between AI and historical bubbles (updated)**

## **9.1 Factors that buffer AI cycles**

- Hyperscaler’s own strong cash flow. Amazon/Microsoft/Google/Meta combined annual free cash flow $300B+. (v3.2 unupdated)

- Upstream revenue is solid and verifiable. NVIDIA Q2 FY27 DC revenue $89.0B (+117% YoY), forward annualized ~$356B. Q3 Guidelines $108B/Q.

- R_T Cash out quickly (most important update). Anthropic went from $9B to $40B (6 months), Microsoft AI ARR $37B, OpenAI ~$24B. AI revenue is cashing out faster than any infrastructure cycle in history.  (v3.2 note: The old6-month9→40 trajectory is unupdated; current Anthropic uses Q3 GAAP annualized67.8, OpenAI official24/reported50 and Microsoft37 unupdated. Mixed dates do not establish one current growth rate)

- Diversification reduces systemic risk. 

- Real advancement of technology. The cost of inference 2023-2026 has been reduced by 10-30 times cumulatively. Hardware is iterated on an 18-24 month cadence. (v3.2 unupdated)

## **9.2 Factors that amplify AI cycles**

- OpenAI commitments stack extreme (raised to $1.4T). vs 2026 ARR ~$24B = 58.3x commitments/revenue ratio. This is unprecedented in history.  (v3.2 note: OpenAI1.4T unupdated; reported50B gives28.0x. Anthropic’s new commitments/quarterly annualization13.2x does not establish a risk rank across different dates)

- Revolving financing is huge. NVIDIA 2026 invests $40B+ in equity bets. NVIDIA’s single $30B investment in OpenAI. NVIDIA + CoreWeave + OpenAI Triangle Loops scale. (v3.2 unupdated)

- Neocloud local high leverage. CoreWeave includes lease leverage of approximately 5.0x annualized revenue, backlog ~$104B (vs Q2 revenue $2.575B = 40.4x quarterly basis; using 2026 full-year revenue guidance of $12.4–13.2B, it is about 8.1x forward annual revenue - both basiss are shown to avoid exaggeration).  (v3.2 note: Q2 debt plus finance/operating leases51.608 divided by Q2 revenue annualized10.3 gives5.0x; backlog is approximately104 per official release. The8.1x ratio uses annual-guide midpoint12.8; see3.2a.)

- Rapid depreciation over GPU life. H100's economic value declined significantly within 24 months of B200/Rubin's emergence. (v3.2 unupdated)

- Open source models challenge proprietary API price tiers. DeepSeek, Llama, Qwen directly threaten proprietary API pricing. This is a factor that 2000 Telecom does not have. 

- Microsoft Copilot penetration remains low (3.3-4.4%). Even though AI ARR $37B seems to be high, the coverage rate is still low compared to the Microsoft 365 commercial base (approximately 400 million seats), which means there is a lot of upside space and also means that R_T's expansion depends on the continued increase in penetration rate. (v3.2 unupdated)  (v3.2 note: Microsoft37 is April disclosure; comparable net revenue is unupdated)

## **9.3 Comprehensive judgment (updated)**

AI cushioning factors are stronger than historical bubbles, and R_T has shown to cash out much faster than 1846 Railroads or 2000 Telecoms. AI amplification factors are also more extreme than historically, especially the size of the OpenAI commitments stack and recurring funding. 

Most likely path (updated):

- Anthropic + Microsoft AI maintain rapid growth → R_T continues to expand → EPR further down in 2027-2028

   - Dropped to 1.0-1.5x range

- At the same time, capex continues to accelerate (Big-5 capex is still being revised upward) → K is also growing rapidly → EPR will not decline quickly

- OpenAI is the most vulnerable point in the industry chain. Commitments 58.3x The revenue ratio cannot be absorbed by revenue expansion alone and requires continued equity financing or commitment write-downs.  (v3.2 note: OpenAI1.4T unupdated; reported50B gives28.0x. Anthropic’s new commitments/quarterly annualization13.2x does not establish a risk rank across different dates)

- Neocloud (CoreWeave, etc.) is also vulnerable. Backlog 40.4x quarterly revenue ratio (about 8.1x forward annual revenue on 2026 guidance) relies on backlog realization. If big clients like Anthropic or Meta renegotiate, it could trigger a chain of events

- Hyperscaler does not have a total collapse. Strong cash flow + diversification. 

NVIDIA won't go bankrupt, but the chance of significant compression in forward multiples remains. Its supply commitments $279B and $40B+ investments in customers are so reflexive that any customer-level slowdowns are immediately transmitted to NVIDIA itself. (v3.2 unupdated)

## **10. Leading indicators**

Monitor high-priority signals for cycle turning points (sorted by importance, adjusted based on updated circumstances):

- 1. Anthropic and OpenAI growth rate. The current about 10-week doubling is an anomaly. Any deceleration to monthly growth <10% is a cycle turning signal. (v3.2 unupdated)

- 2. Hyperscaler asset life policy. Amazon has revised it down from 6 years to 5 years. Microsoft/Google/Meta follow-through will trigger a 10-15% GAAP depreciation upward revision. (v3.2 unupdated)

- 3. OpenAI commitments fulfillment speed. Whether OpenAI can maintain commitments stack schedule deployment. If OpenAI and Oracle, AWS, CoreWeave, etc. start to delay or renegotiate, it will be the earliest manifestation of the pressure on the commitments stack $1.4T. (v3.2 unupdated)

- 4. Neocloud refinancing spread and backlog quality. CoreWeave backlog ~$104B looks thick, but is customer focused. Any customer default or delayed deployment would immediately hit EBITDA.

- 5. Hyperscaler capex guidance tone. Changes in rhetoric from "increasing investment" to "improving efficiency". 

- 6. Changes in NVIDIA supply commitments. Current $279B. The significant month-on-month decline means that NVIDIA has less confidence in its forward orders.

- 7. AI inference gross profit margin. OpenAI/Anthropic inference gross margin trend. Price war suppressing gross profit improvement is an early warning. 

- 8. GPU rental price. H100/H200/B200 spot price. H100 spot Chronically below $3/hour pressure CoreWeave. B200 New cluster breakeven $5/hour. (v3.2 unupdated)

- 9. AI capex in GDP and contribution to GDP growth. Current capex/GDP is about 1.9–2.0% (US). The ratio continues to rise, which means the economy’s reliance on AI reflexivity deepens.  (v3.2 note: Global-company guidance/USGDP scale comparison, not US domestic actual investment; changes require comparable definitions)

- 10. Capital market AI theme valuation quantile. Anthropic current $965B valuation (14.2x ARR); OpenAI $852B (35.5x ARR). The downward movement of these multiples is a periodic signal.  (v3.2 note: Valuations date toMay/March; denominators are Anthropic quarterly annualized67.8 and OpenAI official24; reported50 gives17.0x, dates differ)

The red combination (simultaneous appearance means that the probability of cyclical turning point increases significantly): Anthropic + OpenAI growth rate deceleration + capex still upward revision + GPU rental price decrease + financing spread expansion + neocloud backlog quality decrease + model company commitments renegotiated. 

## **11. Final judgment**

Data available as of 2026-11-09:

Under the assumptions of this article (K=$1.3T, L=6.1 years, R_T=$165-270B), the current EPR_cash of the AI industry chain is in the 1.35x-2.21x range, with a median of about 1.73x. This is lower than early 2.5-3.0x estimates (but the decline after the v3.1 correction is smaller than the first v3 draft claimed), mainly driven by 2026 Anthropic ARR surged from $9B to $40B in the first half of the year, Microsoft AI ARR disclosure $37B, and OpenAI maintaining rapid growth. AI current EPR position:

v3.2 capital-date comparison: The old-K=1.3T midpoint is1.73x; a complete roll to2026-09-30 is unavailable. The original measurement date is unspecified. Four firms’ Q3 cash spending is201.923B, with151.44225B at assumed75%AI, but Oracle’s period differs and other flows are incomplete. There is no new matched-dateK/P/EPR number directly comparable to1.73x and the difference cannot be quantified; only the partial identity in3.1 is given. Updating revenue mechanically lowers fixed-K EPR and does not establish lower matched-date capital risk.

   - Significantly higher than normal industry benchmarks (0.65-0.95x) - AI is still in the "infrastructure bubble level" range

   - At the upper edge of or slightly above 2014 US shale oil (1.5-2x), and higher than 1873 US rail aggregate basis (1.1-1.2x)  (v3.2 note: At old K, midpoint1.73x is within shale’s1.5–2x range; strict2.21x remains above it. The midpoint does not describe the full range)

   - Below the 2000 US Telecom new section (approximately 3x); no ranking against 1846 UK Rail (unified basis 2.5-3x, but only 1.0-1.9x after operating-ratio calibration, so the anchor is unstable)

- AI failure modes compared with history:

   - Unlike 2007 US housing (price + credit + securitization structure)

   - Unlike 1989 Japanese asset bubble (pure price bubble)

   - Similarity to 1840s Railroads and 2000 Telecoms decreases as R_T cashes out much faster than those cycles

   - Rising similarity to 1873 U.S. railroads and 2014 shale oil

AI capex/GDP ratio:

- US capex level/GDP around 1.9–2.0% (medium-high, but well below 1840s rail 7-8%)  (v3.2 note: Only a global-company/USGDP scale comparison, not US domestic investment statistics)

- Net contribution to GDP growth 0.1-0.5 pp (Goldman adjusted for imported capital goods) (v3.2 unupdated)

- Real GDP growth contribution was39% over the first three quarters of2025 (St Louis Fed); Q3 alone11%,0.48pp.

## Most likely path:

- If Anthropic + Microsoft AI + OpenAI, etc. maintain 25%+ annual growth rate, EPR will further decline in 2027-2028, and the AI cycle will achieve "rapid digestion"

- If R_T growth falls below 10% and capex continues at $600B+/year, EPR rebounds above 2x (v3.2 unupdated)  (v3.2 note: Current600B/10% scenario peaks near1.78x; below10% growth or higher capital spending could exceed2x. The author’s conditional judgment remains)

- Neocloud (CoreWeave, etc.) and over-committed model companies (OpenAI 58.3x commitments/revenue ratio) remain the most vulnerable  (v3.2 note: OpenAI1.4T unupdated; reported50B gives28.0x. Anthropic’s new commitments/quarterly annualization13.2x does not establish a risk rank across different dates)

- Hyperscaler has strong cash flow and will not completely collapse

- NVIDIA won't go bankrupt, but massive compression in forward multiples is still possible

One sentence summary: Under the stress test assumptions of this article, AI is a real technology cycle + historical capital front-end + local high leverage + reflexive financing. The order of magnitude of EPR has moved down from 2.5-3x to 1.35-2.21x (median 1.73x), which is a true reflection of the faster-than-expected realization of R_T in the first half of 2026. However, AI is still 2-3 times farther away from the normal industry, the capex side is still accelerating, and the OpenAI commitments stack has reached a historically unprecedented level of $1.4T. The most likely outcome is the combination of "partial clearing + soft digestion" in 2027-2029, not a total collapse; but investors holding partial high-leverage links (neocloud, over-committed model companies, long-tail application layers) will bear substantial losses. The probability of a systemic financial crisis is low, but the probability of partial losses of equity and credit is high.  (v3.2 note: The author’s2027–2029 and local-loss judgments remain; midpoint1.73x applies only to oldK. Matched-date capital data are incomplete and OpenAI commitments unupdated, limiting historical risk comparisons)

## Confidence summary:

- "AI EPR_cash median 1.73x": Medium (R_T key uncertainty reduced but still present; strict basis now uses official $67.8B)  (v3.2 note: Quarterly revenue annualized, not company-defined Run-Rate Revenue)

- "AI EPR far exceeds normal industry benchmarks": High

- "AI magnitude is within historical bubble range": High

- "AI above 1873 railroad aggregate, below the 2000 new telecom segment": Medium-High

- "Ranking against 1846 railroad": Low (sensitive to historical opex calibration)

- "AI is not like 2007 housing or 1989 Japan": High

- "Hyperscaler will not completely collapse": Medium-High

- "OpenAI is the most vulnerable point in the industry chain": high (commitments 58.3x revenue)  (v3.2 note: OpenAI1.4T unupdated; reported50B gives28.0x. Anthropic’s new commitments/quarterly annualization13.2x does not establish a risk rank across different dates)

- "Specific clearing time point": low

## **Twelve, main caveats**

- EPR is not a traditional leverage ratio. is the capital service pressure ratio, which is essentially a simplified form of Jorgenson's capital service cost theory. 

- EPR is not a complete profit margin indicator. Does not include R&D, SG&A, sales, customer service, equity incentives, taxes. Real profit pressure is higher than EPR suggests. 

- EPR > 1 is not the same as "the industry is not profitable". But the terminal revenue is not enough to cover the annual infrastructure pressure defined in this article. 

- Historical EPR is an approximation of the same frame. It is not an accurate measurement of "same basis". All historical EPR confidence low-medium.

- R_T is the most sensitive variable in the full text. Anthropic $40B comes from TechCrunch internal information sources (medium confidence, wide basis only; strict basis uses official $30B); OpenAI ARR, Microsoft AI ARR, etc. are selectively disclosed by the company and may not be audited.  (v3.2 note: Both Anthropic baskets now use Q3 GAAP annualized67.8; old40/30 source allocation is version history only. Other selective disclosures and netting assumptions remain uncertain)

- R_T is a point-in-time run-rate, while P is annualized pressure. In high-growth periods, exit ARR is about twice TTM; TTM-basis EPR is about 2.6x (wide). This article uses the point-in-time basis as the main view and TTM as a reference.  (v3.2 note: v3.2 mixes annualization definitions; Anthropic is not exitARR. TTM140B and the2x statement are unupdated)

- K includes construction in progress. Assets under construction do not operate and are not depreciated; excluding them (15-20% of K) reduces D&A by $32-43B and wide-basis EPR to about 1.19–1.23x. This effect points in the opposite direction from "revenue lags construction in progress," so it is listed as sensitivity rather than the baseline.

- Historical EPR opex parameters are not necessarily on the same basis. After calibrating 1846 and 1873 railways to the period operating ratios, EPR is significantly below the unified o basis (1846: 1.0-1.9x vs 2.5-3x); and 1846 K is committed capital while AI uses deployed capital. Historical ranking conclusions are therefore downgraded.

- Model-layer → application-layer API resale has been deducted (v3.1). Application-layer AI SaaS revenue is included net to avoid double counting with model-company ARR; the uncertainty range for Microsoft AI ARR overlap is widened to ±$5-10B.

- K = $1.3T is the median estimate. Cumulative AI capex stock estimates for hyperscaler/neocloud/other entities are subject to ±20% uncertainty. (v3.2 unupdated)

- Normal industry EPR is an aggregate estimate. The leader in the industry may have a lower EPR and a higher long tail. 

- OpenAI commitments $1.4T contain some overlap. Oracle deal and Stargate partially overlap; Anthropic's Amazon $100B purchase commitment is 10 years cumulative; time windows are inconsistent. (v3.2 unupdated)

- Both Anthropic baskets now use$67.8B annualized Q3 GAAP revenue, above the older reported$65B. The company-defined October-end Run-Rate Revenue amount remains blank; the definitions are not interchangeable.

- AI capex/GDP figures vary widely from source to source. Goldman 1.8% (narrow aperture) vs. this article's 1.9–2.0% (wide aperture includes all hyperscaler AI related capex).  (v3.2 note: Geography, period and definitions differ, not onlyAI share)

- The contribution of AI capex to GDP growth varies greatly. From Goldman net 0.1-0.2 pp to Furman 92% (H1 2025 NIPA subcategory). This article adopts Goldman’s adjusted version of imported capital goods. (v3.2 unupdated)

- Housing EPR ~1x does not mean housing is not dangerous. Housing is a price bubble and the EPR framework does not apply here. 1873 US railroads only use aggregate EPR ~1.2x. There is no reliable new/old line breakdown data. The mechanism of "reflexivity" itself is not directly quantifiable. NVIDIA invests in OpenAI, and OpenAI buys NVIDIA GPU. The scale of this chain is estimated to be $40B+. The nominal value is a reasonable estimate based on public disclosure, not an audited figure. (v3.2 unupdated)

- This article provides a research framework and stress test and does not constitute any recommendation to buy or sell securities. 

## **XIII. Reproducible calculations (added in v3.1)**

All core numbers in the full text (P, EPR, the strict/wide R_T totals, sensitivities, time path, and unified/calibrated historical case basiss) can be recomputed in one command from repo `epr.py` + `data/inputs.json`:

```bash
python3 epr.py
```

The script includes consistency assertions: the R_T itemized table total must match the headline figure, and the company-by-company capex table total must match the summary range. The two inconsistencies in the first v3 draft were caught by this machine check. After changing any input, rerun the script to get the full set of numbers.

## **14. Main sources (v3.2 checked through2026-11-09; original sources retained)**

v3.2 note: The original source list is retained below. Old numbers not replaced by new disclosures are unupdated. New links, dates and treatment are in the [source ledger](data/sources_2026-11.md).

## AI company financial reports and official disclosures (high confidence):

   - NVIDIA Q1 FY27 8-K, CFO commentary, 10-Q (filed 2026-05-20) (v3.2 unupdated)

   - NVIDIA Q4 FY26 CFO commentary (supply commitments $95.2B disclosure) (v3.2 unupdated)

   - Microsoft FY26 Q3 Earnings Call Transcript and 10-Q (2026-04-29, AI ARR $37B) (v3.2 unupdated)

   - Alphabet/Amazon/Meta Q1 2026 10-Q (filed 2026-04-30) (v3.2 unupdated)

- CoreWeave Q1 2026 Earnings Call Transcript and 10-Q (2026-05-08, backlog $99.4B) (v3.2 unupdated)

- Anthropic official announcement (2026-04-06, "run-rate revenue has now surpassed $30 billion") (v3.2 unupdated)

   - Anthropic Series G $30B raised at $380B valuation (Feb 2026) (v3.2 unupdated)

   - Anthropic-Google-Broadcom 3.5 GW TPU deal (Apr 2026) (v3.2 unupdated)

   - OpenAI March 2026 $122B funding round at $852B valuation

- AI related industry analysis (medium confidence):

   - Goldman Sachs Research: AI capex baseline $765B for 2026 (2026-04)

   - Goldman Sachs Research: AI capex GDP impact 0.1-0.2 pp net (Jan Hatzius, 2026-02) (v3.2 unupdated)

   - CreditSights: Hyperscaler Capex 2026 Estimates $750B (2026-02) (v3.2 unupdated)

   - St Louis Fed: AI investment contribution to 2025 Q1–Q3 GDP growth 39% (Jan 2026) (v3.2 unupdated)  (v3.2 note: First three quarters39%; Q3 alone11% /0.48pp, real growth)

   - Jason Furman: H1 2025 GDP growth contribution analysis

   - Bloomberg: AI Circular Deals visualization (2026-03) (v3.2 unupdated)

- Media coverage (should be downgraded to reported): (v3.2 unupdated)

- TechCrunch: Anthropic run rate "closer to $40 billion" per internal sources (2026-04-29)

- Reuters: OpenAI/Oracle $300B deal report (2025-09 via WSJ) (v3.2 unupdated)

- Reuters: Anthropic Google $40B investment (2026-04-24) (v3.2 unupdated)

- Financial Times: Anthropic potential $40-50B raise at $850-900B valuation (2026-05-07) (v3.2 unupdated)

- CNBC: NVIDIA $40B+ equity bets in 2026 (2026-05-09) (v3.2 unupdated)

- VentureBeat: Anthropic $30B ARR with 80x growth (2026-04) (v3.2 unupdated)

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

v3.2 primary additions: Anthropic[S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm) (2026-11-02); Microsoft[Q1 FY27](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1), Alphabet[Q3](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx), Meta[Q3](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx), Amazon[Q3](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf); [NVIDIA FY27Q2](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx) (Q3 scheduled November17, unreleased at cutoff); SpaceX, Oracle, CoreWeave, Nebius and IREN links in3.2a. [Goldman](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026) (2026-08-07); [Fed](https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth) (2026-01-12).
