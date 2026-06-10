Languages: [English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)
PDF: [English](ai-capital-pressure-v3.en.pdf) | [简体中文](ai-capital-pressure-v3.zh-CN.pdf) | [日本語](ai-capital-pressure-v3.ja.pdf)
（PDF 为 v3 存档；v3.1 修订以各语言 Markdown 为准）

# AI Capital Pressure

## **AI 产业链年度资本压力的跨行业与历史比较** 

EPR 框架下的压力测试：与正常行业、与历史四大基础设施周期的同框架对比 _dda | 2026-05-25（v3.1 修订 2026-06-10）|_非投资建议_ | 数据全部更新至 _2026 Q1_ 财报后 

## **数据核查与版本说明** 

**v3.1（2026-06-10）修订说明**：外部复核后修正五处口径，全部数字可由仓库内 `epr.py` + `data/inputs.json` 复算（脚本内置一致性断言）。(1) 严格口径 R_T 改用 Anthropic 官方 $30B（$40B 转引数字仅入宽口径），并扣除应用层付给模型 API 的转售（约 $6-8B），取消此前 $147B→$160B 的向上取整：严格口径 EPR 从 2.28x 修正为 2.81x；宽口径同步扣转售后为 1.66x。(2) 历史案例补运维校准敏感性：1846 英国铁路按当年经营比率（45-55%）校准后 EPR 仅约 1.0-1.9x，"AI 低于 1846 峰值"不再作为头条结论。(3) Big-5 2026 capex 统一为 $755-805B（与 §3.2 逐公司表一致）。(4) 明示 R_T 为瞬时 run-rate，补 TTM 参考口径（约 2.6x）。(5) 敏感性表补"在建工程不计折旧"一行。修正后中心结论的方向不变，幅度变化见下文。


本文所有关键数据已更新至 2026 年 5 月 25 日可得的最新公开来源。相对早期估算的主要更新： 

|**关键数据**|**更新值**|**来源（置信度）**|
|---|---|---|
|Anthropic ARR|约$40B（May 2026<br>，从April<br>$30B进一步上升）|Anthropic<br>官宣$30B +<br>TechCrunch<br>转引内部人士$40B<br>（中）|
|OpenAI ARR|$24-25B（April 2026）|Reuters / Sacra / OpenAI Q1<br>funding announcement（中-高）|
|Microsoft AI ARR|$37B（FY26 Q3）|MSFT官方电话会披露（高）|
|OpenAI<br>总commitments|约$1.4万亿（5+年累计名<br>义）|Sam Altman公开确认（中）|
|Big-5 hyperscaler 2026 capex|$755-805B（Q1后4家<br>中3家上调）|Q1 2026 10-Q +公司指引（高）|
|CoreWeave季度收入|$2.08B（Q1 2026，+112%<br>YoY）|CRWV 10-Q（高）|
|CoreWeave<br>收入backlog|$99.4B（vs<br>早期$30B+）|CRWV Q1 2026披露（高）|
|CoreWeave 2026 capex指引|$31-35B|CRWV指引（高）|
|NVDA Q1 FY27总收入|$81.6B（DC: $75.2B）|NVDA 8-K（高）|
|NVDA Q2 FY27指引|$91B (±2%)|NVDA指引（高）|
|NVDA supply commitments|$95.2B（Q4 FY26披露）|NVDA Q4 FY26 CFO<br>commentary（高）|
|Anthropic估值/融资|$380B (Series G Feb 2026) →<br>$850-900B预期|Anthropic + TechCrunch报道（中-<br>高）|
|OpenAI估值/融资|$852B (March 2026 close<br>$122B round)|官方融资公告（高）|
|Goldman 2026 AI capex<br>baseline|$765B|Goldman Sachs Research 2026-<br>04（高）|

在所有更新中，对结论影响最大的是 Anthropic ARR 从 $8-10B 跃升到 $40B、Microsoft AI ARR 披露 $37B、OpenAI commitments 栈累积到 $1.4T。这显著改变了 R_T 终端收入和 commitments/revenue 比的具体数字，但 EPR 框架的整体结论方向不变。 

## **中心结论** 

结论先行。本文用统一指标 EPR（Economic Pressure Ratio）= 年度资本服务压力 / 可核验终端 收入，把 AI 产业链与正常行业和历史泡沫放在同一框架下比较。 

先明确定义：EPR 不是传统的"杠杆率"（不是 Debt/Equity、不是 Debt/EBITDA），而是 capital service pressure ratio——衡量每年必须从终端收入中消化多少资本相关成本（折旧 + 现金运维 + 利息）。这个指标本质上是 Jorgenson (1963) 资本服务成本理论和公用事业 revenue requirement 模型的简化形式，应用于 AI 周期分析。EPR 是为本文讨论方便而采用的命名，框架 本身不是新的。 

在本文假设下（K=$1.3T，加权资产寿命 6.1 年，o=10%，r=5.5%，d=30%），AI 产业链当前 EPR_cash 处于 1.66x–2.81x 区间（宽/严格口径），中位约 2.1–2.2x。这是基于明确假设的压力测试结果，不是精确的行业测量。 

放进基准里看： 

   - 正常行业（公用事业、电信、成熟 SaaS、汽车、航空）EPR 约 0.65–0.95x。AI 当前 EPR 是正常行业基准的 2–3 倍。 

   - 历史基础设施周期峰值 EPR 同框架近似估算：1840s 英国铁路 2.5–3x、1996–2001 美国 电信光纤（剥离稳态语音业务，仅看新建 IP/data 段）约 3x、1873 美国铁路约 1.2x（聚 合口径）、2014 美国页岩油约 1.5–2x。2007 美国住房 0.9–1.1x，但住房是价格 + 信贷 质量 + 证券化结构泡沫，EPR 不是合适指标。 

- AI 当前 EPR 数量级高于 1873 美国铁路聚合口径（约 1.1-1.2x），处于 2014 美国页岩油（1.5-2x）上沿或略高，低于 2000 电信新建段（约 3x，本文最可靠的高位历史参照）。与 1846 英国铁路的排序不稳健：统一运维口径下 1846 约 2.5-3x，但按当年经营比率校准后仅约 1.0-1.9x（见 5.1），故不作排序结论。较 2025 年中估算的 EPR 中位 2.5-3.0x 有所下移——这反映 2026 上半年 Anthropic ARR 暴涨 （$9B→$40B）、Microsoft AI ARR ($13B→$37B)、OpenAI 高速增长所驱动的 R_T 大 幅扩张。 

