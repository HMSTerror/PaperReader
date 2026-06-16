# DiffCDR: Diffusion Cross-domain Recommendation

- 论文 PDF: [Diffusion Cross-domain Recommendation.pdf](Diffusion Cross-domain Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2402.02182
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

跨域推荐中，目标域交互稀疏，难点是如何把源域用户偏好迁移到目标域。

## 提出了什么方法

把 source 到 target 的用户 embedding 映射看成扩散生成过程，并加入 alignment module 和 task-oriented loss，使生成的目标域表示既对齐又有推荐价值。

## 实验效果如何

论文报告在跨域推荐实验中优于传统映射和对齐方法，特别适合目标域数据少的场景。

## 用最简单的话解释原理

把用户在源域的画像翻译成目标域画像，扩散模型负责生成这份翻译后的偏好向量。
