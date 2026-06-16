# DimeRec: DimeRec: A Unified Framework for Enhanced Sequential Recommendation via Generative Diffusion Models

- 论文 PDF: [DimeRec - A Unified Framework for Enhanced Sequential Recommendation via Generative Diffusion Models.pdf](DimeRec - A Unified Framework for Enhanced Sequential Recommendation via Generative Diffusion Models.pdf)
- 下载来源: https://arxiv.org/pdf/2408.12153
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

DimeRec 处理的是序列推荐中 item representation、兴趣多样性和扩散目标不一致的问题。好的 SR 模型既要表示用户不断变化的历史行为，也要生成多样但准确的候选兴趣。但直接把扩散模型接到 SR 上会遇到两类不匹配：推荐目标是预测兴趣/排序，扩散目标通常是噪声重构；用户历史是 non-stationary 的，而扩散模型更适合在相对稳定的空间里建模分布。

因此论文想解决：如何让扩散模型不是简单生成下一个 item，而是生成用户下一步稳定兴趣，并同时提升推荐质量和多样性。

## 提出了什么方法

DimeRec 由两个模块组成。GEM（Guidance Extraction Module）从用户非平稳历史中提取较稳定的兴趣引导信号；DAM（Diffusion Aggregation Module）以 GEM 的输出为条件，用扩散过程生成或重构用户下一兴趣表示。也就是说，模型不是直接扩散原始交互序列，而是在兴趣空间里做条件生成。

论文还设计了新的噪声空间和 loss，其中包括 guidance loss，以稳定扩散模块引入后的表示学习。Serving 时，生成的用户兴趣向量用于 ANN 检索 Top-N item，因此可以嵌入工业推荐系统。

## 实验效果如何

离线实验使用 YooChoose、KuaiRec、ML-10M 三个公开数据集，并与 SASRec、GRU4Rec、MIND、ComiRec、MultVAE、DreamRec、DiffuRec 等比较。DimeRec 整体优于已有多兴趣模型和扩散模型。论文还用 linear probing accuracy 和推荐类别数分析表示质量：DimeRec 的 linear probing accuracy 达到 0.5683，高于 SASRec 的 0.4947 和 ComiRec 的 0.4917，说明生成的兴趣表示更可判别。

更重要的是，DimeRec 已部署在大规模短视频推荐平台，服务数亿用户。线上 A/B 测试显示，它能提升用户观看时长、满意度和推荐多样性。论文也分析推理效率：反向步数增加会线性增加耗时，但在实际链路中 DimeRec 推理只占很小部分，可以满足线上服务要求。

## 用最简单的话解释原理

DimeRec 的核心不是“生成下一个 item”，而是“生成下一个兴趣”。用户历史很乱，今天看搞笑视频，明天看新闻，直接扩散这串行为会很难；GEM 先把历史整理成稳定兴趣提示，DAM 再根据这个提示生成下一步兴趣。

可以把它看作先从用户历史中提炼主题，再围绕主题生成候选。这样扩散模型生成的是更平滑、更稳定的兴趣分布，而不是被单个历史 item 牵着走。