- 需要警告：EPR 中心 2.1-2.2x 仍远超正常行业基准，仍处于"基础设施泡沫量级"区间。AI 已明显越过 1873 铁路聚合口径的位置；与 1846 铁路的相对位置取决于历史运维校准，不宜下硬结论。 

- AI 不接近 2007 美国住房模式。住房是"价格 + 信贷质量 + 证券化"结构，与 AI 的"capex 前置 + 短资产寿命"是不同的失败模式。 

Capex 占 GDP（严格区分水平和增长贡献）： 

- AI capex 水平 / GDP（存量口径）：Goldman 估算 AI capex 当前占 GDP 约 0.8%。2026 美国 Big-5 hyperscaler 总 capex $755-805B（其中 ~75% 为 AI 相关 ≈ $565-605B），占美国 GDP（~$30T）约 1.9%（含全行业 AI capex 约 2.1-2.2%）。1847 年英国铁路 capex 占 GDP 7-8%。1999-2000 年美国电信 capex 占 GDP 约 1.2%。AI 当前水平略高于 2000 电信峰值，远低于 1840s 铁路。 

- AI capex 对 GDP 增长的贡献（增量口径，比水平口径敏感得多）：圣路易斯联储测算 2025 Q3 AI 相关投资占实际 GDP 增长的 39%。Jason Furman 估算信息处理设备和软件 投资占 H1 2025 GDP 增长的 92%。但 Goldman Sachs（Jan Hatzius）反驳：扣除进口 资本品后，AI capex 对 GDP 增长的净贡献仅 0.1–0.2 个百分点。两个口径相差 100 倍以 上。本文采用 St Louis Fed 数字作为参考，但承认 Goldman 的进口资本品调整是重要的 方法论修正。 

置信度。"AI EPR 远超正常行业基准"：高。"AI EPR 中位 2.1-2.2x"：中（强烈依赖 R_T 口径假设；R_T 估计的最大不确定性在于内部 AI usage 归因和私募 ARR 数字未审计）。"AI 高于 1873 铁路聚合、低于 2000 电信新建段"：中。"与 1846 铁路的排序"：低（对历史运维校准极敏感）。"AI 大概率走类似消化路径而非全面崩盘"：中-高。"具体出 清时点"：低。所有历史 EPR 数字置信度低-中。 

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

## **二、AI 产业链当前 EPR（数据更新）** 

## **2.1 输入参数（更新）** 

|**参数**|**取值（更新）**|**相对早期估计的变化**|
|---|---|---|
|K（已部署+<br>在建AI capex<br>stock）|$1.3万亿|从$1.2T<br>上调8%（capex加速）|
|L（资产加权平均经济寿命）|6.1年|不变|
|o<br>（现金opex / K）|10%|不变|
|r（平均债务融资利率）|5.5%|不变|
|d（债务融资占比）|30%|不变|
|R_T宽口径（瞬时run-rate）|$220B|从$150B大幅上调（+47%）；v3.1扣应用层API转售|
|R_T严格口径（瞬时run-rate）|$130B|从$90B上调（+44%）；v3.1用Anthropic官方$30B、扣API转售、取消向上取整|
|m_T<br>（终端AI毛利率）|50%|不变|

K 上调原因：2025 hyperscaler AI capex 约 $260B + 2026 H1 部署 ~$260B + Neocloud + 其他 主体的累积部署 + 在建工程。 

R_T 大幅上调的核心原因：Anthropic ARR 从 2025 末的 $9B 升至 2026 May 的 ~$40B（增长 4.4x）；Microsoft AI ARR 披露 $37B；OpenAI 维持 ~$25B 但持续高速增长。AI 终端收入快速 兑现是 EPR 改善的最重要变量。 

## **2.2 EPR 计算（更新）** 

|**项目**|**公式**|**结果（更新）**|
|---|---|---|
|年折旧（分层加总）|ΣK_i/L_i = $1.3T ×<br>16.4%|$213B|
|年现金opex|o × K|$130B|
|年现金利息|r × d × K|$21.5B|
|年化经济压力P_cash|小计|$365B|
|EPR_cash宽口径|P / R_T(宽$220B)|1.66x|
|EPR_cash严格口径|P / R_T(严$130B)|2.81x|
|EPR_cash中位估计||约2.1–2.2x|
|EPR_cash（TTM参考口径）|P / TTM宽R_T(~$140B)|约2.6x（R_T为瞬时run-rate，TTM口径更保守）|
|毛利覆盖所需收入R_req|P / m_T|$729B|
|当前缺口（宽）|R_req − R_T|约$509B|
|当前缺口（严）|R_req − R_T|约$599B|

解读。EPR 在宽口径下 1.66x，严格口径下 2.81x。中位估计约 2.1-2.2x。比 2025 年中估算的 2.5-3.0x 有所下移，但下移幅度小于 v3 初版给出的 1.6-2.3x——初版严格口径存在向上取整和未审计数字混入，v3.1 已修正。注意 R_T 是瞬时 run-rate（exit ARR）而 P 是年化压力：在收入半年翻倍的阶段，TTM 口径的 EPR 约 2.6x，瞬时口径天然偏乐观。 

什么变了？R_T 大幅扩张。这是 EPR 改善的全部驱动力。从 2025 年中到 2026 年 5 月，AI 终 端收入大约翻了一倍，而 P（资本压力）只增长了约 8%（K 从 $1.2T 升到 $1.3T）。R_T 增速 >> P 增速 → EPR 下降。 

什么没变？所有缓冲和放大因素仍然存在。OpenAI 总 commitments 涨到 $1.4T、CoreWeave backlog 涨到 $99.4B、NVDA 循环投资规模 >$40B、hyperscaler 2026 capex 指引仍在上修。AI 周期同时在两个方向加速：revenue 在追、capex 也在追。EPR 是这两个 race 的差。 

## **2.3 R_T 自下而上分解（核心更新表）** 

R_T 是 EPR 框架最敏感的输入。下表给出 2026 May 严格口径和宽口径的逐项分解。 

|**类别**|**严格口径**|**宽口径**|**置信度/说明**|
|---|---|---|---|
|Anthropic（Claude API +<br>订阅<br>+ Claude Code）|$30B（官方）|$40B（转引）|TechCrunch转引内部<br>人士May 2026<br>（中）；Anthropic公<br>开$30B April 2026<br>（高）|
|OpenAI（API + ChatGPT订<br>阅）|$25B|$28B|Reuters reports /<br>Sacra（中-高）|
|Microsoft AI净（$37B less|$27B|$30B|MSFT FY26 Q3<br>披露|

