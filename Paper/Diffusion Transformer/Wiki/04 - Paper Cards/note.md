# Diffusion Transformer 推荐系统 Wiki：逐篇阅读卡片

_每篇文章用“研究问题、输入、处理、输出、读法”五件事来读。_

---

## DiT

| 项 | 内容 |
| --- | --- |
| 全名 | Scalable Diffusion Models with Transformers |
| 研究问题 | 能不能把扩散模型里的 U-Net 去噪器换成可扩展的 Transformer。 |
| 输入 | noisy image latent patch、timestep、类别或条件信息。 |
| 处理 | patchify latent，把 timestep/condition 注入 Transformer block，逐步预测噪声或干净 latent。 |
| 输出 | 去噪后的图像 latent。 |
| 新手读法 | 只看它如何把“扩散去噪器”改成 Transformer，这是后面推荐 DiT 的架构源头。 |

## CODIGEM

| 项 | 内容 |
| --- | --- |
| 全名 | Recommendation via Collaborative Diffusion Generative Model |
| 研究问题 | 协同过滤信号弱、latent 表示泛化差，能不能用 DDPM 学更强协同信号。 |
| 输入 | 用户-物品交互数据。 |
| 处理 | 在协同过滤表示上做前向加噪和反向去噪，生成更鲁棒的 latent 表示。 |
| 输出 | 推荐分数或协同过滤表示。 |
| 新手读法 | 把它当作“扩散推荐的开山作之一”，不必一开始深挖架构细节。 |

## DiffRec

| 项 | 内容 |
| --- | --- |
| 全名 | Diffusion Recommender Model |
| 研究问题 | 传统 VAE/GAN 推荐建模不稳定，能不能用扩散直接建模用户交互生成。 |
| 输入 | 用户的交互向量，常见形式是 multi-hot item vector。 |
| 处理 | 对交互向量加噪，再用 denoising model 还原用户偏好；L-DiffRec 进一步在 latent space 压缩。 |
| 输出 | 用户对全量 item 的推荐分数。 |
| 新手读法 | 它不是 DiT，但非常适合理解“推荐里的 x0 可以是交互向量”。 |

## DiffuRec

| 项 | 内容 |
| --- | --- |
| 全名 | DiffuRec: A Diffusion Model for Sequential Recommendation |
| 研究问题 | 固定 item embedding 表达能力有限，能不能把目标 item 表示当成分布来生成。 |
| 输入 | 用户历史 item 序列。 |
| 处理 | 对目标 item embedding 加高斯噪声，再根据历史序列逐步还原目标表示。 |
| 输出 | 目标 item embedding，并通过 rounding 或检索变成 item。 |
| 新手读法 | 这是理解“序列推荐从分类变生成”的关键论文。 |

## DreamRec

| 项 | 内容 |
| --- | --- |
| 全名 | Generate What You Prefer: Reshaping Sequential Recommendation via Guided Diffusion |
| 研究问题 | 负采样分类不一定符合用户“先想象理想物品再选择”的行为。 |
| 输入 | 用户历史 item 序列。 |
| 处理 | Transformer encoder 编码历史，guided diffusion 生成 oracle item embedding。 |
| 输出 | 个性化 oracle item，再映射回候选 item。 |
| 新手读法 | 把它看作 RDT 目标 latent 生成路线的重要前驱。 |

## DiffGT

| 项 | 内容 |
| --- | --- |
| 全名 | A Directional Diffusion Graph Transformer for Recommendation |
| 研究问题 | 隐式反馈图里有假阳性和假阴性，怎么在图上建模噪声。 |
| 输入 | 用户-物品交互图。 |
| 处理 | 在图表示上加入方向性/各向异性高斯噪声，再用 Graph Transformer 去噪。 |
| 输出 | 更干净的用户偏好表示和 Top-K 推荐。 |
| 新手读法 | 重点看“图结构噪声不是普通图像噪声”，它对推荐图做了定制。 |

## EDGE-Rec

| 项 | 内容 |
| --- | --- |
| 全名 | EDGE-Rec: Efficient and Data-Guided Edge Diffusion For Recommender Systems Graphs |
| 研究问题 | 二值交互图太粗糙，评分边权、用户特征、物品特征怎么直接参与扩散。 |
| 输入 | 加权用户-物品交互矩阵、用户特征、物品特征。 |
| 处理 | 用 RCSA attention 和 GDiT 直接去噪加权交互矩阵。 |
| 输出 | 和原始评分尺度一致的 user-item 预测。 |
| 新手读法 | 它适合补齐“矩阵/边权扩散”视角，不是 RDT 最直接主线。 |

## DCRec/DCDT

| 项 | 内容 |
| --- | --- |
| 全名 | Dual Conditional Diffusion Models for Sequential Recommendation |
| 研究问题 | 只把历史压成一个向量会丢细节，只在连续 embedding 中扩散又和离散 item 有鸿沟。 |
| 输入 | 历史序列 embedding 和目标 item embedding。 |
| 处理 | 把历史和目标拼接后扩散，同时用干净历史作为显式条件，通过 DCDT cross-attention 注入。 |
| 输出 | 更稳定的目标 item 表示，并映射到离散 item。 |
| 新手读法 | 这是和 RDT 最接近的论文之一，重点看“隐式条件 + 显式条件”。 |

## iDreamRec

