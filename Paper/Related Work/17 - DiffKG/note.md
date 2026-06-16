# DiffKG: DiffKG: Knowledge Graph Diffusion Model for Recommendation

- 论文 PDF: [DiffKG - Knowledge Graph Diffusion Model for Recommendation.pdf](DiffKG - Knowledge Graph Diffusion Model for Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2312.16890
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

DiffKG 处理知识图谱推荐中的噪声知识问题。KG 可以提供 item 的实体、属性和关系，帮助推荐理解 item 语义；但并不是所有 KG 边都对推荐有用，有些 item-entity 连接可能无关甚至误导用户偏好建模。

已有知识图谱推荐方法往往把 KG 信息整体注入推荐模型，难以区分任务相关知识和噪声知识。论文希望用扩散生成方式，从 noisy KG 中提炼更适合推荐任务的 knowledge-aware item semantics，并让它与协同过滤信号对齐。

## 提出了什么方法

DiffKG 把 generative diffusion model 引入 KG learning。它通过知识图谱扩散过程生成更任务相关的 KG 表示，并把这个增强 KG 用于推荐的数据增强和表征学习。为了避免只从 KG 自身出发，论文设计 collaborative knowledge graph convolution，把用户-item 交互中的协同信号注入 KG diffusion，指导哪些关系更应该保留。

最终模型结合 KG diffusion-enhanced augmentation 和 contrastive learning，使 item 的知识语义与协同关系更一致。它不是简单“多用 KG”，而是先把 KG 过滤/重构成更推荐相关的信号。

## 实验效果如何

实验在 Last-FM、MIND、Alibaba-iFashion 三个数据集上，采用 full-rank evaluation，并与 BPR、NeuMF、LightGCN、SGL、CKE、KTUP、KGNN-LS、KGCN、KGAT、KGIN、MCCLK、KGCL 等比较。Table 2 中 DiffKG 全部最好：Last-FM Recall/NDCG 为 0.0980/0.0911，MIND 为 0.0615/0.0389，Alibaba-iFashion 为 0.1234/0.0773。

消融显示，去掉 KG-enhanced contrastive learning 会显著下降；用 VGAE 替代 diffusion model 也变差；去掉 collaborative knowledge graph convolution 也会下降。尤其在 Last-FM 和 MIND 上，去掉 diffusion 的损失更明显，说明这些 KG 噪声更大，更需要扩散式提炼。

## 用最简单的话解释原理

知识图谱像一本百科，但不是百科里的每一条信息都能帮助推荐。DiffKG 像是在给百科做“推荐任务专用筛选”：把和用户行为有关的知识保留下来，把无关或噪声关系弱化。

扩散过程负责从 noisy KG 中生成更干净的 KG 信号，协同图卷积负责告诉它“用户真实交互更支持哪些知识关系”。两者结合后，推荐模型看到的是更有用的知识图谱。
