# Proxy-based Item Representation for Attribute and Context-aware Recommendation

## Beauty 结果

- NDCG@10: 0.449
- HR@10: 0.626
- 协议提醒: 基于 CARCA 家族数据, LIP 训练, leave-one-out, 100 负采样.

## 数据处理方式

沿用 CARCA 类 Beauty 预处理: 用户序列按时间组织, 用上下文和属性辅助推荐。ProxyRCA 重点不在重新定义数据集, 而在学习更稳的 proxy item 表示。

## 项目结构

- 输入: 用户历史序列 + item 属性/上下文特征.
- 处理: 学习 proxy-based item representation, 用代理表示缓解稀疏 item 表示不稳定的问题.
- 输出: 下一 item 排序分数, 在 Beauty 上用 HR@10 和 NDCG@10 比较.

## 与本项目关系

它和你的 RDT 项目都关心 item representation。区别是 ProxyRCA 强化判别式 item 表示, RDT 则把 CF/text/image 表示作为 latent 和条件, 再用 diffusion 生成目标 item latent。

## 来源

- arXiv: https://arxiv.org/abs/2312.06145