| 项 | 内容 |
| --- | --- |
| 全名 | Generate and Instantiate What You Prefer: Text-Guided Diffusion for Sequential Recommendation |
| 研究问题 | ID embedding 语义弱，如何用文本描述和用户意图控制推荐生成。 |
| 输入 | 用户历史、物品文本描述、文本 embedding、意图 instruction。 |
| 处理 | 用文本 embedding 建立 item 表示，并用 Diffusion Transformer block 做文本条件去噪。 |
| 输出 | 符合语义意图的目标 item 表示和推荐结果。 |
| 新手读法 | 如果你要让 RDT 利用文本和 prompt，这是优先阅读对象。 |

## Prompt-to-Slate

| 项 | 内容 |
| --- | --- |
| 全名 | Prompt-to-Slate: Diffusion Models for Prompt-Conditioned Slate Generation |
| 研究问题 | 推荐列表不是单个 item 相加，能不能一次生成有整体一致性的 slate。 |
| 输入 | 自然语言 prompt。 |
| 处理 | DMSG 学习 slate 的联合分布，用扩散生成符合 prompt 的 item 集合。 |
| 输出 | 歌单、商品 bundle 等 slate。 |
| 新手读法 | 它是“列表整体生成”路线，不是 next-item 预测路线。 |

## CATDiT

| 项 | 内容 |
| --- | --- |
| 全名 | Continuous Data Augmentation via Condition-Tokenized Diffusion Transformer for Sequential Recommendation |
| 研究问题 | 序列推荐数据稀疏，能不能用条件化 DiT 生成高质量连续增强样本。 |
| 输入 | 历史行为条件 token。 |
| 处理 | 把条件 token 化后喂给 Diffusion Transformer，生成连续增强表示。 |
| 输出 | 用于训练推荐器的增强样本。 |
| 新手读法 | 把它当作“条件 token 进入 DiT”的设计参考。 |

## ICDDT

| 项 | 内容 |
| --- | --- |
| 全名 | Target Item-oriented Conditional Diffusion Differential Transformer for Next-Item Prediction |
| 研究问题 | 多行为序列推荐中，如何更好利用目标 item 信息和分布式表示。 |
| 输入 | 多行为历史序列和目标 item 信息。 |
| 处理 | 用条件扩散和 Differential Transformer 建模目标 item-oriented 表示。 |
| 输出 | next-item prediction。 |
| 新手读法 | 它更偏多行为序列推荐，适合了解 CIKM 2025 的新分支。 |

## LPDO

| 项 | 内容 |
| --- | --- |
| 全名 | Listwise Preference Diffusion Optimization for User Behavior Trajectories Prediction |
| 研究问题 | 只预测下一个 item 不够，未来行为轨迹要按整体偏好排序。 |
| 输入 | 用户历史行为。 |
| 处理 | 用 diffusion 生成未来轨迹，并把 Plackett-Luce listwise ranking 放进优化目标。 |
| 输出 | 多步未来用户行为轨迹。 |
| 新手读法 | 如果 RDT 未来要生成多个未来 item，而不是单个 target latent，这篇非常关键。 |

## PaDiRec

| 项 | 内容 |
| --- | --- |
| 全名 | Generating Model Parameters for Controlling: Parameter Diffusion for Controllable Multi-Task Recommendation |
| 研究问题 | 新任务需求变化时，能不能不重训整个推荐模型，而是生成适配参数。 |
| 输入 | 任务需求和控制信号。 |
| 处理 | 对模型参数做扩散生成。 |
| 输出 | 适合当前任务的模型参数。 |
| 新手读法 | 它不是直接生成 item，但能打开“扩散对象也可以是参数”的视角。 |

## ContRec

| 项 | 内容 |
| --- | --- |
| 全名 | Diffusion Generative Recommendation with Continuous Tokens |
| 研究问题 | LLM 推荐里的离散 tokenization 会损失信息，能不能用连续 token。 |
| 输入 | 用户/item continuous token、LLM 上下文。 |
| 处理 | sigma-VAE tokenizer 产生连续 token，Dispersive Diffusion 生成用户偏好表示。 |
| 输出 | 文本推理结果 + latent 表示，共同用于 Top-K 检索。 |
| 新手读法 | 它和 RDT 的 continuous target latent 思想很近，尤其值得看 tokenizer 和检索落地。 |

## CDRec

| 项 | 内容 |
| --- | --- |
| 全名 | Continuous-time Discrete-space Diffusion Model for Recommendation |
| 研究问题 | 连续 embedding 扩散可能丢掉离散 item 信息，能不能直接在离散空间扩散。 |
| 输入 | 用户历史交互 item。 |
| 处理 | 在连续时间里对离散 item 状态做 masking/transition，并加入 popularity-aware schedule。 |
| 输出 | 推荐 item。 |
| 新手读法 | 它适合用来反思 RDT：是否必须一直在 continuous latent 里做扩散。 |

## DualFashion

| 项 | 内容 |
| --- | --- |
| 全名 | Dual-Diffusional Generative Fashion Recommendation |
| 研究问题 | 时尚推荐不仅要推荐 item，还要解释偏好并生成视觉/文本结果。 |
| 输入 | 用户历史、图像、结构化属性 caption。 |
| 处理 | 双分支 diffusion Transformer 同时建模图像和文本。 |
| 输出 | 推荐商品图像和文本描述。 |
| 新手读法 | 它是最新多模态生成式推荐方向，适合给 RDT 的未来扩展找灵感。 |
