# DiffuASR: Diffusion Augmentation for Sequential Recommendation

- 论文 PDF: [Diffusion Augmentation for Sequential Recommendation.pdf](Diffusion Augmentation for Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2309.12858
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

序列推荐常遇到历史短、行为稀疏、长尾 item 难学的问题，手工增强如裁剪、mask、重排表达能力有限。

## 提出了什么方法

用扩散模型生成伪历史序列来增强训练数据。item ID 先转连续表示，扩散模型生成增强序列，再映射回 item，并可用 guidance 贴近用户偏好。

## 实验效果如何

论文报告把该增强方法接到不同序列推荐 backbone 后，能在多个数据集上提升推荐指标。

## 用最简单的话解释原理

给训练集补一些合理的“模拟历史”，让推荐模型见过更多可能的用户行为路径。
