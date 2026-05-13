# Prompt-to-Slate: Diffusion Models for Prompt-Conditioned Slate Generation

- Short name: `DMSG`
- Year: `2024 / 2025`
- Task: `Slate recommendation / playlist or bundle generation`
- URL: [arXiv](https://arxiv.org/abs/2408.06883)
- ACM: [DOI](https://dl.acm.org/doi/10.1145/3705328.3748072)

## Core idea

Prompt-to-Slate shifts the recommendation target from "rank one item at a time" to **generate an entire slate** conditioned on a prompt or context. Instead of producing a single next item, the model generates a latent representation for a whole recommendation set such as a playlist, bundle, or multi-item response panel.

## Model intuition

The core module is a Diffusion Transformer that combines prompt or context information with noisy slate latents through cross-attention. This setup is well matched to slate recommendation because dependencies inside the generated set matter: diversity, compatibility, and coherence are all multi-item properties.

## Why it matters here

This paper is useful for broadening the survey scope beyond next-item recommendation. It shows how diffusion transformers can be used not only for preference recovery but also for **structured set generation** in recommendation.

## Reading focus

1. How the slate latent is parameterized.
2. What kinds of prompts or contexts are supported.
3. Whether the model explicitly controls intra-slate diversity or coherence during denoising.
