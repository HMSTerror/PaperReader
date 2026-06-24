# IISAN: Efficiently Adapting Multimodal Representation for Sequential Recommendation with Decoupled PEFT

- 论文 PDF: [IISAN -  Efficiently Adapting Multimodal Representation for Sequential Recommendation with Decoupled PEFT.pdf](IISAN -  Efficiently Adapting Multimodal Representation for Sequential Recommendation with Decoupled PEFT.pdf)
- 下载来源: https://arxiv.org/pdf/2404.02059
- 年份/会议: SIGIR 2024
- 方向: 多模态序列推荐
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
IISAN 研究如何高效适配大规模多模态基础模型到序列推荐。现有参数高效微调 (Parameter-Efficient Fine-Tuning, PEFT) 如 LoRA/Adapter 虽冻结大模型参数，但反向传播仍需穿过大模型计算图，训练时间和显存开销高。IISAN 提出**解耦 PEFT (Decoupled PEFT, DPEFT)**：冻结多模态 backbone，并将可训练的 side adapted networks 与 backbone 解耦，使训练时可缓存 backbone 输出，显著降低计算图开销。模型还设计 intra-modal 与 inter-modal SAN 来适配推荐任务。三个多模态推荐数据集实验显示，IISAN 在性能接近 full fine-tuning 或先进 PEFT 的同时显著提升 GPU memory 和训练时间效率。

## 背景
多模态推荐越来越依赖 CLIP 等 foundation models，但直接 full fine-tuning 成本高；传统 PEFT 虽减少可训练参数，却未必减少激活存储和反向传播成本。推荐系统需要处理大规模物品和用户序列，因此效率不是附属指标，而是能否部署的核心。

**Research Questions**：1. 能否在不显著损失推荐性能的情况下降低多模态 backbone 适配成本？2. DPEFT 是否比 LoRA/Adapter 更符合推荐任务的实际效率需求？3. intra-modal 与 inter-modal adaptation 如何共同作用？

**Hypotheses**：作者假设 foundation model 的通用多模态表示可冻结复用；推荐任务适配可由轻量 side networks 完成；解耦结构允许缓存 backbone 表示，从而减少训练时间和显存。

## 文献综述
论文综述了多模态推荐、foundation model adaptation 和 PEFT。LoRA、Adapter 等 EPEFT 方法减少参数更新，但仍参与大模型前向/反向图。NLP/CV 中出现的 decoupled PEFT 启发作者将其引入推荐。推荐领域已有 M6-Rec、TallRec 等 PEFT 尝试，但多数关注单模态或忽视实践效率。

文献过渡是：多模态 SR 需要 foundation model 表示，但推荐规模要求更高效率；因此必须评价“参数量、时间、显存”三者平衡，而非只看 accuracy。

## 方法
**Participants**：无受试者；实验使用多模态推荐数据。

**Materials**：论文在三个常用多模态推荐数据集上评估，并与 full fine-tuning、LoRA、Adapter 等方法比较。还提出 TPME 等平衡效率指标。

**Procedure**：IISAN 冻结多模态 backbone，离线或缓存其 item representations。训练阶段只更新 side adapted networks。intra-modal SAN 适配每个模态内部表示，inter-modal SAN 学习模态之间的交互。由于 backbone 不参与反向传播，训练时省去大模型 backward pass 和大部分激活存储。

## 实验和结果
实验验证 IISAN 在三个推荐数据集上取得与 full fine-tuning 和先进 PEFT 相当的推荐效果，同时在 GPU memory、training time 和综合 TPME 指标上更优。理论复杂度分析也说明，DPEFT 的训练迭代成本低于常规 PEFT。

消融实验支持 intra-modal 和 inter-modal SAN 的作用：只做单模态适配会损失跨模态互补，只做融合又可能忽略各模态内部偏差。

## 讨论
IISAN 的价值是把多模态推荐从“能不能用大模型”推进到“能不能高效适配大模型”。对 MLLM/LVLM 推荐尤其重要，因为直接在线调用或全量微调成本可能不可接受。

对你的工作而言，IISAN 提醒 cross-attention 模型需要考虑计算成本。如果 cross-attention 发生在长历史、多候选、多模态之间，推断复杂度可能成为主要瓶颈。可以考虑缓存 item modality features 或采用 decoupled adaptation。

## 结论
作者总结 IISAN 通过 DPEFT、intra/inter-modal SAN 和缓存策略，在效率与效果之间取得平衡。论文明确提出未来工作：将 IISAN 范式扩展到 multimodal retrieval、visual question answering 等更多应用，并探索更多可扩展适配方式。
