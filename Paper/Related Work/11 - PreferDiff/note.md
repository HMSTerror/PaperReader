# PreferDiff: Preference Diffusion for Recommendation

- 论文 PDF: [Preference Diffusion for Recommendation.pdf](Preference Diffusion for Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2410.13117
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

PreferDiff 关注扩散推荐的训练目标不匹配问题。很多 DM-based recommender 仍用 MSE 这类重构损失，或者直接套用传统推荐目标。前者适合像素/向量还原，但不一定适合 personalized ranking；后者又没有充分利用扩散模型作为生成模型的 log-likelihood 结构。

推荐系统最终要优化的是排序：正样本应该排在负样本前面，尤其要处理 hard negatives。仅仅让生成向量接近目标 item，可能无法把用户偏好分布和排序目标结合起来。因此论文要为扩散推荐设计一个真正面向 personalized ranking 的优化目标。

## 提出了什么方法

PreferDiff 把传统 BPR 目标改写进 log-likelihood generative framework，使扩散模型能在生成过程中显式学习“正样本比多个负样本更符合用户偏好”。由于直接优化不可处理，作者用 variational inference 最小化 variational upper bound。

论文还用 cosine error 替代 MSE，使优化更贴合推荐中的相似度排序；同时平衡 generative learning 和 preference modeling，提高训练稳定性。作者进一步指出 PreferDiff 与 Direct Preference Optimization 有理论联系，说明它可以被看作在生成框架中进行用户偏好对齐。

## 实验效果如何

主实验在 Sports and Outdoors、Beauty、Toys and Games 三个 benchmark 上进行。PreferDiff 显著超过其他 DM-based recommenders 和传统序列推荐器，相对第二强基线提升范围为 6.41% 到 19.35%。Table 2 的消融显示，去掉多负样本建模或 cosine error 都会下降，说明 hard negative 信息和推荐友好的误差形式都很重要。

附加实验还在 Yahoo Music、Steam、ML-1M 等不同背景数据集上验证泛化性。比如 Yahoo 子集上 Recall@5/NDCG@5 为 0.1408/0.1106，高于 DreamRec 的 0.1302/0.1025；ML-1M 上为 0.0629/0.0439，高于 DreamRec 的 0.0464/0.0314。整体结论是：扩散推荐不仅要会生成，还要用排序目标来约束生成。

## 用最简单的话解释原理

PreferDiff 可以理解为给扩散推荐换了一个“考试题”。以前的考试是“你还原得像不像目标向量”，但推荐真正关心的是“你能不能把用户喜欢的东西排到不喜欢的东西前面”。

它把 BPR 这种排序思想放进扩散生成的概率框架里，让模型在去噪时不仅恢复目标，还学会避开 hard negatives。这样生成出来的偏好向量更适合做 Top-K 排序。
