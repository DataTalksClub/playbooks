# Transcript Context

Source: /Users/valeria/short-video-automation/A0LmmZf-ggM/full_transcript.json
Duration: 01:33:01
Segments: 1768

Use these windows to mine social post ideas across the full transcript. Ideas may span multiple windows.

## Window 001: 00:00:00 - 00:10:00

[00:00:00 - 00:00:04] So hi everyone, welcome to this
[00:00:02 - 00:00:06] workshop. So this workshop is a part of
[00:00:04 - 00:00:09] uh the course that we are doing right
[00:00:06 - 00:00:11] now. This course is called LLM Zoom
[00:00:09 - 00:00:13] camp. If you're taking this course uh
[00:00:11 - 00:00:15] this workshop is a part of the course,
[00:00:13 - 00:00:17] but we want to make this workshop uh
[00:00:15 - 00:00:18] independent from the course too. So it
[00:00:17 - 00:00:21] doesn't matter if you're taking the
[00:00:18 - 00:00:24] course uh or not, you will still learn
[00:00:21 - 00:00:28] something new. So um this is the the
[00:00:24 - 00:00:30] main idea and um but here if you are
[00:00:28 - 00:00:33] taking the course you can do a little
[00:00:30 - 00:00:36] extra like there is a homework um that
[00:00:33 - 00:00:39] will also include here. So you will see
[00:00:36 - 00:00:41] all these things um but for now I think
[00:00:39 - 00:00:43] um
[00:00:41 - 00:00:46] I don't know if I need to say anything
[00:00:43 - 00:00:49] else. Uh I think Alona you can just u
[00:00:46 - 00:00:51] introduce yourself and we can start uh
[00:00:49 - 00:00:53] with the workshop.
[00:00:51 - 00:00:56] >> Yeah. Thank you, Alexe. Uh, hello
[00:00:53 - 00:00:58] everyone. My name is Alona. I'm a
[00:00:56 - 00:01:01] machine learning engineer in the past. I
[00:00:58 - 00:01:04] worked um a lot with computer vision. I
[00:01:01 - 00:01:08] train models and uh it was like oh my
[00:01:04 - 00:01:10] god five years ago. So it's
[00:01:08 - 00:01:14] very different times and now I work at
[00:01:10 - 00:01:16] Delt Hub already more than three years.
[00:01:14 - 00:01:21] um worked more like data engineer and
[00:01:16 - 00:01:24] deil. So I know how to I know a lot
[00:01:21 - 00:01:27] about both worlds like machine learning
[00:01:24 - 00:01:32] world and data engineering world and how
[00:01:27 - 00:01:37] they work together. So today we will um
[00:01:32 - 00:01:40] like marry these two worlds because um
[00:01:37 - 00:01:42] uh you learn how to use agents, how to
[00:01:40 - 00:01:45] build agents,
[00:01:42 - 00:01:50] but you probably don't know how many
[00:01:45 - 00:01:52] data it produced. Um
[00:01:50 - 00:01:56] for example
[00:01:52 - 00:02:00] uh when you run your cloud code or
[00:01:56 - 00:02:03] codeex or copilot uh locally in your EDA
[00:02:00 - 00:02:07] do you know that actually agent will
[00:02:03 - 00:02:10] store all this data metadata about your
[00:02:07 - 00:02:12] sessions locally on your laptop. So you
[00:02:10 - 00:02:14] have a lot of useful data on your laptop
[00:02:12 - 00:02:18] right now and you do what you can do
[00:02:14 - 00:02:20] with this data. You can just uh run clot
[00:02:18 - 00:02:23] and ask questions about this data like
[00:02:20 - 00:02:26] hey clot can you tell me how much tokens
[00:02:23 - 00:02:30] I used last uh month
[00:02:26 - 00:02:36] or you can ask hey clot can you check if
[00:02:30 - 00:02:40] some secrets were leaked um in my logs?
[00:02:36 - 00:02:42] Um you can do that locally for sure and
[00:02:40 - 00:02:45] um let me probably start sharing my
[00:02:42 - 00:02:48] screen. I want to this workshop actually
[00:02:45 - 00:02:49] supposed to be very hands-on. So please
[00:02:48 - 00:02:53] if you have your laptops right now
[00:02:49 - 00:02:58] please open it like keep keep it open
[00:02:53 - 00:03:01] and um um repeat.
[00:02:58 - 00:03:05] So I start sharing my screen. There is
[00:03:01 - 00:03:10] my um PyCharm. It's EDA. You can use any
[00:03:05 - 00:03:13] DA you have uh PyCharm or VS code or
[00:03:10 - 00:03:16] just terminal or I don't know the
[00:03:13 - 00:03:19] notebook
[00:03:16 - 00:03:23] txt something. Um what I want to do
[00:03:19 - 00:03:25] right now I would like to show you what
[00:03:23 - 00:03:28] are agent traces.
[00:03:25 - 00:03:30] Um that's what what was I um talking
[00:03:28 - 00:03:33] about.
[00:03:30 - 00:03:36] I use clot. So you probably also use
[00:03:33 - 00:03:40] cloth or you use codeex or copilot and
[00:03:36 - 00:03:44] um I use it quite a lot and I want to
[00:03:40 - 00:03:46] show you today how much and um I wanted
[00:03:44 - 00:03:49] to ask to be honest I wanted to ask clot
[00:03:46 - 00:03:53] right now to show you this logs but I
[00:03:49 - 00:03:57] will do that myself manually this time.
[00:03:53 - 00:04:00] So I will go to my home directory then I
[00:03:57 - 00:04:04] will
[00:04:00 - 00:04:06] follow the clot directory for copilot or
[00:04:04 - 00:04:08] codex it could be different
[00:04:06 - 00:04:12] uh you can ask your agent or google it
[00:04:08 - 00:04:16] or you can just explore your home um
[00:04:12 - 00:04:18] directory and find um similar folder
[00:04:16 - 00:04:23] like cloics.
[00:04:18 - 00:04:26] So actually let me use this comment and
[00:04:23 - 00:04:29] see what we have in this folder. So we
[00:04:26 - 00:04:32] have
[00:04:29 - 00:04:35] um many many folders. I will use
[00:04:32 - 00:04:38] projects one. So it means that cloth
[00:04:35 - 00:04:40] keeps traces for each project I work
[00:04:38 - 00:04:43] with.
[00:04:40 - 00:04:48] So here you can see all my projects.
[00:04:43 - 00:04:52] It's mostly GitHub repos. I will choose
[00:04:48 - 00:04:55] um what I will choose for example this
[00:04:52 - 00:04:57] project that's what I was experimenting
[00:04:55 - 00:05:00] um
[00:04:57 - 00:05:03] last week was days
[00:05:00 - 00:05:03] and
[00:05:07 - 00:05:14] go there
[00:05:09 - 00:05:17] um no file territory. Okay, there is
[00:05:14 - 00:05:20] file and I want I want to see this JSON
[00:05:17 - 00:05:20] file.
[00:05:20 - 00:05:26] Um,
[00:05:23 - 00:05:29] you can repeat for me. So, what's
[00:05:26 - 00:05:33] inside? Oh, yeah. It's not very readable
[00:05:29 - 00:05:35] JSON file. It's a list of JSONs file.
[00:05:33 - 00:05:38] Uh, you can we what kind of information
[00:05:35 - 00:05:42] we keep here? Uh, for example,
[00:05:38 - 00:05:46] usage. Yeah. How much tokens we use?
[00:05:42 - 00:05:49] outputs, inputs, cache. Um,
[00:05:46 - 00:05:53] also we have all the information about
[00:05:49 - 00:05:58] let let me search about models. Yeah,
[00:05:53 - 00:06:00] recently I use a lot GL Oppus 4.8 eight
[00:05:58 - 00:06:02] or
[00:06:00 - 00:06:02] [clears throat]
[00:06:02 - 00:06:06] um
[00:06:04 - 00:06:08] it's quite difficult to explore these
[00:06:06 - 00:06:11] logs
[00:06:08 - 00:06:15] manually
[00:06:11 - 00:06:17] but instead of it we can build something
[00:06:15 - 00:06:20] look like
[00:06:17 - 00:06:20] this
[00:06:26 - 00:06:31] what do you see now it's um Tilty Hub
[00:06:29 - 00:06:34] platform
[00:06:31 - 00:06:37] I just deployed my injestion pipeline
[00:06:34 - 00:06:42] here build dashboard and now I can see
[00:06:37 - 00:06:46] how much our um DY hub company actually
[00:06:42 - 00:06:48] spent uh in total for cloud code it's
[00:06:46 - 00:06:50] the secret information.
[00:06:48 - 00:06:53] I still want to show it to you because
[00:06:50 - 00:06:57] it's so cool. Um, so instead of these
[00:06:53 - 00:06:58] unreadable logs, you can build
[00:06:57 - 00:07:01] dashboards.
[00:06:58 - 00:07:06] You can see usage for every day, what
[00:07:01 - 00:07:06] kind of models you use. Yeah.
[00:07:12 - 00:07:16] Yeah. Recently
[00:07:15 - 00:07:20] we use Opus
[00:07:16 - 00:07:25] quite a lot.
[00:07:20 - 00:07:25] Yeah, that's why it's so expensive.
[00:07:25 - 00:07:28] >> Well, payable would be more expensive,
[00:07:27 - 00:07:32] right?
[00:07:28 - 00:07:34] >> Yeah, we not a big fans of to be honest.
[00:07:32 - 00:07:37] >> It's too expensive, right?
[00:07:34 - 00:07:41] >> Yes. So, this is what we want to build
[00:07:37 - 00:07:43] um during this workshop. this like
[00:07:41 - 00:07:45] similar dashboard because we're not
[00:07:43 - 00:07:49] going to use our um internal data of
[00:07:45 - 00:07:50] course. Uh we will start with your local
[00:07:49 - 00:07:53] traces.
[00:07:50 - 00:07:56] Um
[00:07:53 - 00:08:00] so you know that everyone who uses uh
[00:07:56 - 00:08:03] agents locally have these traces locally
[00:08:00 - 00:08:06] on your machines. Now you have um like
[00:08:03 - 00:08:08] um few minutes to find them, open them
[00:08:06 - 00:08:10] or just ask your agent where is it. So
[00:08:08 - 00:08:11] you don't have to search it for
[00:08:10 - 00:08:13] [laughter]
[00:08:11 - 00:08:15] manually. Um you don't have to do
[00:08:13 - 00:08:17] manually anything anymore to be honest.
[00:08:15 - 00:08:20] >> So we can use any agent we want, right?
[00:08:17 - 00:08:23] Could be codex, it could call lot code,
[00:08:20 - 00:08:25] it could be open code, right? Anything
[00:08:23 - 00:08:27] we just ask, hey like where are the
[00:08:25 - 00:08:33] metadata about all the sessions, right?
[00:08:27 - 00:08:37] >> Yeah. So I think any agent stores um
[00:08:33 - 00:08:40] >> traces on your machine so you can try um
[00:08:37 - 00:08:42] what I want to do now I want to take
[00:08:40 - 00:08:48] this logs
[00:08:42 - 00:08:51] and um like let's ask clot
[00:08:48 - 00:08:53] and do something with it. Yes, of course
[00:08:51 - 00:08:56] I trust this folder. Um I give you all
[00:08:53 - 00:08:59] my data. Um, so
[00:08:56 - 00:09:01] >> are you using skip permissions mode?
[00:08:59 - 00:09:02] >> Uh, no, but I like auto mode own.
[00:09:01 - 00:09:05] [laughter]
[00:09:02 - 00:09:08] Um, but uh yeah, please be careful with
[00:09:05 - 00:09:11] your um skip permissions.
[00:09:08 - 00:09:11] Um
[00:09:18 - 00:09:21] um
[00:09:22 - 00:09:27] if I
[00:09:24 - 00:09:27] I don't know
[00:09:32 - 00:09:38] uh for example yeah how we can use this
[00:09:35 - 00:09:43] uh logs we can ask plot to read all of
[00:09:38 - 00:09:48] them, go through all of them. Um, and
[00:09:43 - 00:09:50] answer a question. Yeah. Um, now it will
[00:09:48 - 00:09:54] take a while. So, it needs to read
[00:09:50 - 00:09:57] everything. It needs to um get some
[00:09:54 - 00:10:02] insights from it. It also will take
[00:09:57 - 00:10:02] quite um some amount of tokens.

## Window 002: 00:09:30 - 00:19:30

