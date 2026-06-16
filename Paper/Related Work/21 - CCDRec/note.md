# CCDRec: Curriculum Conditioned Diffusion for Multimodal Recommendation

- 论文 PDF: [Curriculum Conditioned Diffusion for Multimodal Recommendation.pdf](Curriculum Conditioned Diffusion for Multimodal Recommendation.pdf)
- 下载来源: https://ojs.aaai.org/index.php/AAAI/article/download/33422/35577
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

CCDRec 关注多模态推荐中的负采样问题。传统多模态推荐多关注如何融合 item 的图像、文本等信息，却忽略了负样本对个性化偏好学习的影响。随机负采样可能太简单，不能提供有效训练信号；过难或错误负样本又可能误导模型。

论文认为，扩散模型的逐步反向生成特性天然适合构造不同难度的负样本：早期反向步得到的样本更 noisy、更简单；后期样本更接近用户和正样本，更有信息量。因此可以把 diffusion reverse process 与 curriculum negative sampling 结合。

## 提出了什么方法

CCDRec 包含三个模块。DMA（Diffusion-controlled Multimodal Aligning）在概率分布空间中捕获不同模态之间的细粒度关系，把多模态知识与协同信号对齐。NDI（Negative-sensitive Diffusive Inferring）利用扩散反向过程生成不同 hardness 的负样本池。

CNS（Curricular Negative Sampler）按照课程学习思想，从简单到复杂动态选择负样本，让模型逐渐面对更难的训练信号。三个模块都是 model-agnostic，可以与 LATTICE、FREEDOM、MG 等多模态推荐 backbone 结合。

## 实验效果如何

实验在 Baby、Sports、Clothing 三个数据集上进行，比较 CF-based recommenders、传统多模态 recommenders 和不同 backbone 下的 CCDRec。Table 2 显示，CCDRec 在 Recall@5/10 和 NDCG@5/10 上显著超过所有基线。论文特别指出，CCDRec 在 LATTICE 上提升最明显，与 FREEDOM 结合时达到各数据集峰值。

消融实验显示，DMA、NDI、CNS 都不可少。可视化分析也验证了课程负采样直觉：随着反向扩散步数增加，生成的负样本在低维空间中逐渐靠近对应用户和正样本，因此更有训练价值。完整 CCDRec 能更好学习细粒度多模态偏好。

## 用最简单的话解释原理

CCDRec 把负采样看成“给模型出练习题”。一开始给太难的题，模型学不会；一直给太简单的题，模型也进步不了。扩散反向过程刚好能产生从简单到困难的一系列负样本。

DMA 先让多模态表示对齐，NDI 生成不同难度负样本，CNS 决定训练时该用哪种难度。这样模型逐步学会区分用户真正喜欢的 item 和越来越相似但仍不合适的 item。
