# Diffusion Generative Recommendation with Continuous Tokens

- Short name: `ContRec`
- Position in this collection: `Related but not counted as a strict Diffusion Transformer backbone`
- URL: [arXiv](https://arxiv.org/abs/2504.12007)

## Why it is related

ContRec is clearly relevant to diffusion-based recommendation and transformer-related generative modeling. It explores recommendation through **continuous token generation**, which makes it conceptually close to some diffusion-transformer approaches that prefer continuous latent spaces over discrete item IDs.

## Why it is not in the main table

The paper's center of gravity is continuous-token generative recommendation, not the explicit proposal of a **Diffusion Transformer as the core named architectural contribution**. It belongs in the neighborhood, but not in the strictest "DiT in recommender systems" bucket.

## Reading focus

1. How continuous tokens are defined and decoded.
2. How its formulation overlaps with CATDiT-style continuous-space reasoning.
3. Whether its architectural emphasis is more on tokenization than on denoising transformer design.
