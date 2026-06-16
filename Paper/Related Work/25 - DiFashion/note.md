# DiFashion: Diffusion Models for Generative Outfit Recommendation

- 论文 PDF: [Diffusion Models for Generative Outfit Recommendation.pdf](Diffusion Models for Generative Outfit Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2402.17279
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

DiFashion 研究 Generative Outfit Recommendation。传统 outfit recommendation 有两类：从已有套装中推荐，或从已有单品中组合个性化 outfit。但两者都受限于现有商品库，无法真正生成满足用户风格需求的新服装图像。

AIGC 让系统有机会直接生成服装图片和 outfit，但这个任务需要同时满足三点：fidelity，即图片真实好看；compatibility，即多个单品搭配协调；personalization，即符合特定用户的历史偏好。单纯使用 Stable Diffusion 生成单张图片无法保证这些目标同时成立。

## 提出了什么方法

论文定义 Generative Outfit Recommendation（GOR）任务，并提出 DiFashion。DiFashion 使用 diffusion model 并行生成多个 fashion images，组成一个 outfit。为满足三目标，它设计三类条件：类别/文本条件保证生成单品类别和语义，mutual condition 建模多个单品之间的兼容关系，history condition 引入用户交互历史实现个性化。

模型使用 Classifier-Free Guidance 增强生成图像与条件的对齐。DiFashion 同时应用在 PFITB（Personalized Fill-In-The-Blank）和 GOR 两个任务上：前者补全 outfit 中缺失的一件，后者直接生成完整 outfit。

## 实验效果如何

实验在 iFashion 和 Polyvore-U 两个数据集上进行。Table 2 中，DiFashion 在生成质量和个性化指标上明显领先。以 iFashion PFITB 为例，DiFashion 的 FID 为 34.06，低于 SD-v1.5 finetuned 的 42.47；IS 为 29.99，CIS 为 47.36，Personalization 为 55.86，也更高。GOR 中 DiFashion FID 为 20.21，优于多个 Stable Diffusion baseline。

人类评价 Table 5 显示，DiFashion 在 fidelity、compatibility、personalization 上被用户选择的比例均超过 50%。例如 PFITB 中相对 SD-v1.5 的偏好比例为 64.08%、60.44%、68.32%；GOR 中相对 SD-v2 为 66.52%、60.56%、63.72%。消融表明 mutual encoder 中的 MLP、mutual/history conditions 和 guidance scale 都影响表现。

## 用最简单的话解释原理

DiFashion 不是“给用户推荐已有衣服”，而是“为用户画出一套可能喜欢的新 outfit”。它同时考虑这件衣服是什么类别、几件衣服之间搭不搭、用户过去喜欢什么风格。

可以把它想成一个懂搭配的扩散生成器：不是独立生成上衣、裤子、鞋子，而是让这些单品在生成时互相看见，并且一起朝用户偏好靠近。
