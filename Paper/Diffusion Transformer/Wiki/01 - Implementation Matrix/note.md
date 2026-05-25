# Diffusion Transformer 推荐系统 Wiki：论文实现速查表

_用一张表看懂每篇文章“输入什么、处理什么、输出什么”。更新时间：2026-05-25。_

---

## 怎么看这张表

对科研新手来说，读扩散推荐论文最容易迷路的地方是：论文都叫 diffusion，但扩散对象完全不同。下面的“扩散对象”就是训练时被加噪、推理时被逐步还原的核心变量。

| 论文 | 年份 | 任务 | 主输入 | 扩散对象 | 条件信息 | 去噪/主干 | 输出 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DiT | 2022/2023 | 图像生成基础架构 | 图像 latent patch、timestep、类别条件 | 图像 latent | 类别标签或条件 token | Transformer block + adaLN | 还原图像 latent |
| CODIGEM | 2022 | 协同过滤 | 用户-物品交互数据 | 协同过滤 latent 或交互表示 | 协同信号 | DDPM 式生成模型 | 推荐分数或 latent 表示 |
| DiffRec | 2023 | 通用推荐 | 用户交互向量 | 用户-物品交互向量 | 用户历史交互 | MLP/AutoEncoder diffusion | 全量 item 分数 |
| DiffuRec | 2023 | 序列推荐 | 用户历史 item 序列 | 目标 item embedding | 历史序列表示 | Approximator + diffusion | 目标 item 表示，再映射 item |
| DreamRec | 2023 | 序列推荐 | 历史 item 序列 | oracle item embedding | Transformer encoder 产生的 guidance | Guided diffusion | 个性化 oracle item |
| DiffGT | 2024 | Top-K 图推荐 | 用户-物品交互图 | 用户/item 图表示 | 已交互物品等个性化信息 | Graph Transformer + linear attention | 用户偏好表示与 Top-K 推荐 |
| EDGE-Rec | 2024 | 图推荐/评分预测 | 加权用户-物品交互矩阵、用户特征、物品特征 | 加权交互矩阵 | 用户和物品特征 | GDiT + RCSA attention | 评分或交互预测 |
| DCRec/DCDT | 2024 | 序列推荐 | 历史序列 + 目标 item | 历史和目标拼接后的连续表示 | 隐式条件 + 显式干净历史 | Dual Conditional Diffusion Transformer | 目标 item 或目标 embedding |
| iDreamRec | 2024 | 文本引导序列推荐 | 历史序列、物品文本、意图文本 | 目标 item text embedding | 文本描述与 intention instruction | Diffusion Transformer block | 语义可控的目标 item |
| Prompt-to-Slate | 2024/2025 | slate/list 生成 | 自然语言 prompt | 整个 slate 的联合表示 | prompt 文本 | Diffusion Model for Slate Generation | 歌单、商品 bundle 等 slate |
| CATDiT | 2025 | 序列推荐数据增强 | 历史序列条件 token | 连续增强样本 | condition-tokenized 历史条件 | Diffusion Transformer | 训练用增强样本 |
| ICDDT | 2025 | 多行为 next-item 预测 | 多行为历史序列、目标 item 信息 | 分布式 item 表示 | target item-oriented 条件 | Conditional Diffusion Differential Transformer | next item 预测 |
| LPDO | 2025 | 用户行为轨迹预测 | 用户历史行为 | 未来行为轨迹 | listwise 偏好监督 | Diffusion + Plackett-Luce 优化 | 多步未来 item 序列 |
| PaDiRec | 2024 | 多任务可控推荐 | 任务需求、控制条件 | 推荐模型参数 | 任务控制信号 | Parameter diffusion | 适配任务的模型参数 |
| ContRec | 2025 | LLM 推荐/连续 token | 用户/item 连续 token、LLM 上下文 | continuous token | LLM 已生成 token 与用户上下文 | Dispersive Diffusion | Top-K 检索用连续表示 |
| CDRec | 2025/2026 | 离散扩散推荐 | 历史交互 item 序列 | 离散 item 状态 | popularity schedule、多跳协同信号 | 连续时间离散扩散 | 推荐 item |
| DualFashion | 2026 | 生成式时尚推荐 | 历史行为、图像、属性级文本 | 图像分支和文本分支表示 | 图像条件、结构化 caption | Dual-diffusion Transformer | 商品图像 + 文本描述 |

## 按实现路线分类

| 路线 | 代表论文 | 适合借鉴什么 |
| --- | --- | --- |
| 连续 target latent 去噪 | DreamRec, DCRec, iDreamRec, RDT 项目 | 最适合你当前项目，目标是生成下一件物品的 latent。 |
| 图/矩阵去噪 | DiffGT, EDGE-Rec, DiffRec | 适合研究交互图噪声、协同过滤和全量 item ranking。 |
| 离散 item 扩散 | CDRec, ICDDT | 适合避免连续 embedding 到离散 item 的映射损失。 |
| 多模态条件生成 | iDreamRec, DualFashion, Prompt-to-Slate | 适合加入文本、图像、prompt 或解释性输出。 |
| 轨迹/list 级优化 | LPDO, Prompt-to-Slate | 适合不只推荐下一个 item，而是一次生成列表或未来行为路径。 |
| 参数级扩散 | PaDiRec | 适合动态任务控制，不是直接生成 item。 |

## 和 RDT 最接近的论文

| 优先级 | 论文 | 原因 |
| --- | --- | --- |
| 最高 | DCRec/DCDT | 同样关注“历史条件如何参与扩散去噪”，而且明确使用 Diffusion Transformer。 |
| 最高 | iDreamRec | 与 RDT 的文本条件、目标 latent 生成最贴近。 |
| 高 | ContRec | 连续 token/latent 思路和 RDT 的 continuous target latent 很近。 |
| 高 | CATDiT | 适合思考“把条件 token 化后喂给 DiT”。 |
| 中高 | LPDO | 如果 RDT 未来从 next-item 扩展到多步轨迹预测，这篇很重要。 |
| 中 | DiffGT, EDGE-Rec | 对图结构建模有启发，但和 RDT 当前代码路线不是同一主干。 |

## 参考入口

主要论文来源见“新手总览”的“核心来源”表。优先打开 arXiv、NeurIPS、DBLP、CIKM proceedings 和 Spotify Research 等原始或准原始页面。
