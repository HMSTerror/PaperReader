# GiffCF: Graph Signal Diffusion Model for Collaborative Filtering

- 论文 PDF: [Graph Signal Diffusion Model for Collaborative Filtering.pdf](Graph Signal Diffusion Model for Collaborative Filtering.pdf)
- 下载来源: https://arxiv.org/pdf/2311.08744
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

普通高斯噪声不知道 item-item 图结构，可能破坏协同过滤中真正有用的邻接关系。

## 提出了什么方法

在 item-item 图上设计 graph-aware forward diffusion，用合成平滑滤波器沿图结构扩散信号；反向阶段学习恢复用户偏好。

## 实验效果如何

论文在 CF 数据集上报告优于普通扩散和若干图推荐 baseline，说明使用图结构定义噪声过程更适合协同过滤。

## 用最简单的话解释原理

不是随便往偏好里撒噪声，而是按“相似 item 图”去模糊偏好，再把模糊后的偏好复原。
