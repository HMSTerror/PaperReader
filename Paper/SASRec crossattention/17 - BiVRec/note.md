# BiVRec: Bidirectional View-based Multimodal Sequential Recommendation

- 论文 PDF: [BiVRec -  Bidirectional View-based Multimodal Sequential Recommendation.pdf](BiVRec -  Bidirectional View-based Multimodal Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2402.17334
- 年份/会议: arXiv 2024
- 方向: 多模态序列推荐
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
BiVRec 提出**双向视图多模态序列推荐 (Bidirectional View-based Multimodal Sequential Recommendation)**。论文认为，ID view 和 multimodal view 各有优势：ID view 包含强协同信号，multimodal view 具备语义泛化能力。已有方法要么过度依赖 ID，迁移性弱；要么只用模态，忽略 ID 协同信息。BiVRec 同时训练两个视图，并通过 multi-scale interest embedding、intra-view interest decomposition 和 cross-view interest learning 学习二者协同关系。实验在 ML-25M、ML-1M、Electronics、Clothing、Baby 五个数据集上达到 state-of-the-art。

## 背景
MoRec 类研究表明 ID 与模态不是简单替代。问题在于：ID 表示和多模态表示高度异质，无法轻易一一对齐。用户可能同时有多个兴趣簇，例如电影中的导演偏好和类型偏好，电商中的品牌偏好和外观偏好。BiVRec 的目标是先结构化表达每个视图内部兴趣，再学习视图间对应关系。

**Research Questions**：1. ID view 与 multimodal view 能否通过联合训练双向增强？2. 多兴趣结构化表示是否比单一用户向量更适合视图对齐？3. 粗粒度与细粒度 cross-view learning 是否都必要？

**Hypotheses**：作者假设用户兴趣是多粒度、多簇的；ID 与模态 view 之间存在协同但非一一对应关系；通过粗粒度整体语义相似和细粒度兴趣分配相似可提升两个视图。

## 文献综述
论文回顾 ID-based sequential recommendation、多模态推荐和多兴趣推荐。ComiRec 等多兴趣模型说明用户不应被压缩成单向量；MoRec 等工作说明 modality-based 方法有迁移优势但信息利用不足。作者把这些线索结合起来，提出 view-based collaboration。

文献过渡很清晰：如果只融合原始特征，会被异质性困扰；如果先把每个 view 分解为结构化兴趣，再学习 view-level relation，就能更合理地对齐 ID 与模态。

## 方法
**Participants**：无受试者；实验使用用户行为序列与多模态物品特征。

**Materials**：五个数据集包括 ML-25M、ML-1M、Electronics、Clothing、Baby。论文比较 ComiRec-SA、SASRec、FDSA、MMSRec、MMMLP、NOVA、DIF-SR 等基线。

**Procedure**：BiVRec 先用 multi-scale patching 扩展用户交互序列，获得不同尺度的兴趣片段。然后在每个 view 内进行 interest decomposition：Gaussian attention 和 cluster attention 构造多个结构化兴趣向量。最后 cross-view interest learning 同时使用 coarse-grained overall semantic similarity 和 fine-grained interest allocation similarity，让 ID view 与 multimodal view 互相约束和增强。

## 实验和结果
表 1 显示 BiVRec 在五个数据集上整体领先。对比结果说明，仅在 SASRec 等模型上加入模态特征不够；显式建模 ID view 与 multimodal view 的协同关系可以获得更稳定收益。

消融实验表明，多尺度兴趣、视图内分解和跨视图学习都是必要组件。若缺少 cross-view learning，两个视图的信息不能充分互补；若缺少兴趣分解，视图对齐会过于粗糙。

## 讨论
BiVRec 的贡献在于把“融合”提升为“视图协同学习”。它不是简单让模态补充 ID，而是让 ID 和模态各自形成推荐任务，再通过结构化兴趣对齐互相改进。这与 cross-attention 的思想相近，但更强调 view-level bidirectional learning。

对你的工作而言，BiVRec 是强相关 baseline。若你的 cross-attention 设计只在特征级做交互，可能不如 BiVRec 的结构化多兴趣对齐；如果能在候选物品、历史兴趣和模态 view 间做更细粒度交互，则可以形成差异点。

## 结论
作者认为 BiVRec 通过双视图联合训练和兴趣结构化分解提升了多模态序列推荐。论文未单列 limitation；从动机可见，其主要边界是模型结构复杂、依赖多模态特征质量，未来可继续探索更高效的 view alignment 和更强解释性。
