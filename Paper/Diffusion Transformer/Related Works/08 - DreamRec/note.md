# Generate What You Prefer: Reshaping Sequential Recommendation via Guided Diffusion

- 简称：`DreamRec`
- 位置：`相关工作，但不放入严格主表`
- 原网址：[arXiv](https://arxiv.org/abs/2310.20453)

## 为什么相关

DreamRec 是扩散序列推荐里非常重要的前作。它把推荐视为 guided diffusion 生成过程，对后续很多工作都有明显启发。

## 为什么没放进主表

虽然它和 Transformer 有关系，但更准确地说，它是**guided diffusion + Transformer encoder guidance**，而不是明确把 DiT 或 Diffusion Transformer 当作命名主干架构的工作。所以它更适合作为“前驱与近邻工作”来放，而不是严格意义上的主表代表。

## 阅读时重点看

1. Transformer encoder 在这里扮演的是指导器还是去噪主干。
2. 后续像 DCRec、iDreamRec 相比它到底“更 DiT”在哪里。
3. DreamRec 奠定了哪些后来扩散序列推荐的通用设计模式。
