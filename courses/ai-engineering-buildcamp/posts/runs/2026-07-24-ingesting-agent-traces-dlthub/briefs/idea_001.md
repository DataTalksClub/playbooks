# Handoff Brief: Agent Traces Are Data, Not Just Local Log Files

Source: /Users/valeria/.codex/content-runs/2026-07-24-ingesting-agent-traces-dlthub/source/transcript.json

## 00:01:27 - 00:02:36

they work together. So today we will um like marry these two worlds because um uh you learn how to use agents, how to build agents, but you probably don't know how many data it produced. Um for example uh when you run your cloud code or codeex or copilot uh locally in your EDA do you know that actually agent will store all this data metadata about your sessions locally on your laptop. So you have a lot of useful data on your laptop right now and you do what you can do with this data. You can just uh run clot and ask questions about this data like hey clot can you tell me how much tokens I used last uh month or you can ask hey clot can you check if some secrets were leaked um in my logs?

## 00:06:04 - 00:07:50

it's quite difficult to explore these logs manually but instead of it we can build something look like this what do you see now it's um Tilty Hub platform I just deployed my injestion pipeline here build dashboard and now I can see how much our um DY hub company actually spent uh in total for cloud code it's the secret information. I still want to show it to you because it's so cool. Um, so instead of these unreadable logs, you can build dashboards. You can see usage for every day, what kind of models you use. Yeah. Yeah. Recently we use Opus quite a lot. Yeah, that's why it's so expensive. >> Well, payable would be more expensive, right? >> Yeah, we not a big fans of to be honest. >> It's too expensive, right? >> Yes. So, this is what we want to build um during this workshop. this like similar dashboard because we're not going to use our um internal data of course. Uh we will start with your local traces.
