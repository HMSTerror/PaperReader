# CG4CTR: A New Creative Generation Pipeline for Click-Through Rate with Stable Diffusion Model

- 论文 PDF: [A New Creative Generation Pipeline for Click-Through Rate with Stable Diffusion Model.pdf](A New Creative Generation Pipeline for Click-Through Rate with Stable Diffusion Model.pdf)
- 下载来源: https://arxiv.org/pdf/2401.10934
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

CG4CTR 面向在线广告创意生成。广告主通常需要为同一商品制作多张 creative，以找到 CTR 更高的展示图。但人工制作成本高、数量有限，也难以针对不同用户偏好定制。传统 AI 生成方法虽然能生成图像，但生成阶段通常不考虑 CTR 目标；生成后再用 ranking model 挑选，导致生成和排序被分成两个独立任务。

这种两阶段分离会带来问题：如果生成阶段产出很多 CTR 低的图，后续排序也只能在差候选里挑好一点的，线上曝光会被低质量创意稀释。论文希望把 CTR 优化前移到 creative generation 阶段。

## 提出了什么方法

CG4CTR 是一个基于 Stable Diffusion inpainting 的自动创意生成流水线。它使用 LoRA 让 Stable Diffusion 适配广告创意风格；使用 prompt model 生成更适合商品和用户的 prompt；使用 reward model 预测创意的 CTR uplift，从候选图中筛出更可能提升 CTR 的创意。

核心是 self-cycling training。每轮生成后，reward model 选出表现更好的创意作为正样本，其余作为负样本，反过来训练 prompt model 和 LoRA，使下一轮生成更贴近高 CTR 目标。最终每个 item 生成 top 5 creatives，并在线上用 epsilon-greedy 展示策略探索。

## 实验效果如何

线上实验显示 self-cycling 很关键。Table 1 中，不使用 self-cycling 时整体 CTR/Revenue 只提升 4.21%/3.82%；中间版本提升到 8.1%/7.2%；完整方法达到 10.4%/9.7%。分品类看，Women Shoes、Women Bags、Travel、Beauty、Mobile 等都有提升，Mobile 达到 14.2%/14.5%。

Reward model 消融 Table 2 显示，完整模型在 commercial data 上 Top-1 CTR uplift 为 23.81%，优于 VAM、Rank、只用 image、image+title、无预训练、单一 loss 等变体；public data 上 Top-1 为 11.29%。Prompt model 消融显示用户信息很重要：去掉 user 后 CTR/Revenue 提升低于完整 individuated 模型。

## 用最简单的话解释原理

普通流程是先生成很多广告图，再挑可能点击率高的；CG4CTR 则让生成器一开始就朝“更高 CTR”学习。reward model 像评委，prompt model 像文案策划，LoRA 像画师的风格适配器。

每一轮系统都会生成、打分、筛选、再学习。好的创意变成下一轮的训练信号，所以生成器逐渐知道什么样的图更容易被用户点击。
