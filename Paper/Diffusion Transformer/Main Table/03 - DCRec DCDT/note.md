# Dual Conditional Diffusion Models for Sequential Recommendation

- 简称：`DCRec` / `DCDT`
- 时间：`2024 / 2025`
- 任务：`序列推荐`
- 原网址：[arXiv](https://arxiv.org/abs/2410.21967)
- 会议版本：[ACM DOI](https://dl.acm.org/doi/10.1145/3773966.3777926)

## 这篇在做什么

这篇论文认为，仅靠隐式行为序列来做序列推荐往往不够，因为用户行为里混有很多无关噪声。因此它提出在扩散的**前向过程和反向过程同时加入条件信息**，让整个生成和去噪链路都更贴近真实用户意图。

## 核心方法

论文里的 `Dual Conditional Diffusion Transformer` 使用 cross-attention 融合显式信号与隐式序列表示。这样一来，模型不只是“事后参考”额外条件，而是在扩散全过程中都让条件参与信息流动。

## 为什么重要

很多早期扩散推荐方法只是把 Transformer 当编码器或指导器，这篇论文则更明确地把条件感知的 Diffusion Transformer 放在主干位置，因此非常适合作为“更严格意义上的 DiT 推荐模型”代表。

## 阅读时重点看

1. 显式条件具体包含哪些信息。
2. 条件进入前向扩散和反向去噪的位置是否相同。
3. 性能提升究竟来自 dual conditional 设计，还是来自更强的 Transformer 表达能力。
