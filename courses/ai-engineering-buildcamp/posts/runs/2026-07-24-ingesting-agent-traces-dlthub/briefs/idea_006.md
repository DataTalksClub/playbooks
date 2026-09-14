# Handoff Brief: Local Dashboards Are Useful; Shared Dashboards Need Deployment

Source: /Users/valeria/.codex/content-runs/2026-07-24-ingesting-agent-traces-dlthub/source/transcript.json

## 01:16:37 - 01:17:32

Alex say you can sum up what we're doing now because you you do that great. >> Yeah. Um so what we do is we already have this uh dashboards right u that we see. So first of all we ingested this local data then we ingested the data from this API and uh right now I don't want to correct me if I'm wrong. So right now we want to share it with the team. Right. So this is what we started at the beginning. At the beginning we we said okay we want to build this thing that is sharable. So now we want to um actually run the not only to be able to to share it with the rest of the team but also run the injection somewhere in the in the cloud right >> and u this is why we use DT hub so all the things will run there and there we will have the dashboard and this dashboard we can share with the team. We will not be able to do this with the local files those right though right?

## 01:19:08 - 01:20:18

>> So DT hub uh the DT hub platform is >> it's a host is a way to host our DT uh pipelines, right? So what we did locally was a DT hub pipeline, right? So we could do this locally but it's not easy to share. we need to have our computer up and running, right? But with the DT hub platform, all runs there, right? We don't have to worry about those things. >> Correct. You can uh run them here. You can uh schedule them. You can also create um uh pipes like run this pipeline and if it success um run this pipeline then run transformations. If these both injection pipelines succeeded uh then run report. Yeah. So it can be uh connected and triggered uh by rules you provide and um yeah also it's not only about data pipelines, it's also about the reports. So you can deploy any application you want like streaml application, marob notebook application >> and um share it with your team.
