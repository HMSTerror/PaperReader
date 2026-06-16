# DiffMM: DiffMM: Multi-Modal Diffusion Model for Recommendation

- 论文 PDF: [DiffMM - Multi-Modal Diffusion Model for Recommendation.pdf](DiffMM - Multi-Modal Diffusion Model for Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2406.11781
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

多模态推荐有图像、文本、音频等 side information，但用户-物品图和模态特征都可能有噪声。

## 提出了什么方法

用 graph diffusion 生成模态感知的用户-物品图，再通过图神经网络融合协同信号和多模态特征，并配合跨模态对比学习。

## 实验效果如何

论文在多模态推荐数据集上报告优于现有多模态推荐方法，尤其强调扩散图增强提升了表示质量。

## 用最简单的话解释原理

先根据多模态内容把用户和物品之间的关系图补得更合理，再在这张更干净的图上做推荐。
