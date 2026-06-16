# BSPM: Blurring-Sharpening Process Models for Collaborative Filtering

- 论文 PDF: [Blurring-Sharpening Process Models for Collaborative Filtering.pdf](Blurring-Sharpening Process Models for Collaborative Filtering.pdf)
- 下载来源: https://arxiv.org/pdf/2211.09324
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

图协同过滤中的平滑传播能扩散协同信号，但过度平滑会把用户偏好磨平；推荐需要同时保留共性和尖锐的个人偏好。

## 提出了什么方法

提出 Blurring-Sharpening Process Model，把推荐看成图信号的“模糊”和“锐化”：先用 blurring 传播协同信号，再用 sharpening 恢复尖锐偏好。它更像一个基于图滤波和 ODE 的生成式过程，而不是标准 DDPM。

## 实验效果如何

论文在多个 CF 数据集上报告了相对 LightGCN/GF-CF 等图推荐方法的改进，并强调该视角能统一解释一些已有图滤波推荐器。

## 用最简单的话解释原理

先把邻居信息揉进来，让偏好更完整；再把太平均的部分拉回来，让用户自己的偏好重新变清楚。
