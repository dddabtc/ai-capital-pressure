Languages: [English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)
PDF: [English](ai-capital-pressure-v3.en.pdf) | [简体中文](ai-capital-pressure-v3.zh-CN.pdf) | [日本語](ai-capital-pressure-v3.ja.pdf)
（PDF 为 v3 存档；v3.1、v3.2 修订以 Markdown 为准）

# AI Capital Pressure

更新后，在旧资本存量假设不变的条件下，年度资本压力相对收入有所下降，仍高于成熟行业参照。收入数据比以前完整，资本存量还没有同样完整的新统计，不能据此认定整个行业的实际压力已经下降。

行业与历史比较；dda，2026-11-09，v3.2。研究压力测试，非投资建议。B=十亿美元，T=万亿美元。

## 数据核查与版本说明

v3.2（2026-11-09）修订说明：更新 Anthropic、OpenAI 可用的官方/报道收入、四家云厂商自然年资本支出指引、Oracle FY27 指引、GDP和公司最新季报。补入 SpaceX 合并 xAI 的披露，逐家列 CoreWeave、Nebius、IREN。Anthropic 市场销售按总额确认，严格收入表不再另加无法核实的 Bedrock/Vertex 净额；旧模型公司合计无法拆出 xAI，暂不计入，未编拆分。宽/严格 EPR 从1.66x/2.81x改为1.40x/2.70x，几何中点从2.16x改为1.95x，落在页岩油参照区间内。高于正常行业的条件结论更新后仍成立。K仍为旧假设，其他未核实项见来源表。方法和原有情景参数不变，只同步收入起点。

**v3.1（2026-06-10）修订说明**：外部复核后修正五处口径，全部数字可由仓库内 `epr.py` + `data/inputs.json` 复算（脚本内置一致性断言）。(1) 严格口径 R_T 改用 Anthropic 官方 $30B（$40B 转引数字仅入宽口径），并扣除应用层付给模型 API 的转售（约 $6-8B），取消此前 $147B→$160B 的向上取整：严格口径 EPR 从 2.28x 修正为 2.81x；宽口径同步扣转售后为 1.66x。(2) 历史案例补运维校准敏感性：1846 英国铁路按当年经营比率（45-55%）校准后 EPR 仅约 1.0-1.9x，"AI 低于 1846 峰值"不再作为头条结论。(3) Big-5 2026 capex 统一为 $755-805B（与 §3.2 逐公司表一致）。(4) 明示 R_T 为瞬时 run-rate，补 TTM 参考口径（约 2.6x）。(5) 敏感性表补"在建工程不计折旧"一行。修正后中心结论的方向不变，幅度变化见下文。

本次核查截止2026-11-09，不表示每项数据都更新到了同一天。逐项旧值、新值、来源、发布日期和未更新原因见 [来源表](data/sources_2026-11.md)。严格/宽只是原文两组估计的名称，仍含标明的旧估计，不是审计后的行业统计。