[00:09:32 - 00:09:38] uh for example yeah how we can use this
[00:09:35 - 00:09:43] uh logs we can ask plot to read all of
[00:09:38 - 00:09:48] them, go through all of them. Um, and
[00:09:43 - 00:09:50] answer a question. Yeah. Um, now it will
[00:09:48 - 00:09:54] take a while. So, it needs to read
[00:09:50 - 00:09:57] everything. It needs to um get some
[00:09:54 - 00:10:02] insights from it. It also will take
[00:09:57 - 00:10:02] quite um some amount of tokens.
[00:10:04 - 00:10:11] Mhm. So, it's aggregating
[00:10:08 - 00:10:14] And if I want to change my request like
[00:10:11 - 00:10:19] okay how many tokens I used last month
[00:10:14 - 00:10:22] or yeah or last uh six months it will do
[00:10:19 - 00:10:25] the same work again and again
[00:10:22 - 00:10:30] it's probably will reuse some cash. Yeah
[00:10:25 - 00:10:34] but um uh still it will do a lot of
[00:10:30 - 00:10:35] extra work. So y here is our breakdown.
[00:10:34 - 00:10:38] So it's very nice. At least I can do
[00:10:35 - 00:10:41] that locally for myself, but
[00:10:38 - 00:10:43] >> which was faster like my computing.
[00:10:41 - 00:10:45] >> Oh,
[00:10:43 - 00:10:49] maybe you need to reload your laptop for
[00:10:45 - 00:10:52] sure. Um, so what if I want to share
[00:10:49 - 00:10:54] this information with my colleagues?
[00:10:52 - 00:10:56] Not about my personal usage. Yeah. But
[00:10:54 - 00:11:00] what if my company wants to know how
[00:10:56 - 00:11:03] much tokens I use every day, every week?
[00:11:00 - 00:11:06] Uh, or I need to track myself how much
[00:11:03 - 00:11:09] tokens I use. um to control my uh
[00:11:06 - 00:11:13] consumption. Um
[00:11:09 - 00:11:17] again, yeah, we have this um dashboard
[00:11:13 - 00:11:23] here. We can track how many people um
[00:11:17 - 00:11:25] use this um cloud code, who spans the
[00:11:23 - 00:11:27] most of the tokens. So, we can correct
[00:11:25 - 00:11:32] Yeah. this behavior. We can ask people,
[00:11:27 - 00:11:37] yeah, I don't know this me. Yeah.
[00:11:32 - 00:11:40] uh so I I cannot share my local logs
[00:11:37 - 00:11:44] with my uh colleagues and they not going
[00:11:40 - 00:11:46] to do that uh for me as well. Um what
[00:11:44 - 00:11:50] we're going to do is instead we will
[00:11:46 - 00:11:54] take um so what we did already here we
[00:11:50 - 00:11:57] took uh entropic API we built data
[00:11:54 - 00:12:01] pipeline which will take logs from the
[00:11:57 - 00:12:03] cloud from the entropic cloud um and
[00:12:01 - 00:12:06] load this data to our destination to our
[00:12:03 - 00:12:10] database or I don't know a bunch of
[00:12:06 - 00:12:12] files yeah and I can um run this
[00:12:10 - 00:12:15] pipeline every day so it keep it fresh
[00:12:12 - 00:12:18] keep it updated and
[00:12:15 - 00:12:23] um build reports on top of it and deploy
[00:12:18 - 00:12:27] it in cloud uh anywhere where I want in
[00:12:23 - 00:12:30] this case we use DT hub uh platform um
[00:12:27 - 00:12:33] we like it's a dog fooding for for
[00:12:30 - 00:12:38] ourself we built this tool we use it
[00:12:33 - 00:12:40] internally because yeah we like it um
[00:12:38 - 00:12:44] this uh platform helps you deploy your
[00:12:40 - 00:12:48] data pipelines build them and also
[00:12:44 - 00:12:52] deploy your um dashboard your reports.
[00:12:48 - 00:12:53] Um not only that we will also talk about
[00:12:52 - 00:12:57] transformations data quality in the
[00:12:53 - 00:13:00] future that uh further but now let's
[00:12:57 - 00:13:03] focus on data ingestion and data uh and
[00:13:00 - 00:13:03] pipeline deployment.
[00:13:04 - 00:13:09] So
[00:13:06 - 00:13:14] what I want to do now
[00:13:09 - 00:13:14] I want to start with uh some scaffolding
[00:13:15 - 00:13:22] we will use today the comment ux tilty
[00:13:19 - 00:13:24] hub in it
[00:13:22 - 00:13:26] latest lattest so can you see it is it
[00:13:24 - 00:13:28] big enough
[00:13:26 - 00:13:30] >> uh it's okay but I wonder if you you
[00:13:28 - 00:13:33] have any notes that we can share with us
[00:13:30 - 00:13:35] so we can copy or we need to to try to
[00:13:33 - 00:13:37] type along I think it's not very long
[00:13:35 - 00:13:39] comment. We're not going to use many
[00:13:37 - 00:13:42] comments today today to be honest
[00:13:39 - 00:13:43] >> because most of the time now we just
[00:13:42 - 00:13:48] talk to the agents, right?
[00:13:43 - 00:13:52] >> Yeah, true. Uh so it's just uvx delty
[00:13:48 - 00:13:55] hub dashinit at lattest. You can run
[00:13:52 - 00:13:58] without lattice if you never ran this um
[00:13:55 - 00:14:03] comment before. We just make sure that
[00:13:58 - 00:14:07] any cash won't um bother us. So this
[00:14:03 - 00:14:10] comment will scaffold very basic delty
[00:14:07 - 00:14:13] hub workspace. So it will contain some
[00:14:10 - 00:14:16] files like uh the flag file workspace
[00:14:13 - 00:14:18] some config files of course get ignore
[00:14:16 - 00:14:21] to avoid any credentials leaks the
[00:14:18 - 00:14:24] python version deployment.py PI file uh
[00:14:21 - 00:14:29] we will use it for deployment further uh
[00:14:24 - 00:14:31] pi project toml and UV log um we use UV
[00:14:29 - 00:14:34] in this workshop because it's very
[00:14:31 - 00:14:38] convenient if you don't use it yet
[00:14:34 - 00:14:42] please start uh highly recommend it um
[00:14:38 - 00:14:44] but I hope everyone already switch to UV
[00:14:42 - 00:14:46] so it asked me create virtual
[00:14:44 - 00:14:50] environment and is install dependencies
[00:14:46 - 00:14:52] now yes let's do that it will do simple
[00:14:50 - 00:14:55] UV sync
[00:14:52 - 00:14:58] and it's suggested. Yeah, open your
[00:14:55 - 00:15:01] coding agent in this workspace and tell
[00:14:58 - 00:15:01] it what to build.
[00:15:01 - 00:15:08] That's what I'm going to do.
[00:15:05 - 00:15:10] I want to keep this workshop also delt
[00:15:08 - 00:15:15] um
[00:15:10 - 00:15:18] like new newbies friendly. uh uh after
[00:15:15 - 00:15:21] every iteration with cloth with agent I
[00:15:18 - 00:15:25] will try to explain uh what was built
[00:15:21 - 00:15:28] and how it works uh also
[00:15:25 - 00:15:29] let me know if it's not clear enough and
[00:15:28 - 00:15:32] I will repeat
[00:15:29 - 00:15:35] >> yeah I'm taking a look at the live chat
[00:15:32 - 00:15:36] so if any of you have any questions you
[00:15:35 - 00:15:38] can just ask the question if it's
[00:15:36 - 00:15:40] something simple yes or no question I
[00:15:38 - 00:15:44] already answered some of them but yeah
[00:15:40 - 00:15:45] you can ask a question and I will also
[00:15:44 - 00:15:47] uh ask Alona okay
[00:15:45 - 00:15:49] >> these questions but I'm also following
[00:15:47 - 00:15:49] along so if something doesn't work I
[00:15:49 - 00:15:52] will uh
[00:15:49 - 00:15:54] >> Mhm. Thank you so much. Yeah I will try
[00:15:52 - 00:15:56] to keep uh things slower because it's
[00:15:54 - 00:15:59] hands on I expect that you guys will
[00:15:56 - 00:16:01] repeat it. Um so I will try to keep it
[00:15:59 - 00:16:07] slow.
[00:16:01 - 00:16:12] Um so we have uh local traces, we have
[00:16:07 - 00:16:17] um agent, we have our EDA or just
[00:16:12 - 00:16:21] terminal. Um do that how you like it. I
[00:16:17 - 00:16:26] like PyCharm. Highly recommend it.
[00:16:21 - 00:16:28] And so now I will ask clot to build
[00:16:26 - 00:16:31] delty pipeline
[00:16:28 - 00:16:36] for my
[00:16:31 - 00:16:41] local clot logs
[00:16:36 - 00:16:43] ah all the time
[00:16:41 - 00:16:46] local cloud logs
[00:16:43 - 00:16:49] to duct db we will use duck db um this
[00:16:46 - 00:16:51] stage it's a local database you don't
[00:16:49 - 00:16:53] have to configure it um pretty
[00:16:51 - 00:16:57] convenient for demos and tests. So we'll
[00:16:53 - 00:17:04] start with it as destination. So build
[00:16:57 - 00:17:04] pipeline for my for my local logs
[00:17:04 - 00:17:11] to db. Yeah, you can be a bit um
[00:17:11 - 00:17:17] like you can vary the prompt. I also use
[00:17:14 - 00:17:19] every time I use different and it pretty
[00:17:17 - 00:17:24] much works
[00:17:19 - 00:17:30] deterministically. So let's see
[00:17:24 - 00:17:32] lot data like lot row JSON
[00:17:30 - 00:17:34] JSONs
[00:17:32 - 00:17:37] into
[00:17:34 - 00:17:37] um
[00:17:37 - 00:17:43] I think that's that's it. Let's run it.
[00:17:43 - 00:17:50] So what it's going to do right now uh it
[00:17:47 - 00:17:52] started with the skill delt hub router
[00:17:50 - 00:17:54] when we
[00:17:52 - 00:17:59] >> when we ran yeah when [clears throat] we
[00:17:54 - 00:18:02] started uvx um uh delt hub init comment
[00:17:59 - 00:18:06] it scaffolded some skills. So in cloud
[00:18:02 - 00:18:09] folder you can see some skills already
[00:18:06 - 00:18:12] pre configured
[00:18:09 - 00:18:15] and first skill always the dehab router
[00:18:12 - 00:18:19] it will figure out which skill you
[00:18:15 - 00:18:22] should use next. So um in our case our
[00:18:19 - 00:18:26] cloud logs live in folder in the project
[00:18:22 - 00:18:30] folder. So it means that data will be
[00:18:26 - 00:18:32] loaded from the file system as files.
[00:18:30 - 00:18:35] So now delty hop router skill will
[00:18:32 - 00:18:41] figure it out and install um correct
[00:18:35 - 00:18:41] skills for this particular source.
[00:18:42 - 00:18:45] DT hub doesn't have any information
[00:18:44 - 00:18:49] about what exactly is there right it
[00:18:45 - 00:18:52] just cloud knows how the data looks like
[00:18:49 - 00:18:55] and based on that it uh figures out how
[00:18:52 - 00:18:57] to make the the transformations or
[00:18:55 - 00:18:59] whatever it's doing right
[00:18:57 - 00:19:03] >> uh yes so if I if you want to load data
[00:18:59 - 00:19:06] from like entropic API like I um
[00:19:03 - 00:19:09] mentioned before it will use another
[00:19:06 - 00:19:12] skills it will um it will use um rest
[00:19:09 - 00:19:15] API skill for example uh If you want to
[00:19:12 - 00:19:17] load data from another SQL database, it
[00:19:15 - 00:19:21] will use
[00:19:17 - 00:19:23] uh SQL database uh toolkit. Yeah. So in
[00:19:21 - 00:19:25] our case, file system pipeline, it's not
[00:19:23 - 00:19:30] just a skill, it's a it's a whole
[00:19:25 - 00:19:33] toolkit. So it contains uh many skills.

## Window 003: 00:19:00 - 00:29:00

