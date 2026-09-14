# Handoff Brief: Asking An Agent To Re-Scan Raw Logs Does Not Scale

Source: /Users/valeria/.codex/content-runs/2026-07-24-ingesting-agent-traces-dlthub/source/transcript.json

## 00:09:32 - 00:10:35

uh for example yeah how we can use this uh logs we can ask plot to read all of them, go through all of them. Um, and answer a question. Yeah. Um, now it will take a while. So, it needs to read everything. It needs to um get some insights from it. It also will take quite um some amount of tokens. Mhm. So, it's aggregating And if I want to change my request like okay how many tokens I used last month or yeah or last uh six months it will do the same work again and again it's probably will reuse some cash. Yeah but um uh still it will do a lot of extra work. So y here is our breakdown. So it's very nice. At least I can do

## 00:10:43 - 00:12:18

maybe you need to reload your laptop for sure. Um, so what if I want to share this information with my colleagues? Not about my personal usage. Yeah. But what if my company wants to know how much tokens I use every day, every week? Uh, or I need to track myself how much tokens I use. um to control my uh consumption. Um again, yeah, we have this um dashboard here. We can track how many people um use this um cloud code, who spans the most of the tokens. So, we can correct Yeah. this behavior. We can ask people, yeah, I don't know this me. Yeah. uh so I I cannot share my local logs with my uh colleagues and they not going to do that uh for me as well. Um what we're going to do is instead we will take um so what we did already here we took uh entropic API we built data pipeline which will take logs from the cloud from the entropic cloud um and load this data to our destination to our database or I don't know a bunch of files yeah and I can um run this pipeline every day so it keep it fresh keep it updated and um build reports on top of it and deploy
