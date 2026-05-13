# Generate and Instantiate What You Prefer: Text-Guided Diffusion for Sequential Recommendation

- Short name: `iDreamRec`
- Year: `2024 / 2025`
- Task: `Text-guided sequential recommendation`
- URL: [arXiv](https://arxiv.org/abs/2410.13428)

## Core idea

iDreamRec enhances sequential recommendation with **text-guided user intent modeling**. The paper first improves item representation through text descriptions and LLM-related embeddings, then uses a diffusion model to generate the embedding of an "ideal item" the user is likely to prefer next.

## Model intuition

The method section explicitly adopts a **Diffusion Transformer Block with in-context conditioning**. This means text or intent context is not an afterthought; it actively participates in the denoising path so the generated target embedding better reflects semantic user preference rather than only collaborative sequence patterns.

## Why it matters here

This paper is especially interesting when comparing recommendation diffusion models that are purely behavior-driven against those that are **semantically grounded by text**. It sits at the intersection of sequence modeling, text-conditioned generation, and diffusion transformers.

## Reading focus

1. How text descriptions are turned into usable recommendation conditions.
2. Whether the generated "ideal item embedding" is later matched to an item catalog by nearest-neighbor retrieval.
3. How much of the gain comes from richer item semantics versus the diffusion transformer itself.
