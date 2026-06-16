# CF-Diff: Collaborative Filtering Based on Diffusion Models: Unveiling the Potential of High-Order Connectivity

- 论文 PDF: [Collaborative Filtering Based on Diffusion Models - Unveiling the Potential of High-Order Connectivity.pdf](Collaborative Filtering Based on Diffusion Models - Unveiling the Potential of High-Order Connectivity.pdf)
- 下载来源: https://arxiv.org/pdf/2404.14240
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

早期 DiffRec 主要看用户自己的交互向量，利用高阶 user-item graph 连通性的能力不足。

## 提出了什么方法

提出 CF-Diff，在扩散去噪过程中加入高阶连接信息，并用 cross-attention guided multi-hop autoencoder 恢复用户偏好。

## 实验效果如何

论文报告在多个公开 CF 数据集上优于 DiffRec、LightGCN 等 baseline，说明高阶邻居信息能弥补单纯交互向量扩散的不足。

## 用最简单的话解释原理

用户没点过的 item 也可能通过“用户-物品-用户-物品”的多跳路径传来线索。CF-Diff 在去噪时把这些远一点的线索也看进去。
