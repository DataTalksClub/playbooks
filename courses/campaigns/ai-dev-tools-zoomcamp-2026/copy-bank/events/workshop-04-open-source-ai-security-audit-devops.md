Title: DevOps and Observability for AI-Built Apps
Hosted by Grace Lordel Domisiw & Alexey Grigorev
Date: Tuesday, August 18, 2026
Time: 2:00 PM - 3:30 PM GMT+2 / Europe/Madrid
Location: YouTube
Registration: https://luma.com/ycsfxigi

## Launch Positioning

Role in launch: Shows what has to happen after an AI-assisted app is deployed: observability, alerting, incident investigation, bounded response, recovery verification, and audit.

Main audience: Developers, AI engineers, MLOps engineers, DevOps practitioners, and technical leads who want to ship AI-built applications without losing visibility or control in production.

Main promise: You will understand how to tell whether your deployed app still works, and how to put a coding agent in the incident loop without giving it production access.

Course connection: Updates Module 4 and shows the DevOps, observability, security, audit, and responder-governance practices learners can apply to their final project.

## About Event

This is the 4th workshop in our series to update the AI Dev Tools Zoomcamp content.

This workshop updates [Module 4: DevOps and Observability for AI-Built Apps](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/04-devops?utm_source=luma).

The previous workshop ended with an app that deploys automatically when the tests pass. That gets it online. It does not tell you whether it still works.

In this hands-on session, Alexey Grigorev will build the loop that closes that gap: observe user impact, alert with context, investigate from evidence, authorize a bounded response or escalate, verify recovery, and audit both the code and the response trail.

We also put a coding agent inside that loop as the first line of support. It collects the same evidence you would, compares it with recent changes, and proposes an action. What it does not get is production credentials. A model supplies confidence. Code outside the model enforces permission.

## What You'll Learn

- Which questions you cannot answer about your own deployed app right now, and why a dashboard full of CPU graphs is not observability
- How to instrument one important endpoint end to end with OpenTelemetry, so a metric, a trace, and a log all describe the same failed request
- What must never reach your telemetry: passwords, tokens, request bodies, user names
- How to run the pipeline behind a Collector instead of exporting from the app to each backend, with Prometheus for metrics, Loki for logs, Tempo for traces, and Grafana on top
- How to write one alert you would want to be woken up for, with a payload that includes the symptom, the dashboard link, the deployed version, and the runbook
- Why forty alerts you have learned to ignore are worse than one you trust
- How to collect a bounded evidence packet with allowlisted read-only queries before any model is involved
- How to run Codex or Claude Code headless as a read-only investigator that returns facts, ranked hypotheses, a proposed action, and its own uncertainty against a fixed schema
- Why authorization belongs outside the model, and what an action allowlist and autonomy levels look like in practice
- How to run the same incident twice and watch the policy force an escalation the second time, with no change to the agent
- How to layer a security audit: a deterministic scanner for evidence, a model for context and abuse paths, a person to decide
- How to inventory the responder's own capabilities in a permission table, because a prompt that says "read only" is not a read-only token
- Where PR-Agent, Semgrep MCP, Snyk Agent Scan, K8sGPT, HolmesGPT, LiteLLM, and Ollama fit once the problems have names

By the end, you will know how to tell whether your deployed app still works. You will also know how to put an agent in the incident loop without giving it production access, and how to audit both the code it ships and the agent that responds.

Like the other workshops, this will be a live demo with practical tips and time for Q&A.

## All Events in This Series

- [How to Work with AI Coding Agents: Spec-Driven Development, Context and Loop Engineering, Workflows](https://luma.com/lmkti8zj)
- [Build and Ship an AI-Assisted Full-Stack App](https://luma.com/50kvfku2)
- [Test, Containerize, and Deploy an AI-Assisted App](https://luma.com/v5tjy562)
- [DevOps and Observability for AI-Built Apps](https://luma.com/ycsfxigi)
- [AI Dev Tools Zoomcamp 2026 Pre-Course Live Q&A](https://luma.com/a8qa5s2s)
- [AI Dev Tools Zoomcamp 2026 Course Launch](https://luma.com/tsiusx8s)

## Thinking About Joining AI Dev Tools Zoomcamp?

This workshop covers the updated content for [Module 4](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/tree/main/04-devops?utm_source=luma) of [AI Dev Tools Zoomcamp](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp?utm_source=luma), our free course on using AI tools in practical software development workflows.

The course covers AI-assisted planning, coding, review, testing, coding agent capabilities, MCP, skills, plugins, security, audit, DevOps, and a complete final project.

The new cohort of AI Dev Tools Zoomcamp starts on August 31, 2026. You can join it by [registering here](https://courses.datatalks.club/register/ai-dev-tools/?utm_source=luma).

## About the Speaker

Alexey Grigorev is the Founder of DataTalks.Club and creator of the Zoomcamp series.

Alexey is a software and ML engineer with over 10 years in engineering and 6+ years in machine learning. He has deployed large-scale ML systems at companies like OLX Group and Simplaex, authored several technical books, including Machine Learning Bookcamp, and is a Kaggle Master with a 1st place finish in the NIPS'17 Criteo Challenge.

[DataTalks.Club](http://datatalks.club/?utm_source=luma) is the place to talk about data. [Join our Slack community](https://datatalks.club/slack.html?utm_source=luma)!
