# MDiffFR: MDiffFR: Modality-Guided Diffusion Generation for Cold-start Items in Federated Recommendation

- 论文 PDF: [MDiffFR - Modality-Guided Diffusion Generation for Cold-start Items in Federated Recommendation.pdf](MDiffFR - Modality-Guided Diffusion Generation for Cold-start Items in Federated Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2512.24715
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

联邦推荐中，冷启动 item 缺少交互，同时数据分散在各客户端，不能随便集中训练。

## 提出了什么方法

提出 modality-guided diffusion，在保护联邦设置的同时利用文本/图像等模态信息生成冷启动 item embedding，并引入模态指导和隐私约束。

## 实验效果如何

论文报告在冷启动和联邦推荐设置下提升了新 item 推荐效果，并保持隐私友好的训练流程。

## 用最简单的话解释原理

新商品没人点过时，就先看它的图文内容，用扩散模型生成一个可用的初始向量。
