# Diff4Rec: Diff4Rec: Sequential Recommendation with Curriculum-scheduled Diffusion Augmentation

- 论文 PDF: [Diff4Rec - Sequential Recommendation with Curriculum-scheduled Diffusion Augmentation.pdf](Diff4Rec - Sequential Recommendation with Curriculum-scheduled Diffusion Augmentation.pdf)
- 下载来源: https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2023_Diff4Rec%20Sequential%20Recommendation%20with%20Curriculum-scheduled%20Diffusion%20Augmentation.pdf
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

传统序列增强多是固定规则，太简单；直接用强扩散增强又可能一开始太难，训练不稳定。

## 提出了什么方法

提出 curriculum-scheduled diffusion augmentation，让噪声和增强难度随训练阶段逐步变化，从容易增强过渡到更难增强。

## 实验效果如何

论文在多个序列推荐数据集上报告优于常见数据增强方法和若干序列推荐 baseline。

## 用最简单的话解释原理

像教学一样训练：先给模型看轻微扰动的样本，等它学会后再逐渐增加难度。