[00:19:03 - 00:19:09] mentioned before it will use another
[00:19:06 - 00:19:12] skills it will um it will use um rest
[00:19:09 - 00:19:15] API skill for example uh If you want to
[00:19:12 - 00:19:17] load data from another SQL database, it
[00:19:15 - 00:19:21] will use
[00:19:17 - 00:19:23] uh SQL database uh toolkit. Yeah. So in
[00:19:21 - 00:19:25] our case, file system pipeline, it's not
[00:19:23 - 00:19:30] just a skill, it's a it's a whole
[00:19:25 - 00:19:33] toolkit. So it contains uh many skills.
[00:19:30 - 00:19:35] Um the entry skill is always create file
[00:19:33 - 00:19:37] system pipeline. So in our case, it will
[00:19:35 - 00:19:39] start with a simple file system
[00:19:37 - 00:19:43] pipeline.
[00:19:39 - 00:19:47] And if you need to do some extra work
[00:19:43 - 00:19:51] like validate my data, explore my data,
[00:19:47 - 00:19:55] build um transformations for my data
[00:19:51 - 00:19:59] also um improve performance for my data,
[00:19:55 - 00:20:00] it will um
[00:19:59 - 00:20:04] figure it out like it it should it
[00:20:00 - 00:20:08] should uh choose correct skills.
[00:20:04 - 00:20:12] So it's done. Uh there is a plan found
[00:20:08 - 00:20:16] the working deer. Um it's going to
[00:20:12 - 00:20:18] scaffold some basic DT file system
[00:20:16 - 00:20:20] pipeline with with the examples as a
[00:20:18 - 00:20:24] starting point.
[00:20:20 - 00:20:26] Uh also we use um read JSON. It's built
[00:20:24 - 00:20:30] in uh DT function. It will read every
[00:20:26 - 00:20:35] file to get data from it. So our bucket
[00:20:30 - 00:20:38] URL is my local folder.
[00:20:35 - 00:20:41] Um, yeah. Destination Dr. B. So,
[00:20:38 - 00:20:42] everything is correct. Confirm
[00:20:41 - 00:20:43] receipt.
[00:20:42 - 00:20:46] >> I don't know if it was a good idea for
[00:20:43 - 00:20:48] me to deviate from what you do, Alona,
[00:20:46 - 00:20:52] but I ask you to also check my Codex
[00:20:48 - 00:20:53] logs and ingest them, too. So, I'll see.
[00:20:52 - 00:20:57] >> Yeah. Yeah, that's nice. It would be
[00:20:53 - 00:20:59] nice to see what he gets.
[00:20:57 - 00:21:01] >> And I think since everyone uh probably
[00:20:59 - 00:21:03] is doing uh something different, right?
[00:21:01 - 00:21:05] So, not everyone is using lot code. So
[00:21:03 - 00:21:08] maybe you use something else you can
[00:21:05 - 00:21:10] just ask to to to do it with your agent,
[00:21:08 - 00:21:11] right? And then at the end it will be
[00:21:10 - 00:21:13] slightly different but like these agents
[00:21:11 - 00:21:15] will figure this out.
[00:21:13 - 00:21:17] >> Yeah.
[00:21:15 - 00:21:19] Yeah. Also any feedback would be very
[00:21:17 - 00:21:22] very appreciated.
[00:21:19 - 00:21:24] >> So I see a comment it's difficult to
[00:21:22 - 00:21:26] follow along. I don't have any idea
[00:21:24 - 00:21:29] what's happening. So maybe Alona we can
[00:21:26 - 00:21:31] uh pause a little bit and uh actually
[00:21:29 - 00:21:35] describe what's happening right now.
[00:21:31 - 00:21:38] >> Yeah. Okay. Um,
[00:21:35 - 00:21:41] so right now we're trying to build
[00:21:38 - 00:21:44] similar dashboard. Yeah, it's Oh, it
[00:21:41 - 00:21:48] stopped because it was uh unused. So
[00:21:44 - 00:21:51] we're trying to build um we're trying to
[00:21:48 - 00:21:55] understand yeah how do we use agents?
[00:21:51 - 00:22:00] How many tokens we use? How expensive is
[00:21:55 - 00:22:03] it? what's um I don't know um what
[00:22:00 - 00:22:06] models we need the most and so on. So we
[00:22:03 - 00:22:07] want to build similar dashboard ourself
[00:22:06 - 00:22:09] and we want to share it with our
[00:22:07 - 00:22:12] colleagues.
[00:22:09 - 00:22:15] Uh and now we started with our local
[00:22:12 - 00:22:18] logs. We want to explore our local um
[00:22:15 - 00:22:21] agent usage because you probably use uh
[00:22:18 - 00:22:24] some code assistant
[00:22:21 - 00:22:26] uh for example clo or codex or uh
[00:22:24 - 00:22:29] copilot
[00:22:26 - 00:22:31] and um we started with the simple
[00:22:29 - 00:22:36] comment
[00:22:31 - 00:22:41] uvx ty hub in it to scaffold
[00:22:36 - 00:22:44] um basic ty hub workspace. It's almost
[00:22:41 - 00:22:48] empty. There's no pipelines uh in
[00:22:44 - 00:22:51] scaffolded project but there is all
[00:22:48 - 00:22:57] necessary like configurations like all
[00:22:51 - 00:23:01] necessary um files skills um so it also
[00:22:57 - 00:23:03] environment var uh environment um um
[00:23:01 - 00:23:06] virtual environment
[00:23:03 - 00:23:10] um also configured for you. So this is
[00:23:06 - 00:23:10] the only comment we ran
[00:23:11 - 00:23:16] uxy hub in it.
[00:23:14 - 00:23:19] Um
[00:23:16 - 00:23:21] I would like to share it in YouTube but
[00:23:19 - 00:23:22] I I can't.
[00:23:21 - 00:23:26] >> I will do this.
[00:23:22 - 00:23:29] >> Thank you. So we start with this comment
[00:23:26 - 00:23:33] and then we call clot. So now currently
[00:23:29 - 00:23:36] I'm talking to my clot code or you can
[00:23:33 - 00:23:39] use any other agent you have. you use in
[00:23:36 - 00:23:42] other IDE. Yeah. So I use PyCharm
[00:23:39 - 00:23:46] because I got used to it. You can use
[00:23:42 - 00:23:50] regular terminal, you can use um um clin
[00:23:46 - 00:23:51] browser or any other agent. Please feel
[00:23:50 - 00:23:56] free.
[00:23:51 - 00:24:00] Um and after that I just asked
[00:23:56 - 00:24:06] uh agent to build TT pipeline for my
[00:24:00 - 00:24:06] local clock logs and load data to DTB.
[00:24:09 - 00:24:19] So uh some work already uh was done.
[00:24:14 - 00:24:24] Let's look um what happened. So we can
[00:24:19 - 00:24:26] see that in the report that agent built
[00:24:24 - 00:24:31] Tilty pipeline. Tilty pipeline ran
[00:24:26 - 00:24:35] successfully and it created 78 tables
[00:24:31 - 00:24:38] and that's quite a lot and probably
[00:24:35 - 00:24:40] should be one table you you would think
[00:24:38 - 00:24:44] but actually delt
[00:24:40 - 00:24:48] um normalizes data. So initially you
[00:24:44 - 00:24:53] have row JSONs they have no structure
[00:24:48 - 00:24:54] they look um like a dictionary
[00:24:53 - 00:24:57] and if you want to load this data into
[00:24:54 - 00:25:00] relational database you need to unst it
[00:24:57 - 00:25:05] you need to um set columns set data
[00:25:00 - 00:25:08] types and so on and does it for you and
[00:25:05 - 00:25:11] the side effect there is 78 tables
[00:25:08 - 00:25:16] because this data is heavily nested
[00:25:11 - 00:25:18] let's take a look at the data.
[00:25:16 - 00:25:21] No, let's first take a look at the
[00:25:18 - 00:25:21] pipeline.
[00:25:23 - 00:25:30] So, we have couple of imports here. Just
[00:25:26 - 00:25:32] DT as a library. Uh DT it's open source
[00:25:30 - 00:25:35] Python library. So, you can use it for
[00:25:32 - 00:25:38] any project at work or for a pad
[00:25:35 - 00:25:43] projects. Uh doesn't matter. It's Apache
[00:25:38 - 00:25:46] 2. feel free to use um and sources
[00:25:43 - 00:25:53] contains couple of uh pre-built sources
[00:25:46 - 00:25:53] like file system. Yeah, we can see um
[00:25:53 - 00:25:58] okay there is no uh information
[00:25:57 - 00:26:00] for some reason. Okay. Uh
[00:25:58 - 00:26:03] [clears throat] like file system, REST
[00:26:00 - 00:26:07] API source and SQL database.
[00:26:03 - 00:26:12] Um they are generic. You can configure
[00:26:07 - 00:26:14] it for your case and yeah customize it
[00:26:12 - 00:26:17] and run it.
[00:26:14 - 00:26:21] So how does it work? This Python script
[00:26:17 - 00:26:24] contains just one
[00:26:21 - 00:26:27] load messages function.
[00:26:24 - 00:26:30] In this function we define pipeline the
[00:26:27 - 00:26:33] not we agent defined uh [clears throat]
[00:26:30 - 00:26:36] DT pipeline as follows.
[00:26:33 - 00:26:38] It said pipeline name destination in our
[00:26:36 - 00:26:44] case it's DDB but you can easily change
[00:26:38 - 00:26:46] it to bequery yeah or
[00:26:44 - 00:26:49] or postgress
[00:26:46 - 00:26:52] um it depends on your destination
[00:26:49 - 00:26:55] now we use db
[00:26:52 - 00:26:59] let's skip it
[00:26:55 - 00:27:04] um data set name in this case is cloud
[00:26:59 - 00:27:06] logs um I know because I'm a old user of
[00:27:04 - 00:27:09] delt that the pipeline name and data
[00:27:06 - 00:27:11] saying data set name should be different
[00:27:09 - 00:27:14] they shouldn't be the same but we have
[00:27:11 - 00:27:17] this dev mode true it means that on
[00:27:14 - 00:27:20] every run till t will add time stamp to
[00:27:17 - 00:27:24] the data set name so every on every run
[00:27:20 - 00:27:29] it will create new fresh data set
[00:27:24 - 00:27:33] so here it will list all files in your
[00:27:29 - 00:27:35] um bucket directory yeah in your bucket
[00:27:33 - 00:27:38] And
[00:27:35 - 00:27:40] we compon it with the read JSON. It's
[00:27:38 - 00:27:43] pre-built function. It will read every
[00:27:40 - 00:27:50] file from this source
[00:27:43 - 00:27:50] and load it to your destination tag.
[00:27:50 - 00:27:56] To run this pipeline, we just use method
[00:27:52 - 00:28:00] run. Provide the reader. This is our
[00:27:56 - 00:28:01] source. The main table will be named
[00:28:00 - 00:28:04] messages.
[00:28:01 - 00:28:07] And on every run we said that all data
[00:28:04 - 00:28:10] will be read again and replaced. So you
[00:28:07 - 00:28:13] on every run you will have fresh data.
[00:28:10 - 00:28:16] This is not very efficient because you
[00:28:13 - 00:28:19] can have a lot of traces. You can have
[00:28:16 - 00:28:23] millions rows millions I don't know
[00:28:19 - 00:28:26] billions yeah in English. Um so next
[00:28:23 - 00:28:30] step would be make this pipeline
[00:28:26 - 00:28:34] incremental. So on every run you can
[00:28:30 - 00:28:38] load only new data to keep it fast,
[00:28:34 - 00:28:41] efficient and um yeah that it just makes
[00:28:38 - 00:28:45] sense. Uh it's super easy to do with
[00:28:41 - 00:28:47] delty. It's would be our next logical
[00:28:45 - 00:28:50] step but not in this workshop because
[00:28:47 - 00:28:53] this workshop is not about delty. It's
[00:28:50 - 00:28:55] about um agent traces.
[00:28:53 - 00:28:57] So
[00:28:55 - 00:28:59] >> and there is also a question like what
[00:28:57 - 00:29:03] is the difference between a skill and a
[00:28:59 - 00:29:06] tool. So in the course in LMZ camp we uh

## Window 004: 00:28:30 - 00:38:30

[00:28:30 - 00:28:38] load only new data to keep it fast,
[00:28:34 - 00:28:41] efficient and um yeah that it just makes
[00:28:38 - 00:28:45] sense. Uh it's super easy to do with
[00:28:41 - 00:28:47] delty. It's would be our next logical
[00:28:45 - 00:28:50] step but not in this workshop because
[00:28:47 - 00:28:53] this workshop is not about delty. It's
[00:28:50 - 00:28:55] about um agent traces.
[00:28:53 - 00:28:57] So
[00:28:55 - 00:28:59] >> and there is also a question like what
[00:28:57 - 00:29:03] is the difference between a skill and a
[00:28:59 - 00:29:06] tool. So in the course in LMZ camp we uh
[00:29:03 - 00:29:09] work more with like how to implement an
[00:29:06 - 00:29:12] agent but in case of cloud code cloud
[00:29:09 - 00:29:13] code or codex they are coding agents. So
[00:29:12 - 00:29:16] internally they have the tools they have
[00:29:13 - 00:29:19] this bash tool they have the uh read
[00:29:16 - 00:29:21] file tool they have lot file tool and
[00:29:19 - 00:29:23] they also have skills right? So skills
[00:29:21 - 00:29:26] is a way to extend your agent to give it
[00:29:23 - 00:29:29] some functionality uh that uh the
[00:29:26 - 00:29:33] developers of the agent didn't do. So
[00:29:29 - 00:29:34] for you it's just a way to um
[00:29:33 - 00:29:37] you know describe anything you want to
[00:29:34 - 00:29:39] do in simple markdown document and then
[00:29:37 - 00:29:41] the agent will know will know how to do
[00:29:39 - 00:29:44] things. So maybe Alona you can show us
[00:29:41 - 00:29:46] uh some of the skills because it is also
[00:29:44 - 00:29:48] important to understand how exactly this
[00:29:46 - 00:29:51] file system pipeline.py file was
[00:29:48 - 00:29:54] created. So the agent might not really
[00:29:51 - 00:29:56] know DT how to use it properly but we
[00:29:54 - 00:29:58] want to teach it right and the way we
[00:29:56 - 00:30:02] teach it is we describe how to actually
[00:29:58 - 00:30:06] do this in this skillmd and it lets us
[00:30:02 - 00:30:08] extend the functionality of the agent.
[00:30:06 - 00:30:10] Yes, I can add that uh what's the
[00:30:08 - 00:30:13] difference between skill and tool is
[00:30:10 - 00:30:16] that skill just describes what to do.
[00:30:13 - 00:30:18] But tool is usually a piece of code like
[00:30:16 - 00:30:20] repetitive code. If you know that you
[00:30:18 - 00:30:21] need to run the same code again and
[00:30:20 - 00:30:23] again, you don't want to agent rebuild
[00:30:21 - 00:30:27] it from scratch again and again, it will
[00:30:23 - 00:30:30] cost you money and time. Um but if you
[00:30:27 - 00:30:33] have some pre-built tooling, pre-built
[00:30:30 - 00:30:36] uh functions or in our case it's a whole
[00:30:33 - 00:30:41] library, you don't have to reinvent
[00:30:36 - 00:30:44] wheel again and again just uh show just
[00:30:41 - 00:30:49] uh point the agent in what cases use
[00:30:44 - 00:30:53] what tool. Yeah. uh our
[00:30:49 - 00:30:57] um like DTY hobby bench also contains
[00:30:53 - 00:31:00] MCP server and MCP server it's actually
[00:30:57 - 00:31:03] the router for tooling um you have a
[00:31:00 - 00:31:08] bunch of functions uh like to read table
[00:31:03 - 00:31:11] to read file to read um uh to to um
[00:31:08 - 00:31:15] count rows. Yeah. So you know this
[00:31:11 - 00:31:17] deterministic uh functions and agent can
[00:31:15 - 00:31:19] call them
[00:31:17 - 00:31:20] uh and you can describe in skills when
[00:31:19 - 00:31:23] and how [clears throat] you you should
[00:31:20 - 00:31:26] use this tooling
[00:31:23 - 00:31:29] and yeah so that's my opinion about
[00:31:26 - 00:31:32] skills and tools.
[00:31:29 - 00:31:34] Um any questions about skill here? We
[00:31:32 - 00:31:36] shared all our expertise [laughter] all
[00:31:34 - 00:31:38] our experience
[00:31:36 - 00:31:42] um and we keep working on this yeah
[00:31:38 - 00:31:45] workbench. So I think if you use these
[00:31:42 - 00:31:48] skills you can build the most um
[00:31:45 - 00:31:49] efficient DT pipelines then you would do
[00:31:48 - 00:31:51] that without them
[00:31:49 - 00:31:54] >> and the skills appeared when you type
[00:31:51 - 00:31:56] Ubx uh DT hub in it right so it
[00:31:54 - 00:31:58] automatically scaffolded the project and
[00:31:56 - 00:32:00] the skills were included right
[00:31:58 - 00:32:03] >> yeah not all skills it will include only
[00:32:00 - 00:32:05] DT hub router like this three
[00:32:03 - 00:32:09] >> and DTH hub router will figure out which
[00:32:05 - 00:32:11] tooling you need like tool kits yeah you
[00:32:09 - 00:32:12] uh in like in addition
[00:32:11 - 00:32:14] >> Mhm.
[00:32:12 - 00:32:17] >> for example like in the beginning we
[00:32:14 - 00:32:21] have no extra skills here but every time
[00:32:17 - 00:32:25] we talk to agent hopper order things
[00:32:21 - 00:32:27] like okay now I need another tool.
[00:32:25 - 00:32:29] >> So this create system pipeline did not
[00:32:27 - 00:32:31] exist right the routter pulled it and
[00:32:29 - 00:32:32] included this in the skills. Sorry,
[00:32:31 - 00:32:35] what?
[00:32:32 - 00:32:37] >> The create file system pipeline skill
[00:32:35 - 00:32:40] did not exist when we started the
[00:32:37 - 00:32:41] scaffolding. Okay, so it pulled the
[00:32:40 - 00:32:42] Okay, got it.
[00:32:41 - 00:32:43] >> Yeah,
[00:32:42 - 00:32:45] >> that's cool.
[00:32:43 - 00:32:49] >> Mhm. Kind of end.
[00:32:45 - 00:32:49] So this is our delty pipeline. I haven't
[00:32:49 - 00:32:54] >> [clears throat]
[00:32:49 - 00:32:56] >> uh written any uh line of this code uh
[00:32:54 - 00:33:00] but I know from my expertise that it's
[00:32:56 - 00:33:03] correct. Um this would work. Um but how
[00:33:00 - 00:33:06] you should know that it's correct that
[00:33:03 - 00:33:10] it's not the Uh we have a lot
[00:33:06 - 00:33:12] of extra skills in our AI workbench. Not
[00:33:10 - 00:33:15] only skills but also tools. Yeah. Like
[00:33:12 - 00:33:18] MCP um servers.
[00:33:15 - 00:33:18] Um
[00:33:19 - 00:33:25] and you can ask them to verify that your
[00:33:23 - 00:33:28] pipeline is correct. You can ask it to
[00:33:25 - 00:33:32] run it uh debug it validate the data. So
[00:33:28 - 00:33:36] you can notice here like this add limit
[00:33:32 - 00:33:37] method this dev mode through true uh
[00:33:36 - 00:33:39] parameter.
[00:33:37 - 00:33:41] So our skills they know how to debug
[00:33:39 - 00:33:45] your code. They know how it should look
[00:33:41 - 00:33:48] like should know it knows how uh what
[00:33:45 - 00:33:51] the result should be and um yeah what
[00:33:48 - 00:33:54] want to go further I can add incremental
[00:33:51 - 00:33:56] loading or explore your data. Yeah add
[00:33:54 - 00:33:59] some data quality checks and so on. I
[00:33:56 - 00:34:02] can ask you um
[00:33:59 - 00:34:05] debug my pipeline
[00:34:02 - 00:34:10] but it's already did debugging because
[00:34:05 - 00:34:13] um you can see that it's it it works
[00:34:10 - 00:34:15] so it will debug the pipeline until it
[00:34:13 - 00:34:19] works
[00:34:15 - 00:34:21] but I ask it explicitly
[00:34:19 - 00:34:24] and it figured out that we have debug
[00:34:21 - 00:34:24] pipeline skill
[00:34:25 - 00:34:27] another toolkit
[00:34:28 - 00:34:32] It's installing.
[00:34:36 - 00:34:41] So this debug my pipeline the reason we
[00:34:39 - 00:34:43] do this is because we want to make sure
[00:34:41 - 00:34:45] that the pipeline is actually correct.
[00:34:43 - 00:34:48] So you already have the expertise. You
[00:34:45 - 00:34:49] have used DT hub extensively. So you
[00:34:48 - 00:34:52] know which things work and which don't,
[00:34:49 - 00:34:56] right? But I might not know, right? So I
[00:34:52 - 00:34:58] haven't I don't use DT hub extensively.
[00:34:56 - 00:35:00] So and the agent can hallucinate some
[00:34:58 - 00:35:00] code that doesn't exist.
[00:35:00 - 00:35:02] >> True. True.
[00:35:00 - 00:35:05] >> And then that's why we want to do this.
[00:35:02 - 00:35:07] >> Yeah. But uh debugging code it's more
[00:35:05 - 00:35:11] like it's more technical part. So it
[00:35:07 - 00:35:15] just will make sure that your pipeline
[00:35:11 - 00:35:19] um not failed. Yeah. It's it works. It
[00:35:15 - 00:35:21] prod it loads some data but it's not um
[00:35:19 - 00:35:24] cannot say that this data is correct.
[00:35:21 - 00:35:27] uh it can only
[00:35:24 - 00:35:29] um assume so it can give you some
[00:35:27 - 00:35:35] information about data
[00:35:29 - 00:35:35] there's already some adjustments okay um
[00:35:35 - 00:35:41] oh okay look look what it did
[00:35:39 - 00:35:44] um remember I mentioned that it created
[00:35:41 - 00:35:49] like more than 70 tables because data is
[00:35:44 - 00:35:51] heavily nested so agent decided that it
[00:35:49 - 00:35:53] is a schema pollution
[00:35:51 - 00:35:59] And we can reduce the number of tables.
[00:35:53 - 00:36:03] So to do that it set some uh columns as
[00:35:59 - 00:36:05] a JSON data type. So not all data were
[00:36:03 - 00:36:07] unlisted
[00:36:05 - 00:36:13] and instead of 70 tables now we have
[00:36:07 - 00:36:13] just 40. That's very cool. Um
[00:36:15 - 00:36:20] oh I didn't expect that.
[00:36:17 - 00:36:22] So good next steps are view data,
[00:36:20 - 00:36:26] validate data. So it's already human in
[00:36:22 - 00:36:28] the loop. So now you you should take a
[00:36:26 - 00:36:30] look at the data. Uh you should make
[00:36:28 - 00:36:33] sure that it's correct, that that's what
[00:36:30 - 00:36:37] you expected. Um
[00:36:33 - 00:36:40] so I would say here you validate that
[00:36:37 - 00:36:41] pipeline works correctly. We're not
[00:36:40 - 00:36:44] going to do all of these steps because
[00:36:41 - 00:36:47] it will take some time. Let's uh just
[00:36:44 - 00:36:51] take a look. um
[00:36:47 - 00:36:53] um at um dashboard. Let me show you how
[00:36:51 - 00:36:57] to run it. There is a simple command
[00:36:53 - 00:37:01] again. UV run uh from the command line,
[00:36:57 - 00:37:04] not from the clo uh session
[00:37:01 - 00:37:05] uv rund hub
[00:37:04 - 00:37:07] local
[00:37:05 - 00:37:10] show.
[00:37:07 - 00:37:14] It means that we want to open dashboard
[00:37:10 - 00:37:14] for our pipeline locally.
[00:37:15 - 00:37:21] Just
[00:37:16 - 00:37:23] repeat this comment. UV run ty hub local
[00:37:21 - 00:37:25] show.
[00:37:23 - 00:37:29] First you need to make sure that your
[00:37:25 - 00:37:29] pipeline ran successfully.
[00:37:31 - 00:37:35] We'll automatically open uh Marimo
[00:37:34 - 00:37:39] dashboard.
[00:37:35 - 00:37:42] This is pre-built dashboard from DT.
[00:37:39 - 00:37:46] You can see here all information about
[00:37:42 - 00:37:49] the pipeline. You can uh explore your uh
[00:37:46 - 00:37:54] schema how many tables you have. You can
[00:37:49 - 00:37:59] look at this data. Yeah. Messages run
[00:37:54 - 00:38:02] query. It will run query on your local
[00:37:59 - 00:38:05] DDB
[00:38:02 - 00:38:05] uh
[00:38:05 - 00:38:10] file. So when you run your DT pipeline,
[00:38:08 - 00:38:12] it will it should create a local DT DB
[00:38:10 - 00:38:15] file.
[00:38:12 - 00:38:17] and dashboard will read from this file
[00:38:15 - 00:38:20] automatically. So you can look at your
[00:38:17 - 00:38:24] data here. You can you can validate if
[00:38:20 - 00:38:26] that's if that's uh that data is what
[00:38:24 - 00:38:28] you expected.
[00:38:26 - 00:38:32] Okay. Uh of course it's difficult to say
[00:38:28 - 00:38:34] if the data is correct from this um 40

