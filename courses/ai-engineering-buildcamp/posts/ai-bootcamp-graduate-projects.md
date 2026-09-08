---
platform: x
status: published
typefully_id: 7600493
date: 2025-12-30
url: "https://x.com/Al_Grigor/status/2006017526770327556"
typefully_url: "https://typefully.com/?d=7600493&a=188312"
title: "AI Bootcamp Graduate Projects"
tags: ["ai-engineering-buildcamp"]
media_ids: ["b19583d8-1543-4470-9e94-cb0fa9ab3121","c3dc4c3d-57ca-4938-9f3b-efa64ba3657c","186a2729-29d7-46bb-b7a1-9221c0945da2","fea5eae4-dae0-433f-a804-b54427540c33","e7038560-9855-437f-805e-e75208fe704e","3514c481-5d2f-4ea2-a1c5-40d57fdcd53a","3f2473bb-a157-4341-a625-cca359002c59","1b4c11ef-afc0-4953-9a61-86cd607671b7"]
---

1/7

4 AI agents built by AI Bootcamp graduates:

1. Cybersecurity Disclosure Agent
2. User Satisfaction Analyst
3. Habit Builder Agent
4. Intelligent Email Agent

🧵

2/7

1. Cybersecurity Disclosure Agent

Scott DeGeest built an ingestion pipeline for SEC filings. The system parses raw, often malformed XML and performs entity resolution to link subsidiaries to parent companies. The cleaned data is indexed in Elasticsearch for retrieval.

3/7

2. User Satisfaction Analyst

Carlos Pumar-Frohberg implemented a multi-agent orchestrator. The main model routes queries based on intent. Unstructured text queries are sent to a MongoDB agent, while relationship questions are routed to a Neo4j graph agent.

4/7

3. Habit Builder Agent

Vanchesca Dinh built a high-fidelity RAG pipeline. She used Faster Whisper to transcribe audio feeds and stored embeddings in Qdrant. She implemented query rewriting for better retrieval and used Pydantic to enforce guardrails on the output.

5/7

4. Intelligent Email Agent

Asia Amodeo integrated the Gmail API directly with Elasticsearch. The system fetches emails and indexes them, enabling semantic search over a personal inbox through a Streamlit interface.

6/7

I wrote a detailed breakdown of the architecture for these projects in my recent post: https://alexeyondata.substack.com/p/5-ideas-for-ai-agents-and-openais

7/7

A new iteration of the AI Bootcamp starts on January 26, 2026.

It's live, hands-on, and focused on building production-ready AI agents step by step.

Course page: https://maven.com/alexey-grigorev/from-rag-to-agents
