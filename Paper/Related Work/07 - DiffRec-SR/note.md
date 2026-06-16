# DiffRec-SR: Sequential Recommendation with Diffusion Models

- 论文 PDF: [Sequential Recommendation with Diffusion Models.pdf](Sequential Recommendation with Diffusion Models.pdf)
- 下载来源: https://arxiv.org/pdf/2304.04541
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

序列推荐扩散如果把整条历史也加噪，会破坏用户上下文；真正需要生成的是目标 item，而历史应该作为条件保留。

## 提出了什么方法

只对目标 item 的连续 embedding 加噪声，历史序列不加噪，只作为条件输入，训练模型根据历史恢复目标 item 表示。

## 实验效果如何

论文报告在序列推荐数据集上相对常见 backbone 有提升，说明“noise target, keep history clean”的设置更适合 next-item 生成。

## 用最简单的话解释原理

历史是题目，不要把题目弄脏；要被模型恢复的是答案，也就是下一个 item。
