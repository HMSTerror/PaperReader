# Diffusion Generative Recommendation with Continuous Tokens

- 简称：`ContRec`
- 位置：`相关工作，但不放入严格主表`
- 原网址：[arXiv](https://arxiv.org/abs/2504.12007)

## 为什么相关

ContRec 明显属于扩散推荐与 Transformer 相关生成建模这一脉络。它强调的是通过**continuous tokens**来做生成式推荐，这与一些连续 latent 扩散方法在思想上非常接近。

## 为什么没放进主表

这篇工作的中心更偏向 continuous token / generative recommendation 这个表征路线，而不是明确把 Diffusion Transformer 作为论文的核心模型主张。因此它与主表论文高度相关，但放在相关工作区域更合适。

## 阅读时重点看

1. continuous token 的定义和解码方式。
2. 它与 CATDiT 这类连续空间方法在目标和建模对象上有何异同。
3. 论文真正的重点是 token 化方案，还是去噪 Transformer 架构本身。
