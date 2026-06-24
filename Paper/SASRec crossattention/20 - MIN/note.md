# Multimodal Interactive Network for Sequential Recommendation

- 论文 PDF: [Multimodal Interactive Network for Sequential Recommendation.pdf](Multimodal Interactive Network for Sequential Recommendation.pdf)
- 下载来源: https://jcst.ict.ac.cn/en/article/pdf/preview/10.1007/s11390-022-1152-7.pdf
- 年份/会议: JCST 2023
- 方向: Cross-attention 多模态 SR
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
MIN，即 **Multimodal Interactive Network for Sequential Recommendation**，是多模态序列推荐中显式建模视觉-文本交互的重要工作。论文指出，文本或视觉信息可缓解数据稀疏，但多模态异质性使序列场景下的模态交互更复杂。MIN 同时从**物品级交互 (item-level interaction)** 和**序列级交互 (sequence-level interaction)** 利用文本与图像信息，并设计两个自监督任务，通过最大化 item representation 与 visual/textual representation 的互信息来增强表示。四个真实数据集实验显示 MIN 稳定优于序列推荐和多媒体推荐 baseline。

## 背景
传统序列推荐重在 item ID 的时间转移，多媒体推荐重在视觉/文本内容，但二者结合并不容易。若只在物品层融合模态，可能忽略用户兴趣随序列演化；若只在序列层融合，可能忽略单个物品内部图文关系。MIN 的研究空白是同时建模这两个层次。

**Research Questions**：1. 多模态信息如何在 item-level 和 sequence-level 同时帮助 sequential recommendation？2. 视觉与文本之间的交互是否比简单拼接更有效？3. 自监督互信息任务是否能增强多模态表示？

**Hypotheses**：作者假设用户购买决策同时受物品图像、文本描述和历史序列影响；模态间交互具有层次结构；通过互信息最大化可提升物品表示与单模态表示之间的一致性。

## 文献综述
论文综述 sequential recommendation、multimedia recommendation 和 self-supervised learning。GRU4Rec/SASRec 等序列模型强调历史行为，却不充分利用内容；VBPR/MV-RNN 等多媒体推荐使用图像或文本，但对序列结构建模不足。作者指出，多模态交互在序列场景下还没有被系统研究。

文献演进逻辑是：数据稀疏需要内容模态，序列推荐需要时间依赖，多模态推荐需要处理异质性。因此 MIN 同时引入 item-level 和 sequence-level interactions。

## 方法
**Participants**：无受试者；实验使用多模态用户交互序列。

**Materials**：论文在四个真实世界数据集上评估，包含图像和文本信息。基线包括传统序列推荐、单模态/多模态推荐以及 LSTM 变体。

**Procedure**：MIN 首先为每个物品构造 ID、视觉、文本表示，在 item level 学习模态间交互；随后在 sequence level 通过序列模型捕获用户历史中的多模态偏好演化。论文比较 Parallel-LSTM 与 Mixed-LSTM，发现混合式序列建模更能捕获 sequential multimodal features。自监督任务通过最大化 item representation 与 visual/textual representation 的互信息，使融合表示保留模态特征。

## 实验和结果
实验显示 MIN 在四个数据集上显著优于 baseline。变体分析中，Mixed-LSTM 优于 Parallel-LSTM；self-attention 对复杂交互建模有效；最终偏好表示使用 concatenation 获得最佳性能。在 Clothing, Shoes & Jewelry 数据集上，MIN 的 Hit-Ratio@20 和 NDCG@20 高于 MIN-dot、MIN-add 和 LSTM 变体。

结果说明，简单点积或加法不足以表达多模态序列关系，层次化交互和自监督对齐共同贡献性能。

## 讨论
MIN 对你的工作非常关键，因为它已经提出 visual-textual interaction 和 multimodal sequential recommendation 的组合。它的不足是使用的 backbone 与大模型语义表示相对早期，且 cross-attention/Transformer 范式不如后续方法系统。

如果你的方法使用 SASRec backbone 和 cross-attention，可以把 MIN 作为“早期显式多模态交互”的 related work，并说明你的区别在于更现代的 self-attention backbone、候选级 cross-attention 或 ID-语义互补机制。

## 结论
作者总结，MIN 通过 item-level 与 sequence-level 多模态交互、自监督互信息任务提升了序列推荐性能。论文未来方向未集中单列；从讨论可见，可进一步探索更强图神经网络、self-supervised learning 和更复杂模态关系建模。
