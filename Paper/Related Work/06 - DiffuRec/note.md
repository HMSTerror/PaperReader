# DiffuRec: DiffuRec: A Diffusion Model for Sequential Recommendation

- 论文 PDF: [DiffuRec - A Diffusion Model for Sequential Recommendation.pdf](DiffuRec - A Diffusion Model for Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2304.00686
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

序列推荐中，用户下一个兴趣往往不确定，一个 item 可能对应多个潜在兴趣面向。把 item 当成固定点向量会压扁这种不确定性。

## 提出了什么方法

把 item 表示成分布，对目标 item embedding 加噪声，再用 Transformer 条件于历史序列做去噪，最后把生成的连续表示映射回 item。

## 实验效果如何

论文在多个序列推荐数据集上报告优于常见序列推荐模型，并展示分布式 item 表示有助于建模多兴趣和不确定性。

## 用最简单的话解释原理

不要只猜一个固定答案，而是在历史行为条件下生成一个“可能的下一个兴趣位置”，再找最接近这个位置的 item。
