# EDGE-Rec: Efficient and Data-Guided Edge Diffusion For Recommender Systems Graphs

- Year: `2024`
- Task: `Edge prediction / interaction or rating prediction`
- URL: [arXiv](https://arxiv.org/abs/2409.14689)
- Code: [GitHub](https://github.com/upriyam-cmu/EDGE-Rec)

## Core idea

EDGE-Rec directly models recommendation graphs from the perspective of **edges** rather than only node embeddings. The paper introduces a Graph Diffusion Transformer, `GDiT`, which diffuses over the user-item interaction matrix or edge weights and then denoises them under user and item feature conditions.

## Model intuition

The conditioning signal is important here: instead of treating edge recovery as an unconditional generative task, the model uses user and item side information to guide the denoising process. The paper also proposes **Row-Column Separable Attention** so the transformer can handle large interaction matrices more efficiently than naive full attention.

## Why it matters here

This is one of the cleaner cases where a diffusion-style transformer is used for recommendation graph generation or recovery in a way that is operationally close to denoising a matrix-valued recommendation signal.

## Reading focus

1. Whether diffusion is performed on binary edges, weighted edges, or both.
2. How Row-Column Separable Attention changes complexity.
3. How much improvement comes from conditioning versus the denoiser architecture itself.
