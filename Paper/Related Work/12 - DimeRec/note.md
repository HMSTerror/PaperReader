# DimeRec: DimeRec: A Unified Framework for Enhanced Sequential Recommendation via Generative Diffusion Models

- 论文 PDF: [DimeRec - A Unified Framework for Enhanced Sequential Recommendation via Generative Diffusion Models.pdf](DimeRec - A Unified Framework for Enhanced Sequential Recommendation via Generative Diffusion Models.pdf)
- 下载来源: https://arxiv.org/pdf/2408.12153
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

直接生成具体 next item 难度很高，因为 item 空间巨大、稀疏且不平稳，扩散重建损失和推荐排序损失容易冲突。

## 提出了什么方法

不强行生成一个确定 item，而是生成下一阶段兴趣区域。框架包含 guidance extraction module 和 diffusion aggregation module，使生成兴趣与最终推荐表示更一致。

## 实验效果如何

论文报告在序列推荐数据集上提升准确性和多样性，特别强调生成兴趣区域比硬生成单个 item 更稳。

## 用最简单的话解释原理

与其一步猜中具体商品，不如先猜用户下一段兴趣会落在哪个区域，再从这个区域里选 item。