## Window 005: 00:38:00 - 00:48:00

[00:38:02 - 00:38:05] uh
[00:38:05 - 00:38:10] file. So when you run your DT pipeline,
[00:38:08 - 00:38:12] it will it should create a local DT DB
[00:38:10 - 00:38:15] file.
[00:38:12 - 00:38:17] and dashboard will read from this file
[00:38:15 - 00:38:20] automatically. So you can look at your
[00:38:17 - 00:38:24] data here. You can you can validate if
[00:38:20 - 00:38:26] that's if that's uh that data is what
[00:38:24 - 00:38:28] you expected.
[00:38:26 - 00:38:32] Okay. Uh of course it's difficult to say
[00:38:28 - 00:38:34] if the data is correct from this um 40
[00:38:32 - 00:38:39] tables.
[00:38:34 - 00:38:39] Um what we can do
[00:38:40 - 00:38:43] we can
[00:38:44 - 00:38:49] stop it. Close it.
[00:38:49 - 00:38:55] We can ask clot.
[00:38:52 - 00:38:55] Um
[00:39:00 - 00:39:04] um build
[00:39:05 - 00:39:09] my report
[00:39:11 - 00:39:18] or my cloud blocks.
[00:39:23 - 00:39:27] So in my case it was a mistake to run it
[00:39:25 - 00:39:31] uh probably for all the agents because
[00:39:27 - 00:39:34] my DT pipeline is still
[00:39:31 - 00:39:37] >> yeah it says it's all the gigabytes
[00:39:34 - 00:39:42] so it's processing all this stuff.
[00:39:37 - 00:39:44] >> Um yeah I already like maybe for me I
[00:39:42 - 00:39:47] should have asked to do this on like
[00:39:44 - 00:39:49] last week or something right?
[00:39:47 - 00:39:52] >> Yeah it would make sense. I don't have
[00:39:49 - 00:39:52] so many
[00:39:52 - 00:39:57] >> but I I just try to like it's still
[00:39:55 - 00:39:59] processing. I said hey build a minim
[00:39:57 - 00:40:02] report for my cloud locks. So see what
[00:39:59 - 00:40:02] happens.
[00:40:07 - 00:40:14] >> So again yeah it's um um figure out that
[00:40:12 - 00:40:16] we need another toolkit like data
[00:40:14 - 00:40:20] exploration. Uh this uh tool kit
[00:40:16 - 00:40:25] contains a bunch of skills.
[00:40:20 - 00:40:28] Um how to build how to explore data. Um
[00:40:25 - 00:40:32] how to build marima notebooks.
[00:40:28 - 00:40:35] Um something else. Yeah, we can explore
[00:40:32 - 00:40:35] it together.
[00:40:36 - 00:40:42] Uh also yeah as I mentioned we use MCP.
[00:40:42 - 00:40:50] So this is our Dolby Hub MCP and our
[00:40:45 - 00:40:55] skills uh will reuse this MCP for some
[00:40:50 - 00:40:59] simple tasks like read table uh count
[00:40:55 - 00:41:01] number of rows. Yeah. So there is some
[00:40:59 - 00:41:03] predefined number of functions it will
[00:41:01 - 00:41:06] reuse instead of building from scratch
[00:41:03 - 00:41:09] all the time.
[00:41:06 - 00:41:11] Um so it's still thinking.
[00:41:09 - 00:41:13] You're probably very curious what is
[00:41:11 - 00:41:17] Mimo?
[00:41:13 - 00:41:21] Mimo it's a new generation of Jupyter
[00:41:17 - 00:41:24] notebooks. As you know probably Jupyter
[00:41:21 - 00:41:27] notebooks it's pure HTML and you can
[00:41:24 - 00:41:30] open it in um your browser. It has a
[00:41:27 - 00:41:35] very nice UI. You can run cells right
[00:41:30 - 00:41:37] there. Uh so MIMO it's very similar idea
[00:41:35 - 00:41:40] but the implementation is very
[00:41:37 - 00:41:42] different. So every Marimma notebook is
[00:41:40 - 00:41:45] just Python script.
[00:41:42 - 00:41:50] When it's uh ready, I will demonstrate
[00:41:45 - 00:41:50] you how how Marima notebook looks like.
[00:41:50 - 00:41:57] Uh we like it a lot because it's much
[00:41:53 - 00:42:01] easier to review uh in GitHub. It also
[00:41:57 - 00:42:04] more powerful. It has a lot of extra
[00:42:01 - 00:42:08] visuals uh features.
[00:42:04 - 00:42:13] um it's just Python and um agents are
[00:42:08 - 00:42:16] great with Python and with Marimo.
[00:42:13 - 00:42:18] >> So this is for me a convenient way to do
[00:42:16 - 00:42:19] some interactivity interactive stuff
[00:42:18 - 00:42:22] because normally what I do is I ask an
[00:42:19 - 00:42:25] agent to implement like a stream
[00:42:22 - 00:42:27] application right but this is a kind of
[00:42:25 - 00:42:31] lightweight way of doing this.
[00:42:27 - 00:42:33] >> Absolutely. It's more like data
[00:42:31 - 00:42:36] oriented.
[00:42:33 - 00:42:39] So you can see
[00:42:36 - 00:42:43] you can run each cell separately
[00:42:39 - 00:42:46] um as in Jupyter notebook.
[00:42:43 - 00:42:48] Let's um yeah it's still building.
[00:42:46 - 00:42:50] >> It also asked me to install some
[00:42:48 - 00:42:52] libraries. I said yeah go ahead.
[00:42:50 - 00:42:56] [laughter]
[00:42:52 - 00:42:57] >> Yeah I think it also is installing this
[00:42:56 - 00:42:59] alter for you.
[00:42:57 - 00:43:03] >> Mhm. Yeah, it uses alter for good
[00:42:59 - 00:43:05] visuals and MIMO as a main dependency
[00:43:03 - 00:43:07] because yeah, when we install DT, we're
[00:43:05 - 00:43:10] trying to avoid any extra dependencies
[00:43:07 - 00:43:12] to keep it lightweight.
[00:43:10 - 00:43:15] Yeah, because not everyone builds Marim
[00:43:12 - 00:43:15] notebooks.
[00:43:17 - 00:43:25] But we find it very useful because uh
[00:43:20 - 00:43:29] delta agent built a delty pipeline and
[00:43:25 - 00:43:31] we do not participate this um activity.
[00:43:29 - 00:43:37] The only thing we can do right now is to
[00:43:31 - 00:43:40] validate our data. So we can read code,
[00:43:37 - 00:43:44] we can look at the data. But to be
[00:43:40 - 00:43:47] honest, the main validation will happen
[00:43:44 - 00:43:50] when you look at the
[00:43:47 - 00:43:53] data which makes sense for you as a
[00:43:50 - 00:43:56] human being.
[00:43:53 - 00:43:58] So some something was built
[00:43:56 - 00:44:00] some Python uh file cloud logs
[00:43:58 - 00:44:07] dashboard.py.
[00:44:00 - 00:44:10] Um yeah, let's look at this file.
[00:44:07 - 00:44:13] So as I mentioned it's just Python. So
[00:44:10 - 00:44:17] each cell in our Marimma notebook is
[00:44:13 - 00:44:21] just um Python function. It could
[00:44:17 - 00:44:27] contain any Python code, any markdown
[00:44:21 - 00:44:32] text. Yeah. So it's um very native for
[00:44:27 - 00:44:34] Python users. Let's look at the UI. So
[00:44:32 - 00:44:38] this how it looks in browser.
[00:44:34 - 00:44:41] You can see your cells separately. You
[00:44:38 - 00:44:44] can run them separately. But what's
[00:44:41 - 00:44:47] difference between MIMO and Jupiter is
[00:44:44 - 00:44:51] you cannot run them randomly. There's
[00:44:47 - 00:44:53] always a order. So this is
[00:44:51 - 00:44:56] it prevents
[00:44:53 - 00:44:58] um mix of variables and so on. So it's
[00:44:56 - 00:45:02] very strict. So you should run your
[00:44:58 - 00:45:05] cells u one by one.
[00:45:02 - 00:45:05] um
[00:45:05 - 00:45:10] yeah I will run all of them to see some
[00:45:07 - 00:45:10] charts
[00:45:11 - 00:45:20] activity over time. So and this is my
[00:45:15 - 00:45:23] activity or last month. Um,
[00:45:20 - 00:45:26] so you can see I was very active
[00:45:23 - 00:45:29] on June 15
[00:45:26 - 00:45:33] and um, yeah, here you can see some
[00:45:29 - 00:45:38] messages by type that assistant user
[00:45:33 - 00:45:42] take the most and also some extra
[00:45:38 - 00:45:46] tooling from agent. Yeah, doesn't matter
[00:45:42 - 00:45:49] what it means. Also, we can see how what
[00:45:46 - 00:45:52] models I used the most. It's Opus, of
[00:45:49 - 00:45:55] course. Um, also I was a big fan of
[00:45:52 - 00:45:59] Sonet 4.6, but I realized that I have
[00:45:55 - 00:46:01] subscription. Why should I use it?
[00:45:59 - 00:46:03] And yeah, I tried Fable before it was
[00:46:01 - 00:46:06] banned.
[00:46:03 - 00:46:08] And what else? Yeah, the top pro
[00:46:06 - 00:46:12] projects. This is so project I worked
[00:46:08 - 00:46:14] lately. They also contributed into our
[00:46:12 - 00:46:18] Yber bench and our skills.
[00:46:14 - 00:46:21] Um this is some
[00:46:18 - 00:46:21] empty.
[00:46:22 - 00:46:27] So
[00:46:25 - 00:46:29] this is our local dashboard. So we can
[00:46:27 - 00:46:33] see that it's pretty much correct. I can
[00:46:29 - 00:46:37] see from my usage yeah that uh I used
[00:46:33 - 00:46:39] OPOS a lot. I um this is my vacation
[00:46:37 - 00:46:44] week. I know that I didn't uh open my
[00:46:39 - 00:46:47] laptop for the whole week. Um so it's
[00:46:44 - 00:46:50] pretty much correct. I can validate it.
[00:46:47 - 00:46:52] So
[00:46:50 - 00:46:55] um
[00:46:52 - 00:46:55] so
[00:46:57 - 00:47:01] any questions about this part?
[00:47:03 - 00:47:08] >> How useful you find this information?
[00:47:06 - 00:47:11] There is a there are some questions
[00:47:08 - 00:47:15] about MIMA answered like how to to to
[00:47:11 - 00:47:17] spell it. Um so there's a question that
[00:47:15 - 00:47:20] perhaps we should answer later. It's
[00:47:17 - 00:47:22] about telemetry.
[00:47:20 - 00:47:24] Um
[00:47:22 - 00:47:26] this is something we can uh talk about
[00:47:24 - 00:47:28] uh later maybe when we finish because I
[00:47:26 - 00:47:30] think this is also interesting and this
[00:47:28 - 00:47:32] is what I think could be very very
[00:47:30 - 00:47:34] useful for this course because in this
[00:47:32 - 00:47:36] course we are learning how to build
[00:47:34 - 00:47:38] agent not to use like coding agents. We
[00:47:36 - 00:47:40] of course use coding agents but for us
[00:47:38 - 00:47:43] we mostly build agents right would be
[00:47:40 - 00:47:46] very interesting how to to we can use
[00:47:43 - 00:47:49] >> this actually to understand more about
[00:47:46 - 00:47:52] the way the how our agents behave. Yes.
[00:47:49 - 00:47:54] And actually this is our part two. Um
[00:47:52 - 00:47:57] okay. What happened when you build
[00:47:54 - 00:48:01] agent? Yeah. Your agent lives somewhere
[00:47:57 - 00:48:06] else not on your local laptop. And um

