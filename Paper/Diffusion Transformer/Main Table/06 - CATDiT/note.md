# Continuous Data Augmentation via Condition-Tokenized Diffusion Transformer for Sequential Recommendation

- 简称：`CATDiT`
- 时间：`2025`
- 任务：`序列推荐的数据增强`
- 原网址：[ACM DOI](https://dl.acm.org/doi/10.1145/3746252.3761396)
- 补充索引：[DBLP](https://dblp.org/rec/conf/cikm/ShiWT25)

## 这篇在做什么

CATDiT 关注的是序列推荐里的数据增强。传统扩散方法如果直接生成离散 item 序列，通常需要把连续 embedding 再 round 回离散物品，这一步容易造成语义漂移。CATDiT 的思路是：**直接生成连续 embedding 作为增强样本**，避免中间的离散化误差。

## 核心方法

论文提出 `Condition-Tokenized Diffusion Transformer`，在去噪过程中加入与用户意图相关的条件 token，使生成的增强样本不仅“像一个合理物品”，还要“更符合当前用户偏好”。

## 为什么重要

它不是把 Diffusion Transformer 直接当最终推荐器，而是把它当成推荐系统训练前的数据增强器。这说明扩散推荐的价值不一定只体现在预测头本身，也可以体现在上游样本构造环节。

## 当前 PDF 情况

这篇论文的 DOI 来源当前返回访问受限，仓库里暂时还没有成功落下 PDF 文件。我已经保留了题名、中文笔记和原始链接，后续如果你提供开放版本地址，我可以再补下载。

## 阅读时重点看

1. condition token 的构造方式是什么。
2. 连续增强样本最终如何被下游序列推荐器消费。
3. 它在稀疏场景、长尾场景下是否更有效。
