# PDRec: Plug-In Diffusion Model for Sequential Recommendation

- 论文 PDF: [Plug-In Diffusion Model for Sequential Recommendation.pdf](Plug-In Diffusion Model for Sequential Recommendation.pdf)
- 下载来源: https://ojs.aaai.org/index.php/AAAI/article/download/28736/29419
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

PDRec 认为已有扩散序列推荐只利用了扩散模型输出中最高分的 item，忽略了扩散模型对全体 item 的偏好分布。实际上，用户对很多未观察 item 也可能有潜在兴趣，如果只看 top-1 或最高分，就浪费了扩散模型生成出的丰富 soft preference。

同时，序列推荐还面临数据稀疏、历史行为噪声和 false negative sampling 问题。未交互 item 不一定是真负样本；如果负采样采到用户其实会喜欢的 item，会误导训练。

## 提出了什么方法

PDRec 把扩散模型设计成一个 plug-in，而不是替代原推荐器。它先用 time-interval diffusion model 推断用户对所有 item 的动态偏好，然后提供三个模块。HBR（Historical Behavior Reweighting）根据扩散偏好重新衡量历史行为质量，突出重要行为、压低噪声行为。

DPA（Diffusion-based Positive Augmentation）把高分但未观察的 item 作为潜在正样本，引入多样 soft signal 缓解稀疏。NNS（Noise-free Negative Sampling）选择更稳定可靠的负样本，降低 false negative 风险。整个框架可以插到 GRU4Rec、SASRec、CL4SRec 等 backbone 上。

## 实验效果如何

实验使用 Amazon Toys and Games、Video Games 以及 Douban Books、Music 四个数据集，并在 GRU4Rec、SASRec、CL4SRec 三类 backbone 上验证。Table 1 显示 PDRec 在四个数据集上显著超过原 backbone 和 T-DiffRec，所有提升在 paired t-test 下显著。论文也指出，稀疏的 Toy/Game 数据集收益更明显，但较稠密数据集上也有稳定提升。

消融实验表明，HBR、DPA、NNS 都有贡献；跨域序列推荐扩展中，PDRec 相比 T-DiffRec/TI-DiffRec 在混合行为序列上最高提升可达 38.3%。这说明“充分利用扩散偏好分布”比只取最高分 item 更有效。

## 用最简单的话解释原理

PDRec 像是把扩散模型当成一个经验丰富的辅助老师。它不直接替学生答题，而是告诉原推荐模型：哪些历史行为更可信，哪些没点过的 item 其实可能是正样本，哪些负样本比较安全。

因此它的重点不是生成一个答案，而是把扩散模型产生的全量偏好信息拆成三种训练信号，帮助任何序列推荐器学得更稳。
