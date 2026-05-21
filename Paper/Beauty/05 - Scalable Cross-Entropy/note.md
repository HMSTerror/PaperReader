# Scalable Cross-Entropy Loss for Sequential Recommendations with Large Item Catalogs

## Beauty 结果

- NDCG@10: 0.0544
- HR@10: 0.0935
- 设置: SASRec-SCE
- 协议提醒: 仓库自带的另一套 sequential benchmark 预处理, 不要和 CARCA/ProxyRCA 那几行直接比较.

## 数据处理方式

使用另一套大规模 sequential recommendation benchmark 流程。重点是大 item catalog 下如何训练 full/sampled cross-entropy, 而不是复用 CARCA 的 100 负采样榜单。

## 项目结构

- 输入: 用户行为序列和大规模 item catalog.
- 处理: 用可扩展 cross-entropy 训练序列推荐模型, 降低大候选空间下的训练成本.
- 输出: 下一 item 排序, 报告 HR@10 和 NDCG@10.

## 与本项目关系

你的 RDT 训练里有 diffusion loss + ranking loss。SCE 这篇主要值得借鉴的是大 item 表上的检索/分类损失设计, 可作为改进 ranking loss 或 full-catalog retrieval training 的参考。

## 来源

- arXiv: https://arxiv.org/abs/2409.18721
