# iDreamRec: Generate and Instantiate What You Prefer: Text-Guided Diffusion for Sequential Recommendation

- 论文 PDF: [Generate and Instantiate What You Prefer - Text-Guided Diffusion for Sequential Recommendation.pdf](Generate and Instantiate What You Prefer - Text-Guided Diffusion for Sequential Recommendation.pdf)
- 下载来源: https://arxiv.org/pdf/2410.13428
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

iDreamRec 继承 DreamRec 的 oracle item generation 思路，但指出 ID embedding 有两个根本限制。第一，ID embedding 随机初始化，本身没有语义，导致扩散模型要从零学习 item 空间分布。第二，ID embedding 难以接入更丰富的控制信号，例如用户用自然语言表达的意图、约束或偏好。

也就是说，DreamRec 能生成 oracle item，但它的 item 空间缺少可解释的语义坐标。若要让生成推荐支持“我想要更轻松的电影”“想看适合通勤的书”这类意图指令，需要把 item 表示放到文本语义空间中。

## 提出了什么方法

iDreamRec 用 item 的文本描述和 Text Embedding Model 构造 item embedding，而不是使用纯 ID embedding。这样 item 向量天然包含文本语义和大模型先验，并且与意图指令的 embedding 位于同一空间。模型在这个文本 embedding 空间里进行 diffusion-based oracle item generation。

更重要的是，iDreamRec 可以把 intention instruction 编码成控制信号，引导 oracle item 的生成。论文还采用 DDIM 提升采样效率，并对 embedding 空间做归一化/对齐处理，使扩散生成更稳定。推荐时，模型生成语义化 oracle item embedding，再匹配真实 item。

## 实验效果如何

实验在 Goodreads、MovieLens、Steam、Amazon-TV 四个数据集上进行。Table 1 显示 iDreamRec 在所有指标上显著超过 Caser、SASRec、MoRec、UniSRec、DiffRec、DreamRec。比如 MovieLens 上 HR@10/NDCG@10 为 0.1929/0.1011，相对最强基线提升 21.91%/30.03%；Steam 上 NDCG@5 提升 65.16%；Amazon-TV 上 NDCG@5 提升 60.58%。

论文还验证了 intention instruction 的作用：引入意图控制后，推荐可以更精确地朝用户指定方向生成。效率分析显示，iDreamRec 相比其他扩散推荐大幅改善推理速度，接近传统推荐器的量级。但论文也承认，真实用户意图指令数据不足，目前很多指令是启发式或 GPT 构造的。

## 用最简单的话解释原理

DreamRec 是“生成一个理想 item 向量”，iDreamRec 则进一步问：这个向量应该在哪个空间里生成？如果用纯 ID 向量，模型只知道编号，不懂语义；如果用文本 embedding，模型知道 item 的描述、属性和含义。

所以 iDreamRec 像是把推荐系统接到语言世界里。用户的历史、item 描述和意图指令都能变成同一种语义向量，扩散模型就在这个语义空间里生成“你想要的东西”。