|**类别**|**严格口径**|**宽口径**|**置信度/说明**|
|---|---|---|---|
|~$10B Azure-OpenAI转售）|||$37B<br>；本文扣除<br>Azure-OpenAI转售部<br>分|
|xAI、Mistral、Cohere、其他模<br>型公司|$5B|$8B|低-中|
|Google Gemini Advanced +<br>Workspace AI|$5B|$8B|中-低（GOOG未单独<br>披露）|
|专用AI<br>SaaS（Cursor、Glean、Harve<br>y、Perplexity、Cognition、Sie<br>rra）净额|$9B|$12B|中；毛额$15B/$20B，扣除付给模型API的~$6B/$8B（已计入Anthropic/OpenAI ARR）|
|传统SaaS<br>的AI add-on增量<br>（Salesforce<br>Agentforce、ServiceNow Now<br>Assist）|$10B|$15B|低-中（仅增量）|
|中国AI商业化（百度、字节、<br>阿里、智<br>谱、DeepSeek、Moonshot）|$10B|$15B|低|
|AWS Bedrock + GCP Vertex<br>AI<br>终端计费（扣除<br>Anthropic/OpenAI转售）|$5B|$10B|中-低|
|Hyperscaler<br>内部AI usage归<br>因（搜索、广告、推荐增量）|0（不计）|$35B|低（不可独立核验，<br>但规模真实）|
|咨询/专业服务/<br>企业内部<br>productivity savings|0（不计）|$10B|低|
|长尾（其他付费）|$5B|$8B|低|
|排除项1：Azure/AWS/GCP卖<br>给OpenAI/Anthropic的中间收<br>入|排除|排除|避免双重计算|
|排除项2：NVIDIA GPU销售<br>收入|排除|排除|上游资本品收入|
|排除项3：应用层付给模型API<br>的转售部分|排除|排除|避免模型层↔应用层双重计算（v3.1新增）|
|合计（就近取整到$5B）|$131B →<br>取$130B|$219B →<br>取$220B||

两个口径的差异。严格口径只计入可核验的纯 AI 产品收入（API、订阅、Claude Code 类终端产 品）。宽口径加入 hyperscaler 内部 AI usage 归因（搜索、广告、推荐 AI 增量）和企业 productivity savings。两者的差异主要在于 归因可不可信。

Anthropic $40B 的来源与口径分配。公司官方在 4 月 6 日披露 ARR 已超 $30B。TechCrunch 后续报道 4 月底 ARR "closer to $40B" per 内部信息源——该数字未经审计、未在 SEC 文件披露。v3.1 起，严格口径（定义为"可核验"）只用官方 $30B，$40B 仅进宽口径。从 $14B（Feb）→ $19B（March）→ $30B（April）→ $40B（May）的轨迹约相当于 10 周翻倍。 

Microsoft $37B 净 $27B 的拆分逻辑。 Microsoft 官方 FY26 Q3 披露 AI 业务 ARR $37B（+123% YoY）。但这个数字包含 Azure OpenAI Service 中卖给最终客户的部分（已在最 终客户处计费，可计入 R_T）和卖给 OpenAI 自己的转售部分（应排除，避免与 OpenAI ARR 重 复）。本文估算重叠约 $10B，净计入 $27B。注意微软官方口径明示该 $37B "包含所有 model builders 在 Azure 上的收入"，OpenAI 与 Anthropic（承诺采购 $30B Azure）合计的重叠可能大于 $10B，拆分不确定性放宽为 ±$5-10B。 

## **三、K、年度 Capex 与 Commitments 严格分层** 

## AI 产业链涉及三类相关但本质不同的数字。混用导致严重的双重计算或概念错误。 

|**层级**|**定义**|**会计性质**|**在本文中的用途**|**典型2026数字**<br>**（更新）**|
|---|---|---|---|---|
|K<br>：已部署+在建资<br>本存量|账上资产NBV +在建工<br>程|存量|进入EPR分子|估计$1.3T|
|年度Capex|当年PP&E购置流量|流量|预测未来K<br>；用于<br>capex/GDP水平|Big-5 $755-805B；<br>含AI ~$565-605B|
|Commitments|尚未全部部署的合同义<br>务/announced|合同义<br>务/<br>announce<br>d|未来K领先指标|OpenAI<br>总栈~$1.4<br>万亿over 5+年|

## **3.1 K（约 $1.3T，更新拆解）** 

- Hyperscaler AI 累积 capex stock（Big-5 2022-2026 累积按 AI 部分 75%）：约 $780880B 

- Neocloud AI capex stock（CoreWeave PP&E $36.4B + Lambda + Crusoe + Nebius 等）：约 $90-130B 

- 其他（Oracle AI infra、企业自建、政府/sovereign 投资）：$200-300B 

- 合计区间约 $1.07-1.31T；本文取上沿 $1.3T（使 P 偏高、EPR 偏保守）。注意与历史案例比较时的口径差异：AI 的 K 为已部署口径（不含 $1.4T commitments），而 1846 铁路的 £170M 为累积承诺口径——该不对称使历史锚点偏高、AI 偏低（见 5.1） 

## **3.2 年度 Capex（2026 最新指引）** 

|**主体**|**2024**|**2025**|**2026指引/估计（Q1**<br>**后更新）**|**AI**<br>**部分(~75%)**|
|---|---|---|---|---|
|Microsoft|~$56B|~$95B|~$190B<br>（含$25B<br>高<br>component pricing）|~$140B|
|Alphabet|~$53B|~$75B|$180–190B（Q1后从<br>$175-185B上调）|~$140B|
|Amazon|~$78B|~$105B|~$200B|~$150B|
|Meta|~$37B|~$65B|$125–145B（Q1后从<br>$115-135B上调）|~$100B|
|Oracle|~$7B|~$25B|~$60B|~$50B|
|Big-5合计|~$231B|~$365B|$755–<br>805B（CreditSights|~$580B|

|**主体**|**2024**|**2025**|**2026指引/估计（Q1**<br>**后更新）**|**AI**<br>**部分(~75%)**|
|---|---|---|---|---|
||||$750B）||
|Neocloud合计|~$15B|~$35B|~$60-70B|~$65B|
|行业AI capex<br>流量||~$400B|~$645B||

