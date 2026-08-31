---
owner: "alexey"
date: "2026-08-10"
platform: "Alexey Newsletter"
status: "draft"
event: "Workshop 4: DevOps and Observability for AI-Built Apps"
sequence_slot: "Main announcement"
relative_day: "T-8"
created: "2026-08-10"
---

# Newsletter Section

## Knowing whether the deployed app still works

On August 18, Grace Lordel Domisiw and I are running the fourth free workshop for AI Dev Tools Zoomcamp 2026:

DevOps and Observability for AI-Built Apps

The previous workshop ended with an app that deploys automatically when the tests pass. This is a useful milestone, but it does not answer the next production question:

Does the app still work for users?

In this workshop, I will build the loop that answers that question. We will instrument one important endpoint with OpenTelemetry so a metric, a trace, and a log describe the same failed request. We will run the telemetry pipeline behind a Collector, with Prometheus for metrics, Loki for logs, Tempo for traces, and Grafana on top.

Then we will write an alert that is actually useful: symptom, dashboard link, deployed version, and runbook. Forty alerts you ignore are worse than one alert you trust.

After that, we will add a coding agent to the incident loop. The agent will collect a bounded evidence packet with allowlisted read-only queries, compare the evidence with recent changes, and return facts, ranked hypotheses, a proposed action, and uncertainty against a fixed schema.

The important boundary: the agent does not get production credentials. Authorization belongs outside the model. A model can supply confidence; code outside the model enforces permissions, action allowlists, and autonomy levels.

We will also cover how to audit both the code and the responder itself: deterministic scanners for evidence, model-based context and abuse-path analysis, and a person deciding what is allowed.

Join if you want to deploy AI-built apps and still have a clear way to observe, investigate, respond, recover, and audit.

Tuesday, August 18
2:00 PM to 3:30 PM GMT+2
Live on YouTube

RSVP: https://luma.com/ycsfxigi

# Notes

- Angle: Explain why deployment needs an observability and incident-response loop, then introduce safe agent investigation.
- CTA: RSVP for Workshop 4.
- Source material: `copy-bank/events/workshop-04-open-source-ai-security-audit-devops.md`.
