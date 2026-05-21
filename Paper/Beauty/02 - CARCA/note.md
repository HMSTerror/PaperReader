# CARCA: Context and Attribute-Aware Next-Item Recommendation via Cross-Attention

## Beauty 结果

- NDCG@10: 0.396
- HR@10: 0.579
- 协议提醒: CARCA 预处理版, leave-one-out, 100 负采样.

## 数据处理方式

复用 Amazon Beauty 行为序列, 同时保留时间上下文和物品属性。数据按时间切分为训练、验证、测试, 测试时对每个用户用真实下一个 item 加 100 个负样本做排序。

## 项目结构

- 输入: 用户历史 item 序列 + 时间上下文 + item 属性.
- 处理: 用 cross-attention 让用户历史读取上下文和属性信息.
- 输出: 下一件商品的候选排序, 报告 HR@10 和 NDCG@10.

## 与本项目关系

它说明 Beauty 上加入上下文和属性可以显著强于纯 SASRec。你的 RDT 项目里的 text/image/CF 条件分支, 可以看作更强的多模态上下文注入。

## 来源

- arXiv: https://arxiv.org/abs/2204.06519
