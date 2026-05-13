# Listwise Preference Diffusion Optimization for User Behavior Trajectories Prediction

- 简称：`LPDO`
- 时间：`2025 / 2026`
- 任务：`用户行为轨迹预测`
- 原网址：[OpenReview](https://openreview.net/forum?id=x5KUOlYKQr)

## 这篇在做什么

LPDO 把推荐目标从“预测下一个 item”扩展为“预测未来一段用户行为轨迹”。它希望模型不仅判断下一步会点什么，还能生成未来若干步的整体行为序列。

## 核心方法

论文使用扩散模型生成未来行为段，并结合 listwise preference / Plackett-Luce 风格的目标来优化整段序列。补充材料里提到 `Cross-Conditional Diffusion Transformer` 和 cross-step attention，用来建模未来多个动作之间的依赖关系。

## 为什么重要

这篇论文展示了扩散推荐如何从 next-item 走向**多步轨迹建模**。如果把推荐看作更长时程的行为规划问题，这类工作会非常关键。

## 阅读时重点看

1. listwise preference 目标是如何和扩散训练耦合的。
2. cross-step attention 如何刻画未来多个行为之间的相互依赖。
3. 轨迹预测指标和常规序列推荐指标有哪些差异。
