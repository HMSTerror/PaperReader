# Filter-enhanced MLP is All You Need for Sequential Recommendation

- 论文 PDF: [Filter-enhanced MLP is All You Need for Sequential Recommendation.pdf](Filter-enhanced MLP is All You Need for Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2202.13556
- 年份/会议: WWW 2022
- 方向: 序列推荐基础
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
FMLP-Rec 的核心观点是：序列推荐不一定必须依赖 RNN、CNN 或 Transformer attention，简单的 MLP 若结合频域滤波也能成为强 baseline。论文观察到线上行为日志不可避免包含噪声，深层推荐模型容易过拟合这些噪声。作者借鉴信号处理中的**滤波 (filtering)** 思想，将用户行为序列映射到频域，用可学习滤波器衰减无用频率成分，再用 all-MLP 架构完成序列建模。实验在八个真实数据集上表明，FMLP-Rec 超过 RNN、CNN、GNN 和 Transformer 类方法，并具有更低时间复杂度。

## 背景
在 SASRec 之后，大量工作默认 attention 是序列推荐的核心组件。然而，用户点击序列并不总是干净语言序列：误点、偶然浏览和平台曝光都会产生噪声。若模型过强，可能学习到噪声中的伪模式。本文的研究空白是：是否可以不依赖 attention，而通过频域滤波得到更鲁棒的序列表示。

**Research Questions**：1. 经典滤波操作是否能改善序列推荐模型？2. all-MLP 结构配合 learnable filters 是否足以捕获序列模式？3. 可学习滤波器相比固定高通/低通/带阻滤波是否更有效？

**Hypotheses**：作者假设用户行为序列可视为信号，其中高频或特定频段包含噪声；学习式频域过滤能保留稳定偏好模式；attention 并非提升推荐的唯一途径。

## 文献综述
论文把已有序列推荐分为 RNN、CNN、GNN 和 Transformer 路线。GRU4Rec 代表递推式建模，Caser/NextItNet 代表卷积式局部模式，SASRec/BERT4Rec 代表 attention。作者批判性指出，这些模型都强调增强序列捕获能力，却较少直接处理日志噪声。

论文还引用信号处理中的频域滤波思想。其过渡逻辑是：若用户行为序列可看作多维离散信号，那么用快速傅里叶变换 (Fast Fourier Transform, FFT) 将其变到频域，再学习滤波权重，可能比在时域强行 attention 更稳健。

## 方法
**Participants**：无受试者；实验对象是公开用户行为序列。

**Materials**：论文使用八个真实数据集，并与 RNN、CNN、GNN、Transformer 等多类模型比较。评价指标包括 HR、NDCG 等 top-N 推荐指标。

**Procedure**：FMLP-Rec 的核心是 filter block。模型先对序列表示做傅里叶变换，得到频域特征；再用可学习复数滤波器逐维相乘；最后逆变换回时域。论文证明这一操作等价于循环卷积 (circular convolution)，因此仍能捕获序列依赖。模型整体采用 MLP、残差连接和归一化，不使用 self-attention。

## 实验和结果
实验显示，把简单滤波器加入代表性序列模型已经能提升性能，而 FMLP-Rec 的 learnable filter 进一步超过固定 high-pass、low-pass、band-stop 等变体。消融实验表明，移除 filter layer、feed-forward network 或 Add & Norm 都会造成下降，其中 filter layer 最关键。

论文还可视化了学到的滤波器，发现低频信号通常获得更大权重，高频信号被抑制。这与作者关于行为噪声的解释一致：稳定兴趣更像低频模式，偶然点击更像高频扰动。

## 讨论
FMLP-Rec 的学术意义是挑战“attention is all you need”在推荐中的默认假设。它说明序列推荐的核心不只是捕获更长依赖，也包括从噪声日志中提取稳定偏好。对你的工作而言，FMLP-Rec 是强 ID-only baseline：如果 cross-attention 只是增加复杂度而没有更好处理信息互补，就可能被简单而稳健的模型击败。

与 SASRec 相比，FMLP-Rec 解释性不是来自注意力权重，而是来自频域滤波模式。它把推荐序列看作信号，这为分析多模态序列中的噪声、冗余和冲突提供了另一种视角。

## 结论
作者总结 FMLP-Rec 通过 learnable filters 与 all-MLP 架构在八个数据集上取得优越效果。论文未来方向主要体现在附录分析中：进一步解释滤波器行为、研究隐藏维度和不同频率模式对推荐性能的影响。