来源：SEC 10-Q 公开披露、Q1 2026 财报电话会议指引、CreditSights / Goldman Sachs / Yahoo Finance 综合（Q1 后更新）。Big-5 中四家 Q1 后上调 capex 指引；只有 Amazon 维持 原计划（因为已经是行业最高）。 

观察：Goldman Sachs 最新基线模型估算 2026 AI capex $765B，与 CreditSights $750B 估计一 致。Goldman 预测 2031 年 AI capex 达 $1.6T。资本支出/收入比已经突破 Oracle 86%、Meta 54%、Microsoft 47%、Alphabet 46%、Amazon 25%——历史上不可想象的水平。 

## **3.3 OpenAI Commitments 栈（更新到 $1.4T）** 

Sam Altman 公开确认 OpenAI 总 commitments 约 $1.4 万亿（涵盖未来 5+ 年）。这是产业链最 大单点。下表是分解。 

|**合约/承诺**|**名义规模**|**时间窗口**|**置信度**|
|---|---|---|---|
|Oracle compute deal|约$300B|5年（2027-<br>2031）|高（Oracle CEO Safra Catz多<br>次确认）|
|Stargate（OpenAI/<br>SoftBank/Oracle/<br>MGX）|约$500B<br>（已<br>announced<br>$400B+<br>已<br>committed<br>）|4年（2025-<br>2028）|中（announced<br>，与Oracle部分<br>重叠）|
|AMD（6 GW Instinct<br>GPU）|约$90B累<br>积硬件收入|从H2 2026<br>起|中（AMD/OpenAI公开披露）|
|NVIDIA投资|up to<br>$100B|条件性，按每<br>GW部署逐步|中（announced战略合作）|
|Amazon AWS|$38B|7年（2025-<br>2031）|高（2025-11双方签署）|
|Microsoft Azure（重<br>组后）|约$250B<br>cloud<br>purchase|多年|中（双方重组协议）|
|CoreWeave|约$22.4B|至2032|高（CRWV 10-Q披露）|
|Broadcom<br>自研芯片+<br>其他|约$50-<br>100B|多年|中|
|总名义栈（Altman公<br>开数字）|约$1.4万<br>亿|5+年|中-高|
|OpenAI 2026 May|~$25B|当前|中-高|

|**合约/承诺**|**名义规模**|**时间窗口**|**置信度**|
|---|---|---|---|
|ARR||||
|Commitments /<br>Revenue比|||约56x|

OpenAI commitments / revenue 比从早期估算的 28-36x 升至 56x。这是历史上任何模型公司或 客户/供应商关系都未达到的水平。即使 OpenAI ARR 按 100% CAGR 增长（已经是异常乐观），也需要约 4 年才能让 commitments/revenue 比降到 5x 以下（$25B×2⁴=$400B，1400/400=3.5x）；按更现实的 50% CAGR 则需要 6 年以上。

对比 Anthropic commitments 栈： 

|**合约/承诺**|**名义规模**|**说明**|
|---|---|---|
|Amazon|$5B<br>现金+<br>最多$25B + 5GW<br>Trainium + $100B AWS<br>采购<br>(10年)|主要训练伙伴|
|Google|$10B<br>现金+<br>最多$40B + 5GW<br>TPU|4月24日宣布|
|NVIDIA|最多$10B + 1GW GPU供应||
|Microsoft|最多$5B + Anthropic<br>购买<br>$30B Azure compute||
|Broadcom|$21B AI<br>收入(Anthropic 2026<br>估计)|Mizuho测算|
|美国compute基础设<br>施投资承诺|$50B|Nov 2025公开|
|总名义栈估计|$200-300B+|相对ARR $40B<br>比5-7.5x|

Anthropic 的 commitments/revenue 比（5-7.5x）远低于 OpenAI（56x）。这反映两家不同的商 业模式：Anthropic 收入扩张快（约 10 周翻倍），承诺规模相对克制；OpenAI 承诺规模超大，依赖 未来收入兑现。 

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
|AI（v3.1宽口径）|1.66x|混合（4–15y）|远超正常基准|
|AI（v3.1严格口径）|2.81x|同上|远超正常基准|

正常行业 EPR 中位约 0.80x，即便高资本密度行业（公用事业、汽车）也很少超过 1.0x。AI 当前 EPR 是正常行业的 2-3.5 倍。仍然是远离正常基准的量级。 

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

解读。剥离稳态语音业务后，IP/data 新建段 EPR 约 3x。这与 AI 当前情形几乎完全平行： hyperscaler 整体业务（搜索、广告、电商、Office）健康，但新建的 AI 基础设施单独看压力很 大。 

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

## **六、主对比表：AI 在杠杆光谱中的位置（更新）** 

## 把前面所有计算放在一张表里。 

|**案例**|**时期**|**EPR近似估算**|**资产寿命**|**终端崩盘特征**|**与AI相似**<br>**度**|
|---|---|---|---|---|---|
|成熟SaaS|当前|0.69x|3-5y|n/a（稳态）|低|
|传统电信（post-<br>bubble）|当前|0.76x|10-15y|n/a|低|
|公用事业|当前|0.80x|30+y|n/a|低|

|**案例**|**时期**|**EPR近似估算**|**资产寿命**|**终端崩盘特征**|**与AI相似**<br>**度**|
|---|---|---|---|---|---|
|regulated||||||
|航空|当前|0.90x|15-25y|周期性破产|低|
|汽车OEM|当前|0.92x|5-10y|周期性破产|低|
|中国钢铁|2015峰<br>值|0.5-0.7x|20+y|价格跌70%|低|
|美国住房|2007峰<br>值|0.9-1.1x|50+y|房价跌35%，金融<br>危机|低（结构不<br>同）|
|美国铁路|1873峰<br>值|约1.1-1.2x（聚合）|50+y|25%行业破产，6<br>年长萧条|中-高|
|美国页岩油|2014峰<br>值|1.5-2x|5-10y|油价跌<br>75%，~100破产|中|
|AI 2026（宽口径<br>R_T，v3.1）|当前|1.66x|4-15y混合|?|基准|
|AI 2026（严格口<br>径R_T，v3.1）|当前|2.81x|同|?|基准|
|英国铁路|1846峰<br>值|统一2.5-3x /<br>校准1.0-1.9x|50+y|股价跌50-80%|高（排序不稳）|
|美国电信光纤（新<br>建IP/data）|2000峰<br>值|约3x|15-20y|$2T市值蒸<br>发，WorldCom破<br>产|高|

