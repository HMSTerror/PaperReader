# MCDRec: Multimodal Conditioned Diffusion Model for Recommendation

- 论文 PDF: [Multimodal Conditioned Diffusion Model for Recommendation.pdf](Multimodal Conditioned Diffusion Model for Recommendation.pdf)
- 下载来源: https://ercdm.sdu.edu.cn/__local/1/2E/06/BA3A14E80ADD5913EFFB0553083_B0155145_15CACA.pdf
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

MCDRec 处理多模态推荐中“内容特征与协同信号难以对齐”的问题。多模态推荐通常把图像、文本等内容特征加入 item 表示，但很多方法只是围绕某个辅助任务优化多模态表示，没有显式建模这些模态特征的不确定性和分布关系，容易学到 ill-posed item embeddings。

此外，用户-item 图中存在偶然交互和噪声边。已有 degree-sensitive 图去噪策略不一定能捕获用户跨模态的一致偏好。因此论文希望用扩散模型同时解决 item 多模态表示建模和交互图去噪。

## 提出了什么方法

MCDRec 有两个核心模块。MRD（Multimodal-conditioned Representation Diffusion）把预提取的多模态知识作为条件注入 item representation diffusion，使连续多模态特征与协同 item 表示在同一连续空间中对齐，而不是用连续特征去直接指导离散 item 概率。

DGD（Diffusion-guided Graph Denoising）利用 MRD 得到的 diffusion-aware item 表示，重新评估用户-item 边的可靠性，过滤偶然交互。这样 MCDRec 在表示阶段和图结构阶段都利用了扩散知识，并且模块是 model-agnostic 的，可以接入 BM3、FREEDOM 等多模态推荐器。

## 实验效果如何

实验在 Baby 和 Sports 两个真实多模态数据集上进行，数据非常稀疏，Sparsity 分别为 99.88% 和 99.95%。论文比较 CF-based recommenders 和多模态 recommenders，并报告 MCDRec 在 Recall@5/10/20 与 NDCG@5/10/20 上显著优于所有基线。提升在较小 K 上更明显，说明它更能把真正相关的 item 放到前排。

分析显示，MCDRec 对 BM3 这类没有图去噪策略的 backbone 提升最大；与 FREEDOM 结合时达到最好结果，说明扩散引导的图去噪可以补充已有结构去噪。消融也证明 MRD 和 DGD 都有效，视觉化分析显示 MRD 能更好处理用户 embedding 与多模态 item 表示之间的高阶相关。

## 用最简单的话解释原理

MCDRec 的直觉是：商品图片和文字不是简单附加信息，它们应该参与塑造 item 表示；同时，用户点过某个 item 不一定代表强兴趣，交互图也需要去噪。

MRD 负责让 item 的图像/文本特征和协同表示在同一个空间里融合，DGD 负责根据融合后的表示判断哪些交互边更可信。一个修 item 表示，一个修用户-item 图。
