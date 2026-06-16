# PDRec: Plug-In Diffusion Model for Sequential Recommendation

- 论文 PDF: [Plug-In Diffusion Model for Sequential Recommendation.pdf](Plug-In Diffusion Model for Sequential Recommendation.pdf)
- 下载来源: https://ojs.aaai.org/index.php/AAAI/article/download/28736/29419
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

序列推荐需要处理动态偏好、时间间隔和稀疏反馈，但最好不要重写整个推荐 backbone。

## 提出了什么方法

提出可插拔扩散模块，结合 HBR 历史行为重加权、DPA 扩散正样本增强和 NNS 无噪负采样，可接到多种 Transformer 序列推荐模型上。

## 实验效果如何

AAAI 论文报告 PDRec 能稳定增强多个序列推荐 backbone，在多个公开数据集上提升 Top-K 指标。

## 用最简单的话解释原理

不替换原来的推荐模型，而是在旁边加一个扩散插件，帮它生成更可信的正向偏好信号。
