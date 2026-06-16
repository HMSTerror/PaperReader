# iDreamRec: Generate and Instantiate What You Prefer: Text-Guided Diffusion for Sequential Recommendation

- 论文 PDF: [Generate and Instantiate What You Prefer - Text-Guided Diffusion for Sequential Recommendation.pdf](Generate and Instantiate What You Prefer - Text-Guided Diffusion for Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2410.13428
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

DreamRec 使用随机初始化的 item embedding，语义不稳定、解释性弱，也不利于冷启动或跨数据迁移。

## 提出了什么方法

用 LLM 生成 item 文本描述，再用文本嵌入模型得到语义向量，并通过固定 whitening 把目标空间对齐到适合扩散的分布。扩散模型在这个语义空间中生成目标 item embedding。

## 实验效果如何

论文报告在序列推荐数据集上优于 DreamRec 等 baseline，并展示文本语义空间能改善可解释性和 item 表示稳定性。

## 用最简单的话解释原理

先给每个 item 一张“语义身份证”，再让扩散模型生成下一张最合适的身份证，而不是在随机坐标里猜。
