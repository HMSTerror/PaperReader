# PaDiRec: Parameter Diffusion for Controllable Multi-Task Recommendation

- 简称：`PaDiRec`
- 位置：`相关工作，但不放入严格主表`
- 原网址：[OpenReview](https://openreview.net/forum?id=9Zq8fRF4am)

## 为什么相关

PaDiRec 确实属于扩散推荐，但它扩散的对象不是用户行为序列、交互边或推荐 latent，而是**推荐模型参数本身**。这让它和常见的交互建模型扩散推荐工作形成了很不一样的路线。

## 为什么没放进主表

主表聚焦的是“扩散过程直接参与推荐交互建模，且 Diffusion Transformer 是核心主干”的论文。PaDiRec 更偏向参数空间扩散和可控多任务建模，因此放在相关工作里更准确。

## 阅读时重点看

1. 参数扩散如何实现多任务可控性。
2. 参数级扩散和数据级、序列级扩散在优缺点上有什么差别。
3. 这条路线是否有可能与交互建模型 Diffusion Transformer 合流。
