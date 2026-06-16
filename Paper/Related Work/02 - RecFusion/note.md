# RecFusion: RecFusion: A Binomial Diffusion Process for 1D Data for Recommendation

- 论文 PDF: [RecFusion - A Binomial Diffusion Process for 1D Data for Recommendation.pdf](RecFusion - A Binomial Diffusion Process for 1D Data for Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2306.08947
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

用户点击记录本质上是 0/1 稀疏数据，但很多扩散推荐方法直接用连续高斯噪声，这和二值反馈的数据形态不匹配。

## 提出了什么方法

提出 Binomial/Bernoulli diffusion：前向过程不加高斯噪声，而是按概率翻转 0/1 bit；反向过程学习把被翻转的点击向量恢复回来，并用 BCE/ELBO 训练。

## 实验效果如何

论文报告在推荐数据上，二值扩散比直接套用高斯扩散更贴合隐式反馈，能带来更稳定的推荐效果。

## 用最简单的话解释原理

如果数据是开关，就不要用连续小数去污染它。RecFusion 像是随机把一些点击开关拨错，再训练模型把拨错的开关拨回来。
