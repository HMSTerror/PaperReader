# DiffCDR: Diffusion Cross-domain Recommendation

- 论文 PDF: [Diffusion Cross-domain Recommendation.pdf](Diffusion Cross-domain Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2402.02182
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

DiffCDR 研究跨域推荐中的冷启动用户问题。目标域用户交互很少时，推荐系统难以学习其偏好；辅助域数据可以提供补充信息，但关键是如何把辅助域的用户表示迁移到目标域。传统 mapping-based CDR 方法依赖一个映射模块，把源域 embedding 变换到目标域 embedding，但映射质量直接决定推荐效果。

作者观察到，diffusion probabilistic model 本质上也是一种强大的数据转换过程：从带噪样本逐步恢复目标数据。因此论文尝试用扩散模型替代或增强 CDR 中的 mapping module。

## 提出了什么方法

DiffCDR 包含 Diffusion Module（DIM）、Alignment Module（ALM）和 task-oriented loss。DIM 学习在重叠用户上进行跨域迁移：训练时让目标域用户 embedding 加噪，再在源域 latent vector 的条件下反向去噪，生成目标域表示。对冷启动用户，模型用其辅助域信息作为 guidance 生成目标域 embedding。

由于扩散过程有随机性，ALM 进一步对 DIM 输出做对齐，降低随机性带来的不稳定。task-oriented loss 使用目标域标签数据，让生成表示不仅像目标域 embedding，还能提升具体推荐任务表现。

## 实验效果如何

实验基于 Amazon review 数据构造多个跨域任务，评估 cold-start 和 warm-start CDR。冷启动 Table 2 中，DiffCDR 在 Video -> Music、Book -> Video 等任务上多数指标超过 TGT、CMF、EMCDR、SSCDR、LACDR、PTUPCDR。例如 Video -> Music 在 beta=20% 时 MAE 从最佳基线 1.1099 降到 1.0435，NDCG@20 从 0.00984 提升到 0.01026。

论文也发现，不同任务难度不同，某些 RMSE 或 NDCG 指标上提升很小甚至接近基线，但总体结果显示 DiffCDR 在冷启动和暖启动场景下都有效。消融实验表明 DIM、ALM、task loss 都对性能有关键贡献。

## 用最简单的话解释原理

跨域推荐像是把一个人在“视频域”的兴趣翻译成“音乐域”的兴趣。传统方法用一个普通翻译器做映射，DiffCDR 用扩散模型做更细的翻译：先把目标域表示看成被噪声遮住的结果，再根据源域信息一步步还原。

ALM 像校对器，负责把扩散生成的表示再对齐到目标域；task loss 像最终考试，确保翻译出来的表示真的能提升推荐，而不是只在向量空间看起来合理。
