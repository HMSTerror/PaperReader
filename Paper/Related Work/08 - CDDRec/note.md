# CDDRec: Conditional Denoising Diffusion for Sequential Recommendation

- 论文 PDF: [Conditional Denoising Diffusion for Sequential Recommendation.pdf](Conditional Denoising Diffusion for Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2304.11433
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

扩散式序列推荐容易出现生成坍缩、过平滑，对短序列、冷 item 和噪声点击尤其困难。

## 提出了什么方法

提出 conditional denoising diffusion，用 sequence encoder 表示历史，再用 cross-attentive denoising decoder 在不同扩散步恢复目标 item，并加入 cross-divergence 和 contrastive loss 稳定训练。

## 实验效果如何

论文报告在多个序列推荐数据集上提升了整体性能，并缓解了稀疏、短历史场景下的效果下降。

## 用最简单的话解释原理

每一步去噪都回头看历史行为，让生成结果不要飘走；再用对比和分歧约束让模型不要只生成平均答案。
