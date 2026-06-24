# Harnessing Multimodal Large Language Models for Multimodal Sequential Recommendation

- 论文 PDF: [Harnessing Multimodal Large Language Models for Multimodal Sequential Recommendation.pdf](Harnessing Multimodal Large Language Models for Multimodal Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2408.09698
- 年份/会议: AAAI 2025
- 方向: MLLM 多模态 SR
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
MLLM-MSR 探索如何让**多模态大语言模型 (Multimodal Large Language Model, MLLM)** 服务于多模态序列推荐。论文指出，已有 LLM 推荐多把用户行为转为文本 prompt，难以处理图像等多模态输入；而传统多模态推荐虽能融合图文，却缺少 MLLM 的语义理解和总结能力。MLLM-MSR 采用两阶段用户偏好总结：先用 MLLM 对物品图像和文本进行总结，再递归总结用户随时间演化的多模态偏好，并通过监督微调 (Supervised Fine-Tuning, SFT) 适配推荐任务。三个公开数据集实验验证其优于现有方法，并增强推荐可解释性。

## 背景
大语言模型在推荐中常用于 prompt-based ranking 或文本偏好理解，但多模态序列推荐需要处理“用户看过/买过的一系列图文物品”。直接把图像忽略为文本标题会丢失视觉偏好；直接让 MLLM 处理完整长序列又可能成本高、输出不稳定。MLLM-MSR 的研究空白是：如何组织多模态序列，使 MLLM 能理解动态偏好。

**Research Questions**：1. MLLM fine-tuning 是否能提升多模态序列推荐？2. 图像总结与递归用户偏好总结是否比直接推断更有效？3. MLLM 是否能带来推荐解释性？

**Hypotheses**：作者假设 MLLM 能把图像和文本统一为语义摘要；递归总结比一次性输入完整历史更能捕获兴趣演化；SFT 能把通用 MLLM 能力迁移到推荐任务。

## 文献综述
论文综述 LLM for recommendation、多模态推荐和 sequential recommendation。P5、GPT4Rec 等 LLM 推荐强调文本 prompt；MMSRec、MISSRec 等多模态 SR 强调表示学习；MLLM 研究则提供跨图文理解能力。作者指出，如何给 MLLM 注入多模态推荐能力仍未充分探索。

逻辑演进是：既有 LLM 推荐缺图像，既有多模态推荐缺大模型语义总结；MLLM-MSR 将二者结合，并通过 summarization 降低序列输入复杂度。

## 方法
**Participants**：无受试者；实验使用多模态推荐数据。

**Materials**：论文在三个公开数据集上验证，使用图像、文本和用户交互序列。基线包括传统 SR、多模态 SR 和 LLM-based 推荐方法。

**Procedure**：MLLM-MSR 首先对每个物品进行 multimodal summarization，把图像与文本转成统一 item summary。然后按时间顺序对用户历史进行 recurrent preference summarization，逐步更新用户偏好描述。最后，用 SFT 训练 MLLM 根据用户偏好和候选物品做推荐预测。

## 实验和结果
实验显示 MLLM-MSR 在三个数据集上优于 baseline，尤其在动态偏好捕获方面表现好。消融实验比较直接用户偏好推断和递归总结，主模型更优；去掉 image summarization 也会下降，说明图像信息对多模态偏好建模有贡献。

论文还强调可解释性：模型输出的用户偏好摘要可帮助理解推荐原因。这一点是传统 embedding 模型较难提供的。

## 讨论
MLLM-MSR 的贡献是把 MLLM 从通用图文理解工具变成推荐中的偏好总结器。它不是简单用 MLLM 排序候选，而是设计了 item summarization 与 recurrent user summarization 以适配 sequential setting。

对你的工作而言，MLLM-MSR 是高层语义方法。如果你的目标是轻量 cross-attention 模型，可以把 MLLM-MSR 作为“强语义但高成本”的对照，强调你的模型是否更高效、更易部署。

## 结论
作者总结 MLLM-MSR 能利用 MLLM 进行多模态序列推荐，并通过两阶段偏好总结提升准确性与解释性。论文未单列传统 limitation，但在引言和讨论中指出 MLLM fine-tuning 需避免过拟合、保持泛化，且多模态序列处理复杂度仍是挑战。
