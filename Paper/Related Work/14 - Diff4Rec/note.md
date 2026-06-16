# Diff4Rec: Diff4Rec: Sequential Recommendation with Curriculum-scheduled Diffusion Augmentation

- 论文 PDF: [Diff4Rec - Sequential Recommendation with Curriculum-scheduled Diffusion Augmentation.pdf](Diff4Rec - Sequential Recommendation with Curriculum-scheduled Diffusion Augmentation.pdf)
- 下载来源: https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2023_Diff4Rec%20Sequential%20Recommendation%20with%20Curriculum-scheduled%20Diffusion%20Augmentation.pdf
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

Diff4Rec 同样关注序列推荐的数据稀疏，但进一步指出两个挑战。第一，图像扩散模型捕捉的是像素模式，不能直接用于用户-item 关系增强。第二，即使扩散模型能生成交互，生成样本也不一定总是有益；低质量增强样本可能干扰序列推荐器训练。

因此论文要解决的不只是“生成更多数据”，而是“如何让扩散生成的数据按难度和质量逐步进入训练，使它真正帮助模型”。

## 提出了什么方法

Diff4Rec 是一个 curriculum-scheduled diffusion augmentation framework。它先在 recommendation latent space 中预训练扩散模型，通过 corrupting and reconstructing 用户-item 交互来学习生成多样增强样本。然后把生成预测用于扩展稀疏交互。

核心是 curriculum scheduling。论文从两个层面调度增强：interaction augmentation 直接补充序列交互，objective augmentation 把生成样本作为候选加入增强训练目标。课程策略按 easy-to-hard 逐渐引入扩散样本，避免一开始就让模型吸收太多噪声。

## 实验效果如何

实验在 ML-1M、Beauty、Steam 等四个数据集上与 BPR、NCF、GRU4Rec、Caser、SASRec、BERT4Rec、S3Rec、STOSA、ContraRec 等比较。Table 2 显示 Diff4Rec 在全部指标上最好。比如 ML-1M 上 HR@20 为 0.3830，相对最强基线提升 11.90%；Beauty 上 HR@20 为 0.1347，提升 22.54%，NDCG@5 提升 21.50%。论文特别指出，在 Beauty 和 Steam 这类稀疏数据上提升通常超过 20%。

消融实验把 Diff4Rec 接到 GRU4Rec、Caser、SASRec 等不同 sequence encoder 上，仍能稳定提升，说明它是通用增强框架。去掉 curriculum scheduler 或只保留部分增强都会下降，证明“逐步引入生成样本”是关键。

## 用最简单的话解释原理

Diff4Rec 的直觉是：扩散模型可以帮用户历史补充可能的交互，但这些补充样本有好有坏，不能一次性全丢给推荐器。课程学习就像老师给学生安排题目，先做容易且可靠的增强，再逐步加入更难、更丰富的样本。

所以它不是单纯的数据扩增，而是“有节奏的数据扩增”。扩散负责生成候选，课程调度负责决定什么时候、以什么形式让推荐模型学习这些候选。
