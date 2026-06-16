# DreamRec: Generate What You Prefer: Reshaping Sequential Recommendation via Guided Diffusion

- 论文 PDF: [Generate What You Prefer - Reshaping Sequential Recommendation via Guided Diffusion.pdf](Generate What You Prefer - Reshaping Sequential Recommendation via Guided Diffusion.pdf)
- 下载来源: https://arxiv.org/pdf/2310.20453
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

DreamRec 质疑序列推荐长期采用的 learning-to-classify 范式。传统模型给定用户历史和一个正样本，再通过负采样构造负样本，让模型学习区分喜欢/不喜欢。但这种做法有两个问题：第一，人类决策更像先在心里想象一个理想 item，再从候选里找接近它的东西；第二，负采样得到的负样本可能太容易或有噪声，会稀释真正指向理想 item 的偏好信号。

因此论文想解决的问题是：能否不依赖负采样，直接根据用户历史生成一个 oracle item 表示，再用它去匹配真实候选 item？

## 提出了什么方法

DreamRec 把序列推荐重塑为 learning-to-generate。它用 Transformer encoder 编码历史序列，形成 guidance representation；然后对目标 item embedding 加噪，让扩散模型学习 item 空间的底层分布；反向去噪时，模型在历史交互的引导下生成 oracle item embedding，用来恢复正样本。

推荐时，DreamRec 先生成一个理想 item 的向量，再在候选 item 中找与该向量最近的 Top-K item。它使用 guided diffusion 和 classifier-free guidance 控制历史信息对生成过程的影响，因此训练阶段不需要负采样，核心目标是生成用户真正想要的 item 表示。

## 实验效果如何

实验在 YooChoose、KuaiRec、Zhihu 三个数据集上比较 GRU4Rec、Caser、SASRec、IPS、AdaRanker、CL4SRec、DiffRec 等方法。Table 1 显示 DreamRec 全部数据集上最好：例如 YooChoose HR@20/NDCG@20 为 4.78/2.23，高于 CL4SRec 的 4.45/1.86；KuaiRec 上 HR@20/NDCG@20 为 5.16/4.11，明显高于 AdaRanker 或 CL4SRec；Zhihu 上也达到 2.26/0.79。

可视化实验显示，DreamRec 学到的 item embedding 能覆盖更大的 item 空间，而不需要负采样；SASRec 如果没有负采样，item embedding 会挤在有限区域里。guidance strength 的消融说明，适度增强历史引导能提升准确性，但过强会损害生成质量。

## 用最简单的话解释原理

DreamRec 的直觉很像“先想象，再挑选”。用户不是先把所有商品逐个打分，而是心里有个模糊的理想目标；DreamRec 就是生成这个理想目标的向量，再从真实 item 里找最接近的。

这让它摆脱了负采样。传统模型需要告诉它“这些是负例”；DreamRec 直接学习“用户真正想要的东西长什么样”，因此更接近生成式推荐。
