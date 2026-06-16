# DDRM: Denoising Diffusion Recommender Model

- 论文 PDF: [Denoising Diffusion Recommender Model.pdf](Denoising Diffusion Recommender Model.pdf)
- 下载来源: https://arxiv.org/pdf/2401.06982
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

推荐模型学到的 user/item embedding 会被隐式反馈噪声污染，导致后续打分不可靠。

## 提出了什么方法

把扩散模型当成 embedding 去噪器：训练时给 user/item 表示加噪，反向过程恢复更干净的表示；推理时用用户历史偏好 item 的平均表示作为起点生成 ideal item embedding。

## 实验效果如何

论文报告 DDRM 作为插件能提升多个推荐 backbone，在数据稀疏或反馈噪声较强时更有帮助。

## 用最简单的话解释原理

先把推荐模型学到的向量洗干净，再用干净向量做匹配。
