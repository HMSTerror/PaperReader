# CG4CTR: A New Creative Generation Pipeline for Click-Through Rate with Stable Diffusion Model

- 论文 PDF: [A New Creative Generation Pipeline for Click-Through Rate with Stable Diffusion Model.pdf](A New Creative Generation Pipeline for Click-Through Rate with Stable Diffusion Model.pdf)
- 下载来源: https://arxiv.org/pdf/2401.10934
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

广告创意图会影响点击率，但人工设计成本高；直接用 Stable Diffusion 生成也不一定符合 CTR 目标。

## 提出了什么方法

构建广告创意生成流水线：保留主体，用 Stable Diffusion inpainting 生成背景，再用 prompt model 和 reward model 让图片更贴近点击率目标。

## 实验效果如何

论文报告离线评价和线上广告实验都显示生成创意能提升点击相关指标。

## 用最简单的话解释原理

不是随便生成好看的广告图，而是让生成模型按“更可能被点击”的奖励信号去改背景。
