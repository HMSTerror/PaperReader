# Diffusion Transformer 推荐系统 Wiki：扩散输入到底是什么

_回答一个核心问题：推荐系统里的扩散输入，和原始图像生成里的随机噪声是不是一回事？_

---

## 最短答案

不是完全一回事。

图像生成在推理阶段常常从随机噪声开始，然后逐步生成图像；推荐系统里的扩散模型也可能从随机噪声开始，但它几乎总是带着强条件一起去噪，例如用户历史、物品文本、图像特征、交互图、prompt、行为类型等。

更准确地说：

```text
训练时：
干净目标 x0 -> 加噪得到 xt -> 模型看到 xt + timestep + 条件 -> 学会预测噪声或 x0

推理时：
随机 xt 或被扰动的交互状态 -> 模型看到 xt + timestep + 条件 -> 多步去噪 -> 推荐目标
```

## 图像 DiT 的输入

原始 DiT 做图像生成时，通常把图像压到 latent space，然后切成 patch token。训练时：

```text
干净图像 latent x0
随机 timestep t
高斯噪声 epsilon
加噪后的 xt
类别条件或其他条件
```

模型输入不是“只有随机噪声”，而是：

```text
xt + timestep embedding + condition
```

推理时没有干净图像，所以从随机 latent noise 开始，逐步去噪得到图像。

## 推荐系统里的常见输入

| 路线 | 干净 x0 是什么 | 加噪后的 xt 是什么 | 条件是什么 | 最终输出 |
| --- | --- | --- | --- | --- |
| 目标 item embedding 扩散 | 下一个 item 的 embedding | noisy target embedding | 用户历史序列 | 目标 item embedding |
| 历史 + 目标序列扩散 | 历史 item embedding + 目标 item embedding | noisy sequence embedding | 干净历史序列 | 目标 item 或目标 embedding |
| 交互向量扩散 | 用户的 multi-hot 交互向量 | noisy interaction vector | 用户交互模式 | 全量 item 分数 |
| 图扩散 | 用户/item 图表示或边权矩阵 | noisy graph representation | 交互图、用户/物品特征 | 推荐分数 |
| 离散扩散 | item token 或历史 item 状态 | mask/replace 后的离散状态 | popularity、协同信号 | 推荐 item |
| slate 扩散 | 整个推荐列表的表示 | noisy slate representation | 自然语言 prompt | 一个推荐列表 |
| 参数扩散 | 推荐模型参数 | noisy parameters | 任务控制信号 | 可控任务模型参数 |

## 为什么推荐系统不能只看“随机噪声”

推荐的目标不是生成任意东西，而是给某个用户生成符合偏好的 item。因此条件信息比图像生成里还关键。

一个简单类比：

```text
图像生成：随机噪声 + “一只猫”的文本条件 -> 猫图
推荐生成：随机/加噪目标 latent + 用户历史 + 物品文本/图像/CF -> 下一个可能喜欢的 item
```

如果没有用户历史，模型只能生成“总体热门物品”；如果没有物品侧信息，模型很难处理冷启动和语义可控推荐。

## RDT 项目里的输入

你 `E:\RDT` 项目的训练输入可以理解成：

```text
target_item_ids -> item_lookup_table -> target_latents = x0
target_latents + noise + timestep -> noisy_target_latents = xt

semantic-ID 历史 token
text/image/CF/popularity 条件 token
noisy_target_latents
timestep
        -> GenRecHybridDiffusionRunner
        -> prediction
        -> denoised_latents
```

对应代码位置：

| 作用 | 文件/函数 |
| --- | --- |
| 从 item 表取目标 latent | `E:\RDT\scripts\train_genrec_hybrid_diffusion.py::prepare_target_latents` |
| 给目标 latent 加噪 | `E:\RDT\genrec\models\genrec_hybrid_diffusion.py::prepare_training_inputs` |
| 把 noisy target latent 注入目标位置 | `E:\RDT\genrec\models\genrec_hybrid_diffusion.py::_inject_noisy_target_latents` |
| 多模态条件 cross-attention | `E:\RDT\genrec\models\genrec_dit.py::GenRecDiTBlock` |
| 推理时从随机 latent 开始采样 | `E:\RDT\genrec\models\genrec_hybrid_diffusion.py::sample_latents` |

## 你应该记住的公式

推荐论文里常见的连续扩散公式可以先记成这一个：

```text
xt = sqrt(alpha_bar_t) * x0 + sqrt(1 - alpha_bar_t) * epsilon
```

其中：

- `x0` 是干净目标，例如目标 item embedding
- `epsilon` 是随机噪声
- `xt` 是第 `t` 步的 noisy target
- 模型学习从 `xt` 和条件里还原 `x0`，或预测 `epsilon`

RDT 默认更像 `epsilon prediction`：

```text
模型输出 prediction ~= epsilon
denoised_latents = 从 noisy_target_latents 和 prediction 反推 x0
```

## 阅读论文时问这四个问题

每看一篇 diffusion recommendation 论文，都先问：

1. 它把什么当作 `x0`
2. 它怎么把 `x0` 变成 `xt`
3. 去噪网络额外看到了哪些条件
4. 去噪结果怎么变成最终推荐 item

只要这四个问题清楚了，论文的方法部分就不会再像一团雾。
