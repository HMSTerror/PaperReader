# DynamicProductImageGeneration: Dynamic Product Image Generation and Recommendation at Scale for Personalized E-commerce

- 论文 PDF: [Dynamic Product Image Generation and Recommendation at Scale for Personalized E-commerce.pdf](Dynamic Product Image Generation and Recommendation at Scale for Personalized E-commerce.pdf)
- 下载来源: https://arxiv.org/pdf/2408.12392
- 说明: 这是一份面向 related work 写作的精读笔记，重点回答问题、方法、实验效果和直观原理。

## 面对什么问题

这篇工业论文处理电商重定向广告中的商品图展示问题。推荐 item 是否相关很重要，但商品呈现方式也强烈影响用户是否点击。人工为海量商品、不同广告位和不同比例制作背景图成本极高，因此很多系统只能展示原始商品图或简单加设计元素。

问题是，原始商品图经常不够吸引人，尤其在广告场景中用户本来不是主动来买东西。平台希望在不修改商品主体的前提下，为商品生成更吸引人的背景，并根据用户上下文选择合适版本，从而提升 CTR。

## 提出了什么方法

论文把 latent diffusion image generation 与 contextual bandit 结合。图像生成部分使用 Stable Diffusion inpainting/背景生成：保留商品本身，不改动主体，只生成周围环境或背景；prompt 根据商品类别预定义，避免生成不合适的商业图。

个性化选择部分使用 LinUCB 等 contextual bandit。系统为每个商品类别准备多个 prompt/background 方案，在展示时根据用户和上下文特征选择更可能带来点击的版本。bandit 会在探索不同背景和利用当前最优背景之间平衡。

## 实验效果如何

论文报告了三阶段线上实验。Phase I 验证生成背景相对原始商品图能提升 CTR，并且连产品位置/尺寸处理也会影响点击。Phase II 进一步展示，生成图片在不同商家和广告位上均优于 baseline，但相对 CTR 增益范围较大，约 4% 到 40%，取决于商家商品目录、广告位和原始图片质量。

Phase III 验证个性化背景选择的增益：相对随机 prompt 选择，使用 LinUCB 根据上下文和用户特征选 prompt，还能进一步提升约 5%。论文也提到 conversions、CPA 等下游指标会因更多用户进入商家站点而间接受益。所有 CTR gains 均报告为 p < 0.05 显著。

## 用最简单的话解释原理

这篇工作的想法很直接：商品本身不变，但换一个更吸引人的背景，用户更可能点击。扩散模型负责快速生成很多合适背景，bandit 负责决定“给这个用户看哪种背景更可能点”。

它不是为了生成艺术图，而是把生成式图片当作推荐系统的一部分。推荐系统决定推什么商品，扩散模型改善商品怎么展示，bandit 学习不同用户更吃哪种展示风格。
