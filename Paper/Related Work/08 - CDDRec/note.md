# CDDRec: Conditional Denoising Diffusion for Sequential Recommendation

- 论文 PDF: [Conditional Denoising Diffusion for Sequential Recommendation.pdf](Conditional Denoising Diffusion for Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2304.11433
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

CDDRec 面向序列推荐中生成模型训练不稳定、表示过度平滑和数据稀疏噪声的问题。GAN 在推荐中优化不稳定，VAE 容易 posterior collapse，生成出的表示可能过于平滑，导致不同 item 难以区分。序列推荐本身又稀疏、噪声多，这会进一步放大这些问题。

作者认为，扩散模型能把复杂生成过程拆成多个简单去噪步骤，但直接用 MSE 重构 item embedding 仍可能导致 collapse，也不一定能学到有排名能力的表示。因此需要一个既能生成高质量序列/item 表示，又能服务排序目标的训练范式。

## 提出了什么方法

CDDRec 包含 sequence encoder、cross-attentive denoising decoder 和 step-wise diffuser。Sequence encoder 编码用户历史，denoising decoder 用 cross-attention 把扩散步 indicator 作为 query，把序列 embedding 作为 key/value，从而实现条件自回归式去噪生成。

训练目标上，论文提出 cross-divergence loss 和 contrastive loss。Cross-divergence 不只是拉近预测 item 和正样本，还通过负样本让表示更可分，缓解 MSE 带来的 collapse；contrastive loss 则进一步提高表示质量。作者还对不同扩散步做 loss rescale，让模型在多步去噪中训练更稳定。

## 实验效果如何

实验在 Amazon Office、Beauty、Tools、Toys 四个数据集上进行，与 SVAE、ACVAE、ContrastVAE、CL4Rec、DuoRec、CBiT、GRU4Rec、SASRec、Bert4Rec、FMLP 等模型比较。CDDRec 在 Table 2 中整体最好，尤其 Recall@1 提升明显：Office、Beauty、Tools、Toys 上相对第二名分别提升 20.98%、16.67%、17.59%、18.42%。

消融实验显示，若用 MSE 替代 cross-divergence，性能会大幅下降；论文报告 single-view 和 multi-view MSE 变体出现 88.88% 和 91.42% 的显著性能跌落，说明普通重构目标确实会导致 collapse。loss rescale、contrastive loss 和多视图增强都对最终效果有正贡献。

## 用最简单的话解释原理

CDDRec 像是在做“带条件的分步修图”，只不过修的不是图片，而是下一个 item 的表示。用户历史告诉模型应该往哪个方向修，扩散步告诉模型现在处于多模糊的阶段。

它的关键不是单纯把带噪向量变回原向量，而是让修出来的表示在排序时能把正样本和负样本分开。因此它用 cross-divergence 和 contrastive loss，让扩散生成出的 embedding 既像目标 item，又有推荐排序能力。
