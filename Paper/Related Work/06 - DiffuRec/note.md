# DiffuRec: DiffuRec: A Diffusion Model for Sequential Recommendation

- 论文 PDF: [DiffuRec - A Diffusion Model for Sequential Recommendation.pdf](DiffuRec - A Diffusion Model for Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2304.00686
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

DiffuRec 研究的是 sequential recommendation 中 item 表示过于确定的问题。主流序列推荐会把每个 item 表示成固定向量，再根据历史序列预测下一个 item。但一个 item 可能有多个潜在方面，一个用户也可能同时有多种兴趣；固定点向量很难表达这种不确定性和多意图。

论文还指出，序列推荐的训练数据稀疏且行为多样。若模型只学习确定性的 next-item 分类，很容易把用户兴趣压成单一方向，不能充分建模“用户下一步可能喜欢一类 item”的分布。因此作者尝试把扩散模型用于 item representation generation 和 uncertainty injection。

## 提出了什么方法

DiffuRec 把目标 item 的 embedding 当作一个分布，而不是一个固定点。扩散阶段，模型把目标 item embedding 加噪成高斯分布，用这个过程表达 item 的多方面和用户意图的不确定性；随后 Approximator 学习从带噪表示中重构目标 item 表示。

在反向阶段，模型根据用户历史行为，从高斯噪声逐步反推目标 item 表示，再通过 rounding operation 把生成的连续 embedding 映射到真实 item。论文也研究了噪声 schedule、反向步数和训练目标等设计，并说明简单替换成 GRU 或错误的重构方式会显著变差。

## 实验效果如何

实验在 Amazon Beauty、Amazon Toys、MovieLens-1M、Steam 四个数据集上进行，并与九个强序列推荐基线比较。总体结果显示，DiffuRec 在 HR 和 NDCG 上稳定优于所有基线。论文报告相对最佳基线的最大提升分别达到 Beauty 上 HR/NDCG 57.26%/56.72%，Toys 上 22.76%/34.34%，MovieLens-1M 上 10.78%/11.36%，Steam 上 11.84%/11.39%。

消融实验很有说明力：用 GRU 替代核心建模会明显下降；错误的 rounding/representation 处理会导致性能大幅退化。Table 3 中 DiffuRec 在 Beauty 上 HR@20 为 11.1098、NDCG@20 为 5.5566，显著高于对应变体。噪声 schedule 分析显示，truncated linear schedule 在部分数据集上更优，但不同数据也有差异。

## 用最简单的话解释原理

DiffuRec 的直觉是：不要把“下一个 item”看成一个固定答案，而是看成一个可能区域。模型先把真实目标 item 的向量弄模糊，让它变成一个分布；再学习如何根据用户历史把这个模糊分布还原成合适的 item。

这就像用户心里并不是只想要某一个具体商品，而是想要“某类符合当前兴趣的商品”。DiffuRec 用扩散过程生成这个兴趣区域，再从区域里找到最接近的真实 item。
