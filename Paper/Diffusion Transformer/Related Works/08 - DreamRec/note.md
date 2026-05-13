# Generate What You Prefer: Reshaping Sequential Recommendation via Guided Diffusion

- Short name: `DreamRec`
- Position in this collection: `Related but not counted as a strict Diffusion Transformer backbone`
- URL: [arXiv](https://arxiv.org/abs/2310.20453)

## Why it is related

DreamRec is an important earlier diffusion paper for sequential recommendation. It strongly shaped the later line of work that treats recommendation as a guided generative process rather than only a discriminative ranking problem.

## Why it is not in the main table

The key reason is architectural: the paper is better described as **guided diffusion with transformer encoder guidance**, rather than a method that explicitly centers a DiT-style or diffusion-transformer denoising backbone. In other words, the transformer helps condition or guide the process, but it is not framed as the main diffusion transformer architecture in the same way as the main-table papers above.

## Reading focus

1. What type of guidance the transformer encoder provides.
2. How later works like DCRec or iDreamRec become more explicitly diffusion-transformer-centric.
3. Which parts of DreamRec became standard design patterns in later sequential diffusion recommenders.
