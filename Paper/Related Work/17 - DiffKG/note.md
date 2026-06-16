# DiffKG: DiffKG: Knowledge Graph Diffusion Model for Recommendation

- 论文 PDF: [DiffKG - Knowledge Graph Diffusion Model for Recommendation.pdf](DiffKG - Knowledge Graph Diffusion Model for Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2312.16890
- 说明: 这是一份面向快速理解的阅读笔记，重点服务 CARD related work 写作，不替代逐表精读。

## 面对什么问题

知识图谱推荐依赖 KG 结构和关系，但 KG 中也有噪声和无关关系，直接用会干扰偏好建模。

## 提出了什么方法

对 KG 表示或结构进行扩散去噪，过滤无关关系，得到更适合推荐的知识图谱信号，再与用户偏好建模结合。

## 实验效果如何

论文报告在 KG 推荐数据集上优于多种 KG-aware recommendation baseline，说明扩散去噪能提高 KG 信号质量。

## 用最简单的话解释原理

知识图谱里不是每条边都有用，DiffKG 先把图里的噪声关系清一遍，再拿清理后的知识做推荐。
