# A Directional Diffusion Graph Transformer for Recommendation

- Short name: `DiffGT`
- Year: `2024`
- Task: `Top-K recommendation`
- URL: [arXiv](https://arxiv.org/abs/2404.03326)

## Core idea

DiffGT treats the user-item interaction graph as a noisy graph structure and performs diffusion directly over the graph. Its key distinction is that the forward diffusion is not plain isotropic random noise. Instead, it introduces **directional Gaussian noise** designed around graph structure, so the corruption process better reflects how recommendation signals propagate over user-item interactions.

## Model intuition

The reverse process uses a Graph Transformer to denoise the corrupted graph states and recover robust user and item representations. In practice, the method tries to make graph representation learning less brittle by exposing the model to structure-aware corruption and then asking it to reconstruct preference-relevant signals.

## Why it matters here

This paper is a good example of "diffusion + transformer" in recommendation, even though the transformer is graph-oriented rather than a vanilla DiT block. Its contribution is especially meaningful on the **forward process design** side: the diffusion mechanism itself is tailored to recommendation graphs instead of being borrowed unchanged from generic generative modeling.

## Reading focus

1. How the directional noise is defined on user-item interaction graphs.
2. What information the Graph Transformer uses during denoising.
3. Whether the gains mainly come from graph-aware diffusion or from the transformer denoiser.
