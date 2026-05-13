# EDGE-Rec: Efficient and Data-Guided Edge Diffusion For Recommender Systems Graphs

- 时间：`2024`
- 任务：`边预测 / 评分或交互预测`
- 原网址：[arXiv](https://arxiv.org/abs/2409.14689)
- 代码：[GitHub](https://github.com/upriyam-cmu/EDGE-Rec)

## 这篇在做什么

EDGE-Rec 直接从**用户-物品边**的角度建模推荐图，而不是只围绕节点表示做文章。论文提出的 `GDiT` 会对交互矩阵或边权进行扩散和去噪，再结合用户、物品特征恢复更合理的交互结构。

## 核心方法

模型在去噪时加入用户与物品特征作为条件信号，因此不是无条件地“补边”，而是根据实体属性去恢复更可信的边。为了让大规模交互矩阵可训练，论文还设计了 `Row-Column Separable Attention` 来降低标准全注意力的开销。

## 为什么重要

这篇论文很适合放在 Diffusion Transformer 主表里，因为它把扩散对象放到了推荐系统最核心的交互边或边权上，同时又给出了一套矩阵级别可扩展的 Transformer 去噪方案。

## 阅读时重点看

1. 扩散对象到底是二值边、边权，还是两者都支持。
2. 行列分离注意力把复杂度降到了什么量级。
3. 实验中收益更主要来自条件信息还是来自 GDiT 架构本身。
