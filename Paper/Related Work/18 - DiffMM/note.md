# DiffMM: DiffMM: Multi-Modal Diffusion Model for Recommendation

- 论文 PDF: [DiffMM - Multi-Modal Diffusion Model for Recommendation.pdf](DiffMM - Multi-Modal Diffusion Model for Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2406.11781
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

DiffMM 面向多模态推荐中的稀疏和错误增强问题。短视频、商品、新闻等 item 通常有文本、图像、音频等多模态信息，但用户-item 交互仍然稀疏。已有 self-supervised 方法会做随机增强或跨视图对比，但这些增强可能引入无关噪声，不能准确对齐多模态上下文与用户交互。

论文认为，多模态推荐不应只把视觉/文本特征拼接进 embedding，而应自动生成 modality-aware 的用户-item 图，让多模态信息以更符合协同关系的方式参与推荐。

## 提出了什么方法

DiffMM 提出 multi-modal graph diffusion model。它利用扩散模型的生成能力，自动生成带有模态感知信息的 user-item graph，使模型能把有用多模态知识注入用户偏好建模。该过程通过 modality-aware signal injection 引导扩散模块，让生成图更贴合不同模态下的用户-item 关系。

在表示学习上，DiffMM 还加入 cross-modal contrastive learning，利用不同模态中交互模式的一致性增强用户和 item 表示。整体框架把扩散生成图、多模态图聚合和跨模态对比学习结合起来。

## 实验效果如何

实验在 TikTok、Amazon-Baby、Amazon-Sports 三个多模态推荐数据集上进行，采用 Recall、Precision、NDCG 和 all-rank item evaluation，并与 MF-BPR、NGCF、LightGCN、DiffRec、SGL、NCL、HCCF、VBPR、MMGCN、GRCN、LATTICE、MMGCL、BM3 等比较。论文报告 DiffMM 在三个数据集上整体领先。

消融 Table 2 显示完整 DiffMM 最好：TikTok Recall/NDCG 为 0.1129/0.0456，Amazon-Baby 为 0.0975/0.0411，Amazon-Sports 为 0.1017/0.0458。去掉 cross-modal contrastive learning、用 VGAE 替代 diffusion model、去掉 modality-aware signal injection 都会下降，证明三部分都有效。稀疏用户分组实验也显示 DiffMM 对交互少的用户更有帮助。

## 用最简单的话解释原理

DiffMM 的想法是：多模态信息不能只是贴在 item 向量上的标签，而应该参与构造“谁和谁更相关”的图。扩散模型负责生成一张更懂多模态的用户-item 图，对比学习负责让不同模态下的偏好保持一致。

例如一个短视频既有画面又有文字，用户可能因为视觉风格喜欢它，也可能因为主题喜欢它。DiffMM 尝试把这些模态线索转化成更准确的交互结构。
