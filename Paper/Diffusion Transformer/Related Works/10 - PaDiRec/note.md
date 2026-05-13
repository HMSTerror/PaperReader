# PaDiRec: Parameter Diffusion for Controllable Multi-Task Recommendation

- Short name: `PaDiRec`
- Position in this collection: `Related but not counted as a strict Diffusion Transformer backbone`
- URL: [OpenReview](https://openreview.net/forum?id=9Zq8fRF4am)

## Why it is related

PaDiRec is diffusion-based recommendation, but it operates at a different level from most interaction-denoising papers. Instead of diffusing over user behaviors, edges, or recommendation latents, it applies diffusion to **model parameters** for controllable multi-task recommendation.

## Why it is not in the main table

Because the diffusion target is the recommender's parameter space rather than the recommendation interaction modeling path, it does not fit the narrower definition of "Diffusion Transformer in recommender systems" used in the main table.

## Reading focus

1. What controllability means in the multi-task setting.
2. How parameter diffusion compares with data-level or sequence-level diffusion.
3. Whether this line could eventually connect back to transformer-based interaction modeling.
