# Dual Conditional Diffusion Models for Sequential Recommendation

- Short names: `DCRec`, `DCDT`
- Year: `2024 / 2025`
- Task: `Sequential recommendation`
- URL: [arXiv](https://arxiv.org/abs/2410.21967)
- ACM: [DOI](https://dl.acm.org/doi/10.1145/3773966.3777926)

## Core idea

DCRec argues that implicit behavior sequences alone are often insufficient for accurate sequential recommendation. To address this, the method injects **conditional information into both forward and reverse diffusion** stages instead of using conditions only at the final prediction layer.

## Model intuition

Its main architecture, the **Dual Conditional Diffusion Transformer** (`DCDT`), uses cross-attention to fuse explicit signals with implicit sequence representations. The goal is to keep the diffusion process aligned with actual user intent and suppress irrelevant or noisy historical behaviors.

## Why it matters here

This paper fits the "Diffusion Transformer in recommender systems" bucket more tightly than many earlier diffusion recommenders because the transformer is not merely an encoder that provides guidance. The diffusion path itself is designed to stay condition-aware throughout generation and denoising.

## Reading focus

1. What counts as explicit conditional information in the paper.
2. Where conditions enter the forward process and where they enter the reverse process.
3. Whether the main gains come from dual conditioning or from transformer-based denoising capacity.
