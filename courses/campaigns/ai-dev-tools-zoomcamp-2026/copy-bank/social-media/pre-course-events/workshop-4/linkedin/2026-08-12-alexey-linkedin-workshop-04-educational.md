---
owner: "alexey"
date: "2026-08-12"
platform: "Alexey LinkedIn"
status: "draft"
event: "Workshop 4: DevOps and Observability for AI-Built Apps"
sequence_slot: "Educational post"
relative_day: "T-6"
created: "2026-08-10"
---

# Post

A dashboard full of CPU graphs rarely answers the question you actually have during an incident.

You want to know what users are experiencing, which request failed, what changed recently, whether the problem is still happening, and what action is safe to take.

For that, one important endpoint needs connected evidence:

- A metric that shows the symptom
- A trace that shows where the request went
- A log that explains what happened
- A deployed version to compare against
- A runbook that says what to check next

Then, before any model is involved, we need a bounded evidence packet: only allowlisted read-only queries, no secrets, no request bodies, no user names, no production write access.

In Workshop 4 of AI Dev Tools Zoomcamp, I will build this flow and show how a coding agent can act as a read-only investigator. It returns facts, ranked hypotheses, a proposed action, and uncertainty against a fixed schema.

Authorization stays outside the model.

Tuesday, August 18, 2:00 PM GMT+2. RSVP: https://luma.com/ycsfxigi

# Notes

- Angle: Teach the observability-to-evidence chain and connect it to read-only agent investigation.
- CTA: RSVP for Workshop 4.
- Source material: `copy-bank/events/workshop-04-open-source-ai-security-audit-devops.md`.
