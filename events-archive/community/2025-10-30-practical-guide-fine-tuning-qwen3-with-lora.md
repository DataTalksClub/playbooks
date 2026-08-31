# Practical guide: Fine-tuning Qwen3 with LoRA

- **Type:** Workshop
- **Date:** Thursday, October 30, 2025
- **Time:** 12:30 Europe/Berlin
- **Instructor:** Ivan Potapov
- **Luma:** https://luma.com/n41kqkfh
- **Related course:** Open-Source LLM Zoomcamp (adjacent, not part of the series)

## About Event

**Ivan Potapov - Research Engineer, Zalando SE**

In this workshop, we fine-tune Qwen models with parameter-efficient adapters using two complementary approaches: Soft Prompt token tuning and LoRA SFT, with an optional KL-anchored SFT term to keep the model’s behavior close to the base while adding new styles and formats. You’ll see how to prepare open-source data (Dolly 15k), render with chat templates, run short training loops, and monitor validation loss/perplexity with stepwise evaluations.

A tiny KL toy example explains per‑token contributions to H(P), H(P,Q), and KL(P||Q), making the “anchoring” intuition concrete. By the end, you’ll know how to apply Soft Prompt for quick style steering, LoRA for deeper adaptation, and KL regularization to reduce drift and forgetting—plus how to save/load LoRA adapters for deployment.

[Notebook.](https://github.com/ivan-digital/llm-alignment/blob/master/Qwen3_Adapters_SoftPrompt_LoRA_KL_SFT_Workshop.executed.ipynb?utm_source=luma)

## About the speaker:

**Ivan Potapov** is a Research Engineer at Zalando, specializing in **search**. He has taught workshops on **data engineering, AI agents, and LLM alignment**, helping practitioners bridge software engineering with applied machine learning.

**[DataTalks.Club](http://datatalks.club/?utm_source=luma)** is the place to talk about data. **[Join our slack community](https://datatalks.club/slack.html?utm_source=luma)**!
