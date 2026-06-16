# DCDR: Discrete Conditional Diffusion for Reranking in Recommendation

- 论文 PDF: [Discrete Conditional Diffusion for Reranking in Recommendation.pdf](Discrete Conditional Diffusion for Reranking in Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2308.06982
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

重排不是单个 item 打分，而是整个候选列表的排列优化；贪心排序很难直接建模 listwise 结构。

## 提出了什么方法

设计离散条件扩散过程，对 item 排列做随机 swap 和 token 替换，再在用户反馈条件下反向生成更优排列。

## 实验效果如何

论文报告在离线和工业场景中改进 reranking 效果，并提到已在快手相关业务中部署验证。

## 用最简单的话解释原理

把一份候选列表先随机打乱一点，再训练模型一步步把列表排回更好的顺序。
