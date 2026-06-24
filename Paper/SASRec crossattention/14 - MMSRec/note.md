# Self-Supervised Multi-Modal Sequential Recommendation

- 论文 PDF: [Self-Supervised Multi-Modal Sequential Recommendation.pdf](Self-Supervised Multi-Modal Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2304.13277
- 年份/会议: arXiv 2023
- 方向: 多模态序列推荐
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
MMSRec 研究如何在序列推荐中利用多模态信息，并提出**自监督多模态序列推荐 (Self-Supervised Multi-Modal Sequential Recommendation)**。论文指出，许多序列推荐模型依赖 item ID，难以处理冷启动和跨域迁移；已有模态替代方法又常直接比较序列编码输出和低层 item embedding，存在高层用户表示与低层物品特征不一致的问题。作者提出双塔检索架构：一塔编码用户行为序列，另一塔编码物品多模态信息；再通过自监督多模态预训练对齐不同模态组合。五个公开数据集实验显示，该方法显著提升推荐性能。

## 背景
序列推荐需要同时解决动态兴趣建模和物品表示问题。ID embedding 在同域内强，但对新物品无能为力；图像和文本能描述物品内容，却存在模态异质性和表示层级不一致。MMSRec 的研究空白是：如何让序列侧用户表示与物品侧多模态表示在同一检索空间中对齐。

**Research Questions**：1. 双塔 retrieval architecture 是否比直接点积高层序列输出与低层 item embedding 更合理？2. 多模态自监督预训练能否提升 item encoder 的泛化能力？3. 不同模态组合之间的 contrastive learning 是否有助于跨数据集迁移？

**Hypotheses**：作者假设用户序列表示和物品表示应在同一语义层级比较；多模态特征组合的一致性可作为自监督信号；对齐图像、文本和融合表示能提升冷启动与泛化。

## 文献综述
论文回顾 GRU4Rec、SASRec、BERT4Rec 等 ID-based 序列模型，指出其跨域受限。随后讨论 UniSRec 等使用 item text 替代 ID 的方法，以及 CLIP 等多模态预训练思想。作者批判已有方法常把预训练特征当静态输入，没有专门优化推荐检索空间。

文献过渡逻辑是：若推荐最终要从候选物品库检索 next item，那么用户塔输出和物品塔输出应被联合训练；自监督多模态对齐可以让物品塔在不同模态缺失或变化时仍稳定。

## 方法
**Participants**：无受试者；实验使用用户点击/购买序列与物品图像、文本特征。

**Materials**：论文使用五个公开数据集，并报告自监督预训练在视频检索等设置中的表现。基线包括 ID-based 序列模型和多模态推荐模型。

**Procedure**：MMSRec 构建 sequence encoder 与 item encoder。sequence encoder 负责把用户历史编码为高层兴趣向量；item encoder 把图像、文本或多模态组合编码为候选物品向量。训练时采用 retrieval objective，使真实 next item 与用户序列表示接近。自监督预训练阶段构造不同模态组合之间的 contrastive tasks，让模型学习跨模态一致性和细粒度 item discrimination。

## 实验和结果
实验显示，MMSRec 在五个公开数据集上相对基线有显著提升。其优势来自两方面：双塔结构解决了表示层级不一致；自监督预训练提升了多模态 item encoder 的检索能力。

论文还显示，多模态组合对齐有助于模型适应不同数据集可用特征差异。这对真实系统很重要，因为并非所有物品都有完整图片、标题或描述。

## 讨论
MMSRec 的学术意义在于把多模态序列推荐转为统一检索问题。与只在 SASRec 输入端拼接图像/文本不同，MMSRec 让用户塔和物品塔都学习到面向 retrieval 的高层表示。

对 cross-attention 工作而言，MMSRec 是强相关 baseline：它不强调显式 cross-attention，但通过 contrastive alignment 实现模态互补。你的方法若主打 cross-attention，需要说明显式交互相对双塔对齐的优势，例如更细粒度地建模历史物品模态与候选物品模态之间的关系。

## 结论
作者总结，双塔检索架构和自监督多模态预训练能缓解 ID-based 序列推荐的冷启动与迁移问题。论文的局限在于主要依赖表示对齐，并未深入解释模态冲突何时发生；这为后续自适应融合和 cross-attention 方法留下空间。
