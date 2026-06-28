# Self-Attentive Sequential Recommendation

- 论文 PDF: [Self-Attentive Sequential Recommendation.pdf](Self-Attentive Sequential Recommendation.pdf)
- 说明: 本笔记复用 `SASRec crossattention/02 - SASRec` 中的论文精读内容，并补充 Beauty 数据集项目协议，确保项目基线目录与文献目录采用同一阅读模板。

## 摘要
本文提出 **SASRec (Self-Attentive Sequential Recommendation)**，是 Transformer 思想进入序列推荐的代表性工作。研究主题是如何在稀疏和稠密数据之间取得平衡：马尔可夫链 (Markov Chain, MC) 参数少、适合稀疏场景，但只能捕获短期转移；循环神经网络 (Recurrent Neural Network, RNN) 能表达长期依赖，但训练慢且在稀疏数据上容易过拟合。SASRec 使用**单向自注意力 (causal self-attention)** 从用户历史中自适应选择与当前预测相关的物品。实验表明，SASRec 在 Amazon Beauty、Amazon Games、Steam、MovieLens-1M 等数据集上超过 MC/CNN/RNN 类序列推荐模型，并且训练效率比可比 CNN/RNN 模型高一个数量级。

## 背景
序列推荐的核心是同时建模长期偏好和短期上下文。FPMC 之类模型把用户偏好和一阶转移结合起来，但高阶转移阶数需要预设；GRU4Rec 可以累计长历史，但难以并行且在稀疏场景中模型复杂度偏高。本文的重要性在于，它把 Transformer 中的 attention 改造为推荐中的可解释、可并行序列编码器。

论文明确列出四个研究问题：RQ1，SASRec 是否优于 CNN/RNN 等 state-of-the-art 模型；RQ2，架构组件分别有什么作用；RQ3，训练效率和序列长度扩展性如何；RQ4，注意力权重能否学习与位置或物品属性相关的有意义模式。

**Hypotheses**：作者未用 Hypotheses 标题表述，但逻辑上假设：自注意力可以在稀疏场景聚焦少数最近行为，在稠密场景利用更长历史；位置嵌入 (positional embedding) 与因果掩码 (causal mask) 对序列推荐必要；attention 权重能提供一定解释性。

## 文献综述
论文综述从 FPMC（Rendle et al., 2010）、Fossil、Caser、GRU4Rec 到 Transformer（Vaswani et al., 2017）展开。作者指出，MC 类方法强在稀疏数据，RNN 类方法强在复杂序列，但二者各有结构性限制。Caser 代表 CNN 高阶局部模式，GRU4Rec 代表循环状态压缩，FISM 则代表 item similarity 的非序列形式。

作者通过一个很有说服力的理论连接过渡到自身问题：SASRec 在特定退化设置下可近似 FMC、FPMC 或 FISM，因此它不是完全脱离推荐传统的黑盒模型，而是一个能自适应学习注意权重的层次化 item similarity 模型。这解释了为什么它在稀疏和稠密场景都合理。

## 方法
**Participants**：无人工受试者；实验对象是用户隐式反馈序列，交互由评论、评分或游戏行为转化而来。

**Materials**：数据集包括 Amazon Beauty、Amazon Games、Steam 和 MovieLens-1M。基线覆盖 POPRec、BPR-MF、FPMC/FMC、Fossil、Caser、GRU4Rec 等。评价采用 Hit Rate、NDCG 等 top-N 指标。

**Procedure**：SASRec 首先将物品 ID 与位置嵌入相加，得到序列输入；随后堆叠 self-attention block。每个 block 包含 scaled dot-product attention、因果 mask、point-wise feed-forward network、残差连接和归一化。预测第 t+1 个物品时，第 t 个位置只能注意到 1..t 的历史，避免未来泄漏。训练上采用正负样本二分类损失，对每个位置同时拉高真实下一个物品分数、压低采样负物品分数。

## 实验和结果
实验显示，SASRec 在四个稀疏度差异很大的数据集上整体优于既有序列模型。Amazon 数据集非常稀疏，Steam 与 MovieLens 更稠密；注意力可视化表明，稀疏数据中模型更像低阶 MC，倾向关注最近行为，而稠密数据中模型会分配更多权重到较长历史。

消融实验支持各组件的作用：位置嵌入用于区分相同物品在不同位置的含义；因果 mask 保证任务合法；多层 attention 和 feed-forward network 提升非线性表达。效率实验说明 self-attention 可并行处理序列，比逐步递推的 RNN 更适合 GPU。

## 讨论
论文最重要的学术贡献是把 sequential recommendation 从“固定阶数转移”推进到“可学习的历史选择”。它不是简单把 Transformer 搬过来，而是通过 causal attention、next-item objective 与推荐负采样，使模型契合推荐排序任务。

与 GRU4Rec 相比，SASRec 的优势在于并行和可解释注意权重；与 FPMC/Fossil 相比，优势在于无需预设转移阶数；与 Caser 相比，优势在于关注范围不受卷积窗口限制。对你的 cross-attention 工作而言，SASRec 是最直接 backbone：后续 ID/text/image 交互模块通常都要解释其相对 SASRec 的增益来自哪里。

## 结论
作者指出，SASRec 可以扩展到更长序列，但也提到可用 restricted self-attention 或把长序列切成短片段来进一步降低复杂度。论文还指出 Steam 中存在价格、类别、媒体评分等额外信息，未来可利用这些 side information，这为语义增强和多模态扩展留下空间。

## 项目补充

本项目的 Beauty 实验把 Amazon Beauty 用户行为视为隐式反馈序列，按照时间顺序构造训练、验证和测试样本，并使用 leave-last-out 协议评价下一物品预测。已有项目记录显示，SASRec 在 Beauty 协议下取得 NDCG@10 = 0.3219、Hit@10 = 0.4854；这些数值可作为后续扩散推荐、语义增强推荐或多模态推荐实验的非扩散序列推荐基线。由于该目录服务于项目实验复现，本节只补充项目侧协议，不改变论文原始结论。
