# Adaptive Multi-Modalities Fusion in Sequential Recommendation Systems

- 论文 PDF: [Adaptive Multi-Modalities Fusion in Sequential Recommendation Systems.pdf](Adaptive Multi-Modalities Fusion in Sequential Recommendation Systems.pdf)
- 下载来源: https://arxiv.org/pdf/2308.15980
- 年份/会议: CIKM 2023
- 方向: 多模态序列推荐
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
MMSR 研究多模态序列推荐中的**自适应融合 (adaptive fusion)**。论文指出，early fusion 和 late fusion 各有缺陷：early fusion 较难保留单模态内部顺序结构，late fusion 又可能忽视不同模态之间的细粒度关系。作者通过 case study 发现，当打乱 item 顺序或错配模态时，两类融合策略敏感性不同。为此，论文提出 MMSR，使用异构自适应网络与图聚合机制，在 item-level 与 sequence-level 上灵活整合模态信息。实验显示 MMSR 在多数据集和缺失模态场景下优于 state-of-the-art baselines。

## 背景
多模态序列推荐不是简单“图像+文本+ID”。用户行为具有顺序性，各模态又具有异质性：文本可能描述类别和功能，图像反映外观，ID 表示协同模式。不同融合顺序会改变模型看到的信息结构。MMSR 的目标就是处理“先融合再建序列”与“先建序列再融合”的矛盾。

**Research Questions**：1. early fusion 与 late fusion 在序列推荐中各自何时失效？2. 模态间关系和序列内关系能否用统一自适应机制同时建模？3. 当部分模态缺失或错配时，模型是否仍鲁棒？

**Hypotheses**：作者假设融合顺序显著影响推荐性能；不同模态之间存在可学习的层次关系；自适应图聚合比固定 early/late fusion 更能处理模态异质性。

## 文献综述
论文回顾 GRU4Rec、SASRec 等序列模型，也讨论多模态推荐中的 early fusion、late fusion、attention fusion。作者批判已有多模态 SR 往往选择固定融合方式，缺少对融合顺序影响的分析。

论文还借鉴图神经网络和注意力机制，用于建模模态之间的异构关系。逻辑演进是：由于模态和顺序同时存在，模型需要一种能在图结构中动态传播信息的方法，而不是固定拼接。

## 方法
**Participants**：无受试者；实验使用多模态用户行为序列。

**Materials**：论文使用 Amazon 等多模态推荐数据，并设置正常、打乱顺序、模态错配和缺失模态等实验条件。基线包括 GRU4Rec/SASRec 的多模态变体与现有多模态推荐方法。

**Procedure**：MMSR 构造包含不同模态节点和序列关系的异构图，使用 HAN-GNN 类机制进行图注意力聚合。其双图注意力与异步更新策略使模型可以同时保留每个模态内部信息、模态间交互和序列关系。模型根据数据自动学习模态融合权重，而不是预先固定 early 或 late fusion。

## 实验和结果
实验显示，MMSR 在标准推荐指标上优于基线，并在缺失模态场景下保持较好表现。case study 支持作者观察：late fusion 对顺序打乱更敏感，early fusion 对模态错配更敏感；MMSR 通过自适应机制缓解两类问题。

消融结果说明图聚合和自适应融合都是性能来源。若只使用固定融合或去掉模态关系建模，效果会下降。

## 讨论
MMSR 对 cross-attention 研究构成直接挑战：它已经系统讨论 early/late fusion 的不足，并提出自适应融合。你的方法若主张 novelty，需要说明 cross-attention 是解决哪一类 MMSR 尚未充分解决的问题，例如候选物品级交互、历史行为级细粒度对齐，或 ID/语义互补。

论文还强调可解释性未来空间：理解何时 sequentiality 更重要，何时模态互依赖更重要，是多模态推荐走向可靠应用的关键。

## 结论
作者总结 MMSR 能灵活融合多模态并保持序列关系，在缺失模态下也鲁棒。论文结论明确提出未来方向：探索复杂模态关系的可解释性，理解顺序性和模态依赖何时起关键作用。
