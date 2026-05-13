# Prompt-to-Slate: Diffusion Models for Prompt-Conditioned Slate Generation

- 简称：`DMSG`
- 时间：`2024 / 2025`
- 任务：`slate recommendation / playlist 或 bundle 生成`
- 原网址：[arXiv](https://arxiv.org/abs/2408.06883)
- 会议版本：[ACM DOI](https://dl.acm.org/doi/10.1145/3705328.3748072)

## 这篇在做什么

Prompt-to-Slate 不再只做“逐个 item 排序”，而是根据 prompt 或上下文一次性生成一整组推荐结果，例如播放列表、商品 bundle 或一个推荐 slate。

## 核心方法

它的核心模块是 Diffusion Transformer，通过 cross-attention 把 prompt/context 与 noisy slate latent 结合起来做去噪。这样模型在生成时可以显式考虑整组 item 之间的协调性、互补性与多样性，而不只是单个 item 的相关性。

## 为什么重要

这篇论文很好地扩展了扩散推荐的视角：扩散模型不只能做 next-item 推荐，也能做**结构化集合生成**，这对实际推荐系统中的列表生成任务很有价值。

## 阅读时重点看

1. slate latent 的表示形式是什么。
2. prompt 能否表达用户偏好、任务目标和约束条件。
3. 论文是否显式优化了多样性、一致性或覆盖性等列表级指标。
