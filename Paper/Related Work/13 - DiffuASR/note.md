# DiffuASR: Diffusion Augmentation for Sequential Recommendation

- 论文 PDF: [Diffusion Augmentation for Sequential Recommendation.pdf](Diffusion Augmentation for Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2309.12858
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

DiffuASR 面对序列推荐中的数据稀疏和长尾用户问题。很多用户只有很短的交互历史，模型很难准确学习他们的兴趣；已有数据增强方法要么生成整条伪序列、训练流程复杂，要么生成质量不高，容易把噪声带入训练。

作者认为，数据增强确实能缓解稀疏，但关键是生成的增强 item 必须和用户原始意图一致。否则增强越多，噪声越多，模型反而更差。

## 提出了什么方法

DiffuASR 用扩散模型生成 pseudo sequence 做 item-level augmentation。它先把离散 item 序列映射到连续 embedding matrix，再用扩散模型在这个空间里生成可作为前序增强的 item。为适配序列数据，论文设计了 Sequential U-Net（SU-Net），用于恢复 embedding sequence matrix，而不是直接使用图像 U-Net。

为了保证生成 item 与用户偏好一致，论文提出两种 guided strategy：classifier-guided 和 classifier-free。生成出的增强数据可以直接用于训练 Bert4Rec、SASRec、S3Rec 等现有序列推荐模型，不需要复杂的联合训练。

## 实验效果如何

实验在 Yelp、Beauty、Steam 三个数据集上，将 DiffuASR 加到 Bert4Rec、SASRec、S3Rec 三个 backbone 上，并与 Random、Random-Seq、ASReP 等增强方法比较。Table 2 显示 DiffuASR(CF/CG) 在大多数设置下显著最好。例如 Bert4Rec 在 Beauty 上无增强 NDCG@10/HR@10 为 0.2581/0.4302，DiffuASR(CG) 提升到 0.2818/0.4462；S3Rec 在 Yelp 上 DiffuASR(CF) 达到 0.4996/0.7727。

长尾用户分析显示，DiffuASR 对短历史用户提升明显，同时对长历史用户的损害更小；Random-Seq 和 ASReP 在部分 backbone 上会因噪声增强导致下降。超参数实验表明，增强 item 数量适中时效果最好，过多会引入额外噪声。

## 用最简单的话解释原理

DiffuASR 像是在给短历史用户“补几条合理的过去行为”。如果一个用户只点过两三个 item，模型很难判断兴趣；DiffuASR 根据这几条历史生成一些可能也符合兴趣的伪 item，让训练数据更丰富。

它和随机增强的区别是：随机增强只是乱塞 item，DiffuASR 通过扩散和 guidance 尽量生成与原始偏好一致的 item，所以更像“补全缺失历史”，不是“制造噪声”。
