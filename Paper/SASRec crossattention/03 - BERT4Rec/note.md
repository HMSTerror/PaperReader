# BERT4Rec: Sequential Recommendation with Bidirectional Encoder Representations from Transformer

- 论文 PDF: [BERT4Rec -  Sequential Recommendation with Bidirectional Encoder Representations from Transformer.pdf](BERT4Rec -  Sequential Recommendation with Bidirectional Encoder Representations from Transformer.pdf)
- 下载来源: https://arxiv.org/pdf/1904.06690
- 年份/会议: CIKM 2019
- 方向: 序列推荐基础
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
BERT4Rec 将 BERT 的**双向 Transformer 编码 (bidirectional Transformer encoding)** 和**完形填空目标 (Cloze objective)** 引入序列推荐。论文认为，SASRec、GRU4Rec 等从左到右预测下一个物品的模型存在两类局限：一是隐藏表示只能利用左侧历史，表达能力受限；二是它们假定严格顺序，而真实用户行为中部分相邻物品未必具有刚性先后关系。BERT4Rec 随机 mask 序列中的物品，要求模型同时利用左右上下文恢复被 mask 物品。实验在 Beauty、Steam、ML-1M、ML-20M 四个数据集上表明，BERT4Rec 稳定超过 GRU4Rec、Caser、SASRec 等强基线。

## 背景
序列推荐需要从历史行为中学习动态偏好。传统 left-to-right 模型适合在线 next-item prediction，但在训练阶段没有充分利用序列内部全部上下文。自然语言处理中 BERT 证明了 bidirectional self-attention 与 masked language modeling 的有效性，本文的问题是：这种双向预训练思想是否能迁移到推荐行为序列。

**Research Questions**：1. 双向 self-attention 是否比单向序列模型学习到更强用户行为表示？2. Cloze 目标能否避免直接看见预测目标导致的信息泄漏？3. 在稀疏和稠密数据上，BERT4Rec 是否都能提升 top-N 推荐？

**Hypotheses**：论文隐含假设是：用户行为序列中一个物品的意义可由左右邻居共同决定；随机 mask 训练能产生更丰富的序列监督信号；双向编码学到的表示在推断最后一个 [MASK] 时可用于推荐下一个物品。

## 文献综述
作者首先讨论 FPMC、GRU4Rec、Caser、SASRec 等序列推荐方法，它们分别代表马尔可夫链、RNN、CNN 和单向 self-attention。作者指出这些方法共同特点是从左到右编码历史。随后，论文引用 BERT（Devlin et al., 2019）和 Transformer（Vaswani et al., 2017），说明深层双向注意力在文本理解中已证明有效。

文献过渡逻辑是：推荐序列虽然不是自然语言，但同样存在上下文依赖；如果只把历史压缩成单一状态，会损失行为序列中可互相解释的局部结构。因此，作者把 NLP 的 Cloze learning 转换成推荐中的 masked item prediction。

## 方法
**Participants**：无受试者；实验使用匿名用户-物品交互序列。

**Materials**：数据集统计包括 Beauty 40,226 用户、54,542 物品、约 0.35M 行为，Steam 281,428 用户、13,044 物品、约 3.5M 行为，ML-1M 与 ML-20M 两个 MovieLens 数据集。基线包括 PopRec、BPR-MF、FPMC、GRU4Rec、NARM、Caser、SASRec 等。

**Procedure**：训练时，BERT4Rec 随机选择序列中的一部分物品进行 mask，输入变为带 [MASK] 的行为序列。Transformer encoder 使用双向 self-attention，因此每个位置可注意到左右上下文。模型只在被 mask 的位置计算预测损失，从候选物品集合中恢复原物品。推断时，在用户序列末尾追加 [MASK]，用该位置输出预测下一个物品。

## 实验和结果
实验结果显示 BERT4Rec 在四个 benchmark 上整体优于单向模型，尤其在较稠密的 ML-1M/ML-20M 中双向上下文优势明显。论文还做了 mask 比例、层数、隐藏维度等分析，说明 Cloze 目标不是简单的数据增强，而是改变了序列表示学习方式。

与 SASRec 相比，BERT4Rec 的训练信号更多：一个序列中多个位置都可被 mask 并贡献监督，而 SASRec 主要按前缀预测后继。与 RNN/CNN 相比，BERT4Rec 通过 self-attention 缩短依赖路径，能更灵活地建模长距离行为关联。

## 讨论
BERT4Rec 的关键学术意义在于提出“推荐序列不一定只能左到右训练”。不过，这也带来适用边界：真实在线推荐只知道历史，不能知道未来；因此 BERT4Rec 必须通过 mask 机制避免训练泄漏，并在推断时把最后位置视为 [MASK]。这种设计使其更像表示学习模型，而非纯自回归模型。

对 cross-attention 研究而言，BERT4Rec 提醒我们：如果目标是推荐下一物品，信息流方向必须清楚。引入图像、文本或 target item cross-attention 时，也要避免让候选物品信息不当地泄漏到用户历史编码中。

## 结论
作者认为 BERT4Rec 通过深层双向 self-attention 和 Cloze objective 改善了用户行为序列建模。论文未单列局限性；从结论可见，其未来空间主要在于进一步利用更丰富的上下文或 side information，并探索更适合推荐的预训练目标。
