---
issue: 297
send_date: 2026-10-05
status: sent
subject: "📗 Free resource hub for agent memory | DataTalks.Club Weekly"
preview_text: "From a 7-minute explainer to a full offline RAG system on edge hardware: free tutorials and working code for agent memory."
mailchimp_title: "Weekly email #297 (Oct 5, 2026) - sponsored"
archive_url: https://mailchi.mp/datatalks.club/weekly-297
source: Mailchimp export (plain-text version, as sent)
---

## Free Resource Hub: Build Persistent Memory into AI Agents

Agent memory is an architecture problem, and a bigger context window won't fix an agent that keeps forgetting. Actian's free resource hub takes you from a 7-minute explainer on agent memory to a full offline RAG system running on edge hardware, with working code for CrewAI, mem0, LangChain, and OpenClaw.

- Build an agent that remembers users across sessions with no cloud dependency
- Self-host mem0 entirely on your own infrastructure, with no OpenAI or Qdrant required
- Deploy persistent agent memory on edge hardware with no internet connection

Browse Actian's Agent Memory Hub and start with the tutorial for the framework you already use; every implementation uses Actian VectorAI DB, which has a free Community Edition.

[Browse the resource hub](https://bki.sh/UElnLM7)

https://github.com/DataTalksClub/ai-dev-tools-zoomcamp

## Project 1

Module 5 was the final module, so this week is for your project. Project 1 is due October 27, 2026 at 00:00 CET (October 26 at 23:00 UTC).

Still finishing Homework 4? There's still time: you can submit it (https://courses.datatalks.club/ai-dev-tools-2026/homework/hw4) until October 6, 2026, at 01:00 CEST (October 5 at 23:00 UTC).

[Submit your project](https://courses.datatalks.club/ai-dev-tools-2026/project/project1)

https://github.com/DataTalksClub/machine-learning-zoomcamp

## Module 3: Machine Learning for Classification

Many real problems ask a yes-or-no question: will this customer leave, will this lead convert? In Module 3, we build a customer churn model with logistic regression and learn how to read what it predicts.

The deadline for Homework 3 is October 13, 2026 at 01:00 CEST (October 12 at 23:00 UTC).

Still finishing Homework 2? There's still time: you can submit it (https://courses.datatalks.club/ml-zoomcamp-2026/homework/hw02) until October 6, 2026 at 01:00 CEST (October 5 at 23:00 UTC).

Next week, Module 4 covers classification evaluation metrics.

[Join Module 3](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/main/03-classification)

[SPONSORED](https://datatalks.club/blog/sponsor-datatalks-club.html)

## A Data Engineer’s Guide to AI Orchestration with Airflow

The definitive guide for data engineers who are serious about orchestrating AI in production.

Written by Airflow experts, based on real-world examples, and complete with code snippets, DAG patterns, example architectures, and a companion GitHub repo.

Get the 100+ page technical guide to learn:

→ How to orchestrate any AI model with Airflow (any model, any harness)

→ Patterns for LLM, agent orchestration, and multi-agent workflows

→ How to add guardrails, structured outputs, and human review to AI tasks

[Download now](https://www.astronomer.io/ebooks/ai-orchestration-with-apache-airflow/?utm_campaign=2026q3-ebook-ai-orchestration-with-apache-airflow&utm_medium=paidmedia&utm_source=data-talks-club)

NEWS

## DataTalks.Club turned 6, and our Slack passed 100,000 members

DataTalks.Club turned 6 on September 19. We started in 2020 as a small community for data professionals. Since then:

- 100,000+ people have learned through our free courses in ML, data engineering, MLOps, and LLMs
- We've hosted 500+ podcasts, webinars, and workshops

Ten days later, on September 29, our Slack community passed 100,000 members. It has grown into a place where people learn ML, data engineering, and AI engineering together.

Thank you to everyone who joined, asked and answered questions, taught, and contributed. For the story behind it, listen to Alexey on our podcast (https://datatalks.club/podcast/datatalksclub-scaling-and-free-courses.html) .

[Join our Slack](https://datatalks.club/slack.html)

EVENTS

## Upcoming Events

TUE

6

OCT

PODCAST

Building an AI Platform, Part 2: Memory, Tools, Guardrails & Observability

5:30 PM CEST · Dewang Sultania

MON

2

NOV

WEBINAR

GraphRAG in Real-Life Use Cases

12:30 PM CEST · Daan Di Scala

See all upcoming events (https://lu.ma/dtc-events) · Add our events to your calendar (https://calendar.google.com/calendar/?cid=ZjhxaWRqbnEwamhzY3A4ODA5azFlZ2hzNjBAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ)

RECORDINGS

## Workshop Recording: Build an LLM Wiki for Agent Long-Term Memory

On September 8, Paul Iusztin, founder of Decoding AI and author of the LLM Engineer's Handbook, joined us for a hands-on workshop on long-term memory for AI agents. Together we built an LLM Wiki: a knowledge base of cross-linked Markdown files that an agent maintains, without a graph database. We covered:

- Index files for progressive context disclosure
- Ingesting code repos, articles, transcripts, and notes
- Fan-out subagents that process many sources in parallel
- Keeping the wiki up to date as new data arrives

## Podcast Recording: Building an AI Platform, Part 1

On September 29, Suhas Suresha, Senior Machine Learning Engineer at Adobe and co-author of Designing AI Systems, started our series on building AI platforms. We talked about why a prototype built in an evening is far from production, and what a shared platform gives teams instead:

- A model service with routing, failover, and rate limits
- A data service for parsing, chunking, and vector search
- Observability, evaluation, and experimentation
- Memory, tools, guardrails, and orchestration

Part 2 with Dewang Sultania is on October 6.

READ

## Book of the Week: Designing AI Systems

On October 12-16, Suhas Suresha and Dewang Sultania join us to discuss Designing AI Systems.

Their book shows how to build a shared platform for AI applications, covering memory, company data, and safe tool use, with complete Python code.

To take part, join our Slack and ask your questions in #book-of-the-week. [Author first name] will answer questions Monday through Thursday and choose the winners of free book copies on Friday.

[Participate here](https://datatalks.club/books/20261012-designing-ai-systems.html)

## From Alexey on Data: Why I Stopped Using tmux

Do you run coding agents on a remote machine and lose every session when one process runs out of memory?

In his new newsletter, Alexey explains why tmux stopped working for his agents and introduces aplexer, an agent multiplexer written in Rust:

- How PTYs, SSH, and tmux keep processes alive after a disconnect
- How one out-of-memory kill can take down the tmux server and every session
- Why aplexer gives each session its own worker instead of a shared server
- How agents in different sessions send each other messages

[Read here](https://aishippingblog.com/p/aplexer-why-i-stopped-using-tmux)

DataTalks.Club is a global community of data enthusiasts. If you haven't had a chance to join our Slack yet, use this invite link (http://join.datatalks.club/) . If you have problems with the invite link, fill in this form (https://airtable.com/shrhUBN51Jy10fjJq) , and we'll add you to Slack manually.

Do you have any questions? Hit reply, and we'll be glad to answer.

See you in Slack!

Forward to a friend (*|FORWARD|*) · Subscribe (*|LIST:SUBSCRIBE|*) · Past issues (https://us19.campaign-archive.com/home/?u=0d7822ab98152f5afc118c176&id=97178021aa) · Sponsor this newsletter (https://datatalks.club/blog/sponsor-datatalks-club.html)

https://twitter.com/datatalksclub

https://linkedin.com/company/datatalks-club

https://www.youtube.com/c/DataTalksClub

https://datatalks.club/

mailto:alexey@datatalks.club

Copyright (C) *|CURRENT_YEAR|* *|LIST:COMPANY|*. All rights reserved.

*|IFNOT:ARCHIVE_PAGE|**|LIST:DESCRIPTION|**|END:IF|*

Our mailing address is:

*|IFNOT:ARCHIVE_PAGE|**|LIST_ADDRESS|**|END:IF|*

Want to change how you receive these emails?

You can update your preferences (*|UPDATE_PROFILE|*) or unsubscribe (*|UNSUB|*)