警示：所有历史 EPR 是同框架近似估算，不是"同口径"精确测量。 从更新后的表读出几个关键结论： 

结论 1：AI 位置已经从历史泡沫峰值区间下移，但仍在高位。早期 EPR 2.5-3x 估算让 AI 看起来与 1846 铁路和 2000 电信平齐。v3.1 修正后的 1.66-2.81x 让 AI 明显高于 1873 美国铁路聚合（1.1-1.2x），处于 2014 页岩油（1.5-2x）上沿或略高，仍低于 2000 电信新建段（约 3x）。与 1846 铁路不做排序（其 EPR 对运维校准极敏感：2.5-3x 或 1.0-1.9x）。 

结论 2：AI 仍然远超正常行业基准。正常行业 0.65-0.95x，AI 1.66-2.81x。EPR 中位约 2.1-2.2x ≈ 2.7 倍正常行业基准。仍然在"基础设施泡沫量级"，只是不再是峰值。 

结论 3：方向并未改变，只是程度变缓。 AI 仍然显示"资本前置 + 需求外推"特征。但 R_T 兑现 速度比预期快——这是最重要的"逃逸"路径。如果 Anthropic + Microsoft AI + OpenAI 等 2026-2027 继续按当前增速扩张，宽口径 EPR 可能在 2027-2028 间跌破 1.5x，进入与页岩油峰值同等水平之下。

结论 4：AI 与 1846 铁路和 2000 电信的可比性下降，与 1873 铁路 + 页岩油的可比性上升。 1846 铁路和 2000 电信的特征是终端需求增长严重不及 capex 节奏。AI 当前情形不同——R_T 在以 100%+ 速度扩张。这降低了 AI 走向 1846/2000 类似全面崩盘的概率。 

结论 5：但 capex 端仍在加速。 Big-5 2026 capex 指引从年初约 $620B 升到 $755-805B，Microsoft FY27 暗示更高。如果 capex 持续加速 + R_T 增速放缓，EPR 会反弹。当前 1.66-2.81x 不是稳态。 

## **七、Capex / GDP 双口径分析（更新）** 

严格区分两个完全不同的概念：(1) capex 水平占 GDP；(2) capex 对 GDP 增长的贡献。混用是 经常的错误。 

## **7.1 Capex 水平占 GDP** 

|**案例**|**时期**|**Capex**<br>**水平/ GDP（年口**<br>**径）**|**说明**|
|---|---|---|---|
|英国铁路|1847峰<br>值|7-8%|当年新增capex / GDP|
|美国电信|2000峰<br>值|约1.2%|BEA|
|美国住房（住宅投<br>资）|2005-<br>2006|约6.3%|历史高位|
|AI美国（Big-5<br>2026）|2026|约1.9%|$565-605B AI<br>部分/ GDP $30T|
|AI<br>美国（全行业<br>2026）|2026|约2.1-2.2%|含neocloud + Oracle + sovereign|
|Goldman<br>估算AI<br>capex/GDP|当前|约0.8%（窄口径）|Goldman Sachs Research|
|AI<br>全球2026|2026|约0.6-0.7%|$700-750B /<br>全球$110T|

AI 2026 美国 capex/GDP 略高于 2000 电信峰值，远低于 1840s 铁路。Goldman 估算（0.8%）和本文估算（~1.9-2.2%）的差异在于口径：Goldman 用更严格的纯 AI capex 定义，本文按 hyperscaler 总 capex × 75% AI 比例。 

## **7.2 Capex 对 GDP 增长的贡献** 

这是与 capex/GDP 水平完全不同的指标。GDP 增长贡献看的是 capex 同比增量，不是总量。最 新外部估算存在巨大分歧： 

|**口径**|**估计**|**来源**|
|---|---|---|
|Jason Furman:信息处理设备+<br>软件占H1 2025<br>GDP增长|92%|X帖子|
|St Louis Fed: AI<br>相关投资占Q3 2025<br>实际GDP<br>增长|39%|St Louis Fed On the Economy Jan 2026|
|Goldman Sachs: AI capex<br>对GDP增长贡献<br>（capex增量口径）|1.5 pp名义|Goldman Sachs Research|
|Goldman Sachs: AI capex<br>净GDP增长贡献|0.1-0.2 pp|Jan Hatzius|

|**口径**|**估计**|**来源**|
|---|---|---|
|（扣除进口资本品后）|||
|这些数字相差近1,000倍（0.1-0.2 pp<br>到92%）。原因：|||

   - Furman 用的是 NIPA 类别（Information processing equipment + software），这个类别 H1 2025 因为 AI 投资暴涨而对 GDP 增长贡献占比异常高，但分母（总 GDP 增长）也异 常低。这是分母效应。 

- St Louis Fed 用更精确的 AI-related 子类别，得到 39%（更可信，但仍是名义口径）。 

- Goldman 进一步扣除进口资本品（GPU、HBM、服务器大部分进口），得到净 0.1-0.2 pp。GDP 计算的是国内生产，进口商品不算 GDP 增长。 

- 本文采纳 Goldman 的方法论修正。真实 AI capex 对美国 GDP 增长的净贡献可能只有 0.1-0.5 pp，远低于水平占比（1.7-2.0%）会让人以为的程度。这是因为 AI 投资 70%+ 是进口资本品 （NVIDIA 用 TSMC 制造，HBM 来自 SK 海力士和三星）。 但这个修正反过来意味着：AI capex 如果减速，对 GDP 增长的直接拖累也较小（0.1-0.5 pp 反 转）。反身性更多体现在股市估值 → 财富效应 → 消费，而不是直接的 GDP 计算。 

## **八、敏感性分析** 

EPR 中心估计 2.1-2.2x 看起来精确，实际依赖多个不确定参数。下表展示关键参数变化对 EPR 的影响。 

## **8.1 关键参数敏感性（更新基准）** 

