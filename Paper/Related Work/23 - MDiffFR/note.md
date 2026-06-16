# MDiffFR: MDiffFR: Modality-Guided Diffusion Generation for Cold-start Items in Federated Recommendation

- 论文 PDF: [MDiffFR - Modality-Guided Diffusion Generation for Cold-start Items in Federated Recommendation.pdf](MDiffFR - Modality-Guided Diffusion Generation for Cold-start Items in Federated Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2512.24715
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

MDiffFR 处理联邦推荐中的 item cold-start。新 item 没有历史交互，集中式推荐可以利用用户行为和内容特征为它建模，但联邦推荐中用户数据留在客户端，服务器不能直接访问完整交互历史。这使冷启动 item embedding 生成更困难。

已有联邦冷启动方法多采用 mapping-based paradigm：把 item 模态特征一对一映射成 embedding。但这种确定性映射容易造成 embedding misalignment，也可能带来隐私风险，因为攻击者可能从映射关系反推 item 属性或敏感信息。

## 提出了什么方法

MDiffFR 提出 generation-based modality-guided diffusion。服务器端训练扩散模型，学习全局 item embedding 的分布；对新 item，模型不是简单映射模态特征，而是在模态特征条件引导下，通过反向去噪生成符合全局分布的 cold-start item embedding。

论文强调这种生成方式有三点优势：能保持客户端模型的优化方向，不强制一对一映射；能捕获 item embedding 的底层分布；相比映射方法具有更强隐私保护。作者还给出理论分析，讨论在 inversion attack 下 MDiffFR 的隐私优势。

## 实验效果如何

实验在 KU、Food、Dance、Movie 四个真实数据集上进行，与 CS_FedNCF、CS_FCF、IPFedRec、IFedNCF 以及集中式冷启动方法比较。Table 2 中 MDiffFR 在大多数 federated baseline 比较下取得最好或接近最好结果。例如 Food 上 Recall@50 为 19.23、NDCG@50 为 8.08；Dance 上 Recall@50 为 21.37、NDCG@50 为 8.74；KU 上 Recall@50 为 19.46。

隐私和鲁棒性实验显示，即使加入较强噪声扰动，MDiffFR 性能只轻微下降，说明生成式方法对 differential privacy 友好。embedding dimension 分析显示，64 维通常达到效果与成本的较好平衡；16/32 维不足以捕获 item 分布，128 维收益有限但成本翻倍。

## 用最简单的话解释原理

MDiffFR 的想法是：新 item 没有交互，但它有图片、文本等模态信息。与其直接用一个函数把模态信息翻译成 embedding，不如学习“已有 item embedding 长什么分布”，再根据新 item 模态信息生成一个合理 embedding。

这就像给新商品做画像：不是照模板硬填，而是参考同类商品在推荐系统里的整体分布，生成一个既符合内容语义、又能被联邦客户端模型使用的向量。
