# Generate and Instantiate What You Prefer: Text-Guided Diffusion for Sequential Recommendation

- 简称：`iDreamRec`
- 时间：`2024 / 2025`
- 任务：`文本引导的序列推荐`
- 原网址：[arXiv](https://arxiv.org/abs/2410.13428)

## 这篇在做什么

iDreamRec 把文本语义引入序列推荐。它先利用文本描述和与大语言模型相关的 embedding 改善物品表示，然后用扩散模型生成用户下一步可能喜欢的“理想物品 embedding”。

## 核心方法

论文方法部分明确使用了 **Diffusion Transformer Block with in-context conditioning**。也就是说，文本意图不是附加说明，而是真正参与到 noisy latent 的去噪过程里，让生成出来的目标表示更符合用户语义偏好。

## 为什么重要

这篇论文把“协同行为信号”和“文本语义信号”接到了同一条扩散生成链路中，是扩散推荐与文本条件生成结合得比较自然的一篇代表作。

## 阅读时重点看

1. 文本描述和 LLM embedding 是如何构造成条件输入的。
2. 生成出的理想物品 embedding 最终如何映射回真实物品集合。
3. 性能提升更偏向语义增强，还是来自 Diffusion Transformer 生成过程本身。
