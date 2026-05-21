# Self-Attentive Sequential Recommendation

## Beauty 结果

- NDCG@10: 0.3219
- Hit@10: 0.4854
- 协议提醒: 原始 SASRec sequential recommendation 协议, 100 负采样.

## 数据处理方式

把 Amazon Beauty 的用户行为当作隐式反馈序列。先按时间排序, 去掉交互少于 5 的用户和物品, 再用 leave-last-out: 最后一个行为做测试, 倒数第二个通常做验证, 前面的行为做训练。

## 项目结构

- 输入: 用户按时间排列的 item 序列.
- 处理: item embedding + position embedding, 经过 causal self-attention 建模用户历史.
- 输出: 下一件商品的打分排序, 用 Hit@10 和 NDCG@10 评估.

## 与本项目关系

这是 Beauty 顺序推荐最常见的基础基线之一, 适合作为 RDT/GenRec 扩散推荐实验的非扩散对照。

## 来源

- arXiv: https://arxiv.org/abs/1808.09781
