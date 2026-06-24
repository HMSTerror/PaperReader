# Towards Universal Sequence Representation Learning for Recommender Systems

- 论文 PDF: [Towards Universal Sequence Representation Learning for Recommender Systems.pdf](Towards Universal Sequence Representation Learning for Recommender Systems.pdf)
- 下载来源: https://arxiv.org/pdf/2206.05941
- 年份/会议: KDD 2022
- 方向: 语义增强 SR
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
UniSRec 研究如何学习**通用序列表征 (universal sequence representation)**，使推荐模型能够跨领域、跨平台迁移。传统序列推荐依赖物品 ID embedding，但 ID 只在单一平台内部有意义，新领域或新平台中的物品 ID 与旧领域不共享，导致迁移困难。UniSRec 用物品描述文本构造可迁移 item representation，并设计**参数化白化 (parametric whitening)**、**混合专家增强适配器 (MoE-enhanced adaptor)** 与对比式预训练任务。实验表明，UniSRec 在常规推荐、冷启动、少样本和跨平台设置中都优于 ID-based 方法，显示文本语义可以作为跨域序列推荐的桥梁。

## 背景
SASRec/BERT4Rec 等模型在同一数据集内效果强，但它们学到的是数据集特定 ID embedding。真实业务常面临新类目、新平台或新物品，ID embedding 无法直接复用。自然语言描述则具有跨域共享性，例如书籍、电影、食品都可以用文本表达属性。

**Research Questions**：1. 仅依赖物品文本能否学习可迁移的序列表示？2. 多领域预训练是否能提升目标领域推荐？3. 如何缓解预训练语言模型 embedding 的分布问题与领域差异？

**Hypotheses**：作者假设 item text 中包含足以跨域迁移的语义信号；白化能改善文本 embedding 的各向异性 (anisotropy)；MoE adaptor 能吸收不同领域的语义偏差；对比学习能把不同领域序列映射到统一兴趣空间。

## 文献综述
论文回顾了 ID-based sequential recommendation，如 GRU4Rec、SASRec、BERT4Rec，它们善于同域建模但迁移性弱。随后讨论 feature-based 和 text-enhanced recommendation，指出简单把文本 embedding 拼到 ID embedding 上并不能解决跨域 ID 不共享问题。

作者还引入预训练语言模型和对比学习文献。逻辑演进是：既然文本天然跨域，关键就不是“能不能用文本”，而是“如何把文本编码成适合推荐序列的统一表示”。因此，UniSRec 把问题从 item ID 学习转为 universal item/sequence representation learning。

## 方法
**Participants**：无人工受试者；实验使用多领域用户行为序列。

**Materials**：论文使用多个 Amazon 类目和跨平台数据，覆盖源域预训练、目标域迁移和常规推荐。基线包括传统 ID-based 序列模型、文本增强模型和无预训练变体。

**Procedure**：UniSRec 先用预训练语言模型编码物品描述，再通过 parametric whitening 改善 embedding 分布，使其更接近各向同性。随后，MoE-enhanced adaptor 根据领域差异自适应组合多个专家表示。序列编码器学习用户行为序列，并通过两类 contrastive pre-training tasks 拉近语义相似或行为相关序列，提升跨域泛化。目标域可进行 fine-tuning，也可用于少样本/零样本设置。

## 实验和结果
实验显示，多领域预训练优于单领域预训练和无预训练，说明 universal sequence representation 能捕获可迁移的语义行为模式。消融研究表明，去掉 parametric whitening、MoE adaptor 或对比学习都会降低性能，支持各模块必要性。

论文特别强调 cross-platform setting 中的改进，这对推荐系统很重要：模型不是只在同一 catalog 上记住 ID，而是能把“用户喜欢某类语义物品”的规律迁移到新平台。

## 讨论
UniSRec 的价值在于把 sequential recommendation 从封闭 ID 系统推向开放语义系统。它并不否认 ID embedding 的强拟合能力，而是指出 ID 的强项也是迁移的弱点。对你的 SASRec cross-attention 工作来说，UniSRec 是语义增强方向的基础对照：如果引入文本/图像，必须说明这些模态是用于跨域、冷启动，还是仅用于同域增益。

与 Recformer、WhitenRec、AlphaFuse 等后续工作相比，UniSRec 更关注可迁移框架和预训练范式，而不是完全替代 ID 或在 ID/语义之间做正交互补。

## 结论
作者在结论中明确提出未来工作：收集更多推荐数据以训练更大的用户行为模型，并探索更多 side information，例如图像，用于改进物品表示和序列表征学习。