## Window 006: 00:47:30 - 00:57:30

[00:47:30 - 00:47:34] useful for this course because in this
[00:47:32 - 00:47:36] course we are learning how to build
[00:47:34 - 00:47:38] agent not to use like coding agents. We
[00:47:36 - 00:47:40] of course use coding agents but for us
[00:47:38 - 00:47:43] we mostly build agents right would be
[00:47:40 - 00:47:46] very interesting how to to we can use
[00:47:43 - 00:47:49] >> this actually to understand more about
[00:47:46 - 00:47:52] the way the how our agents behave. Yes.
[00:47:49 - 00:47:54] And actually this is our part two. Um
[00:47:52 - 00:47:57] okay. What happened when you build
[00:47:54 - 00:48:01] agent? Yeah. Your agent lives somewhere
[00:47:57 - 00:48:06] else not on your local laptop. And um
[00:48:01 - 00:48:09] for example we built internally our
[00:48:06 - 00:48:11] um our
[00:48:09 - 00:48:13] AI assistant.
[00:48:11 - 00:48:15] You can talk to it. Yeah. like um what
[00:48:13 - 00:48:19] is ZT
[00:48:15 - 00:48:22] and we can collect all the information
[00:48:19 - 00:48:23] about this session using
[00:48:22 - 00:48:26] loggers.
[00:48:23 - 00:48:29] >> Mhm. You will learn you students yeah
[00:48:26 - 00:48:32] you viewers users you will learn more
[00:48:29 - 00:48:37] about monitoring about logging uh later
[00:48:32 - 00:48:40] in um further lessons but uh for our
[00:48:37 - 00:48:43] um workshop I will talk about logfire
[00:48:40 - 00:48:48] >> because we use it in internally logfire
[00:48:43 - 00:48:50] it's a pentic um native um logger it
[00:48:48 - 00:48:52] collects all the information similar to
[00:48:50 - 00:48:56] your clo traces it collects a lot of
[00:48:52 - 00:49:01] metadata like usage models. Yeah. What
[00:48:56 - 00:49:03] tooling was uh called? Uh what um skills
[00:49:01 - 00:49:05] used. Yeah. So collects a lot of
[00:49:03 - 00:49:08] information. It's very useful to know
[00:49:05 - 00:49:11] how our agent works. So we don't much
[00:49:08 - 00:49:16] care about uh questions and answers
[00:49:11 - 00:49:19] here. Logging means uh how agent works,
[00:49:16 - 00:49:23] how uh we can optimize it, what is the
[00:49:19 - 00:49:23] performance. Um [clears throat]
[00:49:26 - 00:49:33] so to uh reproduce the situation without
[00:49:30 - 00:49:36] extra accounts, API tokens and so on, I
[00:49:33 - 00:49:40] created a very simple API
[00:49:36 - 00:49:42] um with a couple of endpoints. uh this
[00:49:40 - 00:49:44] in point contain
[00:49:42 - 00:49:49] >> this is uh this is what you're already
[00:49:44 - 00:49:50] talking about uh this uh DT hub agent
[00:49:49 - 00:49:52] right
[00:49:50 - 00:49:55] >> I'm talking about DY hub agent but we
[00:49:52 - 00:49:56] not going to use our real data yeah um
[00:49:55 - 00:49:58] that's um
[00:49:56 - 00:50:01] >> not a complaint
[00:49:58 - 00:50:07] >> uh but I reproduce the situation yeah
[00:50:01 - 00:50:13] like we have um um some logs
[00:50:07 - 00:50:17] from agent And um I just created like
[00:50:13 - 00:50:20] API which retrieves you these logs. We
[00:50:17 - 00:50:23] um simulate the situation when you
[00:50:20 - 00:50:29] request your logger API. For example, we
[00:50:23 - 00:50:29] use logfire. Yeah. Logire API.
[00:50:33 - 00:50:38] Oh god. Okay. It's not so easy to show
[00:50:36 - 00:50:40] you.
[00:50:38 - 00:50:44] the documentation.
[00:50:40 - 00:50:45] Okay, I have a documentation for clot um
[00:50:44 - 00:50:48] platform.
[00:50:45 - 00:50:50] They have API. You can request it. You
[00:50:48 - 00:50:53] can get your logs
[00:50:50 - 00:50:56] um
[00:50:53 - 00:51:01] from this API. You can get your lose
[00:50:56 - 00:51:03] logs uh leaves live in um some database
[00:51:01 - 00:51:06] somewhere in cloud. The entropic
[00:51:03 - 00:51:10] maintains it and you can get this data
[00:51:06 - 00:51:14] from using API. Same for logfire. Our
[00:51:10 - 00:51:18] traces for this for the support agent
[00:51:14 - 00:51:22] they live in pentic storage somewhere in
[00:51:18 - 00:51:25] cloud. We don't have them to have them
[00:51:22 - 00:51:31] locally. Yeah. Or do something with this
[00:51:25 - 00:51:33] logs. We should request them using API.
[00:51:31 - 00:51:37] Um
[00:51:33 - 00:51:39] so I just imitate this process building
[00:51:37 - 00:51:44] this API with a couple of endpoints. One
[00:51:39 - 00:51:49] end point gives us code um uh traces
[00:51:44 - 00:51:51] format and another like log fire logs
[00:51:49 - 00:51:55] gives us another type of logs because
[00:51:51 - 00:51:58] for each tool you have different type of
[00:51:55 - 00:52:01] traces and logs. They all have different
[00:51:58 - 00:52:05] structure, different different keys,
[00:52:01 - 00:52:08] different order of um fields. Yeah. So
[00:52:05 - 00:52:10] different type of nesting. It's very
[00:52:08 - 00:52:14] difficult to work with this data if you
[00:52:10 - 00:52:18] have several agents. Uh and usually you
[00:52:14 - 00:52:22] will have several agents. you will have
[00:52:18 - 00:52:26] um agent for your cloud assistants for
[00:52:22 - 00:52:30] co-worker for um
[00:52:26 - 00:52:33] for custom agents. Yeah. So it will
[00:52:30 - 00:52:36] always be a problem to have different
[00:52:33 - 00:52:39] types of logs and what you can do with
[00:52:36 - 00:52:42] it you can download these logs you can
[00:52:39 - 00:52:45] request it through API and load it in a
[00:52:42 - 00:52:48] structured format somewhere else. Yeah,
[00:52:45 - 00:52:50] in a database for example. That's what
[00:52:48 - 00:52:52] we're going to do right now.
[00:52:50 - 00:52:54] Um,
[00:52:52 - 00:52:56] >> so we finished the first part, right?
[00:52:54 - 00:52:59] >> So the first part is finished. We have
[00:52:56 - 00:53:02] not so much time. So let's speed it up.
[00:52:59 - 00:53:02] >> Um,
[00:53:03 - 00:53:06] okay.
[00:53:04 - 00:53:08] >> And you're not going to show how to
[00:53:06 - 00:53:10] integrate pantic
[00:53:08 - 00:53:10] how to integrate lockfire into agents,
[00:53:10 - 00:53:13] right?
[00:53:10 - 00:53:16] >> Uh, it's very simple. I think you will
[00:53:13 - 00:53:18] >> I think uh what we can do Alona is uh
[00:53:16 - 00:53:19] people who are taking part in the course
[00:53:18 - 00:53:21] they will do this as a part of their
[00:53:19 - 00:53:24] homework
[00:53:21 - 00:53:27] >> and then in the homework they integrate
[00:53:24 - 00:53:27] uh Penteces
[00:53:28 - 00:53:31] from from there
[00:53:29 - 00:53:33] >> I'm pretty sure you will do that in the
[00:53:31 - 00:53:34] future lessons and
[00:53:33 - 00:53:39] >> yeah it's simple
[00:53:34 - 00:53:39] >> where is the chat
[00:53:39 - 00:53:45] how can I share
[00:53:42 - 00:53:45] link
[00:53:51 - 00:53:59] a if I start this chat it will
[00:53:55 - 00:54:02] >> so right now we see your inbox
[00:53:59 - 00:54:04] >> yeah I'm trying to
[00:54:02 - 00:54:08] >> but yeah I think what we will do is we
[00:54:04 - 00:54:11] will just ask uh in the homework to
[00:54:08 - 00:54:14] learn more about lofire and integrate.
[00:54:11 - 00:54:18] >> Uh can you please share this link with
[00:54:14 - 00:54:20] our um with our students?
[00:54:18 - 00:54:21] >> We we're going to use this link with the
[00:54:20 - 00:54:23] agent.
[00:54:21 - 00:54:25] >> Yes. And for those who are watching this
[00:54:23 - 00:54:28] in the recording, I'm going to put this
[00:54:25 - 00:54:30] in the description.
[00:54:28 - 00:54:33] >> So what we're going to do now, we will
[00:54:30 - 00:54:36] simulate the situation when we have our
[00:54:33 - 00:54:39] agent logs not locally but somewhere
[00:54:36 - 00:54:41] else. Yeah. in our loggers and uh it
[00:54:39 - 00:54:45] could be logfire, it could be langfuse
[00:54:41 - 00:54:48] or langid or anything else. Um you will
[00:54:45 - 00:54:52] learn about all these loggers later in
[00:54:48 - 00:54:54] future lessons. Um but today we will
[00:54:52 - 00:54:56] briefly discuss what to do with this
[00:54:54 - 00:55:00] logs. Yeah.
[00:54:56 - 00:55:03] Um we will just continue working in the
[00:55:00 - 00:55:08] same repo.
[00:55:03 - 00:55:10] We will ask um our agent to do
[00:55:08 - 00:55:14] to build like
[00:55:10 - 00:55:17] buildt pipeline
[00:55:14 - 00:55:19] for my agent
[00:55:17 - 00:55:25] logs
[00:55:19 - 00:55:28] um bought data from
[00:55:25 - 00:55:32] this link. This is our API link. when
[00:55:28 - 00:55:34] you have your uh real lofire account or
[00:55:32 - 00:55:36] any other account you will have you will
[00:55:34 - 00:55:43] do the same. Yeah, you will also have
[00:55:36 - 00:55:45] rest link and um yeah what point um logs
[00:55:43 - 00:55:48] and
[00:55:45 - 00:55:53] point
[00:55:48 - 00:55:54] um to DB. We will work with DB right
[00:55:53 - 00:55:58] now.
[00:55:54 - 00:56:00] and um
[00:55:58 - 00:56:03] like
[00:56:00 - 00:56:07] and okay we will ask
[00:56:03 - 00:56:11] build um marima report
[00:56:07 - 00:56:15] from this data [clears throat]
[00:56:11 - 00:56:19] again you can repeat this um
[00:56:15 - 00:56:22] uh prompt or you can write your own but
[00:56:19 - 00:56:25] the idea should be the same you provide
[00:56:22 - 00:56:30] the API link you mention what kind of
[00:56:25 - 00:56:32] what endpoints you want. Um not not logs
[00:56:30 - 00:56:34] endpoint because I want just one
[00:56:32 - 00:56:36] endpoint
[00:56:34 - 00:56:38] just log endpoint
[00:56:36 - 00:56:40] to uh the destination and ask if you
[00:56:38 - 00:56:43] want something extra. Yeah, I just want
[00:56:40 - 00:56:49] to have it enter. I just want to look at
[00:56:43 - 00:56:51] the data as soon as possible and run it.
[00:56:49 - 00:56:51] [clears throat]
[00:56:56 - 00:57:03] So now it will take a while. We can see
[00:56:59 - 00:57:08] that it it um
[00:57:03 - 00:57:10] now it uses another toolkit called REST
[00:57:08 - 00:57:16] API pipeline toolkit. This toolkit
[00:57:10 - 00:57:18] contains also um set of skills
[00:57:16 - 00:57:21] which are which have different purposes
[00:57:18 - 00:57:25] like create pipeline, debug pipeline,
[00:57:21 - 00:57:29] explore data, uh adjust and point, apply
[00:57:25 - 00:57:34] incremental loading. So it's um in AI
[00:57:29 - 00:57:36] workbench toolkit means um logical uh

## Window 007: 00:57:00 - 01:07:00

