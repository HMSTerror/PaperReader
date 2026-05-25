# Diffusion Transformer 推荐系统 Wiki：与 RDT 项目的关系

_把文献里的方法，对应到 `E:\RDT` 当前 GenRec Hybrid Diffusion 项目。_

---

## RDT 当前做的事情

`E:\RDT` 不是普通 sequential recommender，也不是原始图像生成 DiT。它更像一个“多模态条件下的目标 latent 扩散推荐器”。

核心流程是：

```text
Amazon 原始交互数据
        -> 文本 / 图像 / CF item embedding
        -> semantic ID 量化与 tokenized train/val/test
        -> 训练时取 target item latent 作为 x0
        -> 给 x0 加噪得到 noisy_target_latents
        -> 用历史 semantic-ID token 和多模态条件去噪
        -> 得到 denoised target latent
        -> 与 item latent table 做检索
        -> Top-K 推荐与 hot/mid/cold 分组评估
```

## RDT 的模块对应

| RDT 模块 | 在论文术语里是什么 | 最接近的论文 |
| --- | --- | --- |
| `target_latents` | 干净目标 `x0` | DreamRec, DCRec, iDreamRec, ContRec |
| `noisy_target_latents` | 加噪目标 `xt` | DiffuRec, DreamRec, DCRec |
| semantic-ID 历史 token | 用户历史条件 | DCRec, CATDiT |
| text/image/CF/popularity 条件 token | 多源条件输入 | iDreamRec, DualFashion, EDGE-Rec |
| `GenRecDiTBlock` | DiT 风格去噪 block | DiT, DCRec/DCDT, iDreamRec |
| cross-attention 注入条件 | 显式条件控制 | DCRec, iDreamRec |
| item latent retrieval | 连续生成到离散 item 的落地 | DreamRec, DiffuRec, ContRec |
| ranking loss / auxiliary loss | 让生成 latent 更适合推荐排序 | DiffRec, LPDO, ContRec |

## 最值得借鉴的论文

| 论文 | 对 RDT 的直接启发 |
| --- | --- |
| DCRec/DCDT | RDT 可以借鉴“双条件”：一部分条件进入 noisy sequence，一部分干净历史通过 cross-attention 注入。 |
| iDreamRec | RDT 已经有文本条件，可进一步研究 intention instruction 或用户自然语言偏好如何控制生成。 |
| ContRec | RDT 的 continuous target latent 与 continuous token 路线接近，可借鉴 tokenizer 和 diffusion loss 设计。 |
| CATDiT | RDT 的多模态条件也可以更系统地 token 化，并研究这些 condition token 如何参与数据增强。 |
| LPDO | 如果 RDT 从 next-item 扩展到未来多步轨迹，可以用 listwise preference objective 改造训练目标。 |
| CDRec | 如果 RDT 想减少 continuous latent 到 item ID 的映射损失，可以参考离散扩散或 masking-based 生成。 |
| DualFashion | 如果 RDT 未来强调可解释多模态推荐，可以输出图像/文本解释，而不仅是 item ID。 |

## RDT 和图像 DiT 的关键差别

| 对比项 | 图像 DiT | RDT |
| --- | --- | --- |
| 生成对象 | 图像 latent patch | 目标 item latent |
| 条件 | 类别、文本、图像条件等 | 历史 semantic ID、文本、图像、CF、流行度 |
| 推理起点 | 随机图像 latent noise | 随机 target latent |
| 训练目标 | 还原图像 latent 或噪声 | 还原目标 item latent 或噪声 |
| 输出落地 | VAE decoder 变成图像 | 与 item latent table 检索 Top-K item |

## RDT 当前路线的优势

RDT 的设计比较聪明，因为它避免了两个常见坑：

1. 没有把推荐做成“只预测 item ID 的分类器”
2. 没有把文本、图像、CF 条件粗暴拼接成一个向量

它把目标 item 放在连续 latent 空间里生成，同时用 cross-attention 注入多模态条件。这正是 DiT 在推荐系统里最自然的落点。

## RDT 后续可以研究的方向

| 方向 | 可以怎么做 | 对应论文 |
| --- | --- | --- |
| 更强文本控制 | 加入用户意图 prompt 或自然语言 query | iDreamRec, Prompt-to-Slate |
| 减少离散映射误差 | 加入 discrete diffusion 或 semantic-ID 生成头 | CDRec, ICDDT |
| 多步推荐 | 从单个 target latent 扩展到未来 target latent 序列 | LPDO |
| 图结构增强 | 用交互图边权或用户-item 图表示辅助条件 | DiffGT, EDGE-Rec |
| 可解释多模态输出 | 让模型同时输出推荐理由、属性描述或可视化表示 | DualFashion |
| 条件 ablation 更系统 | 分析 text/image/CF/popularity 哪些条件真正有效 | iDreamRec, EDGE-Rec, CATDiT |

## 一句话结论

RDT 最应该被放在“Diffusion Transformer for multimodal sequential recommendation”的谱系里。它的主输入不是单纯随机噪声，而是：

```text
noisy target latent + 用户历史 token + 多模态条件 token + timestep
```

这个判断能帮你把 RDT 和 DiT、DreamRec、DCRec、iDreamRec、ContRec 等论文自然连起来。
