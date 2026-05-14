# Dual Conditional Diffusion Models for Sequential Recommendation

## 一、基本信息 (Metadata)

- 研究领域：序列推荐 (Sequential Recommendation, SeqRec)；生成式推荐 (Generative Recommendation, GenRec)
- 核心技术：
  - 扩散模型 (Diffusion Models)
  - 扩散变压器 (DiT, Diffusion Transformer)
- 核心问题：
  - 离散物品 ID 与连续生成空间之间的映射偏差
  - 长序列历史信息压缩导致的细粒度偏好遗忘
- 数据类型：用户交互序列（item ID 序列），目标物品 ID
- 创新点：同时建模历史与目标物品的连续表示，实现双重条件解耦

## 二、研究动机与破局点 (Motivation)

### 传统 SeqRec 局限

- 信息瓶颈：如 SASRec 将用户历史压缩为单一向量，微观交互细节容易丢失
- 生成式鸿沟：直接在离散空间生成 item ID 极其困难，梯度难以传递

### 破局点

- 放弃分类/排序交叉熵范式
- 采用连续空间扩散（预测 `x_0` 范式）
- 引入双重条件解耦机制：
  - `Time Condition`：宏观时间控制，稳定去噪
  - `History Condition`：微观历史语义引导，保留序列细节，打破信息压缩瓶颈

## 三、核心架构与方法论 (Methodology)

### 1. 输入阶段（联合加噪）

Embedding 表（端到端可学习）将离散序列转化为连续表示：

- 历史 embedding：`h_0`
- 目标物品 embedding：`e_0`

将二者拼接为 `[h_0; e_0]`，然后注入高斯噪声，得到 `[h_t; e_t]`。

说明：

- `h_0` 保留历史序列维度
- `e_0` 为目标 item embedding

### 2. 双重条件注入机制 (Dual Conditional Injection)

| 条件类型 | 注入路径 | 作用 |
| --- | --- | --- |
| Time Condition | Time Embed -> Linear/MLP -> AdaLN | 宏观调控特征分布尺度，实现去噪稳定 |
| History Condition | History Embed (无噪) -> Cross-Attention | 保留历史序列维度，动态查阅历史物品，增强微观细节 |

`DCDT Block` 在每个 block 中并行处理噪声主流与双重条件信息。

核心意义：

- 解耦宏观进度与微观个性化
- 让模型既稳定，又能精确记忆历史

### 3. 并行解码与连续重构损失 (Decoding & Loss)

解码头 (Prediction Head)：

- 输入：深层特征 + 时间步 `t` + 干净历史 `h_0`
- 输出：`h_0_hat`（重建历史）与 `e_0_hat`（预测目标 embedding）

损失函数：

```text
L_target = || e_0 - e_0_hat ||_2^2
L_history = || h_0 - h_0_hat ||_2^2
```

补充说明：

- `e_0_hat` 为连续 embedding，需要通过 Embedding Table 内积或最近邻检索映射回离散 item ID
- `L_history` 起辅助正则化作用，保证模型理解整体流形结构与时序依赖