[00:57:03 - 00:57:10] now it uses another toolkit called REST
[00:57:08 - 00:57:16] API pipeline toolkit. This toolkit
[00:57:10 - 00:57:18] contains also um set of skills
[00:57:16 - 00:57:21] which are which have different purposes
[00:57:18 - 00:57:25] like create pipeline, debug pipeline,
[00:57:21 - 00:57:29] explore data, uh adjust and point, apply
[00:57:25 - 00:57:34] incremental loading. So it's um in AI
[00:57:29 - 00:57:36] workbench toolkit means um logical uh
[00:57:34 - 00:57:39] set of skills
[00:57:36 - 00:57:42] right right here right now. So it also
[00:57:39 - 00:57:46] can contain MCP
[00:57:42 - 00:57:48] um some uh scripts yeah some Python
[00:57:46 - 00:57:54] function or the languages functions. So
[00:57:48 - 00:57:54] in our case it's just uh skills and MCP.
[00:57:56 - 00:58:02] [clears throat] So this API uh was uh
[00:57:59 - 00:58:06] created by me. There's no authentication
[00:58:02 - 00:58:09] so you can request it freely. uh logs
[00:58:06 - 00:58:11] and point contains 1 million of fake
[00:58:09 - 00:58:14] cloth code traces.
[00:58:11 - 00:58:17] Um they are very similar to my real
[00:58:14 - 00:58:20] logs. Um but I I just don't want to
[00:58:17 - 00:58:24] share my personal data.
[00:58:20 - 00:58:24] Um [clears throat]
[00:58:25 - 00:58:31] so this skill will also figure out what
[00:58:28 - 00:58:33] is the base URL
[00:58:31 - 00:58:37] um what kind of pagenation it has. If
[00:58:33 - 00:58:39] you ever built data pipeline before and
[00:58:37 - 00:58:41] try to request API, you should
[00:58:39 - 00:58:43] understand how difficult it is. You need
[00:58:41 - 00:58:46] to know everything about this API. You
[00:58:43 - 00:58:50] need to know how to request data, how to
[00:58:46 - 00:58:53] pagionate over it. Um
[00:58:50 - 00:58:57] what should be the output? Yeah, in this
[00:58:53 - 00:59:00] case, data selector means that we uh use
[00:58:57 - 00:59:02] logs as a key of a very nested JSON. So
[00:59:00 - 00:59:05] there's so many details you don't need
[00:59:02 - 00:59:09] to know right now. You can just ask
[00:59:05 - 00:59:14] agent do that for you and we gave you
[00:59:09 - 00:59:18] tools um and rules how to do that right
[00:59:14 - 00:59:18] how to do that correctly.
[00:59:19 - 00:59:25] So what you need to do right now open
[00:59:21 - 00:59:26] your report and check data.
[00:59:25 - 00:59:29] [gasps]
[00:59:26 - 00:59:34] So
[00:59:29 - 00:59:34] how many ah my god I pressed
[00:59:35 - 00:59:43] it will load only 1k rows instead of
[00:59:37 - 00:59:47] million because I choose it. Um
[00:59:43 - 00:59:47] it it should make things faster.
[00:59:51 - 00:59:58] So right right now uh the pipeline is
[00:59:54 - 01:00:00] ready and agent just run it as regular
[00:59:58 - 01:00:03] Python script. You can do that manually
[01:00:00 - 01:00:07] in your common line as well
[01:00:03 - 01:00:12] but it's nice if agent do that because
[01:00:07 - 01:00:17] um because it will read logs
[01:00:12 - 01:00:17] and debug it automatically.
[01:00:17 - 01:00:21] >> [clears throat]
[01:00:19 - 01:00:23] >> So just a recap of what we're doing. Um
[01:00:21 - 01:00:25] I think it was a little the transition
[01:00:23 - 01:00:28] between these two things was a bit
[01:00:25 - 01:00:29] quick. So first we inspected the logs
[01:00:28 - 01:00:32] that we keep locally right. So these
[01:00:29 - 01:00:34] logs when we use coding agents
[01:00:32 - 01:00:37] >> they are in these JSON L files
[01:00:34 - 01:00:39] >> right uh so we were ingesting them and
[01:00:37 - 01:00:42] we were checking them in my demo like
[01:00:39 - 01:00:43] what exactly this looks uh what logs
[01:00:42 - 01:00:45] look like right
[01:00:43 - 01:00:48] >> but also when we use clo there are some
[01:00:45 - 01:00:50] logs that are stored on the clo site
[01:00:48 - 01:00:53] right is this when we use the web
[01:00:50 - 01:00:58] browser uh for clot or
[01:00:53 - 01:01:01] >> uh for this we use um fake API I built
[01:00:58 - 01:01:02] >> yeah I But like the fake API for what
[01:01:01 - 01:01:06] exactly what we are faking
[01:01:02 - 01:01:08] >> or for um clogs. Yeah. So just imagine
[01:01:06 - 01:01:12] you have your organization you have
[01:01:08 - 01:01:15] enterprise subscription and uh you have
[01:01:12 - 01:01:19] many workers and they use this cloud
[01:01:15 - 01:01:21] code daily and you want to build um this
[01:01:19 - 01:01:24] um kind of dashboard
[01:01:21 - 01:01:26] >> to know how it was used.
[01:01:24 - 01:01:29] >> Okay. And to get this data you need to
[01:01:26 - 01:01:31] request it through API
[01:01:29 - 01:01:33] >> because you don't have this data
[01:01:31 - 01:01:35] >> that you created a fake version of this.
[01:01:33 - 01:01:38] >> Yeah. So just yeah just imagine that
[01:01:35 - 01:01:43] this is not uh my fake API that it's
[01:01:38 - 01:01:46] entropic API and it has logs at point.
[01:01:43 - 01:01:49] We just build rest API pipeline get this
[01:01:46 - 01:01:52] data from API
[01:01:49 - 01:01:55] and do all the same. We load data to
[01:01:52 - 01:01:58] database and build report on top of it.
[01:01:55 - 01:02:02] >> But the idea is we just drop the link to
[01:01:58 - 01:02:04] whatever API we have into the chat and I
[01:02:02 - 01:02:06] mean to the CL session and then clot
[01:02:04 - 01:02:08] using the skills it figures out how
[01:02:06 - 01:02:11] exactly to load this and it uses this
[01:02:08 - 01:02:14] rest API skill I believe right?
[01:02:11 - 01:02:16] >> Yes correct. Yeah thank you Alex you sum
[01:02:14 - 01:02:20] up very well.
[01:02:16 - 01:02:23] Yeah this is example of my prompt. Yeah,
[01:02:20 - 01:02:24] just it can be there there are no rules
[01:02:23 - 01:02:29] here. Just give as much information as
[01:02:24 - 01:02:31] you have uh especially API link um
[01:02:29 - 01:02:34] destination what in what you want from
[01:02:31 - 01:02:38] to do with this data you can do nothing.
[01:02:34 - 01:02:42] Yeah. So something was built
[01:02:38 - 01:02:45] um let's take a look.
[01:02:42 - 01:02:49] So I think the rest pipeline this is our
[01:02:45 - 01:02:52] pipeline. The source is our fake API. I
[01:02:49 - 01:02:54] shared with you recently the endpoint
[01:02:52 - 01:02:58] logs
[01:02:54 - 01:03:01] it's also correctly um choose the
[01:02:58 - 01:03:01] pagenation
[01:03:01 - 01:03:07] yeah and build ty pipeline so delt
[01:03:04 - 01:03:09] pipeline for rest api source is also
[01:03:07 - 01:03:11] very
[01:03:09 - 01:03:14] intuitive you just need to describe your
[01:03:11 - 01:03:17] API as follows as a config just provide
[01:03:14 - 01:03:20] base URL type of pagionation what
[01:03:17 - 01:03:22] endpoints you want to requests
[01:03:20 - 01:03:24] um and run your pipeline as
[01:03:22 - 01:03:28] [clears throat] we did uh previously in
[01:03:24 - 01:03:30] file system pipeline. Define it, define
[01:03:28 - 01:03:33] source.
[01:03:30 - 01:03:38] Yeah, we can apply limits
[01:03:33 - 01:03:40] and run. So that's
[01:03:38 - 01:03:42] it. Uh this code will take data from
[01:03:40 - 01:03:46] your API doesn't matter. Yeah, it could
[01:03:42 - 01:03:49] be this uh test agent traces API. It
[01:03:46 - 01:03:52] could be entropic API or log fire API.
[01:03:49 - 01:03:52] Um
[01:03:53 - 01:03:59] so yeah and it will load data to your
[01:03:57 - 01:04:02] destination which also can be different.
[01:03:59 - 01:04:06] It could be ductb it could be poss
[01:04:02 - 01:04:10] database. It could be um snowflake or
[01:04:06 - 01:04:15] datab bricks. Um so if we take a look at
[01:04:10 - 01:04:19] delt hub um documentation you can find
[01:04:15 - 01:04:23] all type of destinations it supports.
[01:04:19 - 01:04:26] So you can load data to any destination.
[01:04:23 - 01:04:28] >> So there is a comment that uh it's
[01:04:26 - 01:04:32] difficult to achieve the same result uh
[01:04:28 - 01:04:35] I only have u copilot in visual studio
[01:04:32 - 01:04:37] code. Um
[01:04:35 - 01:04:39] so from what I understood in case of
[01:04:37 - 01:04:42] copilot when we use copilot it also
[01:04:39 - 01:04:45] recognizes this uh agents I believe
[01:04:42 - 01:04:48] right we have this agents folder
[01:04:45 - 01:04:50] >> that we created and it should also have
[01:04:48 - 01:04:53] the same skill discovery mechanism as
[01:04:50 - 01:04:54] clo or codex right
[01:04:53 - 01:04:58] >> so then we have this routter and then
[01:04:54 - 01:05:00] the routter would help uh
[01:04:58 - 01:05:03] >> uh if [laughter]
[01:05:00 - 01:05:07] if for some reason it didn't work uh I
[01:05:03 - 01:05:10] um can I ask you to report this case in
[01:05:07 - 01:05:14] our community? We have Slack community.
[01:05:10 - 01:05:16] You can find it um in our delyhub.com
[01:05:14 - 01:05:20] website
[01:05:16 - 01:05:24] just um
[01:05:20 - 01:05:28] so it's in docs there's a slack button
[01:05:24 - 01:05:33] join um the community and you can
[01:05:28 - 01:05:36] um direct message me or write feedback
[01:05:33 - 01:05:36] um in any channel you like
[01:05:36 - 01:05:38] [clears throat]
[01:05:36 - 01:05:40] >> but you're also in data do club right in
[01:05:38 - 01:05:42] our slack
[01:05:40 - 01:05:46] Yes, also yeah also I'm in a data talk
[01:05:42 - 01:05:49] club Slack as well please uh because we
[01:05:46 - 01:05:51] tested with many agents and with cursor
[01:05:49 - 01:05:53] it should work
[01:05:51 - 01:05:56] perfectly so I'm I I don't know what's
[01:05:53 - 01:05:59] the problem and if there is any problem
[01:05:56 - 01:06:00] we need to solve it as soon as possible
[01:05:59 - 01:06:02] okay
[01:06:00 - 01:06:05] >> yeah maybe what you can also do is just
[01:06:02 - 01:06:08] after this course try to
[01:06:05 - 01:06:09] um because like also we assume you
[01:06:08 - 01:06:12] already have some experience working
[01:06:09 - 01:06:14] with coding assistants. But if for you,
[01:06:12 - 01:06:16] you don't really have this experience
[01:06:14 - 01:06:17] for you. Maybe it's just too much
[01:06:16 - 01:06:20] information right now. So when you
[01:06:17 - 01:06:23] rewatch this video, try to just, you
[01:06:20 - 01:06:25] know, take uh breaks like you're
[01:06:23 - 01:06:27] watching something like just stop look
[01:06:25 - 01:06:30] at what we type and try to type the same
[01:06:27 - 01:06:32] thing in your coding assistant and then
[01:06:30 - 01:06:35] see what happens. So what you should see
[01:06:32 - 01:06:36] happening is that it loads a skill and
[01:06:35 - 01:06:39] then it tries to execute some things and
[01:06:36 - 01:06:41] then you should see the code appear
[01:06:39 - 01:06:44] appearing there. So this is the expected
[01:06:41 - 01:06:47] results and if it is it doesn't work
[01:06:44 - 01:06:49] this way then um contact.
[01:06:47 - 01:06:51] >> Yeah.
[01:06:49 - 01:06:52] But thank you for comments anyway.
[01:06:51 - 01:06:54] Please share your comments. Don't be
[01:06:52 - 01:06:57] shy.
[01:06:54 - 01:06:57] Okay.
[01:06:58 - 01:07:03] Uh let's [sighs and gasps]

## Window 008: 01:06:30 - 01:16:30

