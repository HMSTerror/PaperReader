# When Large Vision Language Models Meet Multimodal Sequential Recommendation: An Empirical Study

- 论文 PDF: [When Large Vision Language Models Meet Multimodal Sequential Recommendation -  An Empirical Study.pdf](When Large Vision Language Models Meet Multimodal Sequential Recommendation -  An Empirical Study.pdf)
- 下载来源: https://openreview.net/pdf?id=E8bjWloEvU
- 年份/会议: WWW 2025
- 方向: LVLM 多模态 SR
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
这篇论文提出 MSRBench，系统评估**大型视觉语言模型 (Large Vision-Language Models, LVLMs)** 接入多模态序列推荐的不同策略。作者认为，LVLM 在图文理解任务中很强，但其在推荐系统中应扮演什么角色并不清楚。论文设计五类策略：LVLM as recommender、item enhancer、reranker，以及 enhancer+recommender、enhancer+reranker 的组合；在 Amazon Review Plus 数据集上评估 GPT-4V、GPT-4o、Claude-3-Opus。主要发现是：LVLM 作为 reranker 最有效，GPT-4o 整体最好，但计算效率是实时部署的主要障碍。

## 背景
传统多模态 SR 多使用浅层图文特征对齐，可能难以捕获复杂跨模态关系。LVLM 具备强图文理解能力，看似适合推荐，但直接用 LVLM 生成推荐可能受 prompt、候选规模、成本和幻觉影响。该论文的重要性在于不提出单一模型，而是建立 benchmark，回答“LVLM 该如何接入推荐 pipeline”。

**Research Questions**：论文明确列出 RQ：RQ1，不同 LVLM 角色在 MSR 中表现如何；RQ2，item modalities 和 image input modes 如何影响性能；RQ3，LVLM 作为 reranker 是否能稳定增强传统序列模型；RQ4，哪种策略在计算效率和推荐准确率之间最平衡。

**Hypotheses**：作者隐含假设为：LVLM 的优势更适合候选重排和语义增强，而非直接从全量物品生成推荐；不同图像输入和文本描述会影响 LVLM 判断；高性能策略可能伴随高计算成本。

## 文献综述
论文综述多模态 sequential recommendation、LVLM 应用和 LLM-based recommendation。既有研究多探索单一接入方式，如把 LVLM 作为特征增强器或推荐器，缺少同一任务下多策略对比。作者还提到传统浅层对齐方法难以捕获图文复杂关系。

逻辑演进是：既然 LVLM 很强但很贵，就必须系统评估“放在 pipeline 哪个位置最划算”。这使 MSRBench 成为方法选择而非单模型宣传。

## 方法
**Participants**：无受试者；实验对象是 Amazon Review Plus 中的用户行为、物品图片、标题和增强描述。

**Materials**：模型包括 GPT-4V、GPT-4o、Claude-3-Opus。传统推荐基线包括 SASRec 和 MoRec。论文也尝试 Qwen-VL、GLM-4V 等开源 LVLM，但因 instruction following 差或幻觉严重而未纳入主实验。

**Procedure**：作者构造五种 LVLM integration strategies。S1 直接让 LVLM 推荐；S2 用 LVLM 增强 item 表示；S3 让 LVLM 对传统 SR 召回候选重排；S4/S5 组合增强与推荐或重排。为控制成本，实验限制用户历史长度和候选样本数，并使用固定 prompt 与 temperature=0。

## 实验和结果
结果显示，LVLM as reranker 最稳定有效，优于直接推荐或单纯 item enhancer。GPT-4o 在多数策略中表现最好，尤其作为 reranker。组合策略并不总是带来增益，有时比简单单策略更差，说明 LVLM 不是越多调用越好。

论文还发现计算效率是关键瓶颈。复杂策略需要更长 prompt 和更多图像/候选输入，延迟与成本难以满足实时工业推荐需求。这支持 RQ4：最佳实践要在效果和效率之间折中。

## 讨论
MSRBench 的贡献在于提供实证指导：LVLM 更适合对小候选集做高语义重排，而不是替代传统推荐系统完成全流程召回。它也说明开源 LVLM 在当时可能存在输出解析和幻觉问题，不能默认可用。

对你的工作而言，这篇论文提供了定位：轻量 SASRec cross-attention 可作为 LVLM reranker 之前的召回/排序模型，也可吸收 LVLM 生成的 item captions。但如果你声称用 LVLM 端到端推荐，必须面对成本和效率问题。

## 结论
作者总结 MSRBench 揭示了 LVLM 接入 MSR 的性能差异。论文在 Limitations and Future Work 中明确指出：由于资源限制，未探索 fine-tuning LVLM；未来将研究 fine-tuning 影响，并扩展数据集多样性。
