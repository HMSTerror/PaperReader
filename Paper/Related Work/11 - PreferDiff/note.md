# PreferDiff: Preference Diffusion for Recommendation

- 论文 PDF: [Preference Diffusion for Recommendation.pdf](Preference Diffusion for Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2410.13117
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

只用 MSE 恢复目标 embedding，不一定等价于推荐排序好；生成得像不代表排得准。

## 提出了什么方法

在扩散生成之外加入 preference/ranking 目标，把正样本和多个负样本的排序关系纳入训练，让生成目标和推荐目标更一致。

## 实验效果如何

论文报告在多个推荐数据集上提升排序指标，说明把偏好排序信号加入扩散训练能缓解“重建目标”和“推荐目标”不一致。

## 用最简单的话解释原理

模型不只要把答案画得像，还要知道哪个答案应该排在前面。
