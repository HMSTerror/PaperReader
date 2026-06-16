# DiFashion: Diffusion Models for Generative Outfit Recommendation

- 论文 PDF: [Diffusion Models for Generative Outfit Recommendation.pdf](Diffusion Models for Generative Outfit Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2402.17279
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

服装推荐不仅要判断哪些 item 合适，还希望直接生成兼容、个性化的 outfit 图像。

## 提出了什么方法

用条件扩散模型生成整套穿搭图像，并通过 guidance 同时约束图像质量、搭配兼容性和用户个性化。

## 实验效果如何

论文报告生成结果在图像质量、搭配兼容性和个性化评价上优于相关生成模型。

## 用最简单的话解释原理

用户不是只收到商品 ID，而是看到一套模型生成的、符合自己偏好的穿搭方案。
