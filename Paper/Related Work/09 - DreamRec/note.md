# DreamRec: Generate What You Prefer: Reshaping Sequential Recommendation via Guided Diffusion

- 论文 PDF: [Generate What You Prefer - Reshaping Sequential Recommendation via Guided Diffusion.pdf](Generate What You Prefer - Reshaping Sequential Recommendation via Guided Diffusion.pdf)
- 下载来源: https://arxiv.org/pdf/2310.20453
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

传统 learning-to-classify 依赖负采样，但未交互 item 不一定是负样本，假负样本会误导推荐。

## 提出了什么方法

提出 learning-to-generate：用 Transformer 编码历史作为 guidance，再用 classifier-free guidance 的扩散模型从噪声生成 oracle item embedding，最后在 item 库中检索最近邻。

## 实验效果如何

论文报告在多个序列推荐数据集上优于分类式和部分生成式 baseline，核心收益来自减少负采样依赖。

## 用最简单的话解释原理

不要先拿一堆可能错误的负样本训练分类器，而是直接生成“用户心里最想要的下一个物品”的向量。
