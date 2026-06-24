# A Comprehensive Survey on Multimodal Recommender Systems: Taxonomy, Evaluation, and Future Directions

- 论文 PDF: [A Comprehensive Survey on Multimodal Recommender Systems -  Taxonomy, Evaluation, and Future Directions.pdf](A Comprehensive Survey on Multimodal Recommender Systems -  Taxonomy, Evaluation, and Future Directions.pdf)
- 下载来源: https://arxiv.org/pdf/2302.04473
- 年份/会议: arXiv 2023
- 方向: 多模态推荐综述
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
这篇综述系统梳理**多模态推荐系统 (multimodal recommender systems)** 的分类、评价和未来方向。论文指出，推荐对象越来越多包含文本、图像、音频、视频、知识图谱等多种信息；多模态推荐的关键不只是“使用更多特征”，而是如何抽取、对齐、融合并评价不同模态。综述从任务、模态、融合策略、训练范式、评价指标和应用场景等维度建立 taxonomy，并讨论数据缺失、模态噪声、可解释性、公平性、效率和大模型等未来问题。

## 背景
传统推荐主要依赖用户-物品交互，面对冷启动、稀疏性和解释性不足。多模态信息可提供物品内容、用户语义和场景上下文，因此成为推荐系统的重要发展方向。然而，该领域文献分散：视觉推荐、文本推荐、视频推荐、多模态融合、跨模态预训练等工作使用不同术语和评价设置，缺少统一框架。

**Research Questions**：作为 survey，论文的问题是：如何系统分类多模态推荐？不同模态和融合方法各自解决什么问题？现有评价是否足以比较模型？未来哪些研究空白最关键？

**Hypotheses**：综述不提出实验假设，但基本判断是：多模态信息能缓解交互稀疏和冷启动；有效融合必须处理模态异质性 (modality heterogeneity) 与噪声；未来推荐将更依赖预训练与生成式模型。

## 文献综述
论文按主题分类而非单纯时间顺序。第一类是视觉推荐，以 VBPR 为代表，使用图像特征补充协同过滤。第二类是文本增强推荐，利用评论、标题、描述提升 item/user representation。第三类是多模态融合推荐，研究 early fusion、late fusion、attention fusion、graph-based fusion 等策略。第四类是多模态序列推荐和会话推荐，关注用户兴趣随时间变化。第五类是预训练和大模型方法，尝试从 CLIP、BERT、LLM/VLM 获得通用表示。

批判性地看，早期视觉/文本推荐往往只把模态当 side feature，缺少跨模态交互；图神经网络方法能传播多模态信息，但计算复杂且依赖图结构；预训练模型增强语义，但可能与推荐协同信号不一致。这些不足共同引出后续多模态序列推荐、cross-attention 和 MLLM 推荐的研究空间。

## 方法
**Participants**：综述不包含受试者。

**Materials**：材料是多模态推荐领域已发表论文、公开数据集和评价协议。论文关注图像、文本、音频、视频、知识图谱等多种模态。

**Procedure**：作者采用文献调研方式，对已有工作进行 taxonomy 构建。分类依据包括：推荐任务类型、使用模态、特征提取方式、融合层级、学习目标、评价指标与应用场景。论文还总结常用数据集和 metric，以便比较不同研究。

## 实验和结果
作为 survey，本文没有提出新的模型实验。其“结果”主要是结构化综述结论：多模态推荐普遍用于缓解冷启动和稀疏性；attention、graph learning 和 self-supervised learning 是常见融合机制；现有评价高度依赖离线 accuracy，较少评估鲁棒性、效率、可解释性和用户体验。

论文还指出，不同工作使用的数据集和划分方式不统一，使得 reported improvements 难以直接比较。这一评价问题对新模型尤其重要：仅报告某个数据集上的 HR/NDCG 不足以证明方法普适。

## 讨论
综述的学术意义是提供“地图”。对初学者而言，它帮助理解多模态推荐不是单一路线，而是从特征、融合、任务、训练、评价多层展开。对你的工作而言，若你要提出 SASRec cross-attention 多模态模型，可以用该综述作为 related work 总体分类依据。

论文也提醒，多模态融合的核心挑战是异质性和缺失：图像、文本、ID 的噪声结构不同，简单拼接可能放大冲突。cross-attention 的潜在价值正在于显式建模模态间关系，但也需要证明其优于更简单的 late/early fusion。

## 结论
作者认为未来方向包括统一评价基准、处理缺失模态、提升可解释性与公平性、增强效率，以及探索大规模预训练/生成式模型在推荐中的作用。该综述本身的局限是时间截面性：2023 年之后 LVLM/MLLM 推荐快速发展，需要结合后续 MLLM-MSR、MSRBench、MLLM-SRec 等工作更新。
