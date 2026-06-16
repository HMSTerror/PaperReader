# LD4MRec: LD4MRec: Simplifying and Powering Diffusion Model for Multimedia Recommendation

- 论文 PDF: [LD4MRec - Simplifying and Powering Diffusion Model for Multimedia Recommendation.pdf](LD4MRec - Simplifying and Powering Diffusion Model for Multimedia Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2309.15363
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

多媒体推荐中的扩散模型推理慢，完整多步去噪难以满足实时推荐需求。

## 提出了什么方法

提出轻量化扩散框架，使用 forward-free 或简化推理，并用 C-Net 结合协同信号和模态偏好进行指导。

## 实验效果如何

论文报告在多媒体推荐数据集上取得接近或优于完整扩散模型的效果，同时显著降低推理成本。

## 用最简单的话解释原理

保留扩散模型“修正偏好”的核心思想，但把多步慢过程压缩成更快的近似过程。
