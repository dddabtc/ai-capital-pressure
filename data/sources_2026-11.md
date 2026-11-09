# 2026 年 11 月数据核查

本版更新了能核实的公司披露，同时保留并标出了旧假设。部分项目没有可比新值，不能把这次更新理解成全行业数据已经测全。资本存量仍用旧假设，因此收入更新后的压力下降只是条件计算。

截止 2026-11-09。金额通常为十亿美元（B），K/GDP为万亿美元（T）；份额和利率为小数。严格/宽是沿用文章的两组估计名称，仍有明确标注的旧估计，均不是审计后的行业统计。所有新增公司收入仅用于背景，除正文R_T表明确列入外不进入分母。

## 输入逐项清单

先列原文件全部输入，再列新增输入。旧版本指 `origin/main` 的 `6113d54`。`null` 表示未单独披露或未核实；收入表中的0表示未计入，不能解释为公司收入为零。

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
| `r_t_strict_billion.anthropic_official` | 30 → 47 | 严格；[Anthropic Series H](https://www.anthropic.com/news/series-h)（2026-05-28）；>值按已披露下限计，不外推。 |
| `r_t_strict_billion.openai` | 25 → 24 | 严格；[OpenAI 融资公告](https://openai.com/index/accelerating-the-next-phase-ai/)（2026-03-31）；公司每月约2乘12=24，为年化换算，不是全年实际收入。 |
| `r_t_strict_billion.microsoft_ai_net_of_openai_resale` | 27 → 27 | 严格；沿用 v3.1 净估计27/30，拆分未核实；[微软 FY26 Q3 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3)（2026-04-29） 的37仅是官方总额；[微软 FY27 Q1 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1)（2026-10-28） 没有更新可比AI总额或净额。 |
| `r_t_strict_billion.xai_mistral_cohere_other` | 5 → "已删除，拆分见新增项" | 严格；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22）；旧合计5/8没有xAI分项，不能编拆分。暂不计入（0是未计入，不是收入为零）；原合计保留在变动记录。 |
| `r_t_strict_billion.google_gemini_workspace` | 5 → 5 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.ai_saas_net_of_api_resale` | 9 → 9 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.trad_saas_ai_addon` | 10 → 10 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.china_ai` | 10 → 10 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.bedrock_vertex_net` | 5 → 0 | 严格；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02）；市场销售已在Anthropic总额确认；无法核实其余净收入，5→0为不计入，防止重复。 |
| `r_t_strict_billion.hyperscaler_internal_attribution` | 0 → 0 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.consulting_productivity` | 0 → 0 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_billion.long_tail` | 5 → 5 | 严格；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_strict_note` | "ai_saas gross ~15 minus ~6 paid to model APIs (already inside Anthropic/OpenAI ARR); Anthropic uses the official 2026-04-06 number, the reported $40B stays in the wide basket" → "Anthropic official May run-rate >47; OpenAI March monthly revenue 2 x 12 = 24. Anthropic S-1/A GAAP quarters are disclosed separately, not substituted for exit run-rate. CSP marketplace sales are gross in Anthropic revenue; no independently verified residual Bedrock/Vertex terminal sales, so strict residual is excluded (0 means not counted). SpaceX SI mixes ads, hosting, Grok, X and Cursor; terminal-only run-rate and the old xAI allocation cannot be separated. Old mixed model-company estimate 5 is excluded rather than inventing a split; other unverified v3.1 estimates remain labelled. AI SaaS gross 15 less API resale 6 = 9 is an unchanged assumption, including Cursor only here." | 严格；说明同步本次已列的官方来源和去重复处理；应用净额9及其他旧估计仍未更新/未核实。 |
| `r_t_wide_billion.anthropic_reported` | 40 → 65 | 宽；[Reuters Anthropic 报道](https://www.investing.com/news/stock-market-news/anthropic-revenue-run-rate-tops-65-billion-source-says-4864031)（2026-08-17）；>值按已披露下限计，不外推。 |
| `r_t_wide_billion.openai` | 28 → 50 | 宽；[Reuters OpenAI 报道](https://www.investing.com/news/stock-market-news/openais-annualized-revenue-20-billion-less-than-previously-signaled-ft-reports-4939854)（2026-10-08（10-09更新））；报道的近50取约50，仅入宽。 |
| `r_t_wide_billion.microsoft_ai_net_of_openai_resale` | 30 → 30 | 宽；沿用 v3.1 净估计27/30，拆分未核实；[微软 FY26 Q3 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3)（2026-04-29） 的37仅是官方总额；[微软 FY27 Q1 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1)（2026-10-28） 没有更新可比AI总额或净额。 |
| `r_t_wide_billion.xai_mistral_cohere_other` | 8 → "已删除，拆分见新增项" | 宽；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22）；旧合计5/8没有xAI分项，不能编拆分。暂不计入（0是未计入，不是收入为零）；原合计保留在变动记录。 |
| `r_t_wide_billion.google_gemini_workspace` | 8 → 8 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.ai_saas_net_of_api_resale` | 12 → 12 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.trad_saas_ai_addon` | 15 → 15 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.china_ai` | 15 → 15 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.bedrock_vertex_net` | 10 → 10 | 宽；[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02）；沿用 v3.1 净额10的估计，假定不含Anthropic/OpenAI全部转售，无法独立核实。 |
| `r_t_wide_billion.hyperscaler_internal_attribution` | 35 → 35 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.consulting_productivity` | 10 → 10 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_billion.long_tail` | 8 → 8 | 宽；沿用 v3.1，未更新/未核实。公开披露不足以重建同定义、扣API转售后的行业合计；见下方分类检索记录。 |
| `r_t_wide_note` | "ai_saas gross ~20 minus ~8 API resale" → "Anthropic >65 (July, Reuters Aug 17) and OpenAI almost 50 (September, Reuters Oct 8) are reported values, not official disclosures. Old mixed model-company estimate 8 is excluded because its xAI allocation is unknown. AI SaaS gross 20 less API resale 8 = 12; Bedrock/Vertex residual 10 is an unverified legacy estimate assumed to exclude all Anthropic/OpenAI sales." | 宽；说明同步本次已列的Reuters报道和去重复处理；应用净额12、市场净额10仍为未核实的旧估计。 |
| `r_t_ttm_wide_billion` | 140 → 140 | 宽参考；沿用 v3.1 的140，行业TTM未更新/未核实；不可称为截至11月的最新TTM。 |
| `capex_2026_billion.microsoft` | [190, 195] → [170, 170] | 严格/宽分子外的资本支出背景；[微软 FY27 Q1 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1)（2026-10-28）；自然2026公司指引，非实际支出。 |
| `capex_2026_billion.alphabet` | [180, 190] → [195, 205] | 严格/宽分子外的资本支出背景；[Alphabet Q3 电话会](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx)（2026-10-28）；自然2026公司指引，非实际支出。 |
| `capex_2026_billion.amazon` | [200, 205] → [220, 220] | 严格/宽分子外的资本支出背景；[Amazon Q3 公告](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf)（2026-10-29）；自然2026公司指引，非实际支出。 |
| `capex_2026_billion.meta` | [125, 145] → [135, 145] | 严格/宽分子外的资本支出背景；[Meta Q3 公告](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx)（2026-10-21）；自然2026公司指引，非实际支出。 |
| `capex_2026_billion.oracle` | [60, 70] → [90, 95] | 严格/宽分子外的资本支出背景；[Oracle FY27 Q1 电话会公开转录](https://www.roic.ai/quote/ORCL/transcripts/2027-year/1-quarter)（2026-09-10（会议日））；FY27毛额，不是自然2026；公开转录未复听录音。 |
| `capex_2026_billion.neocloud` | [60, 70] → "已删除，拆分见新增项" | 背景；旧neocloud60–70未能按公司追溯，不再作为可核实合计；IREN和其他未获可比全年数据，不编数字。 |
| `capex_2026_billion.ai_share_of_hyperscaler` | 0.75 → 0.75 | 假设；沿用 v3.1 75%，未更新/未核实；各公司没有同定义的纯AI占比。 |
| `us_gdp_trillion` | 30 → 33.010036 | GDP分母；[BEA NIPA 1.1.5 工作簿](https://apps.bea.gov/national/Release/XLS/Survey/Section1All_xls.xlsx)（2026-10-29）；T10105-Q，A191RC，2026Q3列33010036百万美元 / 1000000 =33.010036万亿；季调年率，不是2026全年GDP。 |
| `time_path.annual_capex_billion` | 600 → 600 | 情景；公式、年 capex 和增速假设沿用 v3.1；起点同步宽口径收入，不是新预测。 |
| `time_path.r_t_start_billion` | 220 → 260 | 情景；公式、年 capex 和增速假设沿用 v3.1；起点同步宽口径收入，不是新预测。 |
| `time_path.cagr_scenarios` | [0.5, 0.25, 0.1] → [0.5, 0.25, 0.1] | 情景；公式、年 capex 和增速假设沿用 v3.1；起点同步宽口径收入，不是新预测。 |
| `time_path.years` | [2026, 2027, 2028, 2029, 2030, 2031, 2032] → [2026, 2027, 2028, 2029, 2030, 2031, 2032] | 情景；公式、年 capex 和增速假设沿用 v3.1；起点同步宽口径收入，不是新预测。 |
| `sensitivity.r_t_levels` | [300, 400, 180, 130] → [300, 400, 180, 135] | 情景；沿用 v3.1；最后一档收入从旧严格值130同步至135，未改敏感性方法。 |
| `sensitivity.k_levels_trillion` | [1.7, 2.0] → [1.7, 2.0] | 情景；沿用 v3.1；最后一档收入从旧严格值130同步至135，未改敏感性方法。 |
| `sensitivity.gpu_life_extra_dep_billion` | 43 → 43 | 情景；沿用 v3.1；最后一档收入从旧严格值130同步至135，未改敏感性方法。 |
| `sensitivity.opex_15pct_extra_billion` | 65 → 65 | 情景；沿用 v3.1；最后一档收入从旧严格值130同步至135，未改敏感性方法。 |
| `sensitivity.wacc_extra_billion` | 80 → 80 | 情景；沿用 v3.1；最后一档收入从旧严格值130同步至135，未改敏感性方法。 |
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
| `r_t_strict_billion.spacex_xai_terminal_only` | "原版未列" → 0 | 严格；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22）；旧合计5/8没有xAI分项，不能编拆分。暂不计入（0是未计入，不是收入为零）；原合计保留在变动记录。 |
| `r_t_strict_billion.mistral_cohere_other` | "原版未列" → 0 | 严格；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22）；旧合计5/8没有xAI分项，不能编拆分。暂不计入（0是未计入，不是收入为零）；原合计保留在变动记录。 |
| `r_t_wide_billion.spacex_xai_terminal_only` | "原版未列" → 0 | 宽；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22）；旧合计5/8没有xAI分项，不能编拆分。暂不计入（0是未计入，不是收入为零）；原合计保留在变动记录。 |
| `r_t_wide_billion.mistral_cohere_other` | "原版未列" → 0 | 宽；[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22）；旧合计5/8没有xAI分项，不能编拆分。暂不计入（0是未计入，不是收入为零）；原合计保留在变动记录。 |
| `capex_2026_billion.neocloud.coreweave` | "原版未列" → [35, 39] | 背景；[CoreWeave Q2 指引稿](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf)（2026-08-11） 第3页；自然2026指引。 |
| `capex_2026_billion.neocloud.nebius` | "原版未列" → [20, 25] | 背景；[Nebius Q2 电话会公开转录](https://www.fool.com/earnings/call-transcripts/2026/08/19/nebius-nbis-q2-2026-earnings-call-transcript/)（2026-08-19（会议08-12）） CFO Dado Alonso指引段原话；公开转录未复听录音；[Nebius Q2 股东信](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf)（2026-08-12） 第3页确认指引未变。 |
| `capex_2026_billion.neocloud.iren_calendar_2026` | "原版未列" → null | 背景；旧neocloud60–70未能按公司追溯，不再作为可核实合计；IREN和其他未获可比全年数据，不编数字。 |
| `capex_2026_billion.neocloud.other_estimate` | "原版未列" → null | 背景；旧neocloud60–70未能按公司追溯，不再作为可核实合计；IREN和其他未获可比全年数据，不编数字。 |
| `capex_2026_billion.neocloud.note` | "原版未列" → "CoreWeave and Nebius calendar-2026 guidance. IREN: no full calendar-2026 figure verified; FY27 remaining capex 15 is recorded separately. Lambda/Crusoe/other estimates are not newly invented. The old neocloud total 60-70 had no auditable company allocation and is retired, not added on top." | 背景；旧neocloud60–70未能按公司追溯，不再作为可核实合计；IREN和其他未获可比全年数据，不编数字。 |
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

| `disclosed_billion.spacex.ai_capex_2026_q1_from_s1a` | 原版未列 →7.723 | 背景；[SpaceX最新S-1/A](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm)（2026-06-03），“AI Capital Expenditures”段；后续当前数改用Q3。 |

## 一手申报中的收入与重复计算

Anthropic S-1/A 第161页列出2026 Q1/Q2/Q3 GAAP收入4.731、11.555、16.956；合计33.242，连同2025 Q4的2.040得TTM35.282。第58页和财务附注2披露前九个月44%收入来自云厂商市场，附注2“Revenue Recognition”写明公司是主要责任人，按总额确认。市场费用不能让同一笔终端销售再计一次。严格表的Bedrock/Vertex残余项从5改为未计入0；宽表10仅保留原版“已排除全部模型转售”的估计，未核实。微软净额27/30和应用净额9/12仍是旧假设，不能由44%机械扣除。[Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02）

S-1/A 第199页的2026-10-31 Run-Rate Revenue金额仍留空。不能把Q3收入乘4冒充公司披露的最新退出年化收入。因此严格用公司5月公告的>47，宽用7月底>65的报道；季度GAAP和ARR分开列。[Anthropic Series H](https://www.anthropic.com/news/series-h)（2026-05-28）；[Reuters Anthropic 报道](https://www.investing.com/news/stock-market-news/anthropic-revenue-run-rate-tops-65-billion-source-says-4864031)（2026-08-17）

SpaceX Q3 10-Q附注1第10–11页确认：2026-02-02收购后xAI为全资子公司；附注18第32–33页已经合并列报。Q3部门改称SI。附注3第12页及MD&A第41–42、48页：Q3 SI收入7.560、其中Solutions & Infrastructure 7.022；前九个月SI收入10.939。该部门包含X广告、云服务、Grok、X订阅、数据许可和Cursor，纯终端AI年化收入未单独披露。原“xAI/Mistral/Cohere/其他”5/8没有可核实拆分，两个新行都先不计入，而不把5/8全数改称其他公司收入。Cursor只保留在原应用净额估计内，SpaceX整部门收入不再叠加。[SpaceX Q3 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)（2026-10-22）

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
| OpenAI总名义承诺 | 1400 →沿用v3.1，未更新/未核实 | 未找到当前完整一手总表，有重叠，不由各行机械加总；不再用它断言某公司最脆弱。 |
| OpenAI Oracle300 / Stargate500及400+ / AMD90 / NVIDIA100 / Azure250 / CoreWeave22.4 /Broadcom50–100 | 数字沿用v3.1，未更新/未核实；表中逐行标旧值 | 原承诺和供应商股权投资性质不同，未计入K或终端收入；AMD/Broadcom美元数缺合同一手定价，不能称已核实。 |
| Anthropic总承诺 | 200–300+ →895.4 | [Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)（2026-11-02） 第174–175页 Contractual Obligations及导言；含短期、期后及未开始租赁，319.993表内小计不是全部；69.8在后12个月到期。 |
| Anthropic分伙伴：AWS5/25/100/5GW，Google10/40/5GW，NVIDIA10/1GW，微软5/30，Broadcom21，美国基础设施50 | 沿用v3.1，未逐项重新核实；合计比较用S-1/A，旧分项不求和 | 旧分项含融资、采购、容量和券商预测，不能视为同类采购承诺。 |
| Anthropic承诺/ARR /OpenAI承诺/ARR | 5–7.5x /56x →19.1x（47）或13.8x（报道65）；OpenAI58.3x（24）或28.0x（报道50），仅条件对照 | epr.py输入推算；OpenAI总额未更新，不能证明可比时点的风险排序。 |
| Goldman全球AI投资基线 | 765 →约1000；美国581 | [Goldman 全球 AI 投资估计](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026)（2026-08-07）；研究估计，不是公司披露，亦不替代本文capex算法。 |
| Goldman AI capex/GDP | 美国0.8%、全球0.6–0.7% →其估计美国1.8%、全球0.9% | [Goldman 全球 AI 投资估计](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026)（2026-08-07）；地理调整后估计，与本文全球公司/美国GDP不同。 |
| 联储39% /第三季度 | 误写单季39% →前三季39%，单季11%或0.48百分点 | [圣路易斯联储原文](https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth)（2026-01-12）；实际增长，不是名义增长；修正旧文。 |
| Furman92%、Goldman1.5pp/0.1–0.2pp、旧净贡献0.1–0.5pp、进口占70%+ | 沿用v3.1数值但未核实，不再当作当前可靠净贡献 | 不能把“增长贡献占比%”和“百分点pp”直接说成相差100/1000倍；旧比较删去。 |
| 四家公司FCF300+、CoreWeave租赁杠杆4.2x、推理成本下降10–30倍、18–24月硬件节奏、GPU残值24个月、H1003美元/时、B2005美元/时 | 沿用v3.1，未更新/未核实；不用于本版肯定判断 | 未重建同期间报表和市场报价，正文列为旧背景假设。 |
| 微软Copilot渗透率3.3–4.4%、席位400M | 沿用v3.1旧值，未更新/不可作当前渗透率 | [微软 FY27 Q1 电话会](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1)（2026-10-28） 明示未更新Copilot数量；不以旧席位推算11月。 |
| NVIDIA循环股权投资40+ /OpenAI30 | 沿用v3.1、未更新；另列10-Q股权投资99、未来承诺25 | [英伟达 FY27 Q2 10-Q](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf)（2026-08-26）；存量与流量不同，不能把99+25说成“2026新投124”。 |
| K拆解780–880、90–130、200–300；合计1.07–1.31T；2025 AI capex260、2026H1约260 | 沿用v3.1，未更新/未核实 | 与当前已部署资产和折旧口径不可直接对应；Oracle原说明可能重复，不能据此提高K。 |
| capex历史列2024：56/53/78/37/7/合计231/neocloud15；2025：95/75/105/65/25/合计365/neocloud35/行业400；年初620 | 沿用v3.1，未更新/未逐家核实；从当前比较表移除 | 不是本次最新公司披露，且财年/自然年不同，避免旧列误导。 |
| CreditSights750；Goldman2031的1.6T；旧全球700–750/110T；合理90%区间1.1–2.9及1.8–3.8 | 沿用v3.1但未核实，移出当前结论 | 无可复算同定义新证据；情景敏感性不等于统计置信区间。 |
| 正常行业0.69/0.76/0.80/0.90/0.92和0.65–0.95区间 | 沿用v3.1粗估，未更新/未核实 | 固定参照，不称已测得11月行业平均。 |
| 1846：K170、GDP550–600、capex7–8%、寿命30/50+、债务60%、利率4.5–5%、收入10–15、opex10–15%或收入45–55% | 沿用v3.1历史假设 | epr.py统一口径完整范围1.8–3.6x（原文2.5–3只为概括，现列全范围），校准1.0–1.9x；未新查历史档案。 |
| 1873：K2.7、GDP7、38%、寿命30/50+、债务70%、利率7%、收入0.52、opex15%/收入65% | 沿用v3.1历史假设 | epr.py复算1.21x/1.08x；未新查历史档案。 |
| 2000电信：K500、capex120、GDP10.25、1.2%、寿命15/15–20、opex10–12%、债务60%、利率8%、IP收入30–50、EPR2.5–4/约3、整体0.5–0.8 | 沿用v3.1历史假设 | 未更新/未新核实，不是11月数据。 |
| 2007住房：97%、K24T、债务10T、折旧2%/480、opex700/3%、利息600、压力1.78T、租金1.7–2T、EPR0.9–1.1、价格收入3→5 | 沿用v3.1历史假设 | 未更新/未新核实，保留作结构对照。 |
| 历史背景：铁路股跌50–80%、里程35k→70k、89家/25%破产；电信债500+、80M英里、债12.4、亮纤2.7%、价格跌55%、市值2T；日本跌60/80%、钢铁0.5–0.7/跌70%、页岩油1.5–2/跌75%/~100家；房价跌35%、比特币80% | 沿用v3.1历史背景 | 本轮未查原始档案，不用这些数作新的精确历史排序。 |
| 所有情景：年capex600、L6.1、CAGR50/25/10%、K1.7/2.0、额外成本43/65/80、WACC8%、在建15–20% | 沿用v3.1假设，只同步输入起点和输出 | 全部由epr.py重算；不是已发生的未来数据。 |

## 分类检索记录与未更新项

模型公司、Google AI、专用应用、传统SaaS、中国AI、Bedrock/Vertex、内部归因、咨询和长尾逐项检查。单家公司披露不能替代整组扣重叠合计。Salesforce Agentforce和Data 360混合ARR近3.9并非纯AI增量；ServiceNow订阅收入亦非Now Assist独立净收入；百度和阿里披露包含广告、云算力或其他业务，不能整项移入R_T。保留旧9/12、10/15、10/15、Google5/8等，并标未核实。内部归因35、咨询10和长尾5/8没有可直接核实的行业数。[Salesforce FY27 Q2](https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Second-Quarter-Fiscal-2027-Results/default.aspx)（2026-08-26）；[ServiceNow Q3](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Third-Quarter-2026-Financial-Results/default.aspx)（2026-10-28）；[百度 Q2](https://ir.baidu.com/news-releases/news-release-details/baidu-announces-second-quarter-2026-results)（2026-08）；[阿里六月季公告](https://home.alibabagroup.com/en-US/document-2027233133950140416)（2026-08-20）

计算只改输入和原先正文结果的断言，保留P公式、最近5B取整、几何中点、敏感性和资本滚动公式。网页读取失败时尝试了公开网页备用读取；没有安装全局依赖。Oracle和Nebius的全年capex依赖会议原话的第三方公开转录，未复听录音，这一限制在正文和报告中都保留。

2027初步说法：微软FY27下半年加速（2026-10-28电话会）；Alphabet 2027明显增加（2026-10-28电话会）；Meta预算尚未完成、继续大力投资（2026-10-21公告）。这些原话没有提供同一期间可相加的完整金额。Amazon Q3公告未列2027全年capex数，不填估计。

补核SpaceX：[S-1/A提交索引](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/0001628280-26-040364-index.htm)确认最新修订2026-06-03；[424B4索引](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/0001628280-26-042639-index.htm)确认最终招股书2026-06-12。已读S-1/A“AI Capital Expenditures”段及后续Q3合并报表，不把最终招股书错称S-1/A。

三语同步检查发现日文旧版保留了翻译占位符，漏掉日本股市跌60%，并把住房租金1.7–2T前多插入“2,000円”。本版按中文版恢复60%和$1.7–2T；没有修改历史估计方法。