|**假设变化**|**P变化方向**|**对宽口径EPR**<br>**的影响（基准1.66x）**|
|---|---|---|
|R_T<br>从$220B<br>升到$300B<br>（如2027持续高增<br>长）|不变|EPR<br>降至1.22x|
|R_T<br>从$220B<br>升到$400B|不变|EPR<br>降至0.91x（接近正常行业）|
|R_T<br>从$220B<br>降到$180B|不变|EPR<br>升至2.03x|
|R_T<br>从$220B<br>降到$130B（严格口径）|不变|EPR<br>升至2.81x|
|K<br>从$1.3T<br>升到$1.7T（2027末）|P<br>升约$112B|EPR<br>升至2.17x|
|K<br>从$1.3T<br>升到$2.0T（2028）|P<br>升约$196B|EPR<br>升至2.55x|
|GPU/network<br>寿命从4<br>年降到3年|折旧升约$43B|EPR<br>升至1.85x|
|o<br>从10%<br>升到15%<br>（高opex）|opex<br>升$65B|EPR<br>升至1.95x|
|用WACC 8%<br>替代r×d|P<br>升约$80B|EPR_wacc<br>约2.02x|
|在建工程（K的15-20%）<br>不计折旧（v3.1新增）|D&A<br>降$32-43B|EPR<br>降至1.46-1.51x|
|EPR<br>的合理90%可信区间：1.1x-2.9x（宽口径）/ 1.8x-3.8x<br>（严格口径）。点估计是1.66x<br>或<br>2.81x，但实际值在区间内分布。|||

## **8.2 EPR 时间路径（更新）** 

当前 K=$1.3T 仍低于稳态。按年 capex run rate $600B 和 L=6.1 年估算，稳态 K=$3.66T。K 仍 在向上扩张。下面给三档 R_T 增速假设的轨迹（宽口径 $220B 起点）。 假设：年 capex 维持 $600B（2026 实际指引水平）；其他参数不变。 

|**年份**|**K (年初)**|**P**|**R_T**<br>**50%C**<br>**AGR**|**EPR**|**R_T**<br>**25%C**<br>**AGR**|**EPR**|**R_T**<br>**10%C**<br>**AGR**|**EPR**|
|---|---|---|---|---|---|---|---|---|
|2026|$1.3T|$365B|$220B|1.66x|$220B|1.66x|$220B|1.66x|
|2027|$1.7T|$473B|$330B|1.43x|$275B|1.72x|$242B|1.96x|
|2028|$2.0T|$564B|$495B|1.14x|$344B|1.64x|$266B|2.12x|
|2029|$2.3T|$640B|$742B|0.86x|$430B|1.49x|$293B|2.18x|
|2030|$2.5T|$703B|$1114<br>B|0.63x|$537B|1.31x|$322B|2.18x|
|2031|$2.7T|$756B|$1671<br>B|0.45x|$671B|1.13x|$354B|2.13x|
|2032|$2.9T|$800B|$2506<br>B|0.32x|$839B|0.95x|$390B|2.05x|

## 解读： 

- 50% CAGR（接近 2026 上半年实际速度）：R_T 持续按当前速度增长，EPR 在 2027-2028 跌破 1.5x（2028 约 1.14x），2030 接近正常行业基准。这条路径下 AI 周期实现"快速消化"。 

- 25% CAGR（仍然非常激进）：EPR 在 2027 达到峰值约 1.7x，之后缓慢回落。2032 进入正常行业上沿（0.95x）。这是中性情景。 

- 10% CAGR（保守）：EPR 持续在 2x 平台。需要 capex 主动降速才能平衡。可能引发 hyperscaler capex 下修循环。 

注意 50% CAGR 不算极端。 Anthropic 过去 12 个月 ARR 从 $9B → $40B（400%+）。OpenAI 2025 全年从 $6B → $20B（230%）。如果两家继续按 50-100% 增长几年，R_T 完全可能在 2028 达到 $500-600B。 

但当然这也有风险。推理价格战、开源模型挑战、企业渗透饱和都可能让 R_T 增速急停。如果 R_T 增速跌到 10% CAGR 而 capex 继续按 $600B/年水平投放，EPR 会在 2027-2029 持续在 2x 平台，与历史泡沫成立后的消化期相似。 

## **九、AI 与历史泡沫的关键差异（更新）** 

## **9.1 缓冲 AI 周期的因素** 

- Hyperscaler 自身强大现金流。 Amazon/Microsoft/Google/Meta 合并年自由现金流 $300B+。 

- 上游收入扎实可核验。 NVIDIA Q1 FY27 DC 收入 $75.2B（+92% YoY），forward annualized ~$300B+。Q2 指引 $91B/Q。 

- R_T 快速兑现（最重要的更新）。 Anthropic 从 $9B 升到 $40B（6 个月），Microsoft AI ARR $37B，OpenAI ~$25B。AI 收入兑现速度超过历史任何基础设施周期。 

- 多元化降低系统性风险。 

- 技术真实推进。推理成本 2023-2026 累计下降 10-30 倍。Hardware 按 18-24 个月节奏 迭代。 

## **9.2 放大 AI 周期的因素** 

- OpenAI commitments 栈极端（已升至 $1.4T）。 vs 2026 ARR ~$25B = 56x commitments/revenue 比。这是历史前所未有。 

- 循环融资规模庞大。 NVIDIA 2026 投资 $40B+ in equity bets。NVIDIA 单笔 $30B 投入 OpenAI。NVIDIA + CoreWeave + OpenAI 三角循环规模巨大。 

- Neocloud 局部高杠杆。 CoreWeave 含租赁杠杆约 4.2x 年化收入，backlog $99.4B（vs Q1 收入 $2.08B = 48x 季度口径；按 2026 全年收入指引 $12-13B 折算约 8x 前瞻年收入——两个口径都列出以免夸大）。 

- GPU 寿命快速折旧。 H100 在 B200/Rubin 出现后 24 个月内经济价值显著下降。 

- 开源模型挑战专有 API 价格层。 DeepSeek、Llama、Qwen 直接威胁专有 API 定价。这 是 2000 电信没有的因素。 

- Microsoft Copilot 渗透率仍低（3.3-4.4%）。即便 AI ARR $37B 看似很高，但相对 Microsoft 365 商业基础（约 4 亿 seats）覆盖率仍低，意味着上行空间大同时也意味着 R_T 的扩张依赖渗透率持续提升。 

## **9.3 综合判断（更新）** 

AI 缓冲因素比历史泡沫更强，且 R_T 已经显示比 1846 铁路或 2000 电信快得多的兑现速度。 AI 放大因素也比历史更极端，特别是 OpenAI commitments 栈和循环融资规模。 

最可能的路径（更新后）： 

- Anthropic + Microsoft AI 维持高速增长 → R_T 继续扩张 → EPR 在 2027-2028 进一步下 

   - 降到 1.0-1.5x 区间 

- 与此同时，capex 持续加速（Big-5 capex 仍在上修） → K 增速也快 → EPR 下降速度不 会很快 

