# Leveraging Multimodal Large Language Model for Multimodal Sequential Recommendation

- 论文 PDF: [Leveraging Multimodal Large Language Model for Multimodal Sequential Recommendation.pdf](Leveraging Multimodal Large Language Model for Multimodal Sequential Recommendation.pdf)
- 下载来源: https://www.nature.com/articles/s41598-025-14251-1.pdf
- 年份/会议: Scientific Reports 2025
- 方向: MLLM 多模态 SR
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
MLLM-SRec 是 2025 年 Scientific Reports 论文，系统探索**多模态大语言模型 (Multimodal Large Language Model, MLLM)** 在多模态序列推荐中的推理和微调机制。论文指出，现有 LLM/MLLM 推荐方法在多模态特征识别和动态偏好建模上仍不足，常依赖单模态交互信息，未充分利用图文差异和用户兴趣演化。MLLM-SRec 设计多模态 item fusion、temporal-aware user behavior comprehension，并结合 supervised fine-tuning 与多步 Chain-of-Thought prompting 优化。四个 Amazon benchmark 数据集实验显示，该方法显著优于传统 SR 和 LLM-based baseline，同时分析了幻觉对推荐性能的影响。

## 背景
推荐系统正在从 ID-based 表示学习走向生成式和大模型范式。MLLM 能理解图像和文本，但推荐任务要求处理用户历史、候选物品、时间顺序和个性化偏好。直接把多模态信息塞进 prompt 可能导致长上下文、噪声和幻觉。MLLM-SRec 的研究目标是把 MLLM 的图文理解能力迁移到 sequential recommendation，同时显式建模动态偏好。

**Research Questions**：论文列出四个 RQ：RQ1，MLLM-SRec 是否优于 SOTA LLM-based recommendation；RQ2，不同模态及其组合是否更准确捕获动态偏好；RQ3，各组件对效果有何影响；RQ4，不同 fine-tuning 策略配置如何影响性能。

**Hypotheses**：作者假设 MLLM 可生成统一多模态 item semantics；temporal-aware module 能捕获用户兴趣演化；SFT 与 multi-step CoT prompting 能把预训练多模态知识迁移到推荐任务；幻觉会损害推荐，需要被分析和抑制。

## 文献综述
论文综述 LLM for recommendation、多模态推荐和 sequential recommendation。P5、GPT4Rec、VIP5 等工作代表 LLM 推荐；UniSRec、GRU4Rec、SASRec 等代表语义或序列推荐基础；MLLM 研究提供图文联合理解。作者指出，已有方法未充分探索 cross-modal preference differences 和动态多模态行为序列。

文献演进逻辑是：LLM 提供语言推理，多模态推荐提供图文特征，序列推荐提供时间结构；MLLM-SRec 试图把三者统一到一个可微调的推荐框架中。

## 方法
**Participants**：无受试者；实验使用 Amazon Review 类目中的用户历史行为和物品图文信息。

**Materials**：论文选取 baby、sports、beauty、toys 四个 Amazon 类目。模型使用 MLLM/LLM backbone、物品图片、文本描述、用户 profile 与候选 item 信息。评价与 baseline 包括传统 SR、LLM-based recommendation 和多模态方法。

**Procedure**：MLLM-SRec 首先通过 visual information understanding 生成视觉摘要，再把视觉摘要与文本结合生成 multimodal item summary。随后使用滑动窗口构造动态用户行为序列，temporal-aware module 总结用户兴趣演化。最终模型联合用户 profile、动态偏好和目标物品多模态信息，通过 SFT 和 multi-step CoT prompt 学习点击/推荐预测。

## 实验和结果
实验显示 MLLM-SRec 在四个 Amazon benchmark 上显著优于 baseline，并在鲁棒性和多模态适应性上表现较好。消融研究围绕四个 RQ 展开，验证不同模态组合、temporal-aware 模块和 fine-tuning 配置的重要性。

论文还分析幻觉对推荐性能的影响，指出多模态异常输入可能诱发错误理解，进而降低推荐准确率。这一点比单纯报告 accuracy 更深入，因为 MLLM 推荐的风险不仅是排序误差，也包括生成式模型的不可靠解释。

## 讨论
MLLM-SRec 的贡献在于提出更完整的 MLLM-based MSR pipeline：先做 item-level 图文融合，再做 temporal user behavior comprehension，最后进行推荐任务微调。它比 MLLM-MSR 更强调 CoT prompting、幻觉分析和 fine-tuning 策略。

对你的工作而言，MLLM-SRec 代表高成本大模型路线。若你的方法是轻量 cross-attention，可以从它那里借鉴两个思想：一是先把图像和文本转为统一语义表示；二是动态兴趣建模必须保留时间窗口，而不能只做静态用户画像。

## 结论
作者在 Conclusion and future work 中明确提出未来方向：系统研究 MLLM-based RS 中 inference latency 与 computational cost 的权衡；开发 end-to-end joint training framework，结合更强 MLLM、更大参数容量、优化 prompt engineering 和扩展机制。论文也承认大模型推荐仍需处理成本、幻觉和动态多模态数据利用不足的问题。
