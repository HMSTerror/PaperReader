# Time Interval Aware Self-Attention for Sequential Recommendation

- 论文 PDF: [Time Interval Aware Self-Attention for Sequential Recommendation.pdf](Time Interval Aware Self-Attention for Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2002.00741
- 年份/会议: WSDM 2020
- 方向: 序列推荐基础
- 说明: 这是一份面向 SASRec、语义增强、多模态融合与 cross-attention 研究的中文精读报告。

## 摘要
TiSASRec 研究的问题是：SASRec 虽能建模物品顺序，但忽略了相邻行为之间的真实时间间隔。两个行为在序列中相邻，不代表它们在时间上接近；同样，间隔一天和间隔一年可能对应完全不同的偏好演化。论文提出 **Time Interval Aware Self-Attention (TiSASRec)**，在 self-attention 中同时加入**绝对位置 (absolute position)** 和**相对时间间隔 (relative time interval)** 表示，让模型在计算注意力时感知“第几个行为”和“隔了多久”。实验表明，TiSASRec 在多个序列推荐数据集上优于 SASRec 等 baseline，尤其在时间跨度差异明显的行为序列中更有效。

## 背景
序列推荐长期把用户行为按时间排序后只保留离散顺序，但真实推荐系统中的时间间隔包含重要语义。例如，用户连续浏览多个手机配件可能代表当前购买任务；隔数月再次浏览则可能代表新需求。已有 time-aware 推荐方法多用于评分矩阵或时间漂移，尚未充分嵌入 Transformer 式序列推荐。

**Research Questions**：1. 在 self-attention 序列推荐中显式建模时间间隔是否能提升性能？2. 绝对位置和相对时间对推荐是否互补？3. 时间间隔感知机制能否在不同稀疏度数据上稳定有效？

**Hypotheses**：论文隐含假设为：同样的物品转移在不同时间间隔下含义不同；relative time interval embedding 能帮助模型区分短期任务兴趣和长期偏好；只使用 position embedding 不足以表达真实时间。

## 文献综述
作者继承了 SASRec 的 self-attention 框架，也讨论了 FPMC、GRU4Rec、Caser 等序列推荐方法。这些方法关注顺序依赖，但通常把行为间隔压缩为“相邻/不相邻”。论文还连接到 time-aware recommendation 研究，指出既有时间模型常处理全局时间漂移或上下文时间，较少直接进入 attention 权重计算。

文献演进逻辑是：SASRec 已证明 attention 能选择相关历史，但它选择历史时只知道位置，不知道真实间隔。TiSASRec 的创新就在于把时间间隔作为 attention 的一等输入，而非简单拼接特征。

## 方法
**Participants**：无受试者；实验材料是带时间戳的用户交互序列。

**Materials**：论文使用多个公开序列推荐数据集，与 SASRec、Caser、GRU4Rec、FPMC 等方法比较。评价采用 Hit Ratio、NDCG 等 top-N 指标。

**Procedure**：TiSASRec 为每个行为构造物品嵌入、位置嵌入与时间间隔嵌入。在 self-attention 中，query 与 key 的相关性不仅由物品表示决定，还由两个位置之间的相对时间间隔调节。由于真实时间间隔取值很大，论文将时间间隔离散化或截断到可学习范围，使模型能学习“短间隔”“中间隔”“长间隔”的不同影响。模型仍使用因果 mask，保证预测第 t+1 个物品时不访问未来。

## 实验和结果
实验整体表明，TiSASRec 相比 SASRec 有稳定提升，说明时间间隔确实补充了离散顺序无法表达的信息。消融结果通常显示：只使用位置或只使用时间都不如二者结合；这支持“顺序结构”和“真实时间”互补的假设。

论文还通过注意力分析说明，模型会根据时间间隔改变历史行为权重。短间隔历史往往对即时意图更关键，长间隔历史则可能反映长期兴趣或噪声，模型需要数据驱动地区分它们。

## 讨论
TiSASRec 的意义在于提醒后续工作：Transformer backbone 中的 position embedding 不是时间建模的充分替代。对多模态或 cross-attention 推荐来说，这一点也重要：如果图像/文本内容代表物品语义，时间间隔则代表用户兴趣是否仍然有效，二者对应不同信息维度。

与 SASRec 相比，TiSASRec 的结构改动不大，却显著提升了时间敏感场景的表达能力。这说明很多推荐增益可能来自对行为日志中已有上下文的细致建模，而不一定来自更大的模型。

## 结论
作者的结论是：在 self-attention sequential recommendation 中引入 time interval awareness 能更准确刻画用户动态偏好。论文未单列严格 limitation；从方法可见，其局限在于时间间隔离散化和截断超参数可能影响泛化，未来可进一步结合更复杂的时间过程或上下文信息。
