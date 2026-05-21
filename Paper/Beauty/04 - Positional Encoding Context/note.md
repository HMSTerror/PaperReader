# Positional encoding is not the same as context

## Beauty 结果

- NDCG@10: 0.4871
- Hit@10: 0.6793
- 设置: CARCA Abs + Con
- 协议提醒: 明确复用 Rashed et al. 2022 的 CARCA 预处理版, leave-one-out, CARCA 训练框架.

## 数据处理方式

数据处理沿用 CARCA 的 Beauty 版本。论文重点区分 position 和 context: 位置编码只表示序列顺序, 上下文特征表示真实时间、场景或属性信息。

## 项目结构

- 输入: 用户历史序列 + position 信息 + context 信息.
- 处理: 分别建模位置和上下文, 避免把上下文误当成普通位置编码.
- 输出: 下一 item 排序, 在 Beauty 上报告 Hit@10 和 NDCG@10.

## 与本项目关系

这篇对你的 RDT 有启发: 多模态/上下文条件不要只当作普通 token 位置补丁, 而要作为独立条件源进入模型。RDT 当前的 text/image/CF branch schedule 就是在做类似的结构区分。

## 来源

- arXiv: https://arxiv.org/abs/2405.10436
