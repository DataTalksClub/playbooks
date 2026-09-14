# Handoff Brief: Agent Observability Starts With Ingestion

Source: /Users/valeria/.codex/content-runs/2026-07-24-ingesting-agent-traces-dlthub/source/transcript.json

## 00:47:49 - 00:49:23

And actually this is our part two. Um okay. What happened when you build agent? Yeah. Your agent lives somewhere else not on your local laptop. And um for example we built internally our um our AI assistant. You can talk to it. Yeah. like um what is ZT and we can collect all the information about this session using loggers. >> Mhm. You will learn you students yeah you viewers users you will learn more about monitoring about logging uh later in um further lessons but uh for our um workshop I will talk about logfire >> because we use it in internally logfire it's a pentic um native um logger it collects all the information similar to your clo traces it collects a lot of metadata like usage models. Yeah. What tooling was uh called? Uh what um skills used. Yeah. So collects a lot of information. It's very useful to know how our agent works. So we don't much care about uh questions and answers here. Logging means uh how agent works, how uh we can optimize it, what is the performance. Um [clears throat]

## 00:51:33 - 00:52:48

so I just imitate this process building this API with a couple of endpoints. One end point gives us code um uh traces format and another like log fire logs gives us another type of logs because for each tool you have different type of traces and logs. They all have different structure, different different keys, different order of um fields. Yeah. So different type of nesting. It's very difficult to work with this data if you have several agents. Uh and usually you will have several agents. you will have um agent for your cloud assistants for co-worker for um for custom agents. Yeah. So it will always be a problem to have different types of logs and what you can do with it you can download these logs you can request it through API and load it in a structured format somewhere else. Yeah, in a database for example. That's what
