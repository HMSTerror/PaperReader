# Ducho meets Elliot: Large-scale Benchmarks for Multimodal Recommendation

## Beauty 结果

- nDCG: 7.21
- Recall: 13.93
- Hit Ratio: 21.31
- 设置: LATTICE (ALIGN)
- 协议提醒: 多模态 benchmark, 图像/文本特征抽取流程与顺序推荐 100 负采样协议完全不同.

## 数据处理方式

用 Ducho 抽取或整理多模态特征, 包括图像和文本特征, 再交给 Elliot benchmark 中的多模态推荐模型评估。它关注的是多模态特征和模型管线, 不是标准 next-item sequential 协议。

## 项目结构

- 输入: Amazon Beauty 交互数据 + item 图像/文本等多模态内容.
- 处理: Ducho 生成多模态特征, 推荐模型如 LATTICE 使用这些特征建图或融合.
- 输出: 多模态推荐排序结果, 报告 Recall、nDCG、Hit Ratio.

## 与本项目关系

它与你的 RDT 项目在 text/image embedding 准备上最相关。RDT 已经有 text/image/CF embedding 和融合/对齐脚本, 这篇可以作为 Beauty 多模态数据管线和评估协议参考。

## 来源

- arXiv: https://arxiv.org/abs/2409.15857
