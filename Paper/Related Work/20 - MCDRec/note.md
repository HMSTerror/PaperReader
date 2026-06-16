# MCDRec: Multimodal Conditioned Diffusion Model for Recommendation

- 论文 PDF: [Multimodal Conditioned Diffusion Model for Recommendation.pdf](Multimodal Conditioned Diffusion Model for Recommendation.pdf)
- 下载来源: https://ercdm.sdu.edu.cn/__local/1/2E/06/BA3A14E80ADD5913EFFB0553083_B0155145_15CACA.pdf
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

多模态推荐中，模态特征质量不稳定，用户-物品图也有噪声，判别式模型很难同时处理这些不确定性。

## 提出了什么方法

提出 Multimodal Conditioned Diffusion Model，把多模态信息作为条件，引导扩散模型增强 item 表示和用户-物品关系。

## 实验效果如何

论文报告在多个多模态推荐数据集上优于若干多模态推荐 baseline，说明条件扩散能提升模态融合质量。

## 用最简单的话解释原理

让图像、文本等内容告诉扩散模型应该往哪个方向修正 item 表示，而不是盲目去噪。
