# DiffRec-SR: Sequential Recommendation with Diffusion Models

- 论文 PDF: [Sequential Recommendation with Diffusion Models.pdf](Sequential Recommendation with Diffusion Models.pdf)
- 下载来源: https://arxiv.org/pdf/2304.04541
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

这篇 Sequential Recommendation with Diffusion Models 同样研究序列推荐，但切入点是 VAE/GAN 生成式推荐的缺陷。VAE 容易 posterior collapse，GAN 容易 model collapse，虽然它们能建模用户行为不确定性并缓解 exposure bias，但训练稳定性和生成质量限制了它们在序列推荐中的应用。

另一个难点是推荐数据是离散 item 序列，而标准扩散模型主要处理连续图像数据。若直接对整条序列或 item id 加噪，会破坏序列结构，推理成本也会随扩散步数变得很高。

## 提出了什么方法

论文提出一个面向序列推荐的 DiffRec 框架。它修改了扩散模型的 forward 和 reverse process，加入适合离散推荐数据的 transition，使扩散过程能处理 item 序列。与对整条序列加噪不同，模型只对 target item 加噪，保留历史序列作为条件，这更符合“根据历史预测下一个 item”的任务结构。

基于修改后的扩散过程，作者推导了训练目标，并设计 denoise sequential recommender 来完成去噪预测。为了降低成本，论文还提出 efficient training strategy 和 efficient inference strategy，在减少训练/推理开销的同时提升推荐多样性。

## 实验效果如何

论文在三个公开 benchmark 数据集上评估，与当时的 state-of-the-art sequential recommendation 模型比较。结果显示，该方法在推荐准确性上超过已有序列推荐模型，并且有效避免 VAE/GAN 式生成模型常见的 collapse 问题。

实验还说明，专门为推荐设计的 noising strategy 很重要：只污染目标 item 比污染整个序列更适合下一项预测。高效训练和推理策略则缓解了扩散步数带来的时间复杂度，让扩散模型在序列推荐中更可用。

## 用最简单的话解释原理

可以把它理解为：历史序列是题目，目标 item 是答案。模型训练时故意把答案弄模糊，然后学习在题目提示下把答案恢复出来。因为只弄模糊答案，而不破坏题目，所以模型能更好地利用用户历史。

它和分类式推荐不同：分类式模型是在所有 item 里判断哪个最像答案；扩散式模型是先生成一个“理想答案”的表示，再把它对应到真实 item。
