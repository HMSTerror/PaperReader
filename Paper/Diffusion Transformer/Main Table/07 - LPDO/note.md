# Listwise Preference Diffusion Optimization for User Behavior Trajectories Prediction

- Short name: `LPDO`
- Year: `2025 / 2026`
- Task: `User behavior trajectory prediction`
- URL: [OpenReview](https://openreview.net/forum?id=x5KUOlYKQr)

## Core idea

LPDO extends the horizon of sequential recommendation by generating **future behavior trajectories** rather than predicting only the next item. The model uses diffusion to produce a sequence of future actions and then optimizes that sequence with a listwise preference perspective inspired by Plackett-Luce style ranking.

## Model intuition

According to the supplementary description, the method employs a **Cross-Conditional Diffusion Transformer** with cross-step attention so that future actions are not generated independently. This matters because multi-step behavior prediction requires modeling dependencies among several future choices, not just user-to-item relevance at one timestamp.

## Why it matters here

This paper is valuable if your survey wants to show how diffusion transformers move from next-step recommendation to **trajectory-level generation and planning-like prediction**.

## Reading focus

1. How listwise preference optimization is integrated with diffusion training.
2. How cross-step attention models dependency among future actions.
3. Whether trajectory metrics differ substantially from standard next-item recommendation metrics.
