# Context Engineering for Agentic Hybrid Applications

- **Type:** Webinar
- **Date:** Tuesday, March 10, 2026
- **Time:** 17:00 Europe/Berlin
- **Instructor:** Ivan Potapov, Tobias Lindenbauer
- **Luma:** https://luma.com/4298mc3j
- **Related course:** LLM Zoomcamp (adjacent, not part of the series)

## About Event

**Research survey and upcoming trends discussion - Ivan Potapov and Tobias Lindenbauer**

As an agent keeps running, its context window balloons with tool logs, stale diffs, and repeated data dumps. The model starts drowning in irrelevant details and falls victim to "lost-in-the-middle" effects — missing critical facts buried deep in oversized prompts.

We'll walk through research for keeping only high-signal observations: masking vs. summarization trade-offs, compressing bulky tool output (drawing from ideas like LLMLingua-2), and pruning dead branches from the agent's trajectory so it stops dragging noise forward. We'll also share insights on cutting LLM call costs along the way.

Then we'll connect those techniques to bigger-picture design: **memory hierarchies (session → working set → notes → cross-session)** and standardized tool interfaces like MCP that reduce "context debt" and keep the agent's working set clean.

Finally, we'll look at where the field is heading — toward a world where Context Engineering becomes something you train, not just script.

## About the Speakers:

**Tobias Lindenbauer** is an AI researcher at JetBrains Research, where he advances efficient and effective code agents that robustly solve long-horizon software engineering tasks. Currently, he is most interested in efficiency topics, context management, interpretability and data synthesis. He recently presented “The Complexity Trap: Simple Observation Masking Is as Efficient as LLM Summarization for Agent Context Management” at the Deep Learning for Code workshop at NeurIPS 2025, highlighting practical pitfalls of LLM summarization-based context strategies and evidence for more computationally efficient alternatives.

**Ivan Potapov** is a Research Engineer in Discovery Search & Ranking at Zalando, where he builds search retrieval and ranking systems. He teaches data engineering, AI agents, and LLM alignment, with a focus on bridging software engineering and applied ML. His recent work centers on long-running agents and context engineering—memory, state, and retrieval—exploring why many code-first agent designs fall short. His key thesis: context management is becoming something we train and iterate on, not just script. [https://blog.ivan.digital/context-engineering-for-agentic-hybrid-applications-why-code-agents-fail-and-how-to-fix-them-076cab699262](https://blog.ivan.digital/context-engineering-for-agentic-hybrid-applications-why-code-agents-fail-and-how-to-fix-them-076cab699262?utm_source=luma)

**[DataTalks.Club](http://datatalks.club/?utm_source=luma) is the place to talk about data. [Join our Slack community](https://datatalks.club/slack.html?utm_source=luma)!**
