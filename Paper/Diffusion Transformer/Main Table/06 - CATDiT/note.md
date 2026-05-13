# Continuous Data Augmentation via Condition-Tokenized Diffusion Transformer for Sequential Recommendation

- Short name: `CATDiT`
- Year: `2025`
- Task: `Sequential recommendation data augmentation`
- ACM: [DOI](https://dl.acm.org/doi/10.1145/3746252.3761396)
- DBLP: [Entry](https://dblp.org/rec/conf/cikm/ShiWT25)

## Core idea

CATDiT focuses on data augmentation for sequential recommendation and directly addresses a recurring problem in diffusion-based discrete recommendation: generating continuous embeddings and then mapping them back to discrete items can introduce semantic drift. The paper avoids this by **keeping the augmentation target in continuous embedding space**.

## Model intuition

Its **Condition-Tokenized Diffusion Transformer** injects user-intent-related conditions into the denoising process, so the synthesized embeddings are more aligned with user preference rather than being generic perturbations. The generated continuous samples are then used as augmented training data for downstream sequential recommenders.

## Why it matters here

This paper is notable because it uses diffusion transformers not as the final recommender directly, but as a **recommendation-oriented augmentation engine**. That makes it relevant when discussing how diffusion transformers can contribute to recommendation pipelines even when they are not the final prediction head.

## Reading focus

1. How condition tokens are constructed.
2. How augmented continuous samples are consumed by the downstream recommender.
3. Whether the gains are strongest in sparse-data or long-tail settings.
