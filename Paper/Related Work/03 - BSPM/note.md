# BSPM: Blurring-Sharpening Process Models for Collaborative Filtering

- 论文 PDF: [Blurring-Sharpening Process Models for Collaborative Filtering.pdf](Blurring-Sharpening Process Models for Collaborative Filtering.pdf)
- 下载来源: https://arxiv.org/pdf/2211.09324
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

BSPM 处理的是协同过滤中的“如何从已有交互矩阵里直接发现未知交互”的问题。很多 CF 方法会学习用户和 item 的低维 embedding，但这种压缩可能丢掉原始交互矩阵里的细粒度结构。图滤波方法如 GF-CF 证明，不学习 embedding、直接处理用户-item 矩阵也可以很强。

论文受到 score-based generative model 的启发：生成模型常用“先扰动，再恢复”的方式发现新信息。但图像生成面对的是许多图像样本和随机微分方程，而协同过滤通常只有一个用户-item 交互矩阵，不能原样套用 SGM。因此它要回答的问题是：能不能为 CF 设计一种确定性的“扰动-恢复”过程，既保留图滤波的速度，又获得类似生成模型的发现能力？

## 提出了什么方法

论文提出 Blurring-Sharpening Process Model。Blurring 是把交互矩阵模糊化，让用户的行为信号沿图结构传播，混入邻居和协同信息；Sharpening 是把模糊后的信号重新锐化，让模型恢复更符合个体用户的偏好。整个过程用 ODE 描述，是确定性的，不需要像神经网络那样训练参数。

作者设计了 BSPM-LM 和 BSPM-EM 两个变体，区别在于如何连接 blurring 与 sharpening。它们都直接在交互矩阵上操作，不学习用户/item embedding。论文还从理论上说明，若只看部分过程，很多已有图滤波 CF 方法可以被看成 BSPM 的特殊情况，因此 BSPM 更像是一个统一框架，而不只是一个孤立技巧。

## 实验效果如何

实验覆盖 Gowalla、Yelp2018、Amazon-book 三个数据集和 43 个 CF 基线，包括 MF、VAE、图神经网络、LightGCN、UltraGCN、GF-CF、LinkProp 等。Table 4 中 BSPM-EM 在三个数据集上整体最好：Gowalla Recall/NDCG 为 0.1920/0.1597，Yelp2018 为 0.0720/0.0593，Amazon-book 为 0.0733/0.0609；相对第二名提升分别约 0.63%、0.50%、2.71%、3.13%、1.66%、3.74%。

消融结果表明，只有 blurring 不够，加入 sharpening 才能稳定提升；ODE 求解不需要很多步，少量步数就能取得好效果，所以运行时间也保持很快。论文特别强调 BSPM 没有训练阶段，却能在准确率和速度上都很有竞争力，这对实际 CF 系统很重要。

## 用最简单的话解释原理

可以把用户-item 矩阵想成一张有很多空格的表。Blurring 就是先把每个用户的行为和相似用户、相似 item 的行为混一混，让隐藏的协同线索浮出来；Sharpening 再把这个混合信号拉回到某个具体用户身上，突出这个用户最可能喜欢的 item。

所以 BSPM 不是训练一个新模型，而是对原始矩阵做“先扩散信息，再聚焦偏好”的数学处理。它的直觉很像把一张模糊照片先柔化细节、再增强边缘，只不过对象从图像换成了推荐交互矩阵。