- OpenAI 是产业链最脆弱点。 Commitments 56x revenue 比无法仅靠收入扩张消化，需要 持续股权融资或 commitment 减记。 

- Neocloud（CoreWeave 等）也是脆弱点。 Backlog 48x 季度收入比依赖 backlog 兑现。 如果 Anthropic 或 Meta 等大客户重谈，会引发连锁 

- Hyperscaler 不会全面崩塌。现金流强 + 多元化。 

NVIDIA 不会破产，但 forward multiples 大幅压缩的概率仍存在。其 supply commitments $95B 和对客户的 $40B+ 投资形成的反身性，使得任何客户层面减速会立刻传导到 NVIDIA 本身。 

## **十、领先指标** 

监测周期转折的高优先级信号（按重要性排序，根据更新后情况调整）： 

- 1. Anthropic 和 OpenAI 增速。当前约 10 周翻倍是异常状态。任何减速到月度增速 <10% 都 是周期转折信号。 

- 2. Hyperscaler 资产寿命政策。 Amazon 已从 6 年下调到 5 年。Microsoft/Google/Meta 跟进会引发 10-15% GAAP 折旧上修。 

- 3. OpenAI commitments 履约速度。 OpenAI 是否能维持 commitments 栈 schedule 部署。 如果 OpenAI 与 Oracle、AWS、CoreWeave 等开始延后或重谈，是 commitments 栈 $1.4T 压力的最早表现。 

- 4. Neocloud 再融资利差和 backlog 质量。 CoreWeave backlog $99.4B 看起来很厚，但 客户集中。任何客户违约或延后部署会立刻冲击 EBITDA。 

- 5. Hyperscaler capex 指引语气。从"加大投资"到"提高效率"的话术变化。 

- 6. NVIDIA supply commitments 变化。当前 $95B。环比明显下降意味着 NVIDIA 对自己 forward orders 信心下降。 

- 7. AI 推理毛利率。 OpenAI/Anthropic inference gross margin 趋势。价格战压制毛利改善 是早期警告。 

- 8. GPU 租赁价格。 H100/H200/B200 spot 价格。H100 spot 长期低于 $3/hour 压力 CoreWeave。B200 新建集群盈亏平衡 $5/hour。 

- 9. AI capex 占 GDP 与对 GDP 增长贡献。当前 capex/GDP 约 1.7-2.0%（美国）。比例 继续上升意味着经济对 AI 反身性依赖加深。 

- 10. 资本市场 AI 主题估值分位。 Anthropic 当前 $850-900B 估值（21-23x ARR）； OpenAI $852B（34x ARR）。这些倍数下行就是周期信号。 

红色组合（同时出现意味着周期转折概率显著上升）：Anthropic + OpenAI 增速减速 + capex 仍 上修 + GPU 租价下跌 + 融资利差扩大 + neocloud backlog 质量下降 + 模型公司 commitments 重谈。 

## **十一、最终判断** 

截至 2026-05-25 可得数据： 

在本文假设下（K=$1.3T，L=6.1 年，R_T=$130-220B），AI 产业链当前 EPR_cash 处于 1.66x-2.81x 区间，中位约 2.1-2.2x。这低于早期 2.5-3.0x 的估算（但 v3.1 修正后降幅小于 v3 初版声称的水平），主要驱动力是 2026 上半年 Anthropic ARR 从 $9B 暴涨到 $40B、Microsoft AI ARR 披露 $37B、OpenAI 维持高速增长。 AI 当前 EPR 位置： 

   - 明显高于正常行业基准（0.65-0.95x）—— AI 仍处于"基础设施泡沫量级"区间 

   - 处于 2014 美国页岩油（1.5-2x）上沿或略高，高于 1873 美国铁路聚合口径（1.1-1.2x） 

   - 低于 2000 美国电信新建段（约 3x）；与 1846 英国铁路不做排序（统一口径 2.5-3x，经营比率校准后仅 1.0-1.9x，锚点不稳） 

- AI 失败模式与历史比较： 

   - 不像 2007 美国住房（价格+信贷+证券化结构） 

   - 不像 1989 日本资产泡沫（纯价格泡沫） 

   - 与 1840s 铁路和 2000 电信的相似性下降，因为 R_T 兑现速度远超那些周期 

   - 与 1873 美国铁路和 2014 页岩油的相似性上升 

AI capex/GDP 占比： 

- 美国 capex 水平 / GDP 约 1.7-2.0%（中等-高，但远低于 1840s 铁路 7-8%） 

- 对 GDP 增长的净贡献 0.1-0.5 pp（Goldman 进口资本品调整后） 

- 名义 GDP 增长贡献口径可达 39%（St Louis Fed） 

## 最可能的路径： 

- 如果 Anthropic + Microsoft AI + OpenAI 等维持 25%+ 年增速，EPR 在 2027-2028 进一 步下降，AI 周期实现"快速消化" 

- 如果 R_T 增速跌到 10% 以下而 capex 持续 $600B+/年水平，EPR 反弹到 2x 以上 

- Neocloud（CoreWeave 等）和过度承诺的模型公司（OpenAI 56x commitments/revenue 比）仍是最脆弱环节 

- Hyperscaler 现金流强大，不会全面崩塌 

- NVIDIA 不会破产，但 forward multiples 大幅压缩仍可能 

一句话总结：在本文压力测试假设下，AI 是真实技术周期 + 历史性资本前置 + 局部高杠杆 + 反 身性融资。EPR 数量级已经从 2.5-3x 下移到 1.66-2.81x（中位 2.1-2.2x），这是 2026 上半年 R_T 兑现速度超预期的真实反映。但 AI 与正常行业仍有 2-3 倍距离，capex 端仍在加速，OpenAI commitments 栈达 到 $1.4T 这一历史前所未有的水平。最可能的结局是 2027-2029 年的"局部出清 + 软消化"组合， 不是全面崩塌；但持有局部高杠杆环节（neocloud、过度承诺的模型公司、长尾应用层）的投资 者会承担实质损失。系统性金融危机概率低，权益和信用局部损失概率高。 

## 置信度汇总： 

- "AI EPR_cash 中位 2.1-2.2x"：中（R_T 关键不确定性减少但仍存在；严格口径已改用官方 $30B） 

- "AI EPR 远超正常行业基准"：高 

- "AI 数量级在历史泡沫范围内"：高 

- "AI 高于 1873 铁路聚合、低于 2000 电信新建段"：中-高 

- "与 1846 铁路的排序"：低（历史运维校准敏感） 

