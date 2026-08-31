# Durable Agentic Workflows with Temporal.io

- **Type:** Workshop
- **Date:** Tuesday, December 16, 2025
- **Time:** 17:00 Europe/Berlin
- **Instructor:** Alexey Grigorev
- **Luma:** https://luma.com/xbfrz1zp
- **Course:** LLM Zoomcamp, Module 3 (AI Orchestration)

## About Event

In this workshop, you will learn how to create a durable research agent that can answer questions about any YouTube video, using DataTalksClub's podcast collection as the example dataset.

The focus will be on building a reliable end-to-end system: robust transcript ingestion, searchable indexing, and a durable deep-research agent powered by Temporal, Elasticsearch, and PydanticAI.

## 1. Ingesting and Stabilizing YouTube Transcripts

We begin by collecting transcripts from every podcast episode on the channel.

YouTube transcript retrieval is unstable by nature:

*   Transcripts may be missing or temporarily unavailable

*   We have rate limits

*   Proxies to bypass rate limits can be unreliable

You'll see these failure patterns and learn how to turn an unreliable data-fetching script into a Temporal workflow.

We'll implement retries, backoff, proxy rotation, and failure handling so the ingestion continues even when the environment is unreliable.

Once transcripts are consistently fetched, we'll index them in Elasticsearch for fast, structured retrieval.

## 2. Building the Deep-Research Agent

With a searchable index in place, we'll build an agent that can answer grounded questions about any indexed video.

Using PydanticAI, we'll define two core tools, a search tool and a file-retrieval tool, that allow the agent to locate relevant transcript segments and use them to generate accurate, source-based answers.

We then run the agent through Temporal, which gives us:

*   Durability for long-running queries

*   Clear workflow histories

*   Built-in logs and observability

*   Reproducible agent behavior

This creates an agent that is easy to inspect, debug, and keep in production.

By the end of the workshop, you’ll have a complete pattern for building a YouTube question-answering system with:

*   A stable ingestion pipeline

*   A searchable transcript index

*   A durable research agent on top of it

The approach generalizes to any YouTube channel or internal video library that needs reliable, auditable AI-powered research.

* * *

## About the speaker:

**Alexey Grigorev** is the Founder of DataTalks.Club and creator of the Zoomcamp series.

Alexey is a seasoned software and ML engineer with over 10 years in engineering and 6+ years in machine learning. He has deployed large-scale ML systems at companies like OLX Group and Simplaex, authored several technical books, including Machine Learning Bookcamp, and is a Kaggle Master with a 1st place finish in the NIPS'17 Criteo Challenge.

* * *

**[DataTalks.Club](http://datatalks.club/?utm_source=luma)** is the place to talk about data. **[Join our Slack community](https://datatalks.club/slack.html?utm_source=luma)!**

This event is sponsored by [Temporal](https://temporal.io/?_gl=1*1wqns7o*_gcl_au*MjExMTkzNzU4My4xNzYzOTMxOTE3*_ga*MTkyMDE2NjY1NC4xNzYzOTMxOTE3*_ga_R90Q9SJD3D*czE3NjM5MzQxNDckbzIkZzEkdDE3NjM5MzQxNjAkajQ3JGwwJGgw&utm_source=luma).
