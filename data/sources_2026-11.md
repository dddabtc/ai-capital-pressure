# 2026 年 11 月数据核查

本版保留作者原来的结构、判断和预测，并在相关句子后注明新数据的影响。能核实的新值已更新，查不到可比新值的旧数字仍保留并标未更新。旧资本存量日期不明确，不能把收入更新造成的压力比下降当作同期风险改善。

截止2026-11-09。金额通常为十亿美元（B），K/GDP为万亿美元（T）。严格/宽仍是文章的两组估计名称，含明确标注的旧估计，不是完整审计行业统计。除R_T表列入的项目外，公司披露收入只作背景。

## 输入逐项清单

旧值指origin/main的6113d54；当前输入逐项列出。null表示未核实/未披露，严格市场残余0表示未计入。返工后的Anthropic采用季度GAAP年化，不再称整个收入表都是退出年化。

| 输入 | 旧值 → 新值 | 来源、日期、口径或沿用原因 |
|---|---|---|
| `as_of` | "2026-06-10 (v3.1)" → "2026-11-09 (v3.2)" | 本版核查截止日；来源发布时间必须不晚于2026-11-09。 |
| `core.K_trillion` | 1.3 → 1.3 | 严格/宽共用；沿用 v3.1。行业 K、资产寿命、运维、融资、毛利和在建占比没有同定义的新一手行业统计，未更新。 |
| `core.L_years` | 6.1 → 6.1 | 严格/宽共用；沿用 v3.1。行业 K、资产寿命、运维、融资、毛利和在建占比没有同定义的新一手行业统计，未更新。 |
| `core.blended_depreciation_rate` | 0.164 → 0.164 | 严格/宽共用；沿用 v3.1。行业 K、资产寿命、运维、融资、毛利和在建占比没有同定义的新一手行业统计，未更新。 |
| `core.opex_over_K` | 0.1 → 0.1 | 严格/宽共用；沿用 v3.1。行业 K、资产寿命、运维、融资、毛利和在建占比没有同定义的新一手行业统计，未更新。 |
| `core.debt_rate` | 0.055 → 0.055 | 严格/宽共用；沿用 v3.1。行业 K、资产寿命、运维、融资、毛利和在建占比没有同定义的新一手行业统计，未更新。 |
| `core.debt_share` | 0.3 → 0.3 | 严格/宽共用；沿用 v3.1。行业 K、资产寿命、运维、融资、毛利和在建占比没有同定义的新一手行业统计，未更新。 |
| `core.terminal_gross_margin` | 0.5 → 0.5 | 严格/宽共用；沿用 v3.1。行业 K、资产寿命、运维、融资、毛利和在建占比没有同定义的新一手行业统计，未更新。 |
| `core.cip_share_of_K` | [0.15, 0.2] → [0.15, 0.2] | 严格/宽共用；沿用 v3.1。行业 K、资产寿命、运维、融资、毛利和在建占比没有同定义的新一手行业统计，未更新。 |
| `r_t_strict_billion.anthropic_q3_gaap_annualized` | 30 → 67.8 | 严格；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02）第161页：Q3 GAAP收入16.956×4=67.824，按返工指令用67.8。季度GAAP收入年化，非公司定义Run-Rate Revenue；旧报道65已被超过。 |
| `r_t_strict_billion.openai` | 25 → 24 | 严格；[OpenAI 融资公告](https://openai.com/index/accelerating-the-next-phase-ai/)（2026-03-31）；公司每月约2乘12=24，为年化换算，不是全年实际收入。 |
| `r_t_strict_billion.microsoft_ai_net_of_openai_resale` | 27 → 27 | 严格；沿用 v3.1 净估计27/30，拆分未核实；[微软 FY26 Q3 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3)（2026-04-29） 的37仅是官方总额；[微软 FY27 Q1 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1)（2026-10-28） 没有更新可比AI总额或净额。 |
| `r_t_strict_billion.xai_mistral_cohere_other` | 5 → 5 | 严格；沿用v3.1旧估计，未更新/未核实。返工恢复5/8；SpaceX SI整部门收入没有加入R_T，不存在该部门新数再次叠加。 |
| `r_t_strict_billion.google_gemini_workspace` | 5 → 5 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.ai_saas_net_of_api_resale` | 9 → 9 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.trad_saas_ai_addon` | 10 → 10 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.china_ai` | 10 → 10 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.bedrock_vertex_net` | 5 → 0 | 严格；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02）；市场销售已在Anthropic总额确认；无法核实其余净收入，5→0为不计入，防止重复。 |
| `r_t_strict_billion.hyperscaler_internal_attribution` | 0 → 0 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.consulting_productivity` | 0 → 0 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.long_tail` | 5 → 5 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_note` | "ai_saas gross ~15 minus ~6 paid to model APIs (already inside Anthropic/OpenAI ARR); Anthropic uses the official 2026-04-06 number, the reported $40B stays in the wide basket" → "Anthropic Q3 GAAP revenue 16.956 x 4 = 67.824, stored as 67.8 per rework instruction. This is quarterly GAAP revenue annualized, not company-defined Run-Rate Revenue or ARR. OpenAI official monthly revenue about 2 x 12 = 24. The legacy xAI(SpaceX)/Mistral/Cohere/other estimate 5 is retained, unupdated; SpaceX SI revenue is background only and not added. Strict Bedrock/Vertex residual is excluded because Anthropic marketplace sales are recognized gross. Other v3.1 estimates remain unverified. Application net revenue includes Cursor only once." | 严格；同步S-1/A季度GAAP年化、模型公司旧估计恢复和市场去重复计算的说明；其他旧估计未更新。 |
| `r_t_wide_billion.anthropic_q3_gaap_annualized` | 40 → 67.8 | 宽；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02）第161页：Q3 GAAP收入16.956×4=67.824，按返工指令用67.8。季度GAAP收入年化，非公司定义Run-Rate Revenue；旧报道65已被超过。 |
| `r_t_wide_billion.openai` | 28 → 50 | 宽；[Reuters OpenAI 报道](https://www.investing.com/news/stock-market-news/openais-annualized-revenue-20-billion-less-than-previously-signaled-ft-reports-4939854)（2026-10-08（10-09更新））；报道的近50取约50，仅入宽。 |
| `r_t_wide_billion.microsoft_ai_net_of_openai_resale` | 30 → 30 | 宽；沿用 v3.1 净估计27/30，拆分未核实；[微软 FY26 Q3 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3)（2026-04-29） 的37仅是官方总额；[微软 FY27 Q1 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1)（2026-10-28） 没有更新可比AI总额或净额。 |
| `r_t_wide_billion.xai_mistral_cohere_other` | 8 → 8 | 宽；沿用v3.1旧估计，未更新/未核实。返工恢复5/8；SpaceX SI整部门收入没有加入R_T，不存在该部门新数再次叠加。 |
| `r_t_wide_billion.google_gemini_workspace` | 8 → 8 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.ai_saas_net_of_api_resale` | 12 → 12 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.trad_saas_ai_addon` | 15 → 15 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.china_ai` | 15 → 15 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.bedrock_vertex_net` | 10 → 10 | 宽；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02）；沿用 v3.1 净额10的估计，假定不含Anthropic/OpenAI全部转售，无法独立核实。 |
| `r_t_wide_billion.hyperscaler_internal_attribution` | 35 → 35 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.consulting_productivity` | 10 → 10 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.long_tail` | 8 → 8 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_note` | "ai_saas gross ~20 minus ~8 API resale" → "Anthropic Q3 GAAP annualized 67.8 also replaces the older reported 65. OpenAI almost 50 remains a Reuters reported value. Legacy xAI(SpaceX)/Mistral/Cohere/other estimate 8 is retained, unupdated. AI SaaS gross 20 less API resale 8 = 12 and Bedrock/Vertex residual 10 remain unverified v3.1 assumptions; the latter is assumed to exclude all model resale." | 宽；Anthropic季度GAAP年化替换旧报道值，OpenAI报道仅入宽；其他旧估计未更新。 |
| `r_t_ttm_wide_billion` | 140 → 140 | 宽参考；沿用 v3.1 的140，行业TTM未更新/未核实；不可称为截至11月的最新TTM。 |
| `capex_2026_billion.microsoft` | [190, 195] → [170, 170] | 严格/宽分子外的资本支出背景；[微软 FY27 Q1 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1)（2026-10-28）；自然2026公司指引，非实际支出。 |
| `capex_2026_billion.alphabet` | [180, 190] → [195, 205] | 严格/宽分子外的资本支出背景；[Alphabet Q3 电话会](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx)（2026-10-28）；自然2026公司指引，非实际支出。 |
| `capex_2026_billion.amazon` | [200, 205] → [220, 220] | 严格/宽分子外的资本支出背景；[Amazon Q3 公告](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf)（2026-10-29）；自然2026公司指引，非实际支出。 |
| `capex_2026_billion.meta` | [125, 145] → [135, 145] | 严格/宽分子外的资本支出背景；[Meta Q3 公告](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx)（2026-10-21）；自然2026公司指引，非实际支出。 |
| `capex_2026_billion.oracle` | [60, 70] → [90, 95] | 严格/宽分子外的资本支出背景；[Oracle FY27 Q1 电话会公开转录](https://www.roic.ai/quote/ORCL/transcripts/2027-year/1-quarter)（2026-09-10（会议日））；FY27毛额，不是自然2026；公开转录未复听录音。 |
| `capex_2026_billion.ai_share_of_hyperscaler` | 0.75 → 0.75 | 假设；沿用 v3.1 75%，未更新/未核实；各公司没有同定义的纯AI占比。 |
| `capex_2026_billion.neocloud.coreweave` | "原版未列" → [35, 39] | 背景；[CoreWeave Q2 指引稿](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf)（2026-08-11） 第3页；自然2026指引。 |
| `capex_2026_billion.neocloud.nebius` | "原版未列" → [20, 25] | 背景；[Nebius Q2 电话会公开转录](https://www.fool.com/earnings/call-transcripts/2026/08/19/nebius-nbis-q2-2026-earnings-call-transcript/)（2026-08-19（会议08-12）） CFO Dado Alonso指引段原话；公开转录未复听录音；[Nebius Q2 股东信](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf)（2026-08-12） 第3页确认指引未变。 |
| `capex_2026_billion.neocloud.iren_calendar_2026` | "原版未列" → null | 背景；旧neocloud60–70未能按公司追溯，不再作为可核实合计；IREN和其他未获可比全年数据，不编数字。 |
| `capex_2026_billion.neocloud.other_estimate` | "原版未列" → null | 背景；旧neocloud60–70未能按公司追溯，不再作为可核实合计；IREN和其他未获可比全年数据，不编数字。 |
| `capex_2026_billion.neocloud.note` | "原版未列" → "CoreWeave and Nebius calendar-2026 guidance. IREN: no full calendar-2026 figure verified; FY27 remaining capex 15 is recorded separately. Lambda/Crusoe/other estimates are not newly invented. The old neocloud total 60-70 had no auditable company allocation and is retired, not added on top." | 背景；旧neocloud60–70未能按公司追溯，不再作为可核实合计；IREN和其他未获可比全年数据，不编数字。 |
| `us_gdp_trillion` | 30 → 33.010036 | GDP分母；[BEA NIPA 1.1.5 工作簿](https://apps.bea.gov/national/Release/XLS/Survey/Section1All_xls.xlsx)（2026-10-29）；T10105-Q，A191RC，2026Q3列33010036百万美元 / 1000000 =33.010036万亿；季调年率，不是2026全年GDP。 |
| `time_path.annual_capex_billion` | 600 → 600 | 情景；公式、年 capex 和增速假设沿用 v3.1；起点同步宽口径收入，不是新预测。 |
| `time_path.r_t_start_billion` | 220 → 270 | 情景起点220→270，与本版宽收入一致；年600、增速和公式未变。 |
| `time_path.cagr_scenarios` | [0.5, 0.25, 0.1] → [0.5, 0.25, 0.1] | 情景；公式、年 capex 和增速假设沿用 v3.1；起点同步宽口径收入，不是新预测。 |
| `time_path.years` | [2026, 2027, 2028, 2029, 2030, 2031, 2032] → [2026, 2027, 2028, 2029, 2030, 2031, 2032] | 情景；公式、年 capex 和增速假设沿用 v3.1；起点同步宽口径收入，不是新预测。 |
| `sensitivity.r_t_levels` | [300, 400, 180, 130] → [300, 400, 180, 165] | 原敏感性方法保留；r_t_levels末项130→165同步严格收入，其余输入未变。 |
| `sensitivity.k_levels_trillion` | [1.7, 2.0] → [1.7, 2.0] | 原敏感性方法保留；r_t_levels末项130→165同步严格收入，其余输入未变。 |
| `sensitivity.gpu_life_extra_dep_billion` | 43 → 43 | 原敏感性方法保留；r_t_levels末项130→165同步严格收入，其余输入未变。 |
| `sensitivity.opex_15pct_extra_billion` | 65 → 65 | 原敏感性方法保留；r_t_levels末项130→165同步严格收入，其余输入未变。 |
| `sensitivity.wacc_extra_billion` | 80 → 80 | 原敏感性方法保留；r_t_levels末项130→165同步严格收入，其余输入未变。 |
| `historical.uk_rail_1846.K_committed_mGBP` | 170 → 170 | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.uk_rail_1846.L_years` | 30 → 30 | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.uk_rail_1846.opex_uniform_over_K` | [0.1, 0.15] → [0.1, 0.15] | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.uk_rail_1846.operating_ratio_calibrated` | [0.45, 0.55] → [0.45, 0.55] | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.uk_rail_1846.revenue_mGBP` | [10, 15] → [10, 15] | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.uk_rail_1846.debt_share` | 0.6 → 0.6 | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.uk_rail_1846.debt_rate` | [0.045, 0.05] → [0.045, 0.05] | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.us_rail_1873.K_busd` | 2.7 → 2.7 | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.us_rail_1873.L_years` | 30 → 30 | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.us_rail_1873.opex_uniform_over_K` | 0.15 → 0.15 | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.us_rail_1873.operating_ratio_calibrated` | 0.65 → 0.65 | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.us_rail_1873.revenue_busd` | 0.52 → 0.52 | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.us_rail_1873.debt_share` | 0.7 → 0.7 | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `historical.us_rail_1873.debt_rate` | 0.07 → 0.07 | 历史对照；沿用 v3.1。固定历史假设，本次未重新核实原始档案。 |
| `core_note` | "原版未列" → "All core assumptions, including K, are carried from v3.1; not remeasured as of November. The updated EPR is conditional on this unchanged capital stock." | 严格/宽共用；沿用 v3.1。行业 K、资产寿命、运维、融资、毛利和在建占比没有同定义的新一手行业统计，未更新。 |
| `capex_period_note` | "原版未列" → "Microsoft, Alphabet, Amazon and Meta: CY2026 guidance. Oracle: FY2027 (June 2026-May 2027) gross capex guidance, not CY2026 or net cash capex. Totals mix periods and company accounting definitions; not a measured US domestic investment total. SpaceX SI partial-year actual capex is separate, not annualized or added to annual guidance totals." | 说明字段；见本文相应条目。 |
| `time_path_note` | "原版未列" → "Existing illustrative scenario: annual capex 600 and CAGR 50/25/10 percent unchanged; not current guidance or a new forecast. Only starting terminal revenue is updated." | 情景；公式、年 capex 和增速假设沿用 v3.1；起点同步宽口径收入，不是新预测。 |
| `disclosed_billion.anthropic.gaap_2025_q4` | "原版未列" → 2.04 | 背景/独立披露，不直接叠加到终端收入；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02） |
| `disclosed_billion.anthropic.gaap_2026_q1` | "原版未列" → 4.731 | 背景/独立披露，不直接叠加到终端收入；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02） |
| `disclosed_billion.anthropic.gaap_2026_q2` | "原版未列" → 11.555 | 背景/独立披露，不直接叠加到终端收入；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02） |
| `disclosed_billion.anthropic.gaap_2026_q3` | "原版未列" → 16.956 | 背景/独立披露，不直接叠加到终端收入；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02） |
| `disclosed_billion.anthropic.marketplace_share_2026_9m` | "原版未列" → 0.44 | 背景/独立披露，不直接叠加到终端收入；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02） |
| `disclosed_billion.anthropic.committed_spend` | "原版未列" → 895.4 | 背景/独立披露，不直接叠加到终端收入；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02） |
| `disclosed_billion.anthropic.commitments_due_next_12m` | "原版未列" → 69.8 | 背景/独立披露，不直接叠加到终端收入；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02） |
| `disclosed_billion.anthropic.latest_s1a_run_rate` | "原版未列" → null | 背景/独立披露，不直接叠加到终端收入；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02） |
| `disclosed_billion.spacex.xai_wholly_owned_since` | "原版未列" → "2026-02-02" | 背景/独立披露，不直接叠加到终端收入；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22） |
| `disclosed_billion.spacex.latest_quarter` | "原版未列" → "2026-09-30" | 背景/独立披露，不直接叠加到终端收入；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22） |
| `disclosed_billion.spacex.si_revenue_q3` | "原版未列" → 7.56 | 背景/独立披露，不直接叠加到终端收入；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22） |
| `disclosed_billion.spacex.si_solutions_infrastructure_revenue_q3` | "原版未列" → 7.022 | 背景/独立披露，不直接叠加到终端收入；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22） |
| `disclosed_billion.spacex.si_revenue_9m` | "原版未列" → 10.939 | 背景/独立披露，不直接叠加到终端收入；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22） |
| `disclosed_billion.spacex.si_capex_q3` | "原版未列" → 16.444 | 背景/独立披露，不直接叠加到终端收入；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22） |
| `disclosed_billion.spacex.si_capex_9m` | "原版未列" → 39.995 | 背景/独立披露，不直接叠加到终端收入；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22） |
| `disclosed_billion.spacex.pure_terminal_ai_run_rate` | "原版未列" → null | 背景/独立披露，不直接叠加到终端收入；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22） |
| `disclosed_billion.spacex.ai_capex_full_year_guidance` | "原版未列" → null | 背景/独立披露，不直接叠加到终端收入；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22） |
| `disclosed_billion.spacex.note` | "原版未列" → "10-Q Note 1 pp10-11; Note 3 p12; Note 18 pp32-33; MD&A Revenue-SI pp41-42 and 48. SI includes X ads, hosting, data licensing, Grok and Cursor; no whole-segment revenue enters R_T. Do not count xAI separately from SpaceX or Cursor twice." | 背景/独立披露，不直接叠加到终端收入；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22） |
| `disclosed_billion.spacex.ai_capex_2026_q1_from_s1a` | "原版未列" → 7.723 | 背景；[SpaceX最新S-1/A](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm)（2026-06-03），“AI Capital Expenditures”段；后续当前数改用Q3。 |
| `disclosed_billion.oracle.period` | "原版未列" → "FY2027 Q1 ended 2026-08-31" | 背景/独立披露，不直接叠加到终端收入；[Oracle FY27 Q1 公告](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)（2026-09-10） |
| `disclosed_billion.oracle.capex_quarter` | "原版未列" → 28.499 | 背景/独立披露，不直接叠加到终端收入；[Oracle FY27 Q1 公告](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)（2026-09-10） |
| `disclosed_billion.oracle.net_cash_capex_quarter` | "原版未列" → 17.966 | 背景/独立披露，不直接叠加到终端收入；[Oracle FY27 Q1 公告](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)（2026-09-10） |
| `disclosed_billion.oracle.rpo` | "原版未列" → 664 | 背景/独立披露，不直接叠加到终端收入；[Oracle FY27 Q1 公告](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)（2026-09-10） |
| `disclosed_billion.oracle.oci_revenue_quarter` | "原版未列" → 7.4 | 背景/独立披露，不直接叠加到终端收入；[Oracle FY27 Q1 公告](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)（2026-09-10） |
| `disclosed_billion.oracle.gross_capex_fy2027` | "原版未列" → [90, 95] | 背景/独立披露，不直接叠加到终端收入；[Oracle FY27 Q1 电话会公开转录](https://www.roic.ai/quote/ORCL/transcripts/2027-year/1-quarter)（2026-09-10（会议日）） |
| `disclosed_billion.oracle.net_cash_capex_fy2027_max` | "原版未列" → 70 | 背景/独立披露，不直接叠加到终端收入；[Oracle FY27 Q1 电话会公开转录](https://www.roic.ai/quote/ORCL/transcripts/2027-year/1-quarter)（2026-09-10（会议日）） |
| `disclosed_billion.coreweave.period` | "原版未列" → "2026 Q2" | 背景/独立披露，不直接叠加到终端收入；[CoreWeave Q2 公告](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/default.aspx)（2026-08-11） |
| `disclosed_billion.coreweave.revenue_quarter` | "原版未列" → 2.575 | 背景/独立披露，不直接叠加到终端收入；[CoreWeave Q2 公告](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/default.aspx)（2026-08-11） |
| `disclosed_billion.coreweave.backlog` | "原版未列" → 104.2 | 背景/独立披露，不直接叠加到终端收入；[CoreWeave Q2 演示稿](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Presentation.pdf)（2026-08-11） |
| `disclosed_billion.coreweave.revenue_guidance_2026` | "原版未列" → [12.4, 13.2] | 背景/独立披露，不直接叠加到终端收入；[CoreWeave Q2 指引稿](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf)（2026-08-11） |
| `disclosed_billion.coreweave.capex_2026` | "原版未列" → [35, 39] | 背景/独立披露，不直接叠加到终端收入；[CoreWeave Q2 指引稿](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf)（2026-08-11） |
| `disclosed_billion.nebius.period` | "原版未列" → "2026 Q2" | 背景/独立披露，不直接叠加到终端收入；[Nebius Q2 股东信](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf)（2026-08-12） |
| `disclosed_billion.nebius.revenue_quarter` | "原版未列" → 0.5823 | 背景/独立披露，不直接叠加到终端收入；[Nebius Q2 股东信](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf)（2026-08-12） |
| `disclosed_billion.nebius.ai_cloud_revenue_quarter` | "原版未列" → 0.5749 | 背景/独立披露，不直接叠加到终端收入；[Nebius Q2 股东信](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf)（2026-08-12） |
| `disclosed_billion.nebius.capex_quarter_approx` | "原版未列" → 5.7 | 背景/独立披露，不直接叠加到终端收入；[Nebius Q2 股东信](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf)（2026-08-12） |
| `disclosed_billion.nebius.customer_commitments_lower_bound` | "原版未列" → 40 | 背景/独立披露，不直接叠加到终端收入；[Nebius Q2 股东信](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf)（2026-08-12） |
| `disclosed_billion.nebius.comparable_backlog` | "原版未列" → null | 背景/独立披露，不直接叠加到终端收入；[Nebius Q2 股东信](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf)（2026-08-12） |
| `disclosed_billion.nebius.capex_2026` | "原版未列" → [20, 25] | 背景/独立披露，不直接叠加到终端收入；[Nebius Q2 电话会公开转录](https://www.fool.com/earnings/call-transcripts/2026/08/19/nebius-nbis-q2-2026-earnings-call-transcript/)（2026-08-19（会议08-12）） |
| `disclosed_billion.iren.period` | "原版未列" → "FY2027 Q1 ended 2026-09-30" | 背景/独立披露，不直接叠加到终端收入；[IREN FY27 Q1 公告](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results)（2026-11-05） |
| `disclosed_billion.iren.revenue_quarter` | "原版未列" → 0.228 | 背景/独立披露，不直接叠加到终端收入；[IREN FY27 Q1 公告](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results)（2026-11-05） |
| `disclosed_billion.iren.ai_cloud_revenue_quarter` | "原版未列" → 0.2 | 背景/独立披露，不直接叠加到终端收入；[IREN FY27 Q1 公告](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results)（2026-11-05） |
| `disclosed_billion.iren.backlog` | "原版未列" → 20.3 | 背景/独立披露，不直接叠加到终端收入；[IREN FY27 Q1 公告](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results)（2026-11-05） |
| `disclosed_billion.iren.remaining_fy2027_capex` | "原版未列" → 15 | 背景/独立披露，不直接叠加到终端收入；[IREN FY27 Q1 公告](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results)（2026-11-05） |
| `disclosed_billion.iren.calendar_2026_capex` | "原版未列" → null | 背景/独立披露，不直接叠加到终端收入；[IREN FY27 Q1 公告](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results)（2026-11-05） |
| `disclosed_billion.other_neocloud.members` | "原版未列" → ["Lambda", "Crusoe", "others"] | 背景；未单独披露/未核实，无可加总估计，不计入。[Lambda 融资公告](https://lambda.com/blog/lambda-closes-1-billion-senior-secured-credit-facility)（2026-05-07） 仅为融资，不能替代 capex。 |
| `disclosed_billion.other_neocloud.capex_2026_estimate` | "原版未列" → null | 背景；未单独披露/未核实，无可加总估计，不计入。[Lambda 融资公告](https://lambda.com/blog/lambda-closes-1-billion-senior-secured-credit-facility)（2026-05-07） 仅为融资，不能替代 capex。 |
| `disclosed_billion.other_neocloud.revenue_quarter` | "原版未列" → null | 背景；未单独披露/未核实，无可加总估计，不计入。[Lambda 融资公告](https://lambda.com/blog/lambda-closes-1-billion-senior-secured-credit-facility)（2026-05-07） 仅为融资，不能替代 capex。 |
| `disclosed_billion.other_neocloud.backlog` | "原版未列" → null | 背景；未单独披露/未核实，无可加总估计，不计入。[Lambda 融资公告](https://lambda.com/blog/lambda-closes-1-billion-senior-secured-credit-facility)（2026-05-07） 仅为融资，不能替代 capex。 |
| `disclosed_billion.other_neocloud.note` | "原版未列" → "No comparable quarterly filing or annual capex verified; financing/project announcements are not annual capex. Not counted; no estimate invented." | 背景；未单独披露/未核实，无可加总估计，不计入。[Lambda 融资公告](https://lambda.com/blog/lambda-closes-1-billion-senior-secured-credit-facility)（2026-05-07） 仅为融资，不能替代 capex。 |
| `disclosed_billion.nvidia.period` | "原版未列" → "FY2027 Q2 ended 2026-07-26" | 背景/独立披露，不直接叠加到终端收入；[英伟达 FY27 Q2 公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx)（2026-08-26） |
| `disclosed_billion.nvidia.revenue_quarter` | "原版未列" → 96.2 | 背景/独立披露，不直接叠加到终端收入；[英伟达 FY27 Q2 公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx)（2026-08-26） |
| `disclosed_billion.nvidia.data_center_revenue_quarter` | "原版未列" → 89.0 | 背景/独立披露，不直接叠加到终端收入；[英伟达 FY27 Q2 公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx)（2026-08-26） |
| `disclosed_billion.nvidia.revenue_guidance_next_quarter` | "原版未列" → 108 | 背景/独立披露，不直接叠加到终端收入；[英伟达 FY27 Q2 公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx)（2026-08-26） |
| `disclosed_billion.nvidia.supply_capacity_commitments` | "原版未列" → 279 | 背景/独立披露，不直接叠加到终端收入；[英伟达 FY27 Q2 10-Q](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf)（2026-08-26） |
| `disclosed_billion.goldman.published` | "原版未列" → "2026-08-07" | 背景/独立披露，不直接叠加到终端收入；[Goldman 全球 AI 投资估计](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026)（2026-08-07） |
| `disclosed_billion.goldman.global_ai_investment_estimate_2026` | "原版未列" → 1000 | 背景/独立披露，不直接叠加到终端收入；[Goldman 全球 AI 投资估计](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026)（2026-08-07） |
| `disclosed_billion.goldman.us_ai_investment_estimate_2026` | "原版未列" → 581 | 背景/独立披露，不直接叠加到终端收入；[Goldman 全球 AI 投资估计](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026)（2026-08-07） |
| `disclosed_billion.goldman.us_gdp_share_estimate` | "原版未列" → 0.018 | 背景/独立披露，不直接叠加到终端收入；[Goldman 全球 AI 投资估计](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026)（2026-08-07） |
| `disclosed_billion.goldman.global_gdp_share_estimate` | "原版未列" → 0.009 | 背景/独立披露，不直接叠加到终端收入；[Goldman 全球 AI 投资估计](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026)（2026-08-07） |
| `disclosed_billion.stlouis_fed.published` | "原版未列" → "2026-01-12" | 背景/独立披露，不直接叠加到终端收入；[圣路易斯联储原文](https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth)（2026-01-12） |
| `disclosed_billion.stlouis_fed.period` | "原版未列" → "2025 first three quarters / Q3 only" | 背景/独立披露，不直接叠加到终端收入；[圣路易斯联储原文](https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth)（2026-01-12） |
| `disclosed_billion.stlouis_fed.share_of_real_growth_9m` | "原版未列" → 0.39 | 背景/独立披露，不直接叠加到终端收入；[圣路易斯联储原文](https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth)（2026-01-12） |
| `disclosed_billion.stlouis_fed.share_of_real_growth_q3` | "原版未列" → 0.11 | 背景/独立披露，不直接叠加到终端收入；[圣路易斯联储原文](https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth)（2026-01-12） |
| `disclosed_billion.stlouis_fed.contribution_q3_pp` | "原版未列" → 0.48 | 背景/独立披露，不直接叠加到终端收入；[圣路易斯联储原文](https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth)（2026-01-12） |
| `k_rollforward.base_as_of` | "原版未列" → null | 部分资本时点核对；origin/main正文3.1未给K测量日，2.1提到H1部署，5月25日/6月10日只是文稿日期，不能确认为6月30日。目标9月30日；Oracle6–8月错期、其余流量不全，完整K/P/EPR不输出数值。见下方计算说明。 |
| `k_rollforward.target_as_of` | "原版未列" → "2026-09-30" | 部分资本时点核对；origin/main正文3.1未给K测量日，2.1提到H1部署，5月25日/6月10日只是文稿日期，不能确认为6月30日。目标9月30日；Oracle6–8月错期、其余流量不全，完整K/P/EPR不输出数值。见下方计算说明。 |
| `k_rollforward.base_date_evidence` | "原版未列" → "origin/main README section 3.1 gives cumulative 2022-2026 stock without a measurement date; section 2.1 mentions H1 deployments; paper dates May 25 / June 10 do not establish June 30 stock." | 部分资本时点核对；origin/main正文3.1未给K测量日，2.1提到H1部署，5月25日/6月10日只是文稿日期，不能确认为6月30日。目标9月30日；Oracle6–8月错期、其余流量不全，完整K/P/EPR不输出数值。见下方计算说明。 |
| `k_rollforward.actual_period_start` | "原版未列" → "2026-07-01" | 部分资本时点核对；origin/main正文3.1未给K测量日，2.1提到H1部署，5月25日/6月10日只是文稿日期，不能确认为6月30日。目标9月30日；Oracle6–8月错期、其余流量不全，完整K/P/EPR不输出数值。见下方计算说明。 |
| `k_rollforward.cash_ppe_q3_billion.microsoft` | "原版未列" → 39.367 | 已知Q3实际现金PP&E；[微软FY27 Q1公告](https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast)（2026-10-28），现金流量表39,367百万美元，不用45.2报告capex替代现金数。 |
| `k_rollforward.cash_ppe_q3_billion.alphabet` | "原版未列" → 51.355 | Q3实际现金PP&E；[Alphabet SEC公告](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm)（2026-10-28）第6页，51,355百万美元；电话会51.4是四舍五入值。 |
| `k_rollforward.cash_ppe_q3_billion.amazon` | "原版未列" → 77.259 | Q3实际毛现金PP&E；[Amazon Q3公告](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf)（2026-10-29），第6页现金流量表77,259百万美元；非净现金75.878。 |
| `k_rollforward.cash_ppe_q3_billion.meta` | "原版未列" → 33.942 | Q3实际现金PP&E；[Meta Q3公告](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx)（2026-10-21），现金流量表33,942百万美元。 |
| `k_rollforward.company_reported_capex_q3_billion.microsoft` | "原版未列" → 45.2 | 背景；[微软FY27 Q1电话会](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1)（2026-10-28）capex45.2，含融资租赁，非同定义现金数或纯新资产。 |
| `k_rollforward.company_reported_capex_q3_billion.alphabet` | "原版未列" → 51.4 | Q3实际；[Alphabet Q3公司电话会](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx)（2026-10-28），Anat Ashkenazi称CapEx51.4。 |
| `k_rollforward.company_reported_capex_q3_billion.amazon` | "原版未列" → 77.259 | Q3实际毛现金PP&E；[Amazon Q3公告](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf)（2026-10-29），第6页现金流量表77,259百万美元；非净现金75.878。 |
| `k_rollforward.company_reported_capex_q3_billion.meta` | "原版未列" → 34.906 | 背景；[Meta Q3公告](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx)（2026-10-21），33.942现金PP&E+0.964租赁本金=34.906，不把还款全当新增资产。 |
| `k_rollforward.unmatched_oracle_period` | "原版未列" → "2026-06-01 to 2026-08-31; Q1 FY27 actual 28.499, not July-September" | 部分资本时点核对；origin/main正文3.1未给K测量日，2.1提到H1部署，5月25日/6月10日只是文稿日期，不能确认为6月30日。目标9月30日；Oracle6–8月错期、其余流量不全，完整K/P/EPR不输出数值。见下方计算说明。 |
| `k_rollforward.aligned_k_trillion` | "原版未列" → null | 部分资本时点核对；origin/main正文3.1未给K测量日，2.1提到H1部署，5月25日/6月10日只是文稿日期，不能确认为6月30日。目标9月30日；Oracle6–8月错期、其余流量不全，完整K/P/EPR不输出数值。见下方计算说明。 |
| `k_rollforward.note` | "原版未列" → "Only comparable Q3 cash PP&E flows can be subtotalled; 75% AI share is the unchanged paper assumption. Cash PP&E excludes noncash leases and is not complete asset additions. Do not treat reported finance-lease principal payments as new assets. No full roll to September 30: base date unknown, Oracle unmatched, neocloud/sovereign flows and disposals incomplete. Partial identity uses annual 16.4% depreciation / 4; no assumed June 30 starting stock." | 部分资本时点核对；origin/main正文3.1未给K测量日，2.1提到H1部署，5月25日/6月10日只是文稿日期，不能确认为6月30日。目标9月30日；Oracle6–8月错期、其余流量不全，完整K/P/EPR不输出数值。见下方计算说明。 |
| `r_t_strict_billion.anthropic_official` | 30 → 已替换，见新增输入 | Anthropic见同组anthropic_q3_gaap_annualized；季度GAAP年化67.8，不再使用旧官方/报道值。 |
| `r_t_wide_billion.anthropic_reported` | 40 → 已替换，见新增输入 | Anthropic见同组anthropic_q3_gaap_annualized；季度GAAP年化67.8，不再使用旧官方/报道值。 |
| `capex_2026_billion.neocloud` | [60, 70] → 已替换，见新增输入 | 旧60–70保留为版本记录，当前逐家表只计CoreWeave/Nebius已知55–64，不叠加旧总数。 |

## 一手申报中的收入与重复计算

Anthropic S-1/A 第161页列出2026 Q1/Q2/Q3 GAAP收入4.731、11.555、16.956；合计33.242，连同2025 Q4的2.040得TTM35.282。第58页和财务附注2披露前九个月44%收入来自云厂商市场，附注2“Revenue Recognition”写明公司是主要责任人，按总额确认。市场费用不能让同一笔终端销售再计一次。严格表的Bedrock/Vertex残余项从5改为未计入0；宽表10仅保留原版“已排除全部模型转售”的估计，未核实。微软净额27/30和应用净额9/12仍是旧假设，不能由44%机械扣除。[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02）

S-1/A第199页10月末公司定义的Run-Rate Revenue仍空白。本次按返工要求，把第161页Q3 GAAP收入16.956×4=67.824按一位小数列67.8，严格与宽均使用。命名为“季度GAAP收入年化”，不冒称公司定义的Run-Rate Revenue；旧报道65低于新年化数。季度均值本身不能保证期末值更高，只有季内收入持续增长时才能作下限解释。[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02）

SpaceX Q3 10-Q附注1第10–11页确认2026-02-02收购后xAI为全资子公司，附注18第32–33页已合并。Q3 SI收入7.560、其中Solutions & Infrastructure7.022；前九月10.939。部门含X广告、云服务、Grok、X订阅、数据许可和Cursor，纯终端AI年化未单独披露。返工恢复旧xAI(SpaceX)/Mistral/Cohere/其他严格5/宽8，明确未更新。整部门收入没有新加R_T，Cursor只留在原应用净额，不再加一次。[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22）

SpaceX相同文件附注18：Q3 SI资本支出16.444，前九个月39.995。全年AI指引以及GPU采购、数据中心之间的单独金额未单独披露，不外推全年。早期招股材料“AI Capital Expenditures”第93–94页解释其增长来自地面数据中心建设与设备；当前数值以较新的Q3 10-Q为准。[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22）；[SpaceX 上市申报/招股材料](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm)（2026-06-12，424B4最终招股书）

## 资本支出期间与新云厂商

Oracle FY27 Q1截至2026-08-31：毛资本支出28.499，净现金支出17.966，OCI收入约7.4，RPO664。FY27全年90–95、净现金最多70来自CFO Hilary Maxson的财报会原话公开转录；未复听录音，来源性质在此保留。这里替换旧60–70，但FY27为2026-06至2027-05，不能写成自然2026。Big-5的810–835只是四家自然年指引与Oracle财年指引的混合相加。[Oracle FY27 Q1 公告](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx)（2026-09-10）；[Oracle FY27 Q1 电话会公开转录](https://www.roic.ai/quote/ORCL/transcripts/2027-year/1-quarter)（2026-09-10（会议日））

CoreWeave自然2026指引35–39；Nebius20–25来自CFO电话会原话公开转录（未复听录音），公司股东信确认维持全年指引。已列两家指引合计55–64。IREN只核实截至9月底剩余FY27支出15，不能放进自然年合计。Lambda、Crusoe等没有本次核实到的可比申报/全年数据，合并为“其他（估计，金额未核实）”，不填新估计。旧neocloud60–70缺少逐家底稿，已取消总数，不能把它再加到两家之上。[CoreWeave Q2 指引稿](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf)（2026-08-11）；[Nebius Q2 股东信](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf)（2026-08-12）；[Nebius Q2 电话会公开转录](https://www.fool.com/earnings/call-transcripts/2026/08/19/nebius-nbis-q2-2026-earnings-call-transcript/)（2026-08-19（会议08-12））；[IREN FY27 Q1 公告](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results)（2026-11-05）

新云厂商的backlog含义不完全相同。CoreWeave为104.2（其中RPO103.7），IREN为20.3（含履约义务、租赁和其他估计金额），Nebius只核实公司说的>40客户承诺，不改称同定义backlog，也不把三项直接相加。云厂商收入是模型公司的投入成本，不能整项加进终端收入。[CoreWeave Q2 演示稿](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Presentation.pdf)（2026-08-11）；[IREN FY27 Q1 公告](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results)（2026-11-05）；[Nebius Q2 股东信](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf)（2026-08-12）

全球公司指引除以美国GDP只作规模对照。它不是美国境内投资占比。SpaceX、IREN的部分期间实际/剩余支出单列，不参加年度指引合计。K不能由这些年度流量直接替代；不能再把Oracle算进Big-5后又算一次“其他实体”。

## README 正文其余承重数字核查

下表列出输入之外的公司数字和旧估算。未列新值的一律不冒称截至11月已核实；历史、正常行业和原有情景数字只沿用原版。

| 项目 | 旧值 → 本版 | 来源、日期、处理 |
|---|---|---|
| 英伟达季度总收入 / DC收入 | Q1 81.6 /75.2 → Q2 96.2 /89.0 | [英伟达 FY27 Q2 公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx)（2026-08-26）；背景，不进R_T。 |
| 英伟达下一季收入指引 | Q2 91±2% → Q3 108±2% | [英伟达 FY27 Q2 公告](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx)（2026-08-26）；指引，不是已实现收入。 |
| 英伟达供货与产能承诺 | 95.2 →279 | [英伟达 FY27 Q2 10-Q](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf)（2026-08-26），附注10；不是对客户股权投资。 |
| 英伟达Q3发布时间 | 任务预计11月19日左右 → 官方安排11月17日 | [英伟达下次财报安排](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/)（2026-10-28）；截至截止日尚未发布，使用Q2。 |
| CoreWeave季度收入 / backlog | 2.08 /99.4 →2.575 /104.2 | [CoreWeave Q2 公告](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/default.aspx)（2026-08-11）；[CoreWeave Q2 演示稿](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Presentation.pdf)（2026-08-11） 第8/13/15页。 |
| CoreWeave全年收入指引 | 12–13 →12.4–13.2 | [CoreWeave Q2 指引稿](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf)（2026-08-11） 第3页。 |
| backlog/季度 /前瞻年收入 | 48x /约8x →40.5x /8.1x | 上行数据由epr.py计算；前瞻分母取指引中点12.8。 |
| Anthropic估值 /融资 | 380、850–900预期 →965 /65 | [Anthropic Series H](https://www.anthropic.com/news/series-h)（2026-05-28）；已宣布，取消旧融资预期。 |
| OpenAI估值 /融资 | 852 /122 →852 /122 | [OpenAI 融资公告](https://openai.com/index/accelerating-the-next-phase-ai/)（2026-03-31）重新核实；并非11月新融资。 |
| OpenAI AWS采购 | 38 →原38加100，合约合计138（不同期限） | [OpenAI 与 Amazon 协议](https://openai.com/index/amazon-partnership/)（2026-02-27）；新增100为8年，不能称同一7年合同。 |
| OpenAI总名义承诺 | 1400 →沿用v3.1，未更新/未核实 | 未找到当前完整一手总表，有重叠，不由各行机械加总；保留作者“最脆弱”判断并加注该总数未更新、不同日期不能确证排序。 |
| OpenAI Oracle300 / Stargate500及400+ / AMD90 / NVIDIA100 / Azure250 / CoreWeave22.4 /Broadcom50–100 | 数字沿用v3.1，未更新/未核实；正文原表保留，逐行标旧值 | 原承诺和供应商股权投资性质不同，未计入K或终端收入；AMD/Broadcom美元数缺合同一手定价，不能称已核实。 |
| Anthropic总承诺 | 200–300+ →895.4 | [Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02） 第174–175页 Contractual Obligations及导言；含短期、期后及未开始租赁，319.993表内小计不是全部；69.8在后12个月到期。 |
| Anthropic分伙伴：AWS5/25/100/5GW，Google10/40/5GW，NVIDIA10/1GW，微软5/30，Broadcom21，美国基础设施50 | 沿用v3.1，未逐项重新核实；合计比较用S-1/A，旧分项不求和 | 旧分项含融资、采购、容量和券商预测，不能视为同类采购承诺。 |
| Anthropic承诺/ARR /OpenAI承诺/ARR | 5–7.5x /56x →13.2x（季度GAAP年化67.8）；OpenAI58.3x（24）或28.0x（报道50），仅条件对照 | epr.py输入推算；OpenAI总额未更新，不能证明可比时点的风险排序。 |
| Goldman全球AI投资基线 | 765 →约1000；美国581 | [Goldman 全球 AI 投资估计](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026)（2026-08-07）；研究估计，不是公司披露，亦不替代本文capex算法。 |
| Goldman AI capex/GDP | 美国0.8%、全球0.6–0.7% →其估计美国1.8%、全球0.9% | [Goldman 全球 AI 投资估计](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026)（2026-08-07）；地理调整后估计，与本文全球公司/美国GDP不同。 |
| 联储39% /第三季度 | 误写单季39% →前三季39%，单季11%或0.48百分点 | [圣路易斯联储原文](https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth)（2026-01-12）；实际增长，不是名义增长；修正旧文。 |
| Furman92%、Goldman1.5pp/0.1–0.2pp、旧净贡献0.1–0.5pp、进口占70%+ | 沿用v3.1数值但未核实，保留原作者净贡献判断并加未更新说明 | 不能把“增长贡献占比%”和“百分点pp”直接说成相差100/1000倍；原比较句保留并加注；纯单位错误的“1000倍”句改正。 |
| 四家公司FCF300+、CoreWeave租赁杠杆4.2x、推理成本下降10–30倍、18–24月硬件节奏、GPU残值24个月、H1003美元/时、B2005美元/时 | 沿用v3.1，未更新/未核实；作者判断保留，注明旧数字未更新 | 未重建同期间报表和市场报价，正文列为旧背景假设。 |
| 微软Copilot渗透率3.3–4.4%、席位400M | 沿用v3.1旧值，未更新/不可作当前渗透率 | [微软 FY27 Q1 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1)（2026-10-28） 明示未更新Copilot数量；不以旧席位推算11月。 |
| NVIDIA循环股权投资40+ /OpenAI30 | 沿用v3.1、未更新；另列10-Q股权投资99、未来承诺25 | [英伟达 FY27 Q2 10-Q](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf)（2026-08-26）；存量与流量不同，不能把99+25说成“2026新投124”。 |
| K拆解780–880、90–130、200–300；合计1.07–1.31T；2025 AI capex260、2026H1约260 | 沿用v3.1，未更新/未核实 | 与当前已部署资产和折旧口径不可直接对应；Oracle原说明可能重复，不能据此提高K。 |
| capex历史列2024：56/53/78/37/7/合计231/neocloud15；2025：95/75/105/65/25/合计365/neocloud35/行业400；年初620 | 沿用v3.1，未更新/未逐家核实；原表保留，历史列标未更新 | 不是本次最新公司披露，且财年/自然年不同，避免旧列误导。 |
| CreditSights750；Goldman2031的1.6T；旧全球700–750/110T；合理90%区间1.1–2.9及1.8–3.8 | 沿用v3.1但未核实，作者原判断保留，注明旧值未更新或原区间未重新校准 | 无可复算同定义新证据；情景敏感性不等于统计置信区间。 |
| 正常行业0.69/0.76/0.80/0.90/0.92和0.65–0.95区间 | 沿用v3.1粗估，未更新/未核实 | 固定参照，不称已测得11月行业平均。 |
| 1846：K170、GDP550–600、capex7–8%、寿命30/50+、债务60%、利率4.5–5%、收入10–15、opex10–15%或收入45–55% | 沿用v3.1历史假设 | epr.py统一口径完整范围1.8–3.6x（原文2.5–3只为概括，现列全范围），校准1.0–1.9x；未新查历史档案。 |
| 1873：K2.7、GDP7、38%、寿命30/50+、债务70%、利率7%、收入0.52、opex15%/收入65% | 沿用v3.1历史假设 | epr.py复算1.21x/1.08x；未新查历史档案。 |
| 2000电信：K500、capex120、GDP10.25、1.2%、寿命15/15–20、opex10–12%、债务60%、利率8%、IP收入30–50、EPR2.5–4/约3、整体0.5–0.8 | 沿用v3.1历史假设 | 未更新/未新核实，不是11月数据。 |
| 2007住房：97%、K24T、债务10T、折旧2%/480、opex700/3%、利息600、压力1.78T、租金1.7–2T、EPR0.9–1.1、价格收入3→5 | 沿用v3.1历史假设 | 未更新/未新核实，保留作结构对照。 |
| 历史背景：铁路股跌50–80%、里程35k→70k、89家/25%破产；电信债500+、80M英里、债12.4、亮纤2.7%、价格跌55%、市值2T；日本跌60/80%、钢铁0.5–0.7/跌70%、页岩油1.5–2/跌75%/~100家；房价跌35%、比特币80% | 沿用v3.1历史背景 | 本轮未查原始档案，不用这些数作新的精确历史排序。 |
| 所有情景：年capex600、L6.1、CAGR50/25/10%、K1.7/2.0、额外成本43/65/80、WACC8%、在建15–20% | 沿用v3.1假设，只同步输入起点和输出 | 全部由epr.py重算；不是已发生的未来数据。 |

## 分类检索记录与未更新项

模型公司、Google AI、专用应用、传统SaaS、中国AI、Bedrock/Vertex、内部归因、咨询和长尾逐项检查。单家公司披露不能替代整组扣重叠合计。Salesforce Agentforce和Data 360混合ARR近3.9并非纯AI增量；ServiceNow订阅收入亦非Now Assist独立净收入；百度和阿里披露包含广告、云算力或其他业务，不能整项移入R_T。保留旧9/12、10/15、10/15、Google5/8等，并标未核实。内部归因35、咨询10和长尾5/8没有可直接核实的行业数。[Salesforce FY27 Q2](https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Second-Quarter-Fiscal-2027-Results/default.aspx)（2026-08-26）；[ServiceNow Q3](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Third-Quarter-2026-Financial-Results/default.aspx)（2026-10-28）；[百度 Q2](https://ir.baidu.com/news-releases/news-release-details/baidu-announces-second-quarter-2026-results)（2026-08）；[阿里六月季公告](https://home.alibabagroup.com/en-US/document-2027233133950140416)（2026-08-20）

计算保留P公式、最近5B取整、几何中点、敏感性和资本滚动公式。新增实际季度流量小计及资料不足时的部分恒等式与断言。网页读取失败时尝试了公开网页备用读取；没有安装全局依赖。Oracle和Nebius的全年capex依赖会议原话的第三方公开转录，未复听录音，这一限制在正文和报告中都保留。

2027初步说法：微软FY27下半年加速（2026-10-28电话会）；Alphabet 2027明显增加（2026-10-28电话会）；Meta预算尚未完成、继续大力投资（2026-10-21公告）。这些原话没有提供同一期间可相加的完整金额。Amazon Q3公告未列2027全年capex数，不填估计。

补核SpaceX：[S-1/A提交索引](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/0001628280-26-040364-index.htm)确认最新修订2026-06-03；[424B4索引](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/0001628280-26-042639-index.htm)确认最终招股书2026-06-12。已读S-1/A“AI Capital Expenditures”段及后续Q3合并报表，不把最终招股书错称S-1/A。

三语同步检查发现日文旧版保留了翻译占位符，漏掉日本股市跌60%，并把住房租金1.7–2T前多插入“2,000円”。本版按中文版恢复60%和$1.7–2T；没有修改历史估计方法。


## 返工：资本存量日期与部分滚动计算

已逐行查origin/main的3.1、2.1及版本日期。3.1写2022–2026累计范围；2.1写2026H1部署，但文章日期是5月25日、v3.1日期6月10日。没有一句把1.3T明确定义为6月30日存量。因此base_as_of保留null，不把文稿日期当测量日。

7–9月四家现金PP&E实际为39.367+51.355+77.259+33.942=201.923B，旧AI占75%假设得到151.44225B。这是已知部分流量，不是全行业资产增加。公司报告capex45.2+51.4+77.259+34.906=208.765B，租赁定义不同，未用于直接增加NBV。全部来源已在输入逐项表列出。

资本滚动仍为K_next=K+AI capex−折旧。将旧年折旧16.4%按一个季度分摊为4.1%，只可给出部分恒等式K_0930=0.959×K_0630+151.44225B+未核实净增加。若K以B计，年度P=0.2805K；严格EPR=P/165，宽=P/270，中点为几何平均。Oracle28.499B覆盖6–8月，不能作为7–9月填入。新云厂商、其他投资、非现金租赁和处置也不全。未核实6月末K，故完整9月末K/P/EPR都不可得，不编数，也不是零。

旧K头条严格/宽/中点为2.21/1.35/1.73x。原版本1.66/2.81是v3.1修订历史，保留原说明，不再当当前计算。epr.py对新收入、季度实际小计及完整结果不可得均加断言。

三语恢复原文时，另修日文25%CAGR列的旧翻译占位符，以及英日K表少一列和日文年度capex表多出一列的问题；按中文补足，不改数字含义。