[01:06:30 - 01:06:35] see what happens. So what you should see
[01:06:32 - 01:06:36] happening is that it loads a skill and
[01:06:35 - 01:06:39] then it tries to execute some things and
[01:06:36 - 01:06:41] then you should see the code appear
[01:06:39 - 01:06:44] appearing there. So this is the expected
[01:06:41 - 01:06:47] results and if it is it doesn't work
[01:06:44 - 01:06:49] this way then um contact.
[01:06:47 - 01:06:51] >> Yeah.
[01:06:49 - 01:06:52] But thank you for comments anyway.
[01:06:51 - 01:06:54] Please share your comments. Don't be
[01:06:52 - 01:06:57] shy.
[01:06:54 - 01:06:57] Okay.
[01:06:58 - 01:07:03] Uh let's [sighs and gasps]
[01:07:00 - 01:07:06] um let's look at our data
[01:07:03 - 01:07:07] because again it's our main uh
[01:07:06 - 01:07:12] validation
[01:07:07 - 01:07:17] step when the human looks at the data.
[01:07:12 - 01:07:17] Um no it's not
[01:07:19 - 01:07:23] your it's my other report.
[01:07:24 - 01:07:30] Ah, okay.
[01:07:26 - 01:07:30] There is another link.
[01:07:32 - 01:07:38] Let's run it. Run all cells and look at
[01:07:36 - 01:07:40] the charts. Yeah, the data is not so
[01:07:38 - 01:07:43] interesting as previous one because it's
[01:07:40 - 01:07:46] not real and it's pretty much um
[01:07:43 - 01:07:48] boring.
[01:07:46 - 01:07:53] Um,
[01:07:48 - 01:07:56] but it's um the structure is the same as
[01:07:53 - 01:07:58] real. So when you build your own agents
[01:07:56 - 01:08:03] you will have you will have to deal with
[01:07:58 - 01:08:08] this kind of logs with the nested JSONs
[01:08:03 - 01:08:14] uh deeply nested JSONs. Yeah. So okay uh
[01:08:08 - 01:08:17] we built um data pipeline for our logs.
[01:08:14 - 01:08:20] We built reports. We explored data. But
[01:08:17 - 01:08:23] what now? Now we want to
[01:08:20 - 01:08:26] run this pipeline like every day to keep
[01:08:23 - 01:08:29] it fresh to know what um so every day we
[01:08:26 - 01:08:32] should have all updated uh information
[01:08:29 - 01:08:35] about the usage. Uh also we want to
[01:08:32 - 01:08:40] share it with our managers yeah or just
[01:08:35 - 01:08:42] colleagues. Um next steps should be
[01:08:40 - 01:08:46] deployment
[01:08:42 - 01:08:52] and at this step uh DL hub provides
[01:08:46 - 01:08:57] like native DT and AI native solution
[01:08:52 - 01:09:02] uh delt hub um platform.
[01:08:57 - 01:09:06] So we can you we can do that manually.
[01:09:02 - 01:09:09] We can run it manually with couple of um
[01:09:06 - 01:09:12] commands like
[01:09:09 - 01:09:12] hey
[01:09:12 - 01:09:18] [clears throat]
[01:09:13 - 01:09:20] like like u run ty hub
[01:09:18 - 01:09:23] lo
[01:09:20 - 01:09:28] login so this is also uh another comment
[01:09:23 - 01:09:31] I would like you to run it's very short
[01:09:28 - 01:09:34] uv run till the hub log in
[01:09:31 - 01:09:38] and press enter.
[01:09:34 - 01:09:38] It should open. Um,
[01:09:40 - 01:09:45] okay, I'm logged in. So, you just need
[01:09:42 - 01:09:51] to log in again as well. [sighs] Ah,
[01:09:45 - 01:09:51] okay. Let me actually log out
[01:09:53 - 01:09:57] and repeat
[01:09:55 - 01:10:00] your
[01:09:57 - 01:10:00] experience.
[01:10:04 - 01:10:08] and login.
[01:10:10 - 01:10:15] Yeah, this is how it should look like.
[01:10:12 - 01:10:18] So, I will use my
[01:10:15 - 01:10:18] umapp.com
[01:10:23 - 01:10:31] working email.
[01:10:26 - 01:10:31] It should send uh a mail
[01:10:44 - 01:10:48] and close the window.
[01:10:48 - 01:10:54] So
[01:10:50 - 01:10:59] now you are logged. Um so you connected
[01:10:54 - 01:11:02] your local workspace this um project
[01:10:59 - 01:11:05] with the Delta platform. It means if you
[01:11:02 - 01:11:08] run anything on your laptop it will be
[01:11:05 - 01:11:13] synced with Delta platform right now. So
[01:11:08 - 01:11:13] this is everything you need to do. Um
[01:11:13 - 01:11:20] okay for this experiment let's run ty
[01:11:18 - 01:11:22] hub
[01:11:20 - 01:11:25] um
[01:11:22 - 01:11:25] show
[01:11:27 - 01:11:33] ty hub show command will open UI
[01:11:31 - 01:11:37] platform.
[01:11:33 - 01:11:40] Uh it provides explicit link also it
[01:11:37 - 01:11:43] will redirect you to browser. So the
[01:11:40 - 01:11:47] comment is very simple. Tilty hub show.
[01:11:43 - 01:11:50] It should show you the UI.
[01:11:47 - 01:11:51] Every new account has playground
[01:11:50 - 01:11:55] workspace.
[01:11:51 - 01:11:58] And currently your local workspace
[01:11:55 - 01:12:00] should be connected to your playground
[01:11:58 - 01:12:04] workspace. It means if you run anything
[01:12:00 - 01:12:07] locally it it will be automatically
[01:12:04 - 01:12:10] updated here synced with the tilt
[01:12:07 - 01:12:10] platform.
[01:12:10 - 01:12:15] Okay,
[01:12:12 - 01:12:18] we can also
[01:12:15 - 01:12:22] use study hub age to see what kind what
[01:12:18 - 01:12:26] comments we have here. Um
[01:12:22 - 01:12:26] let's try to help workspace.
[01:12:30 - 01:12:36] Build hub workspace has um I also use h
[01:12:33 - 01:12:39] to see what kind of arguments it takes.
[01:12:36 - 01:12:41] Yeah, it has um arguments like lists or
[01:12:39 - 01:12:44] connect or info, show, dashboard,
[01:12:41 - 01:12:47] deploy. You can explore it yourself.
[01:12:44 - 01:12:49] I want to see the list of available
[01:12:47 - 01:12:51] workspaces.
[01:12:49 - 01:12:54] Uh and currently I have only one
[01:12:51 - 01:12:56] workspace. It's playground
[01:12:54 - 01:13:00] and this information is actually matches
[01:12:56 - 01:13:02] with my uh UI platform. I have only one
[01:13:00 - 01:13:06] workspace.
[01:13:02 - 01:13:07] Let's keep work in this workspace.
[01:13:06 - 01:13:10] Uh,
[01:13:07 - 01:13:13] Tilty Hub also provides skills for TyHub
[01:13:10 - 01:13:16] platform. What I can I want to do I just
[01:13:13 - 01:13:21] want to ask you
[01:13:16 - 01:13:21] um run this prompt deploy
[01:13:21 - 01:13:28] um
[01:13:23 - 01:13:28] which one rest. Yeah.
[01:13:39 - 01:13:45] Okay, let's just keep it deploy API
[01:13:42 - 01:13:45] pipeline
[01:13:47 - 01:13:54] and let's see what what happens.
[01:13:50 - 01:13:59] So it found um the hop platform toolkit.
[01:13:54 - 01:14:01] So again to kit um in in the happy hour
[01:13:59 - 01:14:06] bench it's a bunch of
[01:14:01 - 01:14:09] skills MCPS tools. Yeah. So it's could
[01:14:06 - 01:14:09] be anything.
[01:14:10 - 01:14:15] It's not installed yet and it's
[01:14:12 - 01:14:17] installing it now.
[01:14:15 - 01:14:20] Now it should uh go through the project
[01:14:17 - 01:14:22] structure check everything is um in
[01:14:20 - 01:14:25] place.
[01:14:22 - 01:14:29] Um yeah so there are also some checks
[01:14:25 - 01:14:32] five steps of checks. So it will it has
[01:14:29 - 01:14:36] um um defined workflow that should be
[01:14:32 - 01:14:39] done before we go to production
[01:14:36 - 01:14:43] and there is an existing deployment pipe
[01:14:39 - 01:14:47] manifest. Yes. Um now we can use this
[01:14:43 - 01:14:52] file in this file. This file usually
[01:14:47 - 01:14:54] pretty empty. And in this list we um
[01:14:52 - 01:14:56] just
[01:14:54 - 01:14:59] um
[01:14:56 - 01:15:02] provide what pipelines we want to run.
[01:14:59 - 01:15:04] Pipelines or
[01:15:02 - 01:15:08] um interactive jobs like Mariva
[01:15:04 - 01:15:11] notebooks or even streaml
[01:15:08 - 01:15:14] applications. You can everything you can
[01:15:11 - 01:15:17] just u list in this file and everything
[01:15:14 - 01:15:19] will be deployed on delt hub pip delt
[01:15:17 - 01:15:22] hub platform.
[01:15:19 - 01:15:26] Uh we will keep ductt for now. It
[01:15:22 - 01:15:28] suggested as some cloud um destination
[01:15:26 - 01:15:30] because currently we work with duct db
[01:15:28 - 01:15:36] and ddb is local database. It means if
[01:15:30 - 01:15:39] we deploy it on um delt hub platform
[01:15:36 - 01:15:42] delt hub file this one we worked with
[01:15:39 - 01:15:45] before
[01:15:42 - 01:15:50] this delt hub um file
[01:15:45 - 01:15:56] this db file uh it will be
[01:15:50 - 01:15:56] uh erased when your job is done
[01:15:57 - 01:16:05] but for for this step we will use the
[01:16:01 - 01:16:05] beam destination.
[01:16:09 - 01:16:14] So now it's reading deplor base skill.

## Window 009: 01:16:00 - 01:26:00

[01:16:01 - 01:16:05] beam destination.
[01:16:09 - 01:16:14] So now it's reading deplor base skill.
[01:16:30 - 01:16:32] [clears throat]
[01:16:33 - 01:16:36] So
[01:16:37 - 01:16:42] Alex say you can sum up what we're doing
[01:16:39 - 01:16:45] now because you you do that great.
[01:16:42 - 01:16:48] >> Yeah. Um so what we do is we already
[01:16:45 - 01:16:50] have this uh dashboards right u that we
[01:16:48 - 01:16:52] see. So first of all we ingested this
[01:16:50 - 01:16:56] local data then we ingested the data
[01:16:52 - 01:16:58] from this API and uh right now I don't
[01:16:56 - 01:16:59] want to correct me if I'm wrong. So
[01:16:58 - 01:17:01] right now we want to share it with the
[01:16:59 - 01:17:03] team. Right. So this is what we started
[01:17:01 - 01:17:05] at the beginning. At the beginning we we
[01:17:03 - 01:17:08] said okay we want to build this thing
[01:17:05 - 01:17:11] that is sharable. So now we want to um
[01:17:08 - 01:17:13] actually run the
[01:17:11 - 01:17:15] not only to be able to to share it with
[01:17:13 - 01:17:17] the rest of the team but also run the
[01:17:15 - 01:17:18] injection somewhere in the in the cloud
[01:17:17 - 01:17:21] right
[01:17:18 - 01:17:24] >> and u this is why we use DT hub so all
[01:17:21 - 01:17:25] the things will run there and there we
[01:17:24 - 01:17:27] will have the dashboard and this
[01:17:25 - 01:17:29] dashboard we can share with the team. We
[01:17:27 - 01:17:32] will not be able to do this with the
[01:17:29 - 01:17:35] local files those right though right?
[01:17:32 - 01:17:38] >> No. So you need to keep this local files
[01:17:35 - 01:17:40] somewhere in the cloud. So
[01:17:38 - 01:17:41] >> platform has access to it.
[01:17:40 - 01:17:43] >> Um now
[01:17:41 - 01:17:46] >> what if I wanted to share a dashboard
[01:17:43 - 01:17:48] that I built with my demo about uh my
[01:17:46 - 01:17:52] local usage local files. How do I do
[01:17:48 - 01:17:56] this? Can I do this with DT hub?
[01:17:52 - 01:17:57] uh your local cloud logs, you can just
[01:17:56 - 01:18:00] uh
[01:17:57 - 01:18:01] >> you can place these logs in um S3 bucket
[01:18:00 - 01:18:02] for example.
[01:18:01 - 01:18:02] >> Mhm.
[01:18:02 - 01:18:06] >> Uh
[01:18:02 - 01:18:09] >> but like let's say I don't want to
[01:18:06 - 01:18:11] >> keep the let's say if I ingest locally
[01:18:09 - 01:18:12] to some sort of uh data warehouse.
[01:18:11 - 01:18:15] >> Mhm.
[01:18:12 - 01:18:19] >> And then I can have the dashboard
[01:18:15 - 01:18:19] running in uh DT hub, right?
[01:18:20 - 01:18:26] >> Sorry again. Like if I so this talk this
[01:18:24 - 01:18:28] information is kind of private right I
[01:18:26 - 01:18:30] don't want to just uh put it somewhere
[01:18:28 - 01:18:32] on S3 right
[01:18:30 - 01:18:32] >> yeah but it could be your private S3
[01:18:32 - 01:18:35] bucket
[01:18:32 - 01:18:36] >> ah right so I make my bucket private and
[01:18:35 - 01:18:38] then I say okay like in order
[01:18:36 - 01:18:39] >> I provide credentials
[01:18:38 - 01:18:42] >> got it
[01:18:39 - 01:18:45] >> uh another option is you can just copy
[01:18:42 - 01:18:48] your logs into this uh project
[01:18:45 - 01:18:50] >> because uh to deploy this workspace D
[01:18:48 - 01:18:51] hub will wrap all this project
[01:18:50 - 01:18:54] >> mhm
[01:18:51 - 01:18:58] >> into container and run it
[01:18:54 - 01:19:01] >> in a cloud. So if you put your logs
[01:18:58 - 01:19:03] here, they will be deployed as well
[01:19:01 - 01:19:05] >> and uh the Delta Hub platform will have
[01:19:03 - 01:19:08] access to it. I mean so
[01:19:05 - 01:19:13] >> you can read um and build pipelines.
[01:19:08 - 01:19:17] >> So DT hub uh the DT hub platform is
[01:19:13 - 01:19:20] >> it's a host is a way to host our DT uh
[01:19:17 - 01:19:23] pipelines, right? So what we did locally
[01:19:20 - 01:19:25] was a DT hub pipeline, right? So we
[01:19:23 - 01:19:27] could do this locally but it's not easy
[01:19:25 - 01:19:29] to share. we need to have our computer
[01:19:27 - 01:19:32] up and running, right? But with the DT
[01:19:29 - 01:19:34] hub platform, all runs there, right? We
[01:19:32 - 01:19:37] don't have to worry about those things.
[01:19:34 - 01:19:40] >> Correct. You can uh run them here. You
[01:19:37 - 01:19:44] can uh schedule them. You can also
[01:19:40 - 01:19:48] create um uh pipes like run this
[01:19:44 - 01:19:50] pipeline and if it success um run this
[01:19:48 - 01:19:53] pipeline then run transformations. If
[01:19:50 - 01:19:57] these both injection pipelines succeeded
[01:19:53 - 01:20:00] uh then run report. Yeah. So it can be
[01:19:57 - 01:20:04] uh connected and triggered uh by rules
[01:20:00 - 01:20:06] you provide and um yeah also it's not
[01:20:04 - 01:20:10] only about data pipelines, it's also
[01:20:06 - 01:20:12] about the reports. So you can deploy any
[01:20:10 - 01:20:15] application you want like streaml
[01:20:12 - 01:20:18] application, marob notebook application
[01:20:15 - 01:20:22] >> and um share it with your team.
[01:20:18 - 01:20:24] >> Yeah. very very useful. So we have a
[01:20:22 - 01:20:26] question. I don't know it's still doing
[01:20:24 - 01:20:27] something. We can talk about questions,
[01:20:26 - 01:20:29] right?
[01:20:27 - 01:20:32] >> So the question is like when do I
[01:20:29 - 01:20:35] actually need to use uh DT? What is the
[01:20:32 - 01:20:42] advantage of using DT for my projects?
[01:20:35 - 01:20:45] >> Um it's just a bunch of pre-built um
[01:20:42 - 01:20:48] functions. Yeah. Uh you can ask about
[01:20:45 - 01:20:49] any other tool. Why would you use it?
[01:20:48 - 01:20:52] because you don't want to rebuild it
[01:20:49 - 01:20:55] from scratch every time. If you want to
[01:20:52 - 01:20:58] move your data from unstructured JSON to
[01:20:55 - 01:21:01] database, you need to do a lot of work.
[01:20:58 - 01:21:05] You can watch our free code camp course
[01:21:01 - 01:21:07] with Alex uh which demonstrates you uh
[01:21:05 - 01:21:11] how much work you need to do to just
[01:21:07 - 01:21:13] upload one JSON to relational database.
[01:21:11 - 01:21:16] It's uh
[01:21:13 - 01:21:18] you of course you can cloth can build
[01:21:16 - 01:21:21] everything for you every time you need a
[01:21:18 - 01:21:21] new pipeline from scratch but again
[01:21:21 - 01:21:24] >> [clears throat]
[01:21:21 - 01:21:26] >> um how correct it is uh who will is
[01:21:24 - 01:21:28] going to maintain it uh do you know
[01:21:26 - 01:21:33] every feature you need all the best
[01:21:28 - 01:21:35] practices provide um it's just a tool
[01:21:33 - 01:21:38] delt it's a open source Python library
[01:21:35 - 01:21:42] why do you need pandas or numpy yeah
[01:21:38 - 01:21:45] because um you have to do that again and
[01:21:42 - 01:21:48] again and again for new pipelines and
[01:21:45 - 01:21:54] instead of it you can reuse ready to go
[01:21:48 - 01:21:56] code um from experienced data engineers
[01:21:54 - 01:21:58] and good developers
[01:21:56 - 01:22:00] who maintain it for you. So
[01:21:58 - 01:22:04] >> Mhm. So this this is basically a tool uh
[01:22:00 - 01:22:08] that we can use for ingesting any data
[01:22:04 - 01:22:10] from any data source to any target. Just
[01:22:08 - 01:22:14] in this case in this scenario the source
[01:22:10 - 01:22:16] was uh first local uh files that we had
[01:22:14 - 01:22:18] and then from these local files they we
[01:22:16 - 01:22:23] put them in duct DP and visualized and
[01:22:18 - 01:22:26] in the second case uh the source was a
[01:22:23 - 01:22:28] rest API and the target was um again
[01:22:26 - 01:22:30] duct DB right but this time we showed
[01:22:28 - 01:22:35] this in in the cloud there was a
[01:22:30 - 01:22:35] dashboard that we we visualized right
[01:22:35 - 01:22:40] >> okay
[01:22:36 - 01:22:40] >> uh so Uh
[01:22:41 - 01:22:48] so it says that pipeline was deployed.
[01:22:45 - 01:22:50] Let's take a look.
[01:22:48 - 01:22:52] Yeah, it says completed. Data were uh
[01:22:50 - 01:22:55] loaded.
[01:22:52 - 01:22:59] But again, yeah, it was loaded um to
[01:22:55 - 01:23:02] duct DB and DDB is a local uh database.
[01:22:59 - 01:23:04] It means every time when uh the job is
[01:23:02 - 01:23:07] done
[01:23:04 - 01:23:09] everything will be removed like all
[01:23:07 - 01:23:12] local files on this machine will be
[01:23:09 - 01:23:15] removed. It's ephemeral storage to keep
[01:23:12 - 01:23:18] your data somewhere. People usually use
[01:23:15 - 01:23:22] cloud uh cloud
[01:23:18 - 01:23:26] um u databases. It could be your local
[01:23:22 - 01:23:29] Postgress instance deployed on AWS or it
[01:23:26 - 01:23:31] could be snowflake. Yeah, again BigQuery
[01:23:29 - 01:23:33] or Click House.
[01:23:31 - 01:23:34] >> I think your clot suggested to use
[01:23:33 - 01:23:38] mother duck
[01:23:34 - 01:23:42] >> or it could be mother duck but uh for
[01:23:38 - 01:23:43] this um workshop I have idea better
[01:23:42 - 01:23:50] idea.
[01:23:43 - 01:23:52] Uh let's just replace DV to playground.
[01:23:50 - 01:23:56] This is still the app managed storage
[01:23:52 - 01:23:58] for tests, experiments, demos. Yeah. So
[01:23:56 - 01:24:01] you can use this playground destination.
[01:23:58 - 01:24:04] Uh just go to your rest pipeline.py
[01:24:01 - 01:24:08] change it to playground.
[01:24:04 - 01:24:12] Um it was DDB before
[01:24:08 - 01:24:16] we just simply rename it. Yeah. From
[01:24:12 - 01:24:20] duct DB to playground
[01:24:16 - 01:24:22] and run it again.
[01:24:20 - 01:24:26] uh we can
[01:24:22 - 01:24:28] ask agent to do that or we can do that
[01:24:26 - 01:24:33] ourself.
[01:24:28 - 01:24:35] How to do that? UV run delt hub
[01:24:33 - 01:24:39] we run
[01:24:35 - 01:24:43] deploy it will sync your local project
[01:24:39 - 01:24:45] your local workspace with um the dehub
[01:24:43 - 01:24:48] platform because currently we changed
[01:24:45 - 01:24:51] something yeah it's need to be synced so
[01:24:48 - 01:24:54] I run hub deploy it checked everything
[01:24:51 - 01:24:57] is um the same
[01:24:54 - 01:25:00] um
[01:24:57 - 01:25:03] yeah see changed workspace files
[01:25:00 - 01:25:03] and
[01:25:04 - 01:25:10] run and I run it again. You can ask
[01:25:07 - 01:25:13] cloth to do that for you or other agent
[01:25:10 - 01:25:16] to do that for you. Uh all skills knows
[01:25:13 - 01:25:22] know what to do but it's so simple. So I
[01:25:16 - 01:25:22] I don't see any advantage of usage.
[01:25:22 - 01:25:29] Okay, it also gave you some link but we
[01:25:25 - 01:25:32] already have it open. Let's go to jobs.
[01:25:29 - 01:25:36] see all runningings here. This is our
[01:25:32 - 01:25:39] previous run and now we have another run
[01:25:36 - 01:25:42] with different destination.
[01:25:39 - 01:25:45] The previous one was was with ductb a
[01:25:42 - 01:25:50] new one with playground. Playground is a
[01:25:45 - 01:25:50] managed uh ty hub platform destination.
[01:25:54 - 01:26:01] Oh uh I forgot one thing. This
[01:25:56 - 01:26:04] playground destination requires um

