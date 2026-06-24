# MISSRec: Pre-training and Transferring Multi-modal Interest-aware Sequence Representation for Recommendation

- 论文 PDF: [MISSRec -  Pre-training and Transferring Multi-modal Interest-aware Sequence Representation for Recommendation.pdf](MISSRec -  Pre-training and Transferring Multi-modal Interest-aware Sequence Representation for Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2308.11175
- 年份/会议: ACM MM 2023
- 方向: Cross-attention 多模态 SR
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
MISSRec 提出 **Multi-modal Interest-aware Sequence Representation** 的预训练与迁移框架，目标是利用多模态信息解决 ID-heavy sequential recommendation 的冷启动和跨域适配问题。模型包含冻结的文本/图像编码器、模态适配器、Transformer contextual encoder、interest-aware decoder 和轻量动态融合模块。论文通过大规模源域预训练学习多模态兴趣表示，再迁移到目标域。实验覆盖 inductive transfer、缺失模态、跨域适配等设置，显示 MISSRec 具备较强泛化和鲁棒性。

## 背景
ID-based 序列模型在训练域内强，但对冷物品和新域无泛化能力。多模态内容可缓解该问题，但直接使用图像/文本 embedding 存在语义 gap、模态缺失和兴趣粒度不足。MISSRec 的动机是预训练一个能理解多模态兴趣的序列表示模型，而不是为每个目标域从头训练。

**Research Questions**：1. 多模态预训练能否提升目标域序列推荐？2. interest-aware decoder 是否能更好表达用户多兴趣？3. 模态适配器和动态融合能否处理缺失或不完整模态？

**Hypotheses**：作者假设多模态 item content 中包含可迁移兴趣信号；contextual encoder 可学习序列上下文；interest-aware decoder 可捕获多个潜在兴趣；动态融合能根据模态可用性调整表示。

## 文献综述
论文综述序列推荐、用户兴趣建模、多模态推荐和预训练迁移。GRU4Rec/SASRec/BERT4Rec 代表 ID-based SR；MMSRec、UniSRec 等工作探索内容或语义迁移；CLIP/BERT 等预训练模型提供 frozen modality encoders。作者指出，已有方法要么缺少跨域预训练，要么没有针对兴趣感知解码。

逻辑演进是：多模态信息有助于冷启动，但只有结合 sequence representation pre-training 和 interest-aware transfer，才能在新域有效使用。

## 方法
**Participants**：无受试者；实验使用 Amazon 多领域用户行为数据及物品图文信息。

**Materials**：预训练数据包含 Food、CDs、Kindle、Movies、Home 等源域，目标域包括 Scientific、Pantry、Instruments、Arts、Office 等。表格显示预训练集规模超过百万用户和数十万物品，目标域规模较小且图像覆盖率不同。

**Procedure**：MISSRec 首先用冻结文本/图像编码器抽取模态特征，再用 modality-specific adapters 映射到推荐空间。Transformer contextual encoder 编码用户序列，interest-aware decoder 生成多兴趣表示。轻量 dynamic fusion module 根据可用模态融合信息。训练包含序列-序列对比、正交正则和推荐目标，用于预训练与目标域迁移。

## 实验和结果
实验显示，MISSRec 在 inductive transfer 和目标域推荐中优于现有方法。对于冷物品，ID-based 模型无法学习有效 embedding，而 MISSRec 可依赖图文特征生成表示。缺失模态实验说明其动态融合具有实际鲁棒性。

消融研究显示，去掉 modality adapters、只用 encoder 或 decoder、去掉关键对比/正则目标都会降低性能。尤其是 modality adapters 对弥合 frozen encoder 与推荐空间之间的 gap 很重要。

## 讨论
MISSRec 的学术意义是把多模态序列推荐推进到“预训练-迁移”范式。它与 MIN/ODMT 这类同域融合方法不同，更强调 cold-start 和 domain adaptation。

对 cross-attention 工作而言，MISSRec 中 interest-aware decoder 和多模态兴趣表示非常相关。若你的模型关注候选 item 与用户历史 cross-attention，可以将 MISSRec 作为多模态兴趣预训练 baseline，并强调是否需要预训练、是否支持缺失模态、是否改善迁移。

## 结论
作者总结，MISSRec 通过 contextual encoder、interest-aware decoder、dynamic fusion 和多模态预训练，有效缓解 ID-based SR 的冷启动与迁移限制。结论中还强调其对缺失模态的鲁棒性，并指出利用多模态信息进行序列推荐预训练是有前景的未来方向。