- "AI 不像 2007 住房或 1989 日本"：高 

- "Hyperscaler 不会全面崩塌"：中-高 

- "OpenAI 是产业链最脆弱单点"：高（commitments 56x revenue） 

- "具体出清时点"：低 

## **十二、主要 Caveats** 

- EPR 不是传统杠杆率。是 capital service pressure ratio，本质上是 Jorgenson 资本服务 成本理论的简化形式。 

- EPR 不是完整利润率指标。没有纳入 R&D、SG&A、销售、客服、股权激励、税。真实 利润压力比 EPR 暗示的更高。 

- EPR > 1 不等同于"行业不赚钱"。而是终端收入不足以覆盖本文定义下的年度基础设施压 力。 

- 历史 EPR 是同框架近似估算。不是"同口径"精确测量。所有历史 EPR 置信度低-中。 

- R_T 是全文最敏感变量。 Anthropic $40B 来自 TechCrunch 内部信息源（中等置信度，仅入宽口径；严格口径用官方 $30B）；OpenAI ARR、Microsoft AI ARR 等都是公司选择性披露，未必经审计。

- R_T 是瞬时 run-rate，P 是年化压力。高速增长期 exit-ARR 约为 TTM 的两倍，TTM 口径 EPR 约 2.6x（宽）。本文以瞬时口径为主、TTM 为参考。

- K 含在建工程。在建资产不投运不折旧，若剔除（15-20% 的 K），D&A 降 $32-43B、宽口径 EPR 降至约 1.5x；该效应与"收入滞后于在建"方向相反，列入敏感性而非基准。

- 历史 EPR 的运维参数未必同口径。1846 铁路与 1873 铁路按当年经营比率校准后 EPR 显著低于统一 o 口径（1846：1.0-1.9x vs 2.5-3x）；且 1846 的 K 是承诺口径而 AI 用已部署口径。历史排序结论因此降级。

- 模型层→应用层 API 转售已扣除（v3.1）。应用层 AI SaaS 的收入按净额计入，避免与模型公司 ARR 双重计算；微软 AI ARR 重叠扣除的不确定区间放宽为 ±$5-10B。 

- K = $1.3T 是中位估计。 hyperscaler/neocloud/其他实体的累积 AI capex stock 估计存在 ±20% 不确定性。 

- 正常行业 EPR 是聚合估计。行业内龙头可能 EPR 更低，长尾更高。 

- OpenAI commitments $1.4T 含部分重叠。 Oracle deal 和 Stargate 部分重叠；Anthropic 的 Amazon $100B 采购承诺是 10 年累计；时间窗口不一致。 

- Anthropic ARR $40B 是 TechCrunch 转引内部信息。公司官方最新公开数字是 $30B（April 2026）。"$40B" 应被理解为非审计的私募市场指标。 

- AI capex/GDP 数字不同来源差异较大。 Goldman 0.8%（窄口径）vs 本文 1.7-2.0%（宽 口径含全部 hyperscaler AI 相关 capex）。 

- AI capex 对 GDP 增长的贡献口径差异极大。从 Goldman 净 0.1-0.2 pp 到 Furman 92% （H1 2025 NIPA 子类别）。本文取 Goldman 的进口资本品调整版本。 

- 住房 EPR ~1x 不意味住房不危险。住房是价格泡沫，EPR 框架在这里不适用。 1873 美国铁路只用聚合 EPR ~1.2x。没有可靠的新建/老线分解数据。 "反身性"机制本身不可直接量化。 NVIDIA 投资 OpenAI、OpenAI 买 NVIDIA GPU 这种链 条规模估计为 $40B+ 名义是基于公开披露的合理估计，不是审计数字。 

- 本文提供研究框架与压力测试，不构成任何证券买卖建议。 

## **十三、可复现计算（v3.1 新增）**

全文所有核心数字（P、EPR、双口径 R_T 合计、敏感性、时间路径、历史案例的统一/校准双口径）可由仓库内 `epr.py` + `data/inputs.json` 一键复算：

```bash
python3 epr.py
```

脚本内置一致性断言：R_T 分项表合计必须等于头条口径、capex 逐公司表合计必须等于摘要区间——v3 初版的两处不一致正是靠机器检查出来的。改任何输入后重跑脚本即可得到全套数字。

## **十四、主要来源（全部更新至 2026-05-25）** 

## AI 公司财报和官方披露（高置信度）： 

   - NVIDIA Q1 FY27 8-K, CFO commentary, 10-Q (filed 2026-05-20) 

   - NVIDIA Q4 FY26 CFO commentary (supply commitments $95.2B 披露) 

   - Microsoft FY26 Q3 Earnings Call Transcript and 10-Q (2026-04-29，AI ARR $37B) 

   - Alphabet/Amazon/Meta Q1 2026 10-Q (filed 2026-04-30) 

   - CoreWeave Q1 2026 Earnings Call Transcript and 10-Q (2026-05-08，backlog $99.4B) 

- Anthropic 官方公告 (2026-04-06，"run-rate revenue has now surpassed $30 billion") 

   - Anthropic Series G $30B raised at $380B valuation (Feb 2026) 

   - Anthropic-Google-Broadcom 3.5 GW TPU deal (Apr 2026) 

   - OpenAI March 2026 $122B funding round at $852B valuation 

- AI 相关行业分析（中等置信度）： 

   - Goldman Sachs Research: AI capex baseline $765B for 2026 (2026-04) 

   - Goldman Sachs Research: AI capex GDP impact 0.1-0.2 pp net (Jan Hatzius, 2026-02) 

   - CreditSights: Hyperscaler Capex 2026 Estimates $750B (2026-02) 

   - St Louis Fed: AI investment contribution to Q3 2025 GDP growth 39% (Jan 2026) 

   - Jason Furman: H1 2025 GDP growth contribution analysis 

   - Bloomberg: AI Circular Deals visualization (2026-03) 

- 媒体报道（应降级为 reported）： 

- TechCrunch: Anthropic run rate "closer to $40 billion" per internal sources (2026-04-29) 

- Reuters: OpenAI/Oracle $300B deal report (2025-09 via WSJ) 

- Reuters: Anthropic Google $40B investment (2026-04-24) 

- Financial Times: Anthropic potential $40-50B raise at $850-900B valuation (2026-05-07) 

- CNBC: NVIDIA $40B+ equity bets in 2026 (2026-05-09) 

- VentureBeat: Anthropic $30B ARR with 80x growth (2026-04) 

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