## Window 010: 01:25:30 - 01:33:01

[01:25:32 - 01:25:39] previous run and now we have another run
[01:25:36 - 01:25:42] with different destination.
[01:25:39 - 01:25:45] The previous one was was with ductb a
[01:25:42 - 01:25:50] new one with playground. Playground is a
[01:25:45 - 01:25:50] managed uh ty hub platform destination.
[01:25:54 - 01:26:01] Oh uh I forgot one thing. This
[01:25:56 - 01:26:04] playground destination requires um
[01:26:01 - 01:26:06] dela lake
[01:26:04 - 01:26:09] dependency.
[01:26:06 - 01:26:09] Let's
[01:26:11 - 01:26:14] cancel it.
[01:26:15 - 01:26:20] Sync it again. Yeah, you rerun delty hub
[01:26:18 - 01:26:25] deploy.
[01:26:20 - 01:26:29] It's installed data lake dependency in
[01:26:25 - 01:26:29] our pi project toml.
[01:26:31 - 01:26:40] So it was synced
[01:26:35 - 01:26:40] and now if we run the pipeline again
[01:26:40 - 01:26:46] should work.
[01:26:43 - 01:26:49] You can go to jobs. This is our third
[01:26:46 - 01:26:49] run.
[01:26:54 - 01:27:00] What I would also recommend uh like if
[01:26:56 - 01:27:02] you want to learn more about DT uh last
[01:27:00 - 01:27:04] year in zoom camp in this course we also
[01:27:02 - 01:27:08] had a workshop with DT and for the
[01:27:04 - 01:27:10] homework what we did is we took the data
[01:27:08 - 01:27:12] we had and we ingested this data into
[01:27:10 - 01:27:14] quadrant. So this year we don't use
[01:27:12 - 01:27:17] quadrant but for you if you want to
[01:27:14 - 01:27:19] check what you can do with uh DT and
[01:27:17 - 01:27:22] what is useful specifically for LLM
[01:27:19 - 01:27:25] engineering or
[01:27:22 - 01:27:27] AI engineering. Um so this was a very
[01:27:25 - 01:27:30] nice homework that actually shows uh
[01:27:27 - 01:27:32] like how can you use for this thing for
[01:27:30 - 01:27:35] your rack applications for your agents.
[01:27:32 - 01:27:37] So check it out and uh this year we will
[01:27:35 - 01:27:40] come up with some something similar for
[01:27:37 - 01:27:40] the homework.
[01:27:42 - 01:27:45] It takes some time.
[01:27:47 - 01:27:54] I hope uh our dev team didn't change
[01:27:49 - 01:27:57] anything during this workshop.
[01:27:54 - 01:27:57] Yeah.
[01:27:58 - 01:28:06] Okay. It's done.
[01:28:01 - 01:28:06] D to be. Why it's stuck to be again?
[01:28:06 - 01:28:11] Where's the be pipeline? run agent
[01:28:12 - 01:28:15] background.
[01:28:16 - 01:28:22] Okay, maybe we need to rename it. Oh no.
[01:28:26 - 01:28:32] Okay, we have to
[01:28:29 - 01:28:36] we have now two
[01:28:32 - 01:28:36] functions here.
[01:28:38 - 01:28:46] My apology.
[01:28:41 - 01:28:46] Okay. Sync again. Deploy
[01:28:47 - 01:28:50] and run.
[01:28:50 - 01:28:58] We actually can run jobs. We can trigger
[01:28:54 - 01:29:00] them from uh UI.
[01:28:58 - 01:29:04] Um
[01:29:00 - 01:29:05] start run cancel run new details. Manage
[01:29:04 - 01:29:09] schedule. We can schedule it from UI. So
[01:29:05 - 01:29:12] we can schedule it from uh Python.
[01:29:09 - 01:29:14] >> Uh do you have a dashboard that you
[01:29:12 - 01:29:14] already built before to show us?
[01:29:14 - 01:29:16] >> Um
[01:29:14 - 01:29:17] >> so I kind of need to go. So that's why
[01:29:16 - 01:29:24] I'm
[01:29:17 - 01:29:27] >> Oh no. Oh no. Um yeah, let's uh
[01:29:24 - 01:29:32] let's just include it here.
[01:29:27 - 01:29:38] Um from
[01:29:32 - 01:29:38] agent log dish port. I know just import.
[01:29:39 - 01:29:44] So we just include it to our manifest
[01:29:42 - 01:29:46] and it will
[01:29:44 - 01:29:47] um automatically deploy your Marimo
[01:29:46 - 01:29:52] dashboard.
[01:29:47 - 01:29:54] So check logs
[01:29:52 - 01:29:57] um
[01:29:54 - 01:30:01] ah the only moment we need to
[01:29:57 - 01:30:05] um change
[01:30:01 - 01:30:05] our destination here as well.
[01:30:05 - 01:30:15] playground and um data set name genti
[01:30:12 - 01:30:19] looks data playground.
[01:30:15 - 01:30:23] Cool. So now it should be
[01:30:19 - 01:30:23] it should work.
[01:30:25 - 01:30:32] Yeah. So far our pipeline um
[01:30:28 - 01:30:37] successfully completed
[01:30:32 - 01:30:40] and yeah we can see that we added new
[01:30:37 - 01:30:47] job to deploy it will be triggered as
[01:30:40 - 01:30:47] HTTP as a interactive job and run it.
[01:30:47 - 01:30:55] [gasps] Um since uh we already have this
[01:30:51 - 01:30:57] um data in our playground,
[01:30:55 - 01:31:00] we can go to notebooks
[01:30:57 - 01:31:05] and we can see that notebook was
[01:31:00 - 01:31:05] deployed. Just run it.
[01:31:12 - 01:31:20] >> That's the matima n. Yeah, it's um yeah,
[01:31:17 - 01:31:22] it show it in um run mode, not in edit
[01:31:20 - 01:31:25] mode. So there's no code. All the code
[01:31:22 - 01:31:28] is hidden. We can see only reports, only
[01:31:25 - 01:31:31] visuals.
[01:31:28 - 01:31:33] Um so yeah, your report is here. Your
[01:31:31 - 01:31:36] data in your destination. Yeah, it could
[01:31:33 - 01:31:42] be um mother duck, bigquery, snowflake
[01:31:36 - 01:31:47] as or cute any um vector storage
[01:31:42 - 01:31:49] databases like ldb v8 or it could be
[01:31:47 - 01:31:54] file system um it could be bunch of
[01:31:49 - 01:31:57] parker files or json somewhere in your
[01:31:54 - 01:31:59] s3 buckets in a very good structured
[01:31:57 - 01:32:02] format.
[01:31:59 - 01:32:04] So this is um pretty much what I wanted
[01:32:02 - 01:32:07] to show. Um yeah, I have a lot to show
[01:32:04 - 01:32:07] [clears throat] but we have no time to
[01:32:07 - 01:32:09] see.
[01:32:07 - 01:32:11] >> Thanks. Yeah, I really have to run now.
[01:32:09 - 01:32:12] Like people are waiting for my other
[01:32:11 - 01:32:13] stream.
[01:32:12 - 01:32:16] >> Okay, sorry.
[01:32:13 - 01:32:18] >> So yeah, thanks a lot for uh showing
[01:32:16 - 01:32:20] this. Thanks everyone for attending. We
[01:32:18 - 01:32:22] will come up with uh something
[01:32:20 - 01:32:24] interesting for your homework. So there
[01:32:22 - 01:32:27] will be announcements. So thanks for
[01:32:24 - 01:32:29] joining us today and have fun with DT.
[01:32:27 - 01:32:32] It's really good tool and I'm really
[01:32:29 - 01:32:34] happy to see the skills cuz right now I
[01:32:32 - 01:32:36] can just ask what I want and then I go
[01:32:34 - 01:32:38] get some tea, come back and the pipeline
[01:32:36 - 01:32:41] is already working. This is so amazing.
[01:32:38 - 01:32:43] Like when Alona showed me this um was it
[01:32:41 - 01:32:46] a month ago like my mind was blown. So
[01:32:43 - 01:32:50] this is so cool. Um so yeah give it a
[01:32:46 - 01:32:52] try and sorry I need to to kind of rush
[01:32:50 - 01:32:55] and run right now but yeah people are
[01:32:52 - 01:32:57] waiting so I'm yeah I'm leaving. So bye.
[01:32:55 - 01:32:58] Thank you so much for hosting. Thank
[01:32:57 - 01:32:59] you. Thank Thank you so much for
[01:32:58 - 01:33:01] watching.
[01:32:59 - 01:33:01] >> Yeah.
