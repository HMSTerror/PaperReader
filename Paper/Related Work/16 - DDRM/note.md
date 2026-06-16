# DDRM: Denoising Diffusion Recommender Model

- 论文 PDF: [Denoising Diffusion Recommender Model.pdf](Denoising Diffusion Recommender Model.pdf)
- 下载来源: https://arxiv.org/pdf/2401.06982
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

DDRM 关注隐式反馈推荐中的噪声问题。用户点击、购买、浏览等行为包含大量 false positive：点了不一定喜欢，买了也可能只是偶然。已有方法多从数据清洗角度处理噪声，例如重采样、重加权，但这些方法依赖启发式假设，未必能适应不同模型和数据。

另一条思路是从模型角度增强 denoising ability：主动往表示里注入噪声，再训练模型去除噪声。但这要求推荐模型有足够强的表示能力来捕获噪声模式。DDRM 想做一个 model-agnostic 的插件，让任意后端推荐模型的 user/item embedding 都能被扩散去噪增强。

## 提出了什么方法

DDRM 接收后端 recommender 输出的 user embedding 和 item embedding，在 forward process 中加入受控高斯噪声，在 reverse process 中逐步去噪，输出更鲁棒的 embedding。它为用户和 item 分别设计 denoising module，并把协同信息作为 guidance 注入反向去噪。

推理阶段，DDRM 不从纯噪声开始，因为纯噪声缺少个性化。它使用用户历史喜欢 item 的平均 embedding 作为起点，再通过反向扩散生成 ideal item embedding，最后用 rounding function 把生成向量映射到真实 item 候选。论文还加入 reweighted loss，从数据清洗角度补充表示去噪。

## 实验效果如何

实验在 Yelp、Amazon-book、ML-1M 三个数据集上，将 DDRM 接到 MFBPR、LightGCN 等代表性后端模型上，并与 AdaGCL、CDAE、MultiVAE、DiffRec 以及 T-CE、R-CE、DeCA、BOD 等 model-agnostic denoising 方法比较。Table 2 显示，接入 DDRM 后后端模型在自然噪声设置下稳定提升，且相对原后端模型的提升在 p < 0.01 下显著。

论文还在随机噪声等设置下验证鲁棒性，并通过消融证明 user/item denoising module、collaborative guidance、reweighted loss 都有作用。结论是 DDRM 能作为插件增强已有推荐器，而不是要求重建整个推荐模型。

## 用最简单的话解释原理

DDRM 做的事像“给用户和商品向量洗澡”。原推荐模型先学出 user/item embedding，但这些 embedding 受脏反馈影响；DDRM 故意加一点噪声，再训练自己把噪声洗掉，从而得到更稳的表示。

推理时它不从随机点开始，而是从用户喜欢过的 item 平均向量开始，这样生成过程一开始就带有个性化方向。最后它把生成的理想 item 向量落回真实商品库。