| 项目 | 本版数据 | 来源与期间 |
|---|---|---|
| Anthropic | 官方年化>47；报道>65 | [Company](https://www.anthropic.com/news/series-h) (2026-05-28); [Reuters](https://www.investing.com/news/stock-market-news/anthropic-revenue-run-rate-tops-65-billion-source-says-4864031) (2026-08-17) |
| OpenAI | 官方每月约2，乘12=24；报道近50 | [Company](https://openai.com/index/accelerating-the-next-phase-ai/) (2026-03-31); [Reuters](https://www.investing.com/news/stock-market-news/openais-annualized-revenue-20-billion-less-than-previously-signaled-ft-reports-4939854) (2026-10-08（10-09更新）) |
| Microsoft AI | 官方37（旧）；净额27/30是未更新估计 | [FY26 Q3](https://www.microsoft.com/en-us/Investor/events/fy-2026/earnings-fy-2026-q3) (2026-04-29) |
| NVIDIA | FY27 Q2收入96.2，DC89.0；Q3指引108±2% | [IR](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx) (2026-08-26) |
| CoreWeave | Q2收入2.575，backlog104.2；2026 capex35–39 | [IR](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/default.aspx) (2026-08-11); [Outlook](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf) (2026-08-11) |
| US GDP | 2026Q3季调年率33.010036T | [BEA](https://apps.bea.gov/national/Release/XLS/Survey/Section1All_xls.xlsx) (2026-10-29) |

英伟达最新已发布季度为FY27 Q2。官方安排FY27 Q3于2026-11-17发布，截止日尚未发布；这里没有使用Q3实际数。 [IR](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/) (2026-10-28)

## 中心结论

本文用年度折旧、现金运维和利息的合计，除以估计终端收入，衡量资本服务压力，简称EPR。K=$1.3T等旧假设不变时，宽口径1.40x、严格口径2.70x，几何中点1.95x。正常行业参照0.65–0.95x未更新，中点约为其0.80x代表值的2.4倍。

中点从旧版2.16x降到1.95x，进入2014页岩油1.5–2x的区间，旧文“高于其上沿”的说法不再适用。中点仍高于1873铁路聚合1.08–1.21x，低于2000电信新建段约3x。1846铁路随运维假设变化为1.8–3.6x或1.0–1.9x，仍不作稳定排序。严格口径2.70x仍落在原文2.0–4.0x的高压区，不能把中点的位置套到整个区间。

本版无法更新全行业已部署资本存量，也没有可比的完整终端收入普查。因此结论是旧K下的压力测试，不是证明实际风险改善。资本支出指引上调或季度投入增加，不能直接当作当前K增加。住房和日本资产价格泡沫的机制与此不同，EPR不用于给所有泡沫统一排序。

## **一、EPR 框架：是什么，不是什么** 

## **1.1 定义** 

P = K/L + o × K + r × d × K 

EPR_cash = P / R_T 

其中 K=已部署资本存量，L=加权平均经济寿命，o=现金运维 / K，r=平均债务融资利率，d=债务 融资占比，R_T=可核验终端收入。 

## **1.2 框架溯源（不是新发明）** 

严格说，EPR 不是新指标。它本质上是几个既有概念的组合： 

- 经济学层面：Jorgenson (1963) 资本服务成本理论。资本服务价格 c = (i + δ - π) × p_K， 其中 δ 是经济折旧率、i 是利率、π 是资产价格变化。这是现代生产率核算 

   - （BEA、BLS、KLEMS）的基础。 

- 监管经济学：公用事业 revenue requirement 公式。rate base × (depreciation rate + return on capital + O&M) = 必须收回的收入。规制 ROE 模型 60+ 年的标准做法。 

- 地产估值：cap rate（NOI / property value）的倒数即类似指标，1930s 已有。 

- 企业估值：等价于"implied required revenue to justify capex"分析，Damodaran 等多次用 于 hyperscaler AI 业务。 

本文的贡献不在于框架本身，而在于：把它应用到 AI 周期 + 与当前正常行业 + 与历史四大基础 设施周期做横向比较。EPR 是为本文讨论方便采用的命名。 

## **1.3 EPR 是什么** 

- EPR 是 capital service pressure ratio。把行业每年必须从终端收入中消化的资本相关成 本（折旧 + 现金运维 + 利息）压缩成一个数。 

- EPR 比 Debt/Revenue 或 Capex/Revenue 信息密度高，因为同时纳入存量资本压力、运 营压力和融资成本。 

- EPR 可用于跨行业、跨周期同框架比较（虽然历史会计口径差异不可避免）。 

## **1.4 EPR 不是什么** 

- EPR 不是传统杠杆率。它不是 Debt/Equity、Debt/EBITDA、Assets/Equity、Net Debt/Revenue。把 EPR 称为"杠杆率"会让读者误以为衡量的是债务风险，但 AI 的核心风 险很多不是债务，而是股权稀释、折旧吞噬利润、云合同重谈、capex 减速导致估值压缩、 GPU 残值下修。 

- EPR 不是完整利润率指标。本文 P 只纳入基础设施层的折旧 + opex + 利息，没有纳入 模型公司和应用层的 R&D、SG&A、销售、客服、股权激励、数据采购、推广补贴、税。 真实行业利润压力比 EPR 暗示的更高。 

- EPR > 1 不直接等同于"行业不赚钱"。而是终端收入不足以覆盖本文定义下的年度基础设 施压力。 

- EPR_cash 默认用 cash interest（r × d × K），没有 charge 股权资本机会成本。如果改 用 WACC 替代，EPR 会显著升高（见敏感性分析）。 

- 历史 EPR 是同框架近似估算，不是"同口径"精确测量。所有历史 EPR 数字置信度低-中。 

## **1.5 EPR 的解读区间** 

|**EPR_cash区**<br>**间**|**解读**|**典型例子**|
|---|---|---|
|< 0.6x|低资本压力，行业稳态盈利|消费品、互联网平台、轻资产服务|
|0.6–1.0x|中等资本压力，大部分正常行业落点|公用事业、电信、SaaS、汽车、航空|
|1.0–2.0x|高资本压力，需求外推或周期高位|页岩油峰值期、AI当前宽口径、1873美<br>国铁路聚合|
|2.0–4.0x|基础设施泡沫量级，提前资本化未来需求|AI当前严格口径、2000电信光纤新建段、1840s铁路（统一o口径）|
|> 4.0x|极端情况，通常出现在崩盘前最后阶段|少数极端案例|

## 二、AI产业链的条件压力测试

## 2.1 输入参数

| 参数 | 取值 | 状态 |
|---|---|---|
| K | $1.3T | 沿用v3.1，未更新 |
| L / 混合折旧率 | 6.1 / 16.4% | 旧假设 |
| o / r / d | 10% / 5.5% / 30% | 旧假设 |
| R_T 宽/严格 | $260B / $135B | 逐项见2.3 |
| m_T | 50% | 旧毛利假设 |
| 在建工程占K | 15–20% | 旧敏感性假设 |

K的旧拆解是hyperscaler约780–880B、新云厂商90–130B、其他200–300B，合计1.07–1.31T，取上沿1.3T。这些分项没有同定义的11月更新；Oracle原来同时出现在Big-5和“其他”的说明里，可能重复，不能用旧拆解证明新的存量。这里维持K，仅供条件对照。

## 2.2 重算结果

| 项目 | 公式或分母 | 结果 |
|---|---|---|
| 折旧 | 1300 × 16.4% | $213.2B |
| 现金运维 | 1300 × 10% | $130B |
| 现金利息 | 1300 × 5.5% × 30% | $21.45B |
| P | 213.2 + 130 + 21.45 | $364.65B (~$365B) |
| EPR 宽 | 364.65 / 260 | 1.40x |
| EPR 严格 | 364.65 / 135 | 2.70x |
| 几何中点 | sqrt(EPR_wide × EPR_strict) | 1.95x |
| R_req | P / 50% | $729B |
| 收入缺口：宽/严格 | R_req − R_T | $469B / $594B |
| 旧TTM宽参考 | 364.65 / 140 | 2.60x |

TTM指过去连续十二个月。行业TTM宽收入140B沿用v3.1，未更新/未核实，2.60x只能作旧参考。Anthropic单家公司可由申报重建TTM35.282B，但不能据此更新整个行业TTM。官方年化收入、季度GAAP收入和未来指引分别列出，不混用。

## 2.3 终端收入逐项分解

| 类别，$B | 严格 | 宽 | 说明 |
|---|---|---|---|
| Anthropic | 47 | 65 | 官方5月下限 / 7月底报道下限 |
| OpenAI | 24 | 50 | 官方3月每月年化 / 9月报道近值 |
| Microsoft AI 净额 | 27 | 30 | 沿用，扣重叠未核实 |
| SpaceX/xAI 纯终端 | 0 | 0 | 未单独披露，未计入；不是零收入 |
| Mistral/Cohere/其他模型 | 0 | 0 | 旧合计5/8无法拆分，暂未计入 |
| Google Gemini/Workspace AI | 5 | 8 | 沿用估计，未核实 |
| 专用AI SaaS净额（含Cursor） | 9 | 12 | 旧毛额15/20减API转售6/8，未核实 |
| 传统SaaS AI增量 | 10 | 15 | 沿用估计，未核实 |
| 中国AI | 10 | 15 | 沿用估计，未核实 |
| Bedrock/Vertex 净额 | 0 | 10 | 严格未计入；宽为排除全部模型转售后的旧估计，未核实 |
| 内部AI归因 | 0 | 35 | 宽估计，未核实 |
| 咨询/生产率节省 | 0 | 10 | 宽估计，未核实 |
| 长尾 | 5 | 8 | 沿用估计，未核实 |
| 分项合计→最近5B | 137 → 135 | 258 → 260 | 取整方法不变 |

Anthropic S-1/A第161页列Q1/Q2/Q3收入4.731/11.555/16.956B，前三季33.242B。第58页和附注2披露，前三季44%销售经云市场，且按总额确认。因此不能再在Bedrock/Vertex里加同一销售，也不能用44%去扣微软整个AI业务。最新10月末年化收入栏仍空白，严格保持官方47B下限，季度收入不乘4冒充退出年化数。 [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm) (2026-11-02)

xAI已并入SpaceX，后者的SI部门还含广告、云算力、Grok和Cursor。纯终端年化额未单独披露，不能把部门7.560B季度收入整体年化后加入R_T。旧模型公司5/8B无法可靠拆出xAI，所以暂不计整个旧项；新行0只表示未计入。应用净额9/12B保留Cursor，SpaceX部门收入不另加，以免重算。 [10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm) (2026-10-22)

## 三、资本存量、年度支出与合同承诺

K是已经部署或在建的资产存量；capex是某个期间买入资产的流量；commitments是未来合同义务或公告。三者不能相加。年度支出和合同承诺都不直接进入本版P，P仍由旧K计算。

## 3.1 K的保留条件

本版没有足够的一手数据重建各家公司AI资产净值和在建工程。K=$1.3T沿用v3.1，不称为11月实际存量；旧±20%也是估计，不能当统计误差。新增公司披露只说明旧存量需要后续重建，不据此编一个新的K。

## 3.2 各家公司资本支出和最新季度

| 公司 | 年度资本支出指引，$B | 期间和来源 |
|---|---|---|
| Microsoft | 170 | CY2026; [IR](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1) (2026-10-28) |
| Alphabet | 195–205 | CY2026; [IR](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx) (2026-10-28) |
| Amazon | 220 | CY2026; [IR](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf) (2026-10-29) |
| Meta | 135–145 | CY2026; [IR](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx) (2026-10-21) |
| Oracle | 90–95 | FY2027 (2026-06 to 2027-05); [Call transcript](https://www.roic.ai/quote/ORCL/transcripts/2027-year/1-quarter) (2026-09-10（会议日）) |
| Big-5 | 810–835 | 四个自然年加一个财年，期间不同 |
| Big-5假设AI部分 | 607.5–626.25 | 75% × (810–835) |
| CoreWeave | 35–39 | CY2026; [IR](https://s205.q4cdn.com/133937190/files/doc_financials/2026/q2/CoreWeave-Q2-26-Earnings-Outlook-Presentation.pdf) (2026-08-11) |
| Nebius | 20–25 | CY2026; [Call transcript](https://www.fool.com/earnings/call-transcripts/2026/08/19/nebius-nbis-q2-2026-earnings-call-transcript/) (2026-08-19（会议08-12）) |
| 已列两家新云厂商 | 55–64 | 不是全行业合计 |
| IREN | 自然2026未核实；剩余FY27为15 | [IR](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results) (2026-11-05) |
| SpaceX SI | 全年AI未单独披露；前九月实际39.995 | [10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm) (2026-10-22) |
| 其他（估计）：Lambda、Crusoe等 | 金额未核实，不编估计，不计入 | 融资或项目公告不等于年度capex |

Oracle与Nebius全年指引取自财报会原话的公开转录，未复听录音；来源表保留这个限制。原neocloud60–70B没有逐家底稿，不能在列出CoreWeave和Nebius后又加一次，也不能编一个余数分给其他公司。SpaceX与IREN的部分期间数不参加年度指引相加。

| 公司/季度 | 最近季度收入，$B | backlog或RPO，$B | 补充披露 |
|---|---|---|---|
| Oracle FY27 Q1 | OCI ~7.4 | RPO 664 | 资本支出28.499；净现金17.966 |
| CoreWeave Q2 2026 | 2.575 | 104.2 | 全年收入指引12.4–13.2 |
| Nebius Q2 2026 | 0.5823 (AI cloud 0.5749) | 客户承诺>40，不是同定义backlog | Q2支出约5.7 |
| IREN FY27 Q1 | 0.228 (AI cloud 0.200) | 20.3 | 后续剩余财年支出15 |
| SpaceX SI Q3 2026 | 7.560 (Solutions & Infrastructure 7.022) | 此处未作AI终端backlog | Q3支出16.444；前九月收入10.939 |

SpaceX Q3 10-Q附注1（第10–11页）确认xAI为全资子公司；附注3（第12页）及附注18（第32–33页）列收入和资本支出。GPU采购、数据中心等单独资本开支及全年纯AI指引未单独披露。新云厂商的订单指标定义不同，不直接相加；它们的全部收入也不直接加进终端AI收入。 [10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm) (2026-10-22); [Oracle](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Q1-Results-Driven-by-Triple-Digit-Growth-in-Cloud-Infrastructure-Revenues/default.aspx) (2026-09-10); [Nebius](https://assets.nebius.com/assets/a6ecfd85-a6cb-4967-8ef7-9a25bd261f9c/SHLQ226.pdf) (2026-08-12); [IREN](https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results) (2026-11-05)

微软的170B与旧指引不能直接解释为项目规模下降，租赁确认和交付时间会影响报表资本支出。微软表示FY27下半年支出将加速；Alphabet表示2027年支出将明显增加；Meta表示仍在编制2027预算，计划继续大力投入，未给全年金额。Amazon公告没有给可比的2027全年capex数，本版不填数。这些只是已公布的管理层说法，不是本文新增预测。 [Microsoft](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1), [Alphabet](https://abc.xyz/investor/events/event-details/2026/2026-Q3-Earnings-Call-2026-Ujou16CTw9/default.aspx), [Meta](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx), [Amazon](https://ir.aboutamazon.com/files/doc_earnings/2026/q3/earnings-result/AMZN-Q3-2026-Earnings-Release.pdf)

SpaceX最新S-1/A为2026-06-03，已读“AI Capital Expenditures”段：2026 Q1 AI资本支出7.723B，增长来自地面数据中心的建设、设备和配套设施。之后2026-06-12最终招股书沿用该披露；本版当前值采用更晚的Q3 10-Q，而不沿用上市前季度。 [S-1/A](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm), [424B4](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm)

## 3.3 合同承诺与收入

OpenAI旧名义总额1.4T没有核实到当前完整一手总表，沿用作历史背景，不作当前风险排序。原Oracle300、Stargate500（400+计划）、AMD90、NVIDIA最高100、Azure250、CoreWeave22.4、Broadcom50–100B均是未更新的旧行，性质和期限不同，也有重叠，不能相加成债务或K。AWS一项已核实：在原38B多年协议上增加100B、期限8年，合计名义138B但不是同一期限。 [OpenAI](https://openai.com/index/amazon-partnership/) (2026-02-27)

Anthropic S-1/A披露总承诺895.4B，包含长期采购、短期和期后承诺、未开始租赁；其中69.8B在随后十二个月到期。旧200–300+B已被新披露替换，旧伙伴分项含融资、算力容量和券商估计，不能再求和。按官方47B或报道65B年化收入计算，比例约19.1x或13.8x，不能继续写“只有5–7.5x、承诺相对克制”。 [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm) (2026-11-02)

若仅把OpenAI旧1.4T除以本版24B官方年化或50B报道数，得到58.3x或28.0x。这只是不同日期数据的条件对照，不是当前可比风险比率；多年承诺/瞬时年化收入也不是财务杠杆。

## **四、正常行业 EPR 基准（粗估，非审计行业模型）** 

正常行业 EPR 区间作为基准。所有数字基于 2024-2025 年公开财报按行业平均估算，置信度中。 警示：行业聚合数据粗。公司收入、D&A、opex、利息来自不同公司和会计口径，完全同口径不 可能。这些数字是数量级基准，不是精确比较。 

|**行业**|**估计EPR_cash**|**资产寿命特征**|**风险特征**|
|---|---|---|---|
|成熟SaaS|0.69x|短（3–5y）|轻资产，opex可调|
|传统电信（post-2002）|0.76x|中长（10–15y）|稳态行业|
|公用事业（regulated）|0.80x|长（30+y）|高负债+稳定回报|
|航空|0.90x|中（15–25y）|接近平衡线|
|汽车OEM|0.92x|短中（5–10y产品）|接近平衡线|

|**行业**|**估计EPR_cash**|**资产寿命特征**|**风险特征**|
|---|---|---|---|
|AI（v3.2宽口径）|1.40x|混合（4–15y）|远超正常基准|
|AI（v3.2严格口径）|2.70x|同上|远超正常基准|

正常行业代表值0.80x沿用旧估计。AI条件EPR约为其1.8–3.4倍。这些是粗略参照，不是当前经过审计的行业平均。

本节的成熟行业数字沿用v3.1，未更新/未重新核实；只作固定参照。

## **五、历史泡沫的同框架近似估算** 

用同样公式构造四个历史泡沫的 EPR 近似估算。所有数字基于公开学术研究和经济史，会计与 - 统计口径与现代不同，置信度低-中。仅作数量级定位。 

## **5.1 1844-1847 英国铁路狂热** 

背景。1847 年铁路 capex 占英国 GDP 7-8%（Mitchell historical statistics），是军费的两倍。 1844-1846 铁路股票指数翻倍后崩盘，1847-49 股价下跌 50%+。 

|**项目**|**估计值**|**说明**|
|---|---|---|
|累积铁路资本承诺1844-1847|£170M|Odlyzko估计|
|英国GDP 1846|£550-600M|Mitchell historical statistics|
|1847<br>铁路capex/GDP|7-8%|Tandfonline (2022)历史研究|
|年D&A（L=30y on £170M部<br>署）|£5.7M|铁路资产寿命长|
|年opex（统一口径：K的10-15%）|£17-25.5M|与AI同假设，未按行业校准|
|年opex（校准口径：经营比率45-55%）|£4.5-8.2M|当年铁路working expenses约为收入的45-55%（≈K的2.6-4.9%）|
|年利息（d=60%, r=4.5-5%）|£4.6-5.1M||
|P_cash|统一£27-36M / 校准£15-19M||
|1846铁路运营收入|£10-15M||
|估算EPR_cash|统一1.8-3.6x（中位2.5-3x）/ 校准约1.0-1.9x|对o假设极敏感|

解读。统一运维口径下 1840s 英国铁路 EPR 估算 2.5-3x；但按当年实际经营比率校准运维后仅约 1.0-1.9x。两个口径都列出（v3.1）：差异说明该锚点不够稳，叠加 K 用承诺口径（AI 用已部署口径）的不对称，本文不再以"AI 低于 1846 峰值"作为排序结论。机制层面与 AI 仍极相似：真实技术 + 真实未来需求 + 资本市 场提前外推 + 反身性融资。结果：1847 Bank of England 加息和 banking crisis 引发崩盘。铁路 股 1847-1850 跌 50-80%。但铁路网络最终建成并产生持续回报——投资者亏损，社会获益。 

## **5.2 1865-1873 美国铁路扩张** 

背景。1865-1873 美国铁路里程从 35,000 翻倍到 70,000 英里。1873 年 9 月 Jay Cooke 破产引 发 Panic of 1873。1873-1879 长萧条，89 家铁路（约 25%）破产。 

|**项目**|**估计值**|**说明**|
|---|---|---|
|累积铁路资本1865-1873|$2.7B|historical estimates|
|美国GDP 1873|约$7B|Williamson historical|

|**项目**|**估计值**|**说明**|
|---|---|---|
|累积capex / GDP|约38%|极高|
|年D&A（L=30y）|$90M||
|年opex（统一口径：K的15%）|$405M||
|年opex（校准口径：1872经营比率~65%）|$338M（≈K的12.5%）||
|年利息（d=70%, r=7%）|$132M|高杠杆高利率|
|P_cash|统一$627M / 校准$560M||
|年铁路运营收入1872|约$520M|Census/ICC historical|
|估算EPR_cash（聚合）|约1.1-1.2x|统一1.21x / 校准1.08x|

解读。整体铁路 EPR 约 1.1-1.2x。老成熟线路盈利掩盖了新建投机线路的极度压力。崩盘机制：Jay Cooke 募资失败 → 信用紧缩 → 整体铁路债券价格崩塌 → 银行倒闭 → 6 年长萧条。 

## **5.3 1996-2001 美国电信光纤泡沫** 

背景。WorldCom CEO 声称互联网流量每 100 天翻倍（实际每年约 2x）。1996-2001 年美国电 信公司发行新债 $500B+，铺设光纤 80M 英里。Global Crossing 2002 破产留下 $12.4B 债务。 WorldCom 2002 破产，最大美国会计欺诈案。2002 仅 2.7% 美国光纤被"点亮"。2004 长途批发 价同比下跌 55%。 

|**项目**|**估计值**|**说明**|
|---|---|---|
|累积美国电信capex 1996-<br>2001|约$500B|行业聚合|
|峰值年capex (2000)|$120B|BEA|
|美国GDP 2000|$10.25T|BEA|
|峰值capex/GDP|约1.2%||
|年D&A（L=15y on $500B部<br>署）|$33B||
|年opex（K<br>的10-12%）|$50-60B||
|年利息（d=60%, r=8%）|$24B||
|P_cash|$107-117B||
|2001 IP/data终端收入|$30-50B|从总电信收入剥离|
|估算EPR_cash<br>（仅IP/data新<br>建段）|约2.5-4x|中位3x|
|全行业（含语音稳态）EPR|约0.5-0.8x|稳态业务掩盖新建IP压力|

解读。剥离稳态语音业务后，IP/data新建段EPR约3x。这个对照说明，成熟业务的收入可能掩盖新建基础设施的压力。它不证明当前每家云厂商的现金流健康；本版只用前述条件计算比较资本压力。

## **5.4 2005-2008 美国住房（对照案例）** 

|**项目**|**估计值**|**说明**|
|---|---|---|
|住房抵押债务/GDP 2007|97%|FRED|
|住房存量总价值2007Q3|约$24T||
|住房抵押债务2007Q3|约$10T|FRED HHMSDODNS|
|年D&A<br>（住房2%折旧）|$480B||
|年现金opex|$700B|约K<br>的3%|
|年利息|$600B||
|P_cash|约$1.78T||
|年租金收入（实际+imputed）|约$1.7-2T|BEA|
|估算住房EPR_cash|0.9-1.1x||

解读。住房 EPR 约 1.0x，不极端。住房泡沫核心不在 EPR，而在三个不同维度：(1) 价格/收入 比从 3x 升到 5x；(2) 信贷质量（NINJA loans、option ARM）；(3) 证券化的去监管和评级欺诈。 重要结论。EPR 不是衡量所有泡沫的万能指标。住房泡沫是"价格 + 信贷质量 + 证券化"三层结构， 铁路/电信/AI 是"资本前置 + 需求外推 + 资产寿命短"结构。 

## **5.5 其他历史案例（简表）** 

|**案例**|**时期**|**EPR估计**|**主要破裂机制**|
|---|---|---|---|
|日本资产泡沫|1985-1990|n/a（价格泡沫）|股市跌60%<br>，地价跌80%，30<br>年通缩|
|中国钢铁过剩|2010-2016|约0.5-0.7x|价格跌70%，供给侧改革整合|
|美国页岩油|2011-2016|约1.5-2x|油价崩盘75%，~100<br>家E&P破<br>产|
|加密货币<br>（2017/2021<br>）|2017, 2021|n/a（叙事泡沫）|比特币跌80%多次|

本节历史输入沿用v3.1，本次未重新核实原始档案；铁路两种运维假设的数值由epr.py复算。

## 六、更新后的历史位置

| 参照 | EPR | 本版含义 |
|---|---|---|
| 正常行业 | 0.65–0.95x | 旧基准 |
| 1873美国铁路 | 1.08–1.21x | 聚合口径 |
| 2014页岩油 | 1.5–2x | 中点1.95x位于此区间 |
| AI v3.2 宽/严格 | 1.40x / 2.70x | 旧K下的条件计算 |
| 1846英国铁路 | 1.8–3.6x / 1.0–1.9x | 统一/校准，不作稳定排序 |
| 2000电信新建段 | ~3x | 旧高位参照 |

更新后仍高于正常行业，几何中点已进入页岩油区间。收入上升使固定分子下的比率下降，但K未重测、严格表仍含旧估计，不能把条件改善写成行业风险下降或“全面崩盘概率降低”。

## 七、资本支出与GDP

## 7.1 规模比较

用公司全年指引合计作规模比较：Big-5假设AI部分中点616.875B / 美国GDP季调年率33.010036T，约1.9%；再加已列两家新云厂商指引中点59.5B，约2.0%。Oracle财年不同，75%为旧AI占比假设；公司业务在全球，故这不是美国境内AI投资占比，也不是完整行业总量。SpaceX前九月39.995B和IREN剩余财年15B单列，不加进这个全年数。

Goldman在2026-08-07公布的研究估计为全球AI投资约1000B，其中美国581B；其估计美国/GDP1.8%、全球/GDP0.9%。这替换旧0.8%说法，但仍是研究估计，方法和地域范围不同，不代入本文75%算法。历史比较仍用1847铁路7–8%、2000电信约1.2%、2005–2006住房投资约6.3%的旧参照，未重新核实。 [Goldman](https://www.goldmansachs.com/insights/articles/global-investment-is-forecast-to-exceed-1-trillion-in-2026) (2026-08-07)

## 7.2 GDP增长贡献

圣路易斯联储原文的39%是2025年前三季度AI相关投资类别对实际GDP增长的贡献占比，第三季度单季为11%、0.48个百分点。旧文把39%写成单季，并有一处称名义增长，这两处已改。研究涵盖软件、研发、信息设备和数据中心，不全是纯AI投资。 [St. Louis Fed](https://www.stlouisfed.org/on-the-economy/2026/jan/tracking-ai-contribution-gdp-growth) (2026-01-12)

Furman92%、Goldman1.5个百分点和净0.1–0.2个百分点、旧文净贡献0.1–0.5个百分点及进口占70%+，本次未核实或更新，不再作为当前结论。贡献占比与百分点不是同一单位，不能直接说相差100倍或1000倍。公司全球capex/GDP也不能直接推算美国GDP增长贡献。

## 八、敏感性与原有时间情景

## 8.1 单项敏感性

| 变化 | 条件 | EPR 宽 |
|---|---|---|
| R_T → $300B | P = $364.65B | 1.22x |
| R_T → $400B | P = $364.65B | 0.91x |
| R_T → $180B | P = $364.65B | 2.03x |
| R_T → $135B | 严格基准 | 2.70x |
| K → $1.7T | P = $477B (+$112B) | 1.83x |
| K → $2.0T | P = $561B (+$196B) | 2.16x |
| GPU寿命4→3年 | 旧假设折旧增加43B | 1.57x |
| o 10% → 15% | +$65B | 1.65x |
| r×d → WACC 8% | 按旧近似增加80B，替代r×d | 1.71x |
| 在建资产不折旧 | D&A −$32–43B | 1.24–1.28x |

这张表是逐项改变假设，不是统计置信区间。旧版“90%可信区间”没有可复算概率模型，本版不把它当作更新后的区间。

## 8.2 时间路径（原情景，仅更新收入起点）

年capex600B、混合折旧率16.4%、收入CAGR50%/25%/10%均沿用旧情景，不是当前公司指引或新预测。K起点1.3T，收入起点由220B同步到260B；稳态K=600×6.1=3.66T仍只是该情景计算。

| 年份 | K ($T) | P ($B) | R@50% ($B) / EPR | R@25% ($B) / EPR | R@10% ($B) / EPR |
|---|---|---|---|---|---|
| 2026 | 1.3 | 365 | 260 / 1.40x | 260 / 1.40x | 260 / 1.40x |
| 2027 | 1.7 | 473 | 390 / 1.21x | 325 / 1.46x | 286 / 1.65x |
| 2028 | 2.0 | 564 | 585 / 0.96x | 406 / 1.39x | 315 / 1.79x |
| 2029 | 2.3 | 640 | 878 / 0.73x | 508 / 1.26x | 346 / 1.85x |
| 2030 | 2.5 | 703 | 1316 / 0.53x | 635 / 1.11x | 381 / 1.85x |
| 2031 | 2.7 | 756 | 1974 / 0.38x | 793 / 0.95x | 419 / 1.81x |
| 2032 | 2.9 | 800 | 2962 / 0.27x | 992 / 0.81x | 461 / 1.74x |

50%情景在2028年约0.96x；25%情景2027年约1.46x，2031年约0.95x；10%情景在2029–2030年约1.85x。旧文“25%到2032才到0.95x”和“10%维持2x”随起点变化不再成立。不能把这些情景改写成最可能发生的日期。

## 九、公司披露对风险判断的影响

英伟达FY27 Q2数据中心季度收入89B，同比117%；季度数乘4约356B，只是季度年化，不是终端AI收入。供货和产能承诺从旧95.2B更新到279B。10-Q还列股权投资存量99B和未来股权承诺25B，不能把它们当作同一年新增投资合计，更不能和供货承诺混称一类循环投资。 [IR](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Second-Quarter-Fiscal-2027/default.aspx) (2026-08-26); [10-Q](https://investor.nvidia.com/files/doc_financials/2027/NVDA-2027-Q2-10Q-Final-including-exhibits.pdf) (2026-08-26)

CoreWeave backlog104.2B / 季度收入2.575B约40.5x；除以全年收入指引中点12.8B约8.1x。两个分母不同，不能混为同一倍数。其订单和IREN20.3B订单都取决于交付条件，Nebius>40B客户承诺也不能直接称可兑现收入。

旧文四家公司自由现金流300+B、CoreWeave租赁杠杆4.2x、Copilot渗透率3.3–4.4%和400M席位、推理成本下降10–30倍、硬件18–24个月迭代及GPU24个月残值说法，本次未更新/未核实，不用于当前结论。微软本季明确没有更新Copilot数量。不能据此保证某类公司不会破产，或断言哪家公司一定最脆弱。 [IR](https://www.microsoft.com/en-us/Investor/events/fy-2027/earnings-fy-2027-q1) (2026-10-28)

## 十、沿用的观察项目

继续观察模型公司终端收入、资本支出指引、资产寿命政策、订单交付和融资成本。英伟达供货承诺现为279B，CoreWeave backlog104.2B，Anthropic总承诺895.4B。新披露与旧假设要分别保存日期，不能把公司指引当作完成量。

旧H100每小时3美元、B200每小时5美元和月增速10%等观察阈值未核实，本版不将其作为当前市场报价或经验证的转折判据。融资估值使用已经宣布的Anthropic965B和OpenAI852B，前者对应官方47B/报道65B约20.5x/14.8x，后者对应24B/报道50B约35.5x/17.0x；日期不同，不能直接用来排序。

## 十一、最终判断

截至2026-11-09可得资料，在K=$1.3T及原成本参数不变时，R_T严格135B、宽260B，EPR严格2.70x、宽1.40x，几何中点1.95x。高于正常行业的条件结论仍成立；中点已进入页岩油1.5–2x区间，旧上沿以上的定位需改。1846铁路的排序仍不稳定。

公司收入增长和承诺扩大都有一手证据，但不完整的资本存量、模型/云/应用之间的扣重叠估计，限制了风险判断。本版不保留“Anthropic承诺相对克制”“最可能在某年消化完”“某类公司不会破产”的肯定说法，也不把条件重算写成全行业实际改善。

## 十二、限制

EPR不是传统财务杠杆，也不含模型与应用层的研发、销售、管理、税和股权机会成本。R_T混合不同测量日期，且宽口径含报道和内部归因，严格口径仍含标明的旧估计；数据不足的项目未计入会低估分母。K和行业TTM未更新，capex期间及租赁确认也不一致。历史和成熟行业均为旧粗估，敏感性不是统计区间。

Anthropic云市场总额与SpaceX合并收入尤其容易重复。本文不重复加入Anthropic模型转售，不把SpaceX SI整体或新云厂商整体收入当终端收入；但微软净额、应用API扣除等仍缺完整明细，不能宣称已完全消除所有重复。

## 十三、可复现计算

```bash
python3 epr.py
```

inputs.json保存输入和新增披露；epr.py复算P、R_T合计、EPR、资本支出、敏感性、时间情景和铁路对照，并断言正文基准P=364.65、严格/宽收入135/260、Big-5混合期间合计810/835。来源表区分假设、报道、官方披露及公开电话会转录。

## 十四、来源

本次逐项来源和旧值处理完整列于 [data/sources_2026-11.md](data/sources_2026-11.md)。公司披露、统计和报道的日期不同，未更新项不称为最新值。以下保留原文的历史和方法参考，不表示本次已重新核实。

## 历史泡沫： 

- Andrew Odlyzko, "Collective Hallucinations and Inefficient Markets: The British Railway Mania of the 1840s" (2010) 

- Andrew Odlyzko, "The Railway Mania of the 1860s" 

- Mitchell, B.R., British Historical Statistics 

- Williamson, J.G., American Growth and the Balance of Payments 1820-1913 

- "Dark Fiber—an Archaeology of the Dot-Com Bubble" (Technostatecraft, 2025) 

- "Lessons from History: The Rise and Fall of the Telecom Bubble" (Fabricated Knowledge, 2023) 

- Global Crossing bankruptcy filings (2002) 

- WorldCom Form 10-K 2001 (SEC EDGAR) 

- FRED HHMSDODNS, DPI (US housing leverage) 

- Federal Reserve History: "The Great Recession and Its Aftermath" 

## 框架与方法论： 

- Jorgenson, D.W. (1963), "Capital Theory and Investment Behavior" 

- Public utility revenue requirement framework (standard regulatory economics) 

- Damodaran, A. (2024-2025), "Implied required revenue to justify AI capex" blog series
