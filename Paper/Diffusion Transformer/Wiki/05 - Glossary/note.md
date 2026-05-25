# Diffusion Transformer 推荐系统 Wiki：术语表

_读论文前先把高频词翻译成“人话”。_

---

## 基础术语

| 术语 | 简单解释 |
| --- | --- |
| `x0` | 干净数据。推荐里可能是目标 item embedding、用户交互向量、未来轨迹或 slate 表示。 |
| `xt` | 第 `t` 步加噪后的数据。模型训练时看到的是它，而不是直接看到干净答案。 |
| `epsilon` | 加到 `x0` 上的随机噪声。 |
| timestep | 当前噪声强度的位置。越靠后通常噪声越大。 |
| denoiser | 去噪网络。DiT 里的 denoiser 是 Transformer。 |
| condition | 条件信息。推荐里通常是用户历史、文本、图像、图结构、prompt、行为类型等。 |
| reverse process | 反向去噪过程，从 `xt` 逐步还原推荐目标。 |
| prediction type | 模型预测什么。常见是预测噪声 `epsilon` 或直接预测干净样本 `x0`。 |

## 推荐系统术语

| 术语 | 简单解释 |
| --- | --- |
| sequential recommendation | 根据用户过去的交互序列预测下一个 item。 |
| Top-K recommendation | 给用户输出前 K 个最可能喜欢的 item。 |
| item embedding | item 的向量表示，可以来自 ID、文本、图像或协同过滤。 |
| semantic ID | 把 item 表示量化成一串离散 token，方便像语言模型一样建模 item。 |
| oracle item | 用户心里理想的下一件物品，不一定直接等于候选池里的某个 item。 |
| slate | 一次展示给用户的一组 item，例如歌单、商品组合、视频列表。 |
| cold item | 冷门或交互少的 item，推荐难度更高。 |
| CF embedding | collaborative filtering embedding，来自用户-物品协同交互的表示。 |

## 架构术语

| 术语 | 简单解释 |
| --- | --- |
| DiT | Diffusion Transformer，用 Transformer 作为扩散去噪主干。 |
| Graph Transformer | 在图结构上做 attention 的 Transformer，常用于用户-物品图。 |
| cross-attention | 让目标 token 主动读取条件 token，例如 noisy target 读取历史文本/图像条件。 |
| conditional layer norm | 用条件信息动态改变归一化参数，让条件更深地影响模型。 |
| continuous token | 连续向量 token，不像普通词表 token 那样是离散 ID。 |
| discrete diffusion | 在离散状态上扩散，例如 mask item、替换 item，而不是加高斯噪声。 |
| parameter diffusion | 扩散对象不是数据，而是模型参数。 |

## 指标术语

| 术语 | 简单解释 |
| --- | --- |
| HR@K / Hit@K | 推荐前 K 个里是否命中真实 item。 |
| Recall@K | 真实相关 item 中有多少被前 K 个推荐覆盖。 |
| NDCG@K | 命中位置越靠前分数越高，比 HR 更重视排序。 |
| SeqMatch | LPDO 中用于评估多步轨迹是否精确匹配的指标。 |
| PPL | Perplexity，衡量生成序列的概率质量。 |

## 新手最容易混的三组概念

| 容易混淆 | 区别 |
| --- | --- |
| DiT vs diffusion recommendation | DiT 是去噪网络架构；diffusion recommendation 是把扩散思想用于推荐任务。推荐论文可以用 DiT，也可以不用 DiT。 |
| noisy target vs condition | noisy target 是被还原的对象；condition 是帮助还原它的信息。RDT 里 `noisy_target_latents` 是前者，历史和多模态 token 是后者。 |
| continuous diffusion vs discrete diffusion | continuous diffusion 常给 embedding 加高斯噪声；discrete diffusion 常对 item token 做 mask、replace 或转移。 |

## 读论文时的万能模板

每篇论文都可以填这张小表：

| 问题 | 我的答案 |
| --- | --- |
| 它的 `x0` 是什么？ |  |
| 它怎么得到 `xt`？ |  |
| denoiser 是什么结构？ |  |
| condition 有哪些？ |  |
| 输出怎么变成推荐 item？ |  |
| 和 RDT 哪个模块最像？ |  |
