# DCDR: Discrete Conditional Diffusion for Reranking in Recommendation

- 论文 PDF: [Discrete Conditional Diffusion for Reranking in Recommendation.pdf](Discrete Conditional Diffusion for Reranking in Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2308.06982
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

DCDR 研究多阶段推荐系统最后的 reranking。召回和粗排已经给出候选列表，重排需要考虑 item 之间的相互影响，把列表重新排列成整体效用更高的序列。难点在于排列空间是组合爆炸的，且 item permutation 是离散数据，不适合直接用连续扩散模型。

此外，推荐重排不是普通生成任务。生成序列必须满足用户兴趣和反馈条件，还要足够高效，才能部署到真实推荐系统中。因此论文要解决离散排列、条件控制和线上效率三类问题。

## 提出了什么方法

DCDR 提出 Discrete Conditional Diffusion Reranking。Forward process 使用离散操作给 item 序列加噪，例如 step-wise swapping 或 token-level 替换，并且保持 tractable posterior。Reverse process 则在用户期望反馈条件下生成更好的 item 排列。

论文给出两种变体：DCDR-P 使用 permutation-level 操作，DCDR-T 使用 token-level 操作。为了部署，作者还设计 beam search、early stop、合适 reverse steps 和 noise scale 等推理优化，让扩散重排在真实系统中可用。

## 实验效果如何

离线实验在 Avito 和 VideoRerank 数据集上，与 PRM、EGRerank、SetRank、DLCM、DiffusionLM-R 等比较。Table 1 中 DCDR-P 最好：Avito AUC/NDCG@3 为 0.9172/0.3901，VideoRerank 为 0.6361/0.6576；DCDR-T 也显著优于 DiffusionLM-R。说明为离散重排专门设计的扩散比直接改造文本扩散更合适。

线上实验部署在快手 App，涉及超过 3 亿日活的真实系统。Table 2 显示 DCDR-P 相对线上 PRM baseline 使 Views 提升 0.341%，Likes 提升 0.884%，Follows 提升 1.100%，Collects 提升 1.299%，Downloads 提升 1.358%，均为显著提升。效率分析表明有额外延迟，但在系统中可接受。

## 用最简单的话解释原理

重排就像把一串视频重新排序。DCDR 先把一个列表故意打乱一点，再训练模型学会在用户反馈条件下把它恢复成更好的顺序。因为 item 顺序是离散的，所以它不用连续高斯噪声，而是用交换、替换这类离散操作。

它的核心是把“生成列表”变成“逐步修复列表”。每一步都让列表更符合用户可能喜欢、看完、点赞的方向。
