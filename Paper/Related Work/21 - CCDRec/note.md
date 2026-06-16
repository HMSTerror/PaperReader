# CCDRec: Curriculum Conditioned Diffusion for Multimodal Recommendation

- 论文 PDF: [Curriculum Conditioned Diffusion for Multimodal Recommendation.pdf](Curriculum Conditioned Diffusion for Multimodal Recommendation.pdf)
- 下载来源: https://ojs.aaai.org/index.php/AAAI/article/download/33422/35577
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

多模态推荐中的不同模态难度不同，直接把所有条件一次性喂给扩散模型，可能训练不稳或被噪声模态拖累。

## 提出了什么方法

提出 curriculum conditioned diffusion，把条件学习做成由易到难的课程，并结合多模态对齐和推荐目标。

## 实验效果如何

论文报告在多个多模态推荐数据集上优于 DiffMM、MCDRec 等相关方法，说明课程式条件扩散更稳定。

## 用最简单的话解释原理

先让模型学容易的模态信号，再逐步加入更难、更嘈杂的条件。
