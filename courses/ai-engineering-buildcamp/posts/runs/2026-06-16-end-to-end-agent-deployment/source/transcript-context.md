# Transcript Context

Source: /Users/valeria/short-video-automation/h84rcRezNM4/full_transcript.json
Duration: 01:56:11
Segments: 2377

Use these windows to mine social post ideas across the full transcript. Ideas may span multiple windows.

## Window 001: 00:00:01 - 00:08:01

[00:00:01 - 00:00:06] Oh, hi everyone. Welcome to this event.
[00:00:04 - 00:00:07] This is actually our first event of AI
[00:00:06 - 00:00:10] shipping lab. So, I'm very excited about
[00:00:07 - 00:00:13] this. And typically, uh, when I do
[00:00:10 - 00:00:15] events publicly, I try to make them very
[00:00:13 - 00:00:18] polished. So, I really go through many
[00:00:15 - 00:00:19] iterations before I do this. Today, I
[00:00:18 - 00:00:21] want to do something differently,
[00:00:19 - 00:00:24] something different with you. So, I want
[00:00:21 - 00:00:26] to show a process that is more row that
[00:00:24 - 00:00:27] I have some ideas of what we want to
[00:00:26 - 00:00:31] implement, but we will go through this
[00:00:27 - 00:00:34] together. And um
[00:00:31 - 00:00:36] I want you to also feel free to
[00:00:34 - 00:00:38] interrupt me and ask questions as we go
[00:00:36 - 00:00:40] along. Ask me, hey, why did you do this?
[00:00:38 - 00:00:44] Why did you do that? So I want to make
[00:00:40 - 00:00:46] this as interactive as possible. And um
[00:00:44 - 00:00:48] yeah, I have some I have prepared some
[00:00:46 - 00:00:52] materials. I'm going to share uh my
[00:00:48 - 00:00:55] screen now. So what I did is oops this
[00:00:52 - 00:00:57] oops this uh gist. So this notebook. So
[00:00:55 - 00:00:59] there is some code that I'm going to use
[00:00:57 - 00:01:02] so I don't spend a lot of time typing.
[00:00:59 - 00:01:05] Uh and the goal to for today is we want
[00:01:02 - 00:01:07] to have something deployed right. So we
[00:01:05 - 00:01:09] want to create an agent and for this
[00:01:07 - 00:01:12] agent we want to have back end and front
[00:01:09 - 00:01:14] end and we want to deploy it somewhere
[00:01:12 - 00:01:17] right um I have some ideas of how we
[00:01:14 - 00:01:18] will go about that but also feel free
[00:01:17 - 00:01:21] during the session to stop me and say
[00:01:18 - 00:01:24] hey but how about we do it this way and
[00:01:21 - 00:01:28] I'm happy to adjust along the way how we
[00:01:24 - 00:01:30] do this. So the goal is that we we do
[00:01:28 - 00:01:32] this interactively. This is the first
[00:01:30 - 00:01:35] time I'm trying to do this at least
[00:01:32 - 00:01:38] online. So I've did I have done
[00:01:35 - 00:01:41] something similar um offline where we
[00:01:38 - 00:01:44] sit in one room but today I I want to
[00:01:41 - 00:01:46] try something like that um offline. So
[00:01:44 - 00:01:50] what we want today what we want to build
[00:01:46 - 00:01:53] today is an agent that we will reply. So
[00:01:50 - 00:01:56] this is a rack agent. So this rack agent
[00:01:53 - 00:01:59] will reply to our questions and we want
[00:01:56 - 00:02:02] to build a nice interface for that.
[00:01:59 - 00:02:05] Right. So um
[00:02:02 - 00:02:08] what we will use the data set is uh from
[00:02:05 - 00:02:10] our data talks club courses. So we have
[00:02:08 - 00:02:15] courses we have frequently asked
[00:02:10 - 00:02:16] questions for these courses and there um
[00:02:15 - 00:02:18] it's actually this is the website where
[00:02:16 - 00:02:21] these questions are. So this is how
[00:02:18 - 00:02:24] these questions look like. So for
[00:02:21 - 00:02:26] example um the typical question that we
[00:02:24 - 00:02:29] uh course participants of this course
[00:02:26 - 00:02:31] can ask are I just discovered the course
[00:02:29 - 00:02:33] can I still join right so this is a very
[00:02:31 - 00:02:35] typical question that uh course
[00:02:33 - 00:02:38] participants can ask these questions are
[00:02:35 - 00:02:40] available in JSON format right so uh
[00:02:38 - 00:02:43] what we can do is for example if we're
[00:02:40 - 00:02:45] interested in this data engineering zoom
[00:02:43 - 00:02:49] cam questions then we can just take this
[00:02:45 - 00:02:52] path and append it here and then we will
[00:02:49 - 00:02:56] get machine readable format. So we will
[00:02:52 - 00:02:59] get JSON data uh from this. Um so this
[00:02:56 - 00:03:01] is the data we are going to uh use today
[00:02:59 - 00:03:04] and we are going to build a bot that uh
[00:03:01 - 00:03:07] will reply uh to these questions and I'm
[00:03:04 - 00:03:08] going to start completely from scratch.
[00:03:07 - 00:03:10] So uh cuz for you it could be
[00:03:08 - 00:03:13] interesting also to see the setup I
[00:03:10 - 00:03:15] have. So the setup I have right now is I
[00:03:13 - 00:03:19] have a remote machine. So this remote
[00:03:15 - 00:03:23] machine uh is running on HNAER.
[00:03:19 - 00:03:26] Hadner um so on HNER you can um get a
[00:03:23 - 00:03:29] dedicated server that you can rent u
[00:03:26 - 00:03:32] like they they just get an actual server
[00:03:29 - 00:03:36] and install it in um
[00:03:32 - 00:03:38] I don't know data center somewhere.
[00:03:36 - 00:03:41] So it's kind of like cloud but more long
[00:03:38 - 00:03:43] term right? So it's not really like AWS
[00:03:41 - 00:03:46] you actually rent an actual server
[00:03:43 - 00:03:49] right. So with specific characteristics
[00:03:46 - 00:03:52] with
[00:03:49 - 00:03:55] yeah a server. So um I have a server. So
[00:03:52 - 00:03:58] for me I have an alias for connecting to
[00:03:55 - 00:04:02] this server. Uh it's just h so for me
[00:03:58 - 00:04:06] it's it's SSA it's a alias for SSHA. So
[00:04:02 - 00:04:08] then I can SSH to this uh address.
[00:04:06 - 00:04:10] So this is a fairly good machine. So
[00:04:08 - 00:04:11] then I don't know if you're interested
[00:04:10 - 00:04:13] maybe you want to get something like
[00:04:11 - 00:04:15] that. Running things locally is totally
[00:04:13 - 00:04:19] fine too. It's just for me I have
[00:04:15 - 00:04:22] multiple u laptops. Um so for me I have
[00:04:19 - 00:04:25] this remote environment where I work
[00:04:22 - 00:04:28] right. Um so in this remote environment
[00:04:25 - 00:04:31] it's Linux usual Linux. So I'll just
[00:04:28 - 00:04:33] create a folder that we will um use for
[00:04:31 - 00:04:35] today's workshop. So the folder I'll
[00:04:33 - 00:04:40] call this folder
[00:04:35 - 00:04:43] um I don't know and to end agent. I just
[00:04:40 - 00:04:45] came up with this name. Um
[00:04:43 - 00:04:48] so I will commit this code uh and share
[00:04:45 - 00:04:52] it the link with you after we finish. So
[00:04:48 - 00:04:55] I'll share the link uh in our slack.
[00:04:52 - 00:05:00] Um but yeah so this is um where we are
[00:04:55 - 00:05:04] going to uh work and I'll use uh so I
[00:05:00 - 00:05:07] have these things from zoom that really
[00:05:04 - 00:05:10] interfere with
[00:05:07 - 00:05:13] um so I'm going to use in it to start a
[00:05:10 - 00:05:15] project and we will do we will add
[00:05:13 - 00:05:18] Jupiter
[00:05:15 - 00:05:21] we will add open AI
[00:05:18 - 00:05:25] and I want to add UV uh I want to add
[00:05:21 - 00:05:28] Jupiter as a deaf uh dependency Jupiter
[00:05:25 - 00:05:31] cuz as a develop I want to use Jupiter
[00:05:28 - 00:05:33] but later uh when we actually deploy it
[00:05:31 - 00:05:36] we don't need Jupyter that's why I add
[00:05:33 - 00:05:40] Jupiter as a dependency
[00:05:36 - 00:05:44] and um I will now start Jupyter notebook
[00:05:40 - 00:05:44] run Jupiter notebook
[00:05:44 - 00:05:51] also now I want to connect to u this
[00:05:48 - 00:05:55] folder from my visual studio
[00:05:51 - 00:05:57] So I will um I have an extension called
[00:05:55 - 00:06:02] remote extension. So I can actually
[00:05:57 - 00:06:04] connect to uh my head snare server
[00:06:02 - 00:06:06] like you again you can use your local
[00:06:04 - 00:06:09] environment doesn't matter. I just
[00:06:06 - 00:06:12] wanted to show how I usually work.
[00:06:09 - 00:06:16] Uh so then I um
[00:06:12 - 00:06:20] open um this end to end agent folder. So
[00:06:16 - 00:06:20] now I have it in my Visual Studio Code.
[00:06:24 - 00:06:32] U so Vancheska. Hi Vesa. You can follow
[00:06:28 - 00:06:34] along. Yes. Um or you can watch and ask
[00:06:32 - 00:06:38] questions.
[00:06:34 - 00:06:40] It can be fast but you can stop me
[00:06:38 - 00:06:42] right. Um some things at some point I
[00:06:40 - 00:06:45] think may get fast. So at the beginning
[00:06:42 - 00:06:47] I use um
[00:06:45 - 00:06:49] this thing that I shared with you.
[00:06:47 - 00:06:52] Right. So I will be copy pasting things
[00:06:49 - 00:06:54] from this document and then we will um
[00:06:52 - 00:06:56] edit some things but at some point when
[00:06:54 - 00:07:00] I start using coding agents this could
[00:06:56 - 00:07:02] be difficult to follow right so maybe at
[00:07:00 - 00:07:04] uh at this point you can just watch and
[00:07:02 - 00:07:06] ask me questions um I don't know up to
[00:07:04 - 00:07:07] you you can try to do this some things
[00:07:06 - 00:07:12] might not work for you in the same way
[00:07:07 - 00:07:14] as for me um so yeah but I think it
[00:07:12 - 00:07:17] wouldn't hurt to actually try to follow
[00:07:14 - 00:07:17] as much as you
[00:07:18 - 00:07:23] Uh which service are you using for
[00:07:20 - 00:07:25] running this and why? Uh what do you
[00:07:23 - 00:07:26] mean which service? Like what exactly do
[00:07:25 - 00:07:30] you mean like right now we are not
[00:07:26 - 00:07:33] running anything? Aher. Okay. So HNER
[00:07:30 - 00:07:36] headser is a remote machine. So think of
[00:07:33 - 00:07:38] um an instance in AWS something similar
[00:07:36 - 00:07:40] right. So it's just a computer that is
[00:07:38 - 00:07:43] not with me all the time. I can connect
[00:07:40 - 00:07:45] to it from my laptop from my tablet that
[00:07:43 - 00:07:48] is always up and running. So I can some
[00:07:45 - 00:07:50] I can have some long running jobs there.
[00:07:48 - 00:07:53] I can have my coding agents doing stuff
[00:07:50 - 00:07:55] there. Uh it doesn't have to u be up and
[00:07:53 - 00:07:59] running all the time. So it's called
[00:07:55 - 00:08:02] headsner. So this is the service.
[00:07:59 - 00:08:06] And for this machine I payund

## Window 002: 00:07:31 - 00:15:31

[00:07:33 - 00:07:38] um an instance in AWS something similar
[00:07:36 - 00:07:40] right. So it's just a computer that is
[00:07:38 - 00:07:43] not with me all the time. I can connect
[00:07:40 - 00:07:45] to it from my laptop from my tablet that
[00:07:43 - 00:07:48] is always up and running. So I can some
[00:07:45 - 00:07:50] I can have some long running jobs there.
[00:07:48 - 00:07:53] I can have my coding agents doing stuff
[00:07:50 - 00:07:55] there. Uh it doesn't have to u be up and
[00:07:53 - 00:07:59] running all the time. So it's called
[00:07:55 - 00:08:02] headsner. So this is the service.
[00:07:59 - 00:08:06] And for this machine I payund
[00:08:02 - 00:08:06] something per month.
[00:08:08 - 00:08:11] uh could you also explain why you chose
[00:08:10 - 00:08:14] these specific tools to build the
[00:08:11 - 00:08:16] pipeline as we go through this uh
[00:08:14 - 00:08:18] workshop you can just stop me and ask me
[00:08:16 - 00:08:23] hey why do you do this this way so I
[00:08:18 - 00:08:23] think will be easier
[00:08:23 - 00:08:32] okay so um now I have created this um
[00:08:29 - 00:08:34] this is the what we have
[00:08:32 - 00:08:37] um so what I want to do next is I want
[00:08:34 - 00:08:39] to create a file so this is where we are
[00:08:37 - 00:08:44] going to keep our secrets. So I'm going
[00:08:39 - 00:08:48] to also add uh n to get ignore and I
[00:08:44 - 00:08:52] want to use open AI API key
[00:08:48 - 00:08:53] to for today right so like if you use
[00:08:52 - 00:08:55] something else feel free to use
[00:08:53 - 00:08:59] something else could be grock could be
[00:08:55 - 00:09:01] anthropic whatever so I'll use um openai
[00:08:59 - 00:09:04] so uh right now uh what I will do is
[00:09:01 - 00:09:08] I'll go to openai I'll create a new
[00:09:04 - 00:09:10] secret key and I'll call it uh end to
[00:09:08 - 00:09:14] end workshop. So for a moment I'll stop
[00:09:10 - 00:09:14] sharing the screen.
[00:09:14 - 00:09:23] I'll get the key
[00:09:18 - 00:09:23] and I will put this key inside my
[00:09:23 - 00:09:28] and I will start sharing the screen
[00:09:25 - 00:09:30] again.
[00:09:28 - 00:09:33] So now I have my
[00:09:30 - 00:09:37] and uh wait.
[00:09:33 - 00:09:37] So let me close that.
[00:09:37 - 00:09:44] So Jupiter is running. I think one more
[00:09:40 - 00:09:48] thing I want to uh add here in Jupiter
[00:09:44 - 00:09:48] is uh I want to install here
[00:09:50 - 00:09:58] workshop. So I want to add
[00:09:55 - 00:10:01] uh python.
[00:09:58 - 00:10:06] So then I can parse these things uh this
[00:10:01 - 00:10:06] um these keys.
[00:10:06 - 00:10:13] Okay. So, I'm creating a new notebook.
[00:10:09 - 00:10:18] I'll call it uh notebook and then I'll
[00:10:13 - 00:10:19] do from uh nth import maybe you know
[00:10:18 - 00:10:22] what uh maybe I should actually instead
[00:10:19 - 00:10:24] of using that
[00:10:22 - 00:10:27] I'll see. So I was thinking whether I
[00:10:24 - 00:10:30] should use um Visual Studio Code Jupiter
[00:10:27 - 00:10:32] or I should use that. In Visual Studio
[00:10:30 - 00:10:35] Code it's convenient that I can have
[00:10:32 - 00:10:38] autocomplete and I can also have Copilot
[00:10:35 - 00:10:41] helping me. Um
[00:10:38 - 00:10:44] okay so what I will do now is I'll just
[00:10:41 - 00:10:48] load my file. So if I see true it means
[00:10:44 - 00:10:52] my file is loaded. So now I can do from
[00:10:48 - 00:10:56] open AI import open AI
[00:10:52 - 00:10:59] and do open AI client
[00:10:56 - 00:11:01] open AI.
[00:10:59 - 00:11:03] So this thing works. It means I
[00:11:01 - 00:11:07] successfully configured OpenAI. So my
[00:11:03 - 00:11:10] key works. It's loaded and I should be
[00:11:07 - 00:11:11] able to send requests. And this is what
[00:11:10 - 00:11:14] I usually use in my courses and
[00:11:11 - 00:11:17] workshops. But today I want to use a
[00:11:14 - 00:11:20] different client. So instead of using
[00:11:17 - 00:11:25] simple openAI client, I want to use a
[00:11:20 - 00:11:27] sync OpenAI client. A sync OpenAI. Yeah.
[00:11:25 - 00:11:31] And the reason we want to use a sync is
[00:11:27 - 00:11:33] later we want to send uh we want to have
[00:11:31 - 00:11:35] established communication a
[00:11:33 - 00:11:37] communication channel between front end
[00:11:35 - 00:11:40] and the back end. And when we are
[00:11:37 - 00:11:43] streaming responses from um from the
[00:11:40 - 00:11:45] OpenAI client, we want to stream these
[00:11:43 - 00:11:46] responses not to the terminal, not to
[00:11:45 - 00:11:48] Jupyter notebook. We want to stream
[00:11:46 - 00:11:51] these responses to front end, right? And
[00:11:48 - 00:11:55] for that we actually will need to have
[00:11:51 - 00:11:55] an async uh client.
[00:11:56 - 00:12:03] Okay, so uh that's one thing. So now I
[00:12:00 - 00:12:05] will need to open this Jupyter notebook.
[00:12:03 - 00:12:08] So there's a bit of boilerplate code
[00:12:05 - 00:12:10] that I prepared. So I think I already
[00:12:08 - 00:12:13] showed you this, right? So now what I
[00:12:10 - 00:12:16] want to do is I want to load this data
[00:12:13 - 00:12:18] from um
[00:12:16 - 00:12:22] yeah from this JSON file. So for that I
[00:12:18 - 00:12:24] will need to have u
[00:12:22 - 00:12:27] requests.
[00:12:24 - 00:12:31] Yeah. And I just do requests get and
[00:12:27 - 00:12:31] this file.
[00:12:31 - 00:12:36] Um, so if you're following along, you
[00:12:33 - 00:12:38] can just um use this code. It also
[00:12:36 - 00:12:40] works.
[00:12:38 - 00:12:44] So, but I don't want to load all the
[00:12:40 - 00:12:49] data. I think I'll just uh use
[00:12:44 - 00:12:52] um response spots
[00:12:49 - 00:12:52] JSON.
[00:12:52 - 00:12:56] Let's just sp
[00:12:57 - 00:13:03] Yeah. So, um this is the data we have
[00:12:59 - 00:13:06] here, right? So um I just thought okay
[00:13:03 - 00:13:08] we can just use this data engineering
[00:13:06 - 00:13:11] zoom camp u and we don't need anything
[00:13:08 - 00:13:11] else.
[00:13:15 - 00:13:22] Uh I think you already did the port
[00:13:18 - 00:13:26] binding before the class. Uh so for the
[00:13:22 - 00:13:29] port binding um I use a special tool
[00:13:26 - 00:13:34] um that I wrote. I mean cloud call help
[00:13:29 - 00:13:39] me of course but this tool is called um
[00:13:34 - 00:13:39] uh SSH auto forward.
[00:13:40 - 00:13:44] So what it's doing it's automatically
[00:13:41 - 00:13:47] detecting if any port is running uh on
[00:13:44 - 00:13:49] my machine and it forwards on the remote
[00:13:47 - 00:13:51] machine and it forwards them to my
[00:13:49 - 00:13:53] machine. So it's like we have port
[00:13:51 - 00:13:55] forwarding in Visual Studio Code but
[00:13:53 - 00:13:58] it's outside of Visual Studio Code. So
[00:13:55 - 00:14:00] it works for everything. So you don't
[00:13:58 - 00:14:04] have to actually run Visual Studio Code.
[00:14:00 - 00:14:08] I think um I wrote about this on my
[00:14:04 - 00:14:11] substack. I think here somewhere we have
[00:14:08 - 00:14:11] archive.
[00:14:11 - 00:14:17] Yeah, if you're interested five useful
[00:14:14 - 00:14:22] useful utilities I wrote. I'll just add
[00:14:17 - 00:14:24] the link. So one of them is u this SSH
[00:14:22 - 00:14:27] autoforward. So I find it pretty
[00:14:24 - 00:14:30] convenient uh that um yeah it just
[00:14:27 - 00:14:32] detects if anything is running on the
[00:14:30 - 00:14:33] remote machine and it automatically
[00:14:32 - 00:14:35] forwards it to my host machine. So I
[00:14:33 - 00:14:38] don't need to worry about uh forwarding
[00:14:35 - 00:14:40] these ports.
[00:14:38 - 00:14:43] Okay. So this is the data we are going
[00:14:40 - 00:14:45] to have. Maybe I'll call it uh data
[00:14:43 - 00:14:48] engineering
[00:14:45 - 00:14:51] uh data.
[00:14:48 - 00:14:53] Yeah, data engineering data.
[00:14:51 - 00:14:58] uh and now what I actually do with this
[00:14:53 - 00:15:01] with this data is I index this data
[00:14:58 - 00:15:05] right so I use min search mean search is
[00:15:01 - 00:15:09] a library uh for doing search so I do uv
[00:15:05 - 00:15:12] at min search so this is a very simple
[00:15:09 - 00:15:14] search engine it doesn't need to have
[00:15:12 - 00:15:16] any so it runs inside python so it
[00:15:14 - 00:15:19] doesn't have to it doesn't need to have
[00:15:16 - 00:15:21] any back end and stuff so if you took uh
[00:15:19 - 00:15:24] any of my courses you probably have
[00:15:21 - 00:15:24] seen.
[00:15:24 - 00:15:32] Okay. So now um I think maybe I'll call
[00:15:28 - 00:15:32] this thing before documents.

## Window 003: 00:15:01 - 00:23:01

[00:15:05 - 00:15:12] at min search so this is a very simple
[00:15:09 - 00:15:14] search engine it doesn't need to have
[00:15:12 - 00:15:16] any so it runs inside python so it
[00:15:14 - 00:15:19] doesn't have to it doesn't need to have
[00:15:16 - 00:15:21] any back end and stuff so if you took uh
[00:15:19 - 00:15:24] any of my courses you probably have
[00:15:21 - 00:15:24] seen.
[00:15:24 - 00:15:32] Okay. So now um I think maybe I'll call
[00:15:28 - 00:15:32] this thing before documents.
[00:15:34 - 00:15:40] So yeah.
[00:15:38 - 00:15:44] So now it should have indexed that. And
[00:15:40 - 00:15:46] now when I do search I can do um can I
[00:15:44 - 00:15:50] join
[00:15:46 - 00:15:50] the course? No.
[00:15:50 - 00:15:53] Oops. Search. Can I join the course now?
[00:15:52 - 00:15:56] And then it returns the results. All
[00:15:53 - 00:15:59] right, we have now we have search. Um,
[00:15:56 - 00:16:02] so um this is going to be one of the the
[00:15:59 - 00:16:04] only tool actually we will have for our
[00:16:02 - 00:16:07] agent. So now I'll just create it as a
[00:16:04 - 00:16:09] tool. So it's going to be this search
[00:16:07 - 00:16:11] tool,
[00:16:09 - 00:16:14] right? So this search tool, this search
[00:16:11 - 00:16:17] function will just use index with some
[00:16:14 - 00:16:20] extra things like
[00:16:17 - 00:16:23] making sure that we are quering only uh
[00:16:20 - 00:16:25] data engineer zoom cam. In my case, I
[00:16:23 - 00:16:27] didn't get any other data. So it's only
[00:16:25 - 00:16:29] data engineer zoom cam. Then it applies
[00:16:27 - 00:16:31] some boosting. It doesn't really matter
[00:16:29 - 00:16:35] here. And then it's limit like five
[00:16:31 - 00:16:38] right now. So we only return five
[00:16:35 - 00:16:43] uh five results.
[00:16:38 - 00:16:43] How do I join the course now?
[00:16:43 - 00:16:50] So yeah, so this is going to be our tool
[00:16:46 - 00:16:53] that we are going to use for our agent,
[00:16:50 - 00:16:55] right? So I by the way I don't plan to
[00:16:53 - 00:16:59] use any specific library. So I just want
[00:16:55 - 00:17:02] to use plain open AI or communicating uh
[00:16:59 - 00:17:07] with um like the open AI SDK for
[00:17:02 - 00:17:08] communicating with uh open AI.
[00:17:07 - 00:17:12] In practice you want to use something
[00:17:08 - 00:17:14] like pedantic AI or open AI agents SDK
[00:17:12 - 00:17:16] or I don't know like chain whatever. So
[00:17:14 - 00:17:18] for now I want to keep things simple. Um
[00:17:16 - 00:17:21] there will be some code because of that
[00:17:18 - 00:17:24] more code but will also give us more
[00:17:21 - 00:17:26] flexibility.
[00:17:24 - 00:17:27] Um I see a question will I get the
[00:17:26 - 00:17:31] recording of this session? Um so yes I
[00:17:27 - 00:17:34] will share the recording on Slack. Uh
[00:17:31 - 00:17:37] yes uh so here I assume that you are a
[00:17:34 - 00:17:39] bit familiar with um agents. Uh if
[00:17:37 - 00:17:42] you're not familiar some of this
[00:17:39 - 00:17:45] information might think uh uh might
[00:17:42 - 00:17:47] might seem a bit um difficult to grasp
[00:17:45 - 00:17:49] from the very beginning. So of course uh
[00:17:47 - 00:17:53] in this case I would recommend to to I
[00:17:49 - 00:17:55] would recommend checking uh this AI
[00:17:53 - 00:17:59] shipping labs. Um so first of all of
[00:17:55 - 00:18:01] course if you're taking um our if you're
[00:17:59 - 00:18:03] taking my Maven course then you will
[00:18:01 - 00:18:06] learn this. If you're not taking my
[00:18:03 - 00:18:09] Maven course, what you can do is we have
[00:18:06 - 00:18:14] this course.
[00:18:09 - 00:18:18] Okay, this one AI hero course where you
[00:18:14 - 00:18:21] can get an introduction to um
[00:18:18 - 00:18:23] Q agents. I see a question from SR. Are
[00:18:21 - 00:18:26] you using any vector database? Right now
[00:18:23 - 00:18:31] not, but at the end we will. Um so right
[00:18:26 - 00:18:31] now we just use a text search.
[00:18:31 - 00:18:38] Okay, where did I stop? Um,
[00:18:35 - 00:18:40] yeah, this part. So, I think I already
[00:18:38 - 00:18:42] did these imports. Let me just repeat
[00:18:40 - 00:18:45] them one more time
[00:18:42 - 00:18:48] because we will have this uh OpenAI
[00:18:45 - 00:18:50] client and also I already selected. So I
[00:18:48 - 00:18:53] actually want to use um I noticed that
[00:18:50 - 00:18:57] this GPT4 mini model like it wasn't
[00:18:53 - 00:19:00] always it was never very intelligent but
[00:18:57 - 00:19:04] recently it became very like even more
[00:19:00 - 00:19:06] stupid than before. So I think they are
[00:19:04 - 00:19:09] making it more stupid on purpose. So
[00:19:06 - 00:19:12] people are upgrading to uh newer models.
[00:19:09 - 00:19:15] I don't know but I'm going to use DPD
[00:19:12 - 00:19:18] 5.4 mini. Um yeah. So I don't know
[00:19:15 - 00:19:20] what's the why they are making it more
[00:19:18 - 00:19:23] stupid or maybe it's just my impression.
[00:19:20 - 00:19:27] I don't know but sometimes like um it
[00:19:23 - 00:19:30] doesn't really work properly.
[00:19:27 - 00:19:33] Okay. So I'll stick to a newer model. So
[00:19:30 - 00:19:35] I think it was released just a week ago
[00:19:33 - 00:19:38] maybe two weeks ago. I don't remember.
[00:19:35 - 00:19:42] And then since we want to use our um
[00:19:38 - 00:19:44] search function as a tool, we need to
[00:19:42 - 00:19:48] define uh this description. Right? So
[00:19:44 - 00:19:51] again, if this is new for you, um this
[00:19:48 - 00:19:53] AI hero course can help. And probably
[00:19:51 - 00:19:55] maybe if you're taking my Maven course
[00:19:53 - 00:19:58] right now, um I'm also explaining these
[00:19:55 - 00:19:58] things there.
[00:20:02 - 00:20:07] Okay.
[00:20:04 - 00:20:11] Yeah. a common to make people pay valid.
[00:20:07 - 00:20:14] Yeah, maybe because GPD for O mini is a
[00:20:11 - 00:20:16] pretty cheap model. Yeah. And this one
[00:20:14 - 00:20:21] is a bit more expensive.
[00:20:16 - 00:20:23] Anyways, um so now what we what else do
[00:20:21 - 00:20:26] we need for the agent? So we have the
[00:20:23 - 00:20:28] tool. This is our tool. We also need um
[00:20:26 - 00:20:30] to this our LM provider. We also need
[00:20:28 - 00:20:34] instructions for the agent. Right. So
[00:20:30 - 00:20:35] our instructions are
[00:20:34 - 00:20:38] you are a teaching assistant for data
[00:20:35 - 00:20:40] talks club zoom camp answer with the
[00:20:38 - 00:20:44] user question but this is standard stuff
[00:20:40 - 00:20:46] right and also at the end we ask to give
[00:20:44 - 00:20:48] citations.
[00:20:46 - 00:20:49] Yeah. So these are simple instructions.
[00:20:48 - 00:20:51] I didn't think much about this. I think
[00:20:49 - 00:20:53] I just copied from some other workshop
[00:20:51 - 00:20:57] and that was it.
[00:20:53 - 00:20:59] And now um
[00:20:57 - 00:21:02] we start our conversation with the
[00:20:59 - 00:21:04] agent. So the question I want to ask uh
[00:21:02 - 00:21:08] the agent is I just discovered the
[00:21:04 - 00:21:12] course can I still join? So what
[00:21:08 - 00:21:15] uh we know will happen is that um the LM
[00:21:12 - 00:21:17] provider will see okay now we have this
[00:21:15 - 00:21:19] tool we have the search tool we need to
[00:21:17 - 00:21:21] invoke it so we will need to write this
[00:21:19 - 00:21:25] agentic to call loop. So I'll do this
[00:21:21 - 00:21:26] quickly right now. So, um I don't want
[00:21:25 - 00:21:28] to spend a lot of time on that, but
[00:21:26 - 00:21:32] still if you have any questions along
[00:21:28 - 00:21:34] the way, um
[00:21:32 - 00:21:35] yeah, feel free to ask. And I see a
[00:21:34 - 00:21:39] question from Marcelo. What do you think
[00:21:35 - 00:21:42] of the free models? Uh free models are
[00:21:39 - 00:21:45] good, but uh the problem with three this
[00:21:42 - 00:21:48] with these free models is you still need
[00:21:45 - 00:21:52] to somehow uh host them somewhere,
[00:21:48 - 00:21:54] right? So one thing is um
[00:21:52 - 00:21:57] using grock.
[00:21:54 - 00:22:01] Grock is good and you can actually use
[00:21:57 - 00:22:03] some of the models for free but uh too
[00:22:01 - 00:22:06] many people used grog for free. So now
[00:22:03 - 00:22:08] they are actually making it more and
[00:22:06 - 00:22:11] more difficult to use it for free. So
[00:22:08 - 00:22:13] like I think the the free lunch is over
[00:22:11 - 00:22:16] when it comes to gro. So you actually
[00:22:13 - 00:22:20] have to pay to use it. Um so unless you
[00:22:16 - 00:22:23] have a good GPU and then you still need
[00:22:20 - 00:22:26] to be able to use an LM right and then
[00:22:23 - 00:22:29] uh for that the easiest way is to use an
[00:22:26 - 00:22:31] LM provider. It could be Grock which
[00:22:29 - 00:22:34] hosts open source models. It could be
[00:22:31 - 00:22:38] some other provider which hosts cost
[00:22:34 - 00:22:42] models like up to you. But um I actually
[00:22:38 - 00:22:47] I really like this ZAI thing.
[00:22:42 - 00:22:52] So uh ZAI uh they are known uh for the
[00:22:47 - 00:22:54] JLM 5.1. So this is an open model um and
[00:22:52 - 00:22:59] they are the company behind this open
[00:22:54 - 00:23:01] model JM 5.1 and uh what they have is
[00:22:59 - 00:23:04] they u make this model available through
[00:23:01 - 00:23:07] API but if you have a powerful machine

## Window 004: 00:22:31 - 00:30:31

[00:22:34 - 00:22:42] models like up to you. But um I actually
[00:22:38 - 00:22:47] I really like this ZAI thing.
[00:22:42 - 00:22:52] So uh ZAI uh they are known uh for the
[00:22:47 - 00:22:54] JLM 5.1. So this is an open model um and
[00:22:52 - 00:22:59] they are the company behind this open
[00:22:54 - 00:23:01] model JM 5.1 and uh what they have is
[00:22:59 - 00:23:04] they u make this model available through
[00:23:01 - 00:23:07] API but if you have a powerful machine
[00:23:04 - 00:23:10] you can host this model. So I use them
[00:23:07 - 00:23:12] quite often.
[00:23:10 - 00:23:15] So because I don't have the resources to
[00:23:12 - 00:23:18] host the models uh these models, but I
[00:23:15 - 00:23:22] can use them to be able to actually use
[00:23:18 - 00:23:24] them. Okay. Um so this is how we um I
[00:23:22 - 00:23:26] think it's very similar to what we do it
[00:23:24 - 00:23:28] with a usual client when we want to
[00:23:26 - 00:23:30] stream the responses with not in a sync
[00:23:28 - 00:23:34] client.
[00:23:30 - 00:23:36] Um but yeah here um this is how we get
[00:23:34 - 00:23:39] the response
[00:23:36 - 00:23:42] and output now will contain this uh
[00:23:39 - 00:23:45] function to call. There's a slight
[00:23:42 - 00:23:48] difference between this one uh and
[00:23:45 - 00:23:50] standard classic one so not a sync one
[00:23:48 - 00:23:53] is that it has this new thing called
[00:23:50 - 00:23:54] parse arguments. I don't know why they
[00:23:53 - 00:23:56] are different here but this is a
[00:23:54 - 00:23:59] distinction that is actually important
[00:23:56 - 00:24:01] for us because um later we will see that
[00:23:59 - 00:24:03] um
[00:24:01 - 00:24:07] yeah we will need to to handle this case
[00:24:03 - 00:24:10] but otherwise like it's um
[00:24:07 - 00:24:14] now we have this uh call
[00:24:10 - 00:24:16] right and this call contains arguments
[00:24:14 - 00:24:20] JSON
[00:24:16 - 00:24:22] uh call arguments that we parse right so
[00:24:20 - 00:24:24] this is our arguments
[00:24:22 - 00:24:26] And then we use this to invoke our
[00:24:24 - 00:24:29] search function,
[00:24:26 - 00:24:32] right? And this is the these are the
[00:24:29 - 00:24:35] results we get
[00:24:32 - 00:24:36] results
[00:24:35 - 00:24:41] and this is what we need to send back to
[00:24:36 - 00:24:45] the LLM, right? Um so I have a snippet
[00:24:41 - 00:24:49] for that. So we iterate over all the um
[00:24:45 - 00:24:51] over all the responses or all the output
[00:24:49 - 00:24:54] items in the response.
[00:24:51 - 00:24:56] And if this is uh not a function call,
[00:24:54 - 00:24:58] we don't do anything. So, but if it's a
[00:24:56 - 00:25:00] function call, we invoke it. Now, we
[00:24:58 - 00:25:03] assume that this is search because we
[00:25:00 - 00:25:05] don't have any other functions, right?
[00:25:03 - 00:25:06] And then we append these things to
[00:25:05 - 00:25:08] history. So, remember I was talking
[00:25:06 - 00:25:11] about this parse arguments. So, if I
[00:25:08 - 00:25:14] don't do it this way and I just append
[00:25:11 - 00:25:16] the item without doing anything, then
[00:25:14 - 00:25:19] open AI will complain that um hey,
[00:25:16 - 00:25:21] you're doing something wrong.
[00:25:19 - 00:25:22] So right now our message history looks
[00:25:21 - 00:25:27] like that.
[00:25:22 - 00:25:31] So we have um
[00:25:27 - 00:25:34] the um the system prompt my prompt
[00:25:31 - 00:25:39] function call and function call output.
[00:25:34 - 00:25:39] And so now we make another call
[00:25:40 - 00:25:46] and then we should see ideally we should
[00:25:43 - 00:25:48] see that it streams the response, right?
[00:25:46 - 00:25:49] Yes, you can still join even if you just
[00:25:48 - 00:25:52] discover the course because it already
[00:25:49 - 00:25:55] has all the content the context it needs
[00:25:52 - 00:26:00] in order to answer questions.
[00:25:55 - 00:26:03] Um so now I want to do a bit of um
[00:26:00 - 00:26:05] how to say um so I want to organize this
[00:26:03 - 00:26:08] code into something that we can later
[00:26:05 - 00:26:11] use um because the goal for us is to
[00:26:08 - 00:26:14] build back end right um so in order to
[00:26:11 - 00:26:16] build back end we need to uh turn this
[00:26:14 - 00:26:19] into something manageable right so for
[00:26:16 - 00:26:22] that um I have this abstraction called
[00:26:19 - 00:26:22] notebook renderer
[00:26:25 - 00:26:32] So this is um
[00:26:28 - 00:26:33] this abstraction allows. So it just says
[00:26:32 - 00:26:35] when we have a two call we need to
[00:26:33 - 00:26:37] invoke this function when we have a two
[00:26:35 - 00:26:40] call result we invoke this function when
[00:26:37 - 00:26:44] we get a new token uh when we stream we
[00:26:40 - 00:26:46] invoke this function and so on right um
[00:26:44 - 00:26:48] so the reason for that is right now we
[00:26:46 - 00:26:50] use Jupyter notebook so then this is
[00:26:48 - 00:26:54] Jupyter notebook friendly this is also
[00:26:50 - 00:26:56] terminal friendly but once we go to um
[00:26:54 - 00:26:58] front end back end interaction we'll
[00:26:56 - 00:27:04] need to replace it with something else
[00:26:58 - 00:27:06] right so we have this sender and um
[00:27:04 - 00:27:08] so there are a few helper functions that
[00:27:06 - 00:27:12] I want to use along the way. So first of
[00:27:08 - 00:27:14] all this uh request response function.
[00:27:12 - 00:27:17] So I am sending a request like I did
[00:27:14 - 00:27:20] here right. So then I am iterating over
[00:27:17 - 00:27:22] the events in the stream and if the type
[00:27:20 - 00:27:24] is this delta I print it. So this is
[00:27:22 - 00:27:27] what we just did right now. Right? So
[00:27:24 - 00:27:29] this allows us to actually steam data as
[00:27:27 - 00:27:32] we receive it.
[00:27:29 - 00:27:36] Right? But instead of uh just doing this
[00:27:32 - 00:27:40] print, what I do right now is I use this
[00:27:36 - 00:27:43] renderer. Right? So I just do um handle
[00:27:40 - 00:27:47] events. This is and I pass the
[00:27:43 - 00:27:49] information about that. Right? Okay. So
[00:27:47 - 00:27:51] this is one function.
[00:27:49 - 00:27:55] Then another function is just a
[00:27:51 - 00:27:57] simplification of uh this. So I don't
[00:27:55 - 00:28:01] need to do this. I can just invoke this
[00:27:57 - 00:28:06] function once. Yeah, I don't like this
[00:28:01 - 00:28:06] formatting. So, quickly edit this.
[00:28:07 - 00:28:14] Okay.
[00:28:08 - 00:28:14] And then finally, uh handle tool calls
[00:28:14 - 00:28:19] and collect answers. So, handle tool
[00:28:15 - 00:28:21] calls. This is our I don't know why we
[00:28:19 - 00:28:24] need it this way. Sorry.
[00:28:21 - 00:28:28] So some of this code is AI generated and
[00:28:24 - 00:28:31] actually uh AI likes to be verbose right
[00:28:28 - 00:28:33] but uh we invoke our search function. So
[00:28:31 - 00:28:35] this is very similar to what I was doing
[00:28:33 - 00:28:40] here. So we iterate over all the output
[00:28:35 - 00:28:43] items here. Then uh we invoke the search
[00:28:40 - 00:28:48] function except that I add add a few
[00:28:43 - 00:28:51] handlers along the way. Right? So um
[00:28:48 - 00:28:55] here handle event. So there's an event
[00:28:51 - 00:28:57] two call. So I want to um trigger sort
[00:28:55 - 00:29:00] of a call back saying hey like we just
[00:28:57 - 00:29:04] had a two call event let's display it.
[00:29:00 - 00:29:08] Um oh this is the result right to result
[00:29:04 - 00:29:08] that's another thing. Um
[00:29:08 - 00:29:14] and then append two messages is this
[00:29:11 - 00:29:16] function right. Um and then what it
[00:29:14 - 00:29:19] returns at the end whether it had two
[00:29:16 - 00:29:23] calls or not. So we can use this to stop
[00:29:19 - 00:29:25] our um aentic loop.
[00:29:23 - 00:29:28] Okay. And at the end we have our aentic
[00:29:25 - 00:29:28] loop.
[00:29:32 - 00:29:38] So we iterate we do. So here we only do
[00:29:36 - 00:29:40] five iterations.
[00:29:38 - 00:29:42] Um so we restrict our agent. We don't
[00:29:40 - 00:29:46] want the agent to go crazy. We only
[00:29:42 - 00:29:50] restrict it to five iterations. Um so we
[00:29:46 - 00:29:52] uh so so this is um so we start with our
[00:29:50 - 00:29:55] instructions and the question from the
[00:29:52 - 00:29:58] user then we iterate uh then we send the
[00:29:55 - 00:30:00] request then we handle two calls and if
[00:29:58 - 00:30:03] there are not cool two calls we get the
[00:30:00 - 00:30:07] final answer and we return otherwise uh
[00:30:03 - 00:30:10] we iterate but then at the end if um we
[00:30:07 - 00:30:12] don't have a response we um say okay
[00:30:10 - 00:30:14] sorry we couldn't find the response to
[00:30:12 - 00:30:17] this question the the the we couldn't
[00:30:14 - 00:30:20] answer this question.
[00:30:17 - 00:30:24] So let me quickly test it and this is
[00:30:20 - 00:30:27] actually all I prepared for um for this.
[00:30:24 - 00:30:30] So the rest we are going to improvise
[00:30:27 - 00:30:32] right. So okay don't think maybe I
[00:30:30 - 00:30:35] didn't

## Window 005: 00:30:01 - 00:38:01

[00:30:03 - 00:30:10] we iterate but then at the end if um we
[00:30:07 - 00:30:12] don't have a response we um say okay
[00:30:10 - 00:30:14] sorry we couldn't find the response to
[00:30:12 - 00:30:17] this question the the the we couldn't
[00:30:14 - 00:30:20] answer this question.
[00:30:17 - 00:30:24] So let me quickly test it and this is
[00:30:20 - 00:30:27] actually all I prepared for um for this.
[00:30:24 - 00:30:30] So the rest we are going to improvise
[00:30:27 - 00:30:32] right. So okay don't think maybe I
[00:30:30 - 00:30:35] didn't
[00:30:32 - 00:30:39] work some of the things and so right now
[00:30:35 - 00:30:42] you can see that uh it is u
[00:30:39 - 00:30:45] this part I think wasn't necessary
[00:30:42 - 00:30:48] with collect answer so let me try one
[00:30:45 - 00:30:48] more time
[00:30:49 - 00:30:53] yeah answers defined
[00:30:56 - 00:31:02] Okay. Um, so
[00:30:59 - 00:31:04] this is what I prepared. So right now,
[00:31:02 - 00:31:06] uh, what I want to do together with you
[00:31:04 - 00:31:09] is I want to figure out how to deploy
[00:31:06 - 00:31:11] it, right? So this is this was, uh, I
[00:31:09 - 00:31:14] mean it's not something I typically
[00:31:11 - 00:31:16] show. So this for some of you this can
[00:31:14 - 00:31:18] be actually new information cuz what we
[00:31:16 - 00:31:21] do here is we use this as sync client,
[00:31:18 - 00:31:23] not the usual client. But otherwise, if
[00:31:21 - 00:31:25] you took like this AI shipping labs
[00:31:23 - 00:31:28] course or maybe you took the Maven
[00:31:25 - 00:31:30] course, like this should sound familiar.
[00:31:28 - 00:31:34] And if it's not familiar for you, like
[00:31:30 - 00:31:38] this AI hero course will help.
[00:31:34 - 00:31:40] Um, and of course like if you feel a bit
[00:31:38 - 00:31:42] lost, we can talk in Slack and then I
[00:31:40 - 00:31:45] can also help you find information like
[00:31:42 - 00:31:49] so next time, uh, you can understand
[00:31:45 - 00:31:52] like these things. uh but what we
[00:31:49 - 00:31:54] haven't done in any of the courses is um
[00:31:52 - 00:31:56] actually deploying this and this is what
[00:31:54 - 00:31:59] I want to focus on but before we can
[00:31:56 - 00:32:04] deploy this we actually need to turn
[00:31:59 - 00:32:07] this into a proper Python project right
[00:32:04 - 00:32:11] so let me quickly check questions
[00:32:07 - 00:32:13] are you using API responses uh open AI
[00:32:11 - 00:32:18] responses API yes so this is responses
[00:32:13 - 00:32:18] API or
[00:32:20 - 00:32:27] Where do I see it? Yeah, you see it's
[00:32:23 - 00:32:29] only clientres responses.
[00:32:27 - 00:32:32] Yeah, with chat completions I think it's
[00:32:29 - 00:32:32] similar.
[00:32:33 - 00:32:39] So what I want to do now is I want to
[00:32:36 - 00:32:42] turn this into a proper uh Python
[00:32:39 - 00:32:46] project and then I want to turn this
[00:32:42 - 00:32:48] Python project into a fast API back end.
[00:32:46 - 00:32:51] Right? So for that I'm going to use a
[00:32:48 - 00:32:54] coding assistant
[00:32:51 - 00:32:58] here. Um I also want to like since I use
[00:32:54 - 00:33:01] SSH what I also want to do is I want to
[00:32:58 - 00:33:05] use a tuk or t-muk I don't know how I
[00:33:01 - 00:33:07] pronounce it. um in order to create a
[00:33:05 - 00:33:12] session. So if for for some reasons my
[00:33:07 - 00:33:14] SSH SSH session gets uh interrupted then
[00:33:12 - 00:33:17] like the process actually keeps running.
[00:33:14 - 00:33:21] Uh so for this thing I have an utility
[00:33:17 - 00:33:23] called TMUX CL. Um so this is uh
[00:33:21 - 00:33:26] something I also created. I don't think
[00:33:23 - 00:33:32] I wrote any article about this but this
[00:33:26 - 00:33:34] just makes it easier for me to use um
[00:33:32 - 00:33:36] timuk. So typically I would need to
[00:33:34 - 00:33:40] write something like this. Timuk's new
[00:33:36 - 00:33:45] session minus s uh and then the name of
[00:33:40 - 00:33:49] the session could be um
[00:33:45 - 00:33:51] I don't know uh end to end workshop I'll
[00:33:49 - 00:33:54] just call 10 to end right uh but when I
[00:33:51 - 00:33:59] want to join an existing attach existing
[00:33:54 - 00:34:01] session I would need to write attach
[00:33:59 - 00:34:03] and then minus t and then um the name of
[00:34:01 - 00:34:07] the session. So these are very
[00:34:03 - 00:34:09] different. These are very long and um
[00:34:07 - 00:34:11] yeah I find it a bit inconvenient. So
[00:34:09 - 00:34:16] instead I created a tool that I called
[00:34:11 - 00:34:18] t-muk ctl or um there is also another t
[00:34:16 - 00:34:22] and then what I can do is I have I can
[00:34:18 - 00:34:24] have this syntax for create or attach.
[00:34:22 - 00:34:27] So what I can do is like if the session
[00:34:24 - 00:34:29] does not exist it will create the
[00:34:27 - 00:34:32] session. Now I press Ctrl +BD to
[00:34:29 - 00:34:36] disconnect and now I can connect to the
[00:34:32 - 00:34:36] session that is already exist
[00:34:36 - 00:34:40] then I connect to the existing session.
[00:34:38 - 00:34:43] I find it quite convenient because like
[00:34:40 - 00:34:46] I don't really like the this common line
[00:34:43 - 00:34:48] interface for T-M
[00:34:46 - 00:34:50] uh but yeah
[00:34:48 - 00:34:53] um so I see that there are some
[00:34:50 - 00:34:56] questions so let me quickly check them.
[00:34:53 - 00:35:00] How is uh rack getting used in this? So
[00:34:56 - 00:35:03] when it comes to rack, so this part is
[00:35:00 - 00:35:05] rack or whatever. So it's not simple
[00:35:03 - 00:35:08] rack, it's a gentic rack because we have
[00:35:05 - 00:35:10] a s function called search and then our
[00:35:08 - 00:35:13] agent can decide to invoke this function
[00:35:10 - 00:35:16] or not invoke
[00:35:13 - 00:35:18] um minarch. Ah yeah that was the
[00:35:16 - 00:35:24] question I guess minarch looks in the
[00:35:18 - 00:35:27] text questions. Yeah exactly. Thank you.
[00:35:24 - 00:35:30] Um okay so I was talking about this
[00:35:27 - 00:35:32] Timmuk CLI. So now when I disconnect and
[00:35:30 - 00:35:33] then I do this again I attach to the
[00:35:32 - 00:35:36] same session. So I find it convenient.
[00:35:33 - 00:35:39] So maybe if you also
[00:35:36 - 00:35:41] need to use these things often this
[00:35:39 - 00:35:45] timct
[00:35:41 - 00:35:47] you can check it out.
[00:35:45 - 00:35:48] Okay. Um
[00:35:47 - 00:35:51] and there are a few other things uh that
[00:35:48 - 00:35:53] I find quite convenient. So I can
[00:35:51 - 00:35:56] connect to a session by ID. So I can
[00:35:53 - 00:35:58] just write T1 and then connect to the
[00:35:56 - 00:36:01] session. So here what I want to do is I
[00:35:58 - 00:36:03] want to start a CL code session. So for
[00:36:01 - 00:36:06] me I have an alias for doing that. So
[00:36:03 - 00:36:09] typically I would need to write clot
[00:36:06 - 00:36:13] dangerously dangerously
[00:36:09 - 00:36:15] skip permissions because I'm running on
[00:36:13 - 00:36:19] a remote machine. I'm not really afraid
[00:36:15 - 00:36:21] of cloud code nuking my computer because
[00:36:19 - 00:36:23] it's a remote machine. I try not to give
[00:36:21 - 00:36:27] any uh very sensitive data on these
[00:36:23 - 00:36:30] machines. Uh so like for example, I
[00:36:27 - 00:36:33] don't have my AWS credentials here. So
[00:36:30 - 00:36:35] that's why um I usually use uh this
[00:36:33 - 00:36:37] dangerous list keep permissions because
[00:36:35 - 00:36:40] it's faster. I don't need to babysit and
[00:36:37 - 00:36:44] approve every every change wants to
[00:36:40 - 00:36:46] make. And for me like this um instead of
[00:36:44 - 00:36:50] typing load dangerous list keep
[00:36:46 - 00:36:52] permissions I have an alias which is clo
[00:36:50 - 00:36:56] keep permissions right can trust this
[00:36:52 - 00:36:58] folder so this is just easier for me to
[00:36:56 - 00:37:01] do this and um maybe if you're
[00:36:58 - 00:37:03] interested I have this
[00:37:01 - 00:37:06] clot repository
[00:37:03 - 00:37:09] where I have all these uh things set up
[00:37:06 - 00:37:11] right so if you want to have um some
[00:37:09 - 00:37:13] aliases
[00:37:11 - 00:37:17] Where are they? Yeah. So, here I have
[00:37:13 - 00:37:21] this addresses. C for cl CC for cl
[00:37:17 - 00:37:24] continue. Uh this uh CSP skip
[00:37:21 - 00:37:27] permissions and this one continue and
[00:37:24 - 00:37:30] skip permissions.
[00:37:27 - 00:37:34] Um okay. So what I want to do here uh I
[00:37:30 - 00:37:37] want to ask it um so I also like using
[00:37:34 - 00:37:39] uh voice voice call voice typing voice
[00:37:37 - 00:37:43] dictation.
[00:37:39 - 00:37:46] Uh so I have a bug I have to turn on and
[00:37:43 - 00:37:49] off this fluid dictation. So what I
[00:37:46 - 00:37:51] wanted to do is I want now to uh like if
[00:37:49 - 00:37:54] you're on Windows you can get this thing
[00:37:51 - 00:37:56] by pressing window key.h on Mac mark. I
[00:37:54 - 00:37:58] think there is also a built-in dictation
[00:37:56 - 00:38:02] mechanism.
[00:37:58 - 00:38:04] So um uh what I want you to do is I want

## Window 006: 00:37:31 - 00:45:31

[00:37:34 - 00:37:39] uh voice voice call voice typing voice
[00:37:37 - 00:37:43] dictation.
[00:37:39 - 00:37:46] Uh so I have a bug I have to turn on and
[00:37:43 - 00:37:49] off this fluid dictation. So what I
[00:37:46 - 00:37:51] wanted to do is I want now to uh like if
[00:37:49 - 00:37:54] you're on Windows you can get this thing
[00:37:51 - 00:37:56] by pressing window key.h on Mac mark. I
[00:37:54 - 00:37:58] think there is also a built-in dictation
[00:37:56 - 00:38:02] mechanism.
[00:37:58 - 00:38:04] So um uh what I want you to do is I want
[00:38:02 - 00:38:06] you to take a look at what we have in
[00:38:04 - 00:38:08] this repository. There is a notebook. I
[00:38:06 - 00:38:10] want to turn this notebook into a script
[00:38:08 - 00:38:13] and then based on that I want to create
[00:38:10 - 00:38:16] a fast API application. So we use UV
[00:38:13 - 00:38:22] here in this project. So I want you to
[00:38:16 - 00:38:24] add a fast API uh dependency and um
[00:38:22 - 00:38:27] yeah so split it into multiple files.
[00:38:24 - 00:38:30] There should be an app.py file. There
[00:38:27 - 00:38:32] should be um yeah maybe you can suggest
[00:38:30 - 00:38:35] me what kind of structure there could
[00:38:32 - 00:38:37] be.
[00:38:35 - 00:38:40] Okay. Okay, so this is my prompt. Emman,
[00:38:37 - 00:38:43] do you have a question?
[00:38:40 - 00:38:44] Cuz you're unmuted. And if you have a
[00:38:43 - 00:38:46] question, feel free to ask. But if you
[00:38:44 - 00:38:51] don't, it would be nice if you mute mute
[00:38:46 - 00:38:51] mute yourself cuz I hear you.
[00:38:52 - 00:38:55] Okay. If you don't mind, I'll just mute
[00:38:54 - 00:38:58] you.
[00:38:55 - 00:39:02] But if you feel like asking question,
[00:38:58 - 00:39:02] please just go ahead and ask.
[00:39:03 - 00:39:07] Okay. So this is my interaction with
[00:39:05 - 00:39:11] cloud code like it doesn't have to like
[00:39:07 - 00:39:14] let's say uh you use charg
[00:39:11 - 00:39:17] but if you use charg and if you are on a
[00:39:14 - 00:39:19] paid plan on plus plan you have codex so
[00:39:17 - 00:39:24] then you can use codex for instead of
[00:39:19 - 00:39:28] that um then um you can use anti-gravity
[00:39:24 - 00:39:31] um also with anti-gravity you can create
[00:39:28 - 00:39:34] these things or I also like github
[00:39:31 - 00:39:37] copilot and in github copilot Do you
[00:39:34 - 00:39:40] also have CLI tool? You also like it's
[00:39:37 - 00:39:42] integrated in Visual Studio Code like I
[00:39:40 - 00:39:45] would if you're not using AI assistance
[00:39:42 - 00:39:47] now for um writing code. I would highly
[00:39:45 - 00:39:49] recommend to do this.
[00:39:47 - 00:39:52] Okay.
[00:39:49 - 00:39:54] So uh it checked the notebook uh it
[00:39:52 - 00:39:58] explained what it's doing. So and it
[00:39:54 - 00:40:02] suggests to have a file app.py for fast
[00:39:58 - 00:40:06] API things agent.py Pi for agent stuff.
[00:40:02 - 00:40:11] Search renderer schemas.
[00:40:06 - 00:40:14] Okay, I'm fine. Let's go.
[00:40:11 - 00:40:16] Um, yeah, sometimes I even don't spend
[00:40:14 - 00:40:18] that much time reading what it's doing.
[00:40:16 - 00:40:22] Like for me it's important that it has a
[00:40:18 - 00:40:23] plan, right? And if it has a plan then
[00:40:22 - 00:40:26] like it's better than, you know, no
[00:40:23 - 00:40:30] plan. But in this particular case, I
[00:40:26 - 00:40:33] also wanted to see what kind of um setup
[00:40:30 - 00:40:33] it will suggest.
[00:40:35 - 00:40:40] Um any specific tool you use for voice
[00:40:38 - 00:40:43] instructions? I think I mentioned I just
[00:40:40 - 00:40:46] use uh built-in Windows voice
[00:40:43 - 00:40:46] recognition.
[00:40:51 - 00:40:58] Um, how would you compare skills versus
[00:40:53 - 00:41:00] agents? For that, I had uh Majeska, I
[00:40:58 - 00:41:02] see that you raised a hand. I'll answer
[00:41:00 - 00:41:05] this question and then feel free to
[00:41:02 - 00:41:08] unmute yourself and ask your question.
[00:41:05 - 00:41:12] So, I want to quickly say about uh
[00:41:08 - 00:41:15] skills and agents. I had a workshop
[00:41:12 - 00:41:18] here, Skills MD from scratch. So, I'll
[00:41:15 - 00:41:21] share the link with you.
[00:41:18 - 00:41:24] So you can check it. Uh we are not going
[00:41:21 - 00:41:25] to cover skills today. So then um yeah I
[00:41:24 - 00:41:28] would recommend just to check this
[00:41:25 - 00:41:29] webinar. Yeah, what's up?
[00:41:28 - 00:41:30] >> Hi. Uh
[00:41:29 - 00:41:32] >> hi.
[00:41:30 - 00:41:33] >> It's nice to see you by the way.
[00:41:32 - 00:41:35] >> Yeah, likewise.
[00:41:33 - 00:41:37] >> Uh I I I'm a little lost because I think
[00:41:35 - 00:41:38] I missed what um
[00:41:37 - 00:41:40] >> Okay. Yeah.
[00:41:38 - 00:41:44] >> TMUXTL.
[00:41:40 - 00:41:48] What is that used for? So tmx is a tool
[00:41:44 - 00:41:50] for uh t- mukes.
[00:41:48 - 00:41:54] So I'm so this what you see right now
[00:41:50 - 00:41:56] this terminal is my it's not my local
[00:41:54 - 00:41:58] machine. So this is my local machine
[00:41:56 - 00:42:01] right. So this is a windows machine. So
[00:41:58 - 00:42:04] what I do is I SSH to a machine that is
[00:42:01 - 00:42:04] running remotely. So I do sshner.
[00:42:04 - 00:42:07] >> Yeah.
[00:42:04 - 00:42:09] >> Yeah. So instead of typing shner I just
[00:42:07 - 00:42:12] type h. These are the same things. I
[00:42:09 - 00:42:14] like shortcuts. Right. And um I'm
[00:42:12 - 00:42:17] running something here. Let's say I go
[00:42:14 - 00:42:19] here to to this TMP uh end to end
[00:42:17 - 00:42:23] session
[00:42:19 - 00:42:25] and to how do you call it? End to end
[00:42:23 - 00:42:28] workshop, right? And then I start a
[00:42:25 - 00:42:31] codex session, right?
[00:42:28 - 00:42:34] So I start a codex session and then my
[00:42:31 - 00:42:36] connection is interrupted.
[00:42:34 - 00:42:38] So in this case what happens is
[00:42:36 - 00:42:41] everything that leaves that is attached
[00:42:38 - 00:42:43] to this uh SSH session dies with the
[00:42:41 - 00:42:46] connection right. So if an agent is
[00:42:43 - 00:42:49] doing something and my Wi-Fi uh
[00:42:46 - 00:42:52] interrupts or I need to uh I don't know
[00:42:49 - 00:42:54] close my laptop laptop and go somewhere
[00:42:52 - 00:42:58] the work will stop
[00:42:54 - 00:43:00] in order to avoid that. Um so I don't
[00:42:58 - 00:43:03] know I will probably not be able to uh
[00:43:00 - 00:43:05] model this right now. uh I don't want to
[00:43:03 - 00:43:07] interrupt my connection. Uh but the
[00:43:05 - 00:43:11] thing is like yeah it will stop working.
[00:43:07 - 00:43:13] So in order to um
[00:43:11 - 00:43:17] deal with this problem you can use
[00:43:13 - 00:43:20] timuku. TMUX is I think it's terminal
[00:43:17 - 00:43:22] multiplexer or something like this. Uh
[00:43:20 - 00:43:25] so it actually allows you to disconnect
[00:43:22 - 00:43:29] to run processes that are not attached
[00:43:25 - 00:43:33] to your SS SSH session. So you do timuk
[00:43:29 - 00:43:37] new session and then uh codex right and
[00:43:33 - 00:43:43] then inside this session you do codex
[00:43:37 - 00:43:45] yellow and then say u tell
[00:43:43 - 00:43:47] me about
[00:43:45 - 00:43:50] about this project and right now what I
[00:43:47 - 00:43:52] can do is I can disconnect from this and
[00:43:50 - 00:43:55] I go I can go I don't know for a walk I
[00:43:52 - 00:43:58] can come back and then I can connect to
[00:43:55 - 00:44:03] my session again and now I need to write
[00:43:58 - 00:44:06] tmuk attach minus t uh codex
[00:44:03 - 00:44:09] right so it's different syntax so it was
[00:44:06 - 00:44:12] first it was new session minus s and now
[00:44:09 - 00:44:14] in order to attach I use this syntax
[00:44:12 - 00:44:16] right so you can see that this is
[00:44:14 - 00:44:18] different so for me it was a bit
[00:44:16 - 00:44:22] annoying and then I also need to type a
[00:44:18 - 00:44:26] lot of things so I built a small wrapper
[00:44:22 - 00:44:29] that lets me just do this codex t codex
[00:44:26 - 00:44:31] >> so If it does not exist, it creates a
[00:44:29 - 00:44:33] new session. If it exists, it attaches
[00:44:31 - 00:44:35] to this session. Right.
[00:44:33 - 00:44:37] >> But realistically, not realistically,
[00:44:35 - 00:44:39] but if we're just testing things on our
[00:44:37 - 00:44:39] local machines,
[00:44:39 - 00:44:41] >> you don't need that.
[00:44:39 - 00:44:43] >> Don't really need to do this.
[00:44:41 - 00:44:46] >> Yes. You don't need to do that. Exactly.
[00:44:43 - 00:44:49] Uh, and then one other thing I like is
[00:44:46 - 00:44:51] because I can attach sessions instead of
[00:44:49 - 00:44:53] writing like big name, long name, I can
[00:44:51 - 00:44:56] just do T1 and then I would attach to
[00:44:53 - 00:44:59] this collection, right? So this is very
[00:44:56 - 00:45:02] convenient if you're running things
[00:44:59 - 00:45:04] remotely, right? So for me um cuz for
[00:45:02 - 00:45:08] example I travel right now I'm in
[00:45:04 - 00:45:12] Amsterdam. Um and then I don't know
[00:45:08 - 00:45:14] before um I fly back to Berlin in my
[00:45:12 - 00:45:16] plane on my plane I can give an
[00:45:14 - 00:45:18] instruction to the agent. I can close my
[00:45:16 - 00:45:22] laptop and this thing will continue
[00:45:18 - 00:45:24] working. It's very
[00:45:22 - 00:45:25] >> Yeah. Um can I ask a quick question?
[00:45:24 - 00:45:28] >> Of course.
[00:45:25 - 00:45:30] So if we're working on our like pet
[00:45:28 - 00:45:33] project or just like a small project
[00:45:30 - 00:45:34] then and we still want to create a front

## Window 007: 00:45:01 - 00:53:01

[00:45:02 - 00:45:08] example I travel right now I'm in
[00:45:04 - 00:45:12] Amsterdam. Um and then I don't know
[00:45:08 - 00:45:14] before um I fly back to Berlin in my
[00:45:12 - 00:45:16] plane on my plane I can give an
[00:45:14 - 00:45:18] instruction to the agent. I can close my
[00:45:16 - 00:45:22] laptop and this thing will continue
[00:45:18 - 00:45:24] working. It's very
[00:45:22 - 00:45:25] >> Yeah. Um can I ask a quick question?
[00:45:24 - 00:45:28] >> Of course.
[00:45:25 - 00:45:30] So if we're working on our like pet
[00:45:28 - 00:45:33] project or just like a small project
[00:45:30 - 00:45:34] then and we still want to create a front
[00:45:33 - 00:45:35] end and a back end.
[00:45:34 - 00:45:38] >> Yeah.
[00:45:35 - 00:45:40] >> Realistically we wouldn't need to access
[00:45:38 - 00:45:41] a remote machine. Yeah.
[00:45:40 - 00:45:44] >> Yeah. It's fine. Like if you just use
[00:45:41 - 00:45:45] your laptop it's fine.
[00:45:44 - 00:45:48] >> Okay.
[00:45:45 - 00:45:50] >> Yeah. Like if you want this thing to
[00:45:48 - 00:45:52] continue run running when you close the
[00:45:50 - 00:45:54] lid of your laptop then you need a
[00:45:52 - 00:45:55] remote machine.
[00:45:54 - 00:45:59] And so for me for example I have like
[00:45:55 - 00:46:00] different uh telegram bots uh that
[00:45:59 - 00:46:02] actually require a machine that is
[00:46:00 - 00:46:06] always up and running. I have long
[00:46:02 - 00:46:08] running codeex and uh code code
[00:46:06 - 00:46:10] sessions. So for me it's just I don't
[00:46:08 - 00:46:11] want to keep my computer on all the
[00:46:10 - 00:46:14] time.
[00:46:11 - 00:46:17] >> Mhm. And also computers um like my old
[00:46:14 - 00:46:18] computer broke um so I also want to have
[00:46:17 - 00:46:21] an environment that is you know
[00:46:18 - 00:46:23] independent from a specific piece of
[00:46:21 - 00:46:25] machines like specific piece of hardware
[00:46:23 - 00:46:26] specific laptop.
[00:46:25 - 00:46:29] >> Mhm.
[00:46:26 - 00:46:31] >> But for you like when you need it I
[00:46:29 - 00:46:34] think you'll understand it before you
[00:46:31 - 00:46:37] feel like okay I need a remote machine
[00:46:34 - 00:46:41] you don't need. And um what I also like
[00:46:37 - 00:46:42] is in GitHub you have code spaces and
[00:46:41 - 00:46:44] this is a very convenient way probably
[00:46:42 - 00:46:47] you use it for a course. I don't know if
[00:46:44 - 00:46:50] you used this for the for the the build
[00:46:47 - 00:46:52] camp for Maven course. Um but uh it's
[00:46:50 - 00:46:54] very convenient because you can just you
[00:46:52 - 00:46:57] know keep all the things there and you
[00:46:54 - 00:46:59] can join you can use these code spaces
[00:46:57 - 00:47:01] from different computers.
[00:46:59 - 00:47:01] >> Yeah.
[00:47:01 - 00:47:03] >> Thanks.
[00:47:01 - 00:47:06] >> Yeah. You're welcome. Any other
[00:47:03 - 00:47:09] questions? I see some things in chat.
[00:47:06 - 00:47:11] Let me check.
[00:47:09 - 00:47:13] It means tuk helps us to create multiple
[00:47:11 - 00:47:16] sessions on one machine without
[00:47:13 - 00:47:17] interrupting the others. Yes.
[00:47:16 - 00:47:19] Uh what would be your minimum
[00:47:17 - 00:47:20] recommended stack for building both
[00:47:19 - 00:47:22] front end and back end for a genic
[00:47:20 - 00:47:24] project like today? So we will do
[00:47:22 - 00:47:28] something like this right now. So right
[00:47:24 - 00:47:32] now uh I implemented a fast API but we
[00:47:28 - 00:47:32] haven't implemented back end yet.
[00:47:32 - 00:47:37] Yeah. What is a sage comment? Thanks for
[00:47:34 - 00:47:42] answering that. I um need to quickly get
[00:47:37 - 00:47:42] some water. I'll be right back.
[00:47:56 - 00:48:01] >> So, I see that um we've been already
[00:47:59 - 00:48:05] doing this for 50 minutes. I don't
[00:48:01 - 00:48:07] really have uh a specific time in mind
[00:48:05 - 00:48:12] when we finish. Well, probably I need to
[00:48:07 - 00:48:16] finish it by uh 7. Um yeah, but like if
[00:48:12 - 00:48:18] you need to go, feel free to go. Um so
[00:48:16 - 00:48:21] it will take some time to finish cuz I
[00:48:18 - 00:48:23] think we're like halfway through. Um
[00:48:21 - 00:48:26] this is how I wanted these sessions to
[00:48:23 - 00:48:28] be, right? So we talk, you ask questions
[00:48:26 - 00:48:30] like why did you use this tool? So of
[00:48:28 - 00:48:34] course it takes some time to actually
[00:48:30 - 00:48:36] explain this and as I said also for me I
[00:48:34 - 00:48:39] am only partly partially prepared right.
[00:48:36 - 00:48:41] So I want to actually do this together
[00:48:39 - 00:48:43] with you.
[00:48:41 - 00:48:48] Okay. So yeah it will take maybe one
[00:48:43 - 00:48:50] more hour to finish it think.
[00:48:48 - 00:48:52] So what service do you use to actually
[00:48:50 - 00:48:55] host the remote sessions? From my
[00:48:52 - 00:48:56] understanding Timuk is used to manage it
[00:48:55 - 00:48:58] to actually host remote sessions. So
[00:48:56 - 00:49:02] this is uh I'm not sure I understood
[00:48:58 - 00:49:05] your question um fully but um so I have
[00:49:02 - 00:49:09] a remote machine and the remote machine
[00:49:05 - 00:49:12] is hosting the remote sessions and tuxer
[00:49:09 - 00:49:14] manages it
[00:49:12 - 00:49:17] so I where do you host your remote
[00:49:14 - 00:49:19] machine I already answered this um so
[00:49:17 - 00:49:24] you ask if it's cloud or on premise it's
[00:49:19 - 00:49:28] kind of both so um HNER is more is
[00:49:24 - 00:49:30] closer to on premise than cloud. So what
[00:49:28 - 00:49:32] you get when you get a rent a machine on
[00:49:30 - 00:49:34] headner you actually get a piece of
[00:49:32 - 00:49:37] hardware right so it's not cloud where
[00:49:34 - 00:49:39] you can okay now I need an instance and
[00:49:37 - 00:49:41] then next second I don't need it so you
[00:49:39 - 00:49:44] actually get a physical
[00:49:41 - 00:49:47] thing that is inserted somewhere that is
[00:49:44 - 00:49:48] stored somewhere in a data center you
[00:49:47 - 00:49:51] don't have direct access to the data
[00:49:48 - 00:49:53] center but you have an SSH access to
[00:49:51 - 00:49:55] this thing right so the machine is
[00:49:53 - 00:49:57] actually a physical machine somewhere so
[00:49:55 - 00:49:59] it's on premise but because it's not
[00:49:57 - 00:50:01] under my table. I don't need to host it.
[00:49:59 - 00:50:02] So, it's not on premise. So, it's kind
[00:50:01 - 00:50:05] of both cloud and on premise. I don't
[00:50:02 - 00:50:09] know if it makes sense, but like
[00:50:05 - 00:50:11] if you want to buy a machine on HNER,
[00:50:09 - 00:50:14] sometimes you actually need to wait till
[00:50:11 - 00:50:16] they order the machine and they install
[00:50:14 - 00:50:18] it. And there is also what they call
[00:50:16 - 00:50:21] installation cost, right? So you
[00:50:18 - 00:50:23] actually need to pay like a onetime fee
[00:50:21 - 00:50:26] for them to um I don't know unpack the
[00:50:23 - 00:50:29] server and insert it into the Iraq,
[00:50:26 - 00:50:32] right? So I would say it's closer to on
[00:50:29 - 00:50:37] premise than cloud but uh because of
[00:50:32 - 00:50:39] that it's way cheaper than um than AWS.
[00:50:37 - 00:50:43] So for this machine that I pay uh so
[00:50:39 - 00:50:47] here I pay
[00:50:43 - 00:50:50] let's see what I actually have here.
[00:50:47 - 00:50:53] Oops. It's H.
[00:50:50 - 00:50:56] So, I have like 60 gigs of RAM and 12
[00:50:53 - 00:51:00] cores. For a machine of this sort, uh,
[00:50:56 - 00:51:03] you'll pay on AWS maybe like 4 or 500
[00:51:00 - 00:51:06] per month and I pay only 100.
[00:51:03 - 00:51:10] And also
[00:51:06 - 00:51:10] what they have is um
[00:51:10 - 00:51:17] they have like a marketplace with uh
[00:51:14 - 00:51:17] like used computers.
[00:51:20 - 00:51:24] Uh this server auction, right? So you
[00:51:22 - 00:51:26] can actually
[00:51:24 - 00:51:30] Wait, did I say I pay over 100? I think
[00:51:26 - 00:51:32] I pay less. So this is how much I pay.
[00:51:30 - 00:51:35] Yeah, it's a lot cheaper.
[00:51:32 - 00:51:38] So then you can get like for $40
[00:51:35 - 00:51:41] you can get this type of machine.
[00:51:38 - 00:51:44] So it's really convenient. Anyways like
[00:51:41 - 00:51:46] the point wasn't I didn't want to spend
[00:51:44 - 00:51:49] a lot of time talking about this. I find
[00:51:46 - 00:51:53] it convenient.
[00:51:49 - 00:51:53] Okay. Uh any more questions?
[00:51:55 - 00:51:58] I just got my cloud practitioner
[00:51:56 - 00:51:59] certification with AWS and learned that
[00:51:58 - 00:52:01] apparently you can also provision
[00:51:59 - 00:52:03] dedicated host machine like what you
[00:52:01 - 00:52:06] explained with header. Yeah, it will be
[00:52:03 - 00:52:08] more expensive. Uh
[00:52:06 - 00:52:10] in real world applications, do you
[00:52:08 - 00:52:12] follow a standard folder structure or
[00:52:10 - 00:52:15] best practice for a fast API or do you
[00:52:12 - 00:52:17] typically let agents organize things? I
[00:52:15 - 00:52:20] typically let agents organize it. To be
[00:52:17 - 00:52:23] honest, I don't know if there is a good
[00:52:20 - 00:52:26] structure that um I would follow for
[00:52:23 - 00:52:28] fast API. For jungo, there is uh like
[00:52:26 - 00:52:29] for jungo,
[00:52:28 - 00:52:32] you have to follow a certain structure.
[00:52:29 - 00:52:34] So the framework dictates the structure.
[00:52:32 - 00:52:37] So there is no other way around. Like
[00:52:34 - 00:52:39] for fast API, it's kind of wild west.
[00:52:37 - 00:52:41] You can put everything in one file, it
[00:52:39 - 00:52:44] will work. Um
[00:52:41 - 00:52:46] you can also have structure. I don't
[00:52:44 - 00:52:48] have a favorite one. So that's why for
[00:52:46 - 00:52:50] me it's easier. I just need don't need
[00:52:48 - 00:52:53] to use my mental energy to decide these
[00:52:50 - 00:52:56] things. So then I just let the agent uh
[00:52:53 - 00:52:56] decide.
[00:52:58 - 00:53:02] >> Okay. Somebody has questions.

## Window 008: 00:52:31 - 01:00:31

[00:52:32 - 00:52:37] So there is no other way around. Like
[00:52:34 - 00:52:39] for fast API, it's kind of wild west.
[00:52:37 - 00:52:41] You can put everything in one file, it
[00:52:39 - 00:52:44] will work. Um
[00:52:41 - 00:52:46] you can also have structure. I don't
[00:52:44 - 00:52:48] have a favorite one. So that's why for
[00:52:46 - 00:52:50] me it's easier. I just need don't need
[00:52:48 - 00:52:53] to use my mental energy to decide these
[00:52:50 - 00:52:56] things. So then I just let the agent uh
[00:52:53 - 00:52:56] decide.
[00:52:58 - 00:53:02] >> Okay. Somebody has questions.
[00:53:02 - 00:53:11] >> Okay. I think I muted some of you.
[00:53:07 - 00:53:13] Okay. Um you won't need Docker for this.
[00:53:11 - 00:53:15] Uh for what we do today, we will need
[00:53:13 - 00:53:17] Docker. Yes, we will need because we uh
[00:53:15 - 00:53:19] the plan is to then eventually deploy
[00:53:17 - 00:53:21] it. So for that we will need docker.
[00:53:19 - 00:53:22] Okay, where did we stop? So I hope we
[00:53:21 - 00:53:25] actually finished today. So let's
[00:53:22 - 00:53:27] continue. Okay, this was a different
[00:53:25 - 00:53:29] one.
[00:53:27 - 00:53:32] So now what we have is we have the
[00:53:29 - 00:53:35] search agent renderer schemas and
[00:53:32 - 00:53:39] app.py. So let's actually see what we
[00:53:35 - 00:53:44] have. So this is our entry point.
[00:53:39 - 00:53:47] Um so we have health check we have ask
[00:53:44 - 00:53:49] so this is the endpoint we will use for
[00:53:47 - 00:53:52] asking this
[00:53:49 - 00:53:54] dam so run agent so this is the function
[00:53:52 - 00:53:58] we implemented actually in our notebook
[00:53:54 - 00:53:58] so this was the function
[00:54:00 - 00:54:06] um here oops
[00:54:03 - 00:54:11] yeah this is what this is the our two
[00:54:06 - 00:54:14] call loop here so It uses this
[00:54:11 - 00:54:16] and at the end it sends an ask response.
[00:54:14 - 00:54:18] Okay,
[00:54:16 - 00:54:21] I think uh
[00:54:18 - 00:54:23] ah ask stream. Okay, I was thinking like
[00:54:21 - 00:54:25] uh did we not mention that we watch
[00:54:23 - 00:54:28] streaming? I don't remember mentioning
[00:54:25 - 00:54:31] it. But actually yes. So it uses this
[00:54:28 - 00:54:34] SSA. I think it's server side events.
[00:54:31 - 00:54:39] This is exactly what we need uh for uh
[00:54:34 - 00:54:42] for us because we want to um be able to
[00:54:39 - 00:54:44] push events to front end. I'm not really
[00:54:42 - 00:54:47] an expert in these things like I know
[00:54:44 - 00:54:49] these things exist and I know how to ask
[00:54:47 - 00:54:51] lot to implement these things. That's
[00:54:49 - 00:54:54] pretty much the extent of the knowledge
[00:54:51 - 00:54:58] I have about these things. Uh but um
[00:54:54 - 00:55:00] from what I see I have no objections to
[00:54:58 - 00:55:02] the way it wrote the code. Like for me
[00:55:00 - 00:55:05] it's actually
[00:55:02 - 00:55:09] let's say understandable
[00:55:05 - 00:55:12] I uh okay it's interesting
[00:55:09 - 00:55:14] init index open a client yeah this is
[00:55:12 - 00:55:18] the first time actually I see this
[00:55:14 - 00:55:18] construct construction
[00:55:18 - 00:55:25] okay
[00:55:20 - 00:55:27] so um I would typically define like a um
[00:55:25 - 00:55:30] global variable here
[00:55:27 - 00:55:36] and then they would access it here,
[00:55:30 - 00:55:40] right? Uh but I will undo it.
[00:55:36 - 00:55:41] I I'll I'll trust uh the agent.
[00:55:40 - 00:55:45] Um
[00:55:41 - 00:55:47] but yeah, it looks okay. I mean, I still
[00:55:45 - 00:55:50] uh don't have a lot of ideas what's
[00:55:47 - 00:55:53] happening here. Uh so there is event
[00:55:50 - 00:55:56] generator. So there's producer. Okay. So
[00:55:53 - 00:55:58] we have this run agent and run agent is
[00:55:56 - 00:56:00] producing some events. So if we go
[00:55:58 - 00:56:04] inside so these are the events right so
[00:56:00 - 00:56:05] this handle event uh so I think what is
[00:56:04 - 00:56:08] happening inside
[00:56:05 - 00:56:11] um okay so we have this base renderer so
[00:56:08 - 00:56:14] this is an abstract class and then this
[00:56:11 - 00:56:14] collecting renderer
[00:56:15 - 00:56:20] yeah ah okay so this is what the thing
[00:56:17 - 00:56:22] we need so we have this Q and this thing
[00:56:20 - 00:56:25] puts this event to the queue and these
[00:56:22 - 00:56:27] events are sent to the front end so this
[00:56:25 - 00:56:29] is my interpretation
[00:56:27 - 00:56:32] This this is what I think is happening.
[00:56:29 - 00:56:35] But like I'm not an expert that's why I
[00:56:32 - 00:56:39] cannot really uh judge the quality of
[00:56:35 - 00:56:43] this code. But on the first look I think
[00:56:39 - 00:56:45] it looks pretty neat. Like the nothing
[00:56:43 - 00:56:48] sc jumps at me and screams like hey like
[00:56:45 - 00:56:50] I so overall I'm actually surprised that
[00:56:48 - 00:56:53] I don't need to ask it to refactor at
[00:56:50 - 00:56:58] least yet. Right. So it actually used
[00:56:53 - 00:56:58] the the code we implemented.
[00:56:58 - 00:57:05] So it didn't attempt to change it very
[00:57:01 - 00:57:07] much. Um so I recognize this code. This
[00:57:05 - 00:57:09] is the code we just wrote, right? So it
[00:57:07 - 00:57:11] didn't change. So we have our
[00:57:09 - 00:57:13] instructions.
[00:57:11 - 00:57:15] Um so let's see what we have in
[00:57:13 - 00:57:17] renderer. So we already talked about
[00:57:15 - 00:57:20] this. So this is what we are going to
[00:57:17 - 00:57:24] use for pushing events to front end
[00:57:20 - 00:57:26] schemas. Um, okay. Nothing super
[00:57:24 - 00:57:32] interesting here. So, these are just how
[00:57:26 - 00:57:34] the responses will look like and search.
[00:57:32 - 00:57:37] Okay. I
[00:57:34 - 00:57:39] I don't really like this uh because it's
[00:57:37 - 00:57:42] a global variable.
[00:57:39 - 00:57:42] Um,
[00:57:43 - 00:57:47] I think I will just let it be like I
[00:57:45 - 00:57:50] don't want to spend time refactoring
[00:57:47 - 00:57:53] this cuz our code is fairly small. It's
[00:57:50 - 00:57:56] just like 55 lines of code. Like if we
[00:57:53 - 00:57:58] had more tools then the way the what I
[00:57:56 - 00:58:01] would do is I would put all these tools
[00:57:58 - 00:58:04] inside one single class and if you took
[00:58:01 - 00:58:06] the Maven course maybe you have must
[00:58:04 - 00:58:08] maybe you remember seeing how we
[00:58:06 - 00:58:11] organized the tools there. So I would
[00:58:08 - 00:58:13] would do something similar here. So
[00:58:11 - 00:58:15] instead of having a global variable I
[00:58:13 - 00:58:17] would um
[00:58:15 - 00:58:19] define this somewhere here in up right.
[00:58:17 - 00:58:22] So here for me it's okay to have global
[00:58:19 - 00:58:24] variables inside app but like in other
[00:58:22 - 00:58:30] modules I don't want that like it's
[00:58:24 - 00:58:32] easier to manage maintain test and so on
[00:58:30 - 00:58:33] no needs for structured output I think
[00:58:32 - 00:58:36] eventually we might need to have
[00:58:33 - 00:58:37] structured output um I don't want to
[00:58:36 - 00:58:40] over complicate this particular project
[00:58:37 - 00:58:43] right now uh but as we know that usually
[00:58:40 - 00:58:45] when we have structured output we kind
[00:58:43 - 00:58:49] of force the agent to be better right so
[00:58:45 - 00:58:52] eventually uh for version
[00:58:49 - 00:58:53] um I don't know for version number two
[00:58:52 - 00:58:56] for the next version I would actually
[00:58:53 - 00:58:58] add this
[00:58:56 - 00:59:00] here I just want to focus first on
[00:58:58 - 00:59:03] making it work end to end because when
[00:59:00 - 00:59:05] we add structured output we actually add
[00:59:03 - 00:59:07] one more layer of complexity right
[00:59:05 - 00:59:10] because when we talk about structured
[00:59:07 - 00:59:13] output and streaming at the same time we
[00:59:10 - 00:59:16] will need to stream things online and
[00:59:13 - 00:59:17] this makes the code that is already a
[00:59:16 - 00:59:19] bit complic complicated even more
[00:59:17 - 00:59:21] complicated right so I don't want to I
[00:59:19 - 00:59:23] want to avoid it for this particular
[00:59:21 - 00:59:25] session but um I think it was actually
[00:59:23 - 00:59:28] creating an application that I wanted to
[00:59:25 - 00:59:31] use I would first make this thing work
[00:59:28 - 00:59:33] end to end so I want to create front end
[00:59:31 - 00:59:35] now or maybe we can actually first test
[00:59:33 - 00:59:38] back end but I want to create front end
[00:59:35 - 00:59:40] now and I would then test that these
[00:59:38 - 00:59:43] things work then I would deploy it and
[00:59:40 - 00:59:45] only after that I would think okay now I
[00:59:43 - 00:59:47] need this this and that right so let's
[00:59:45 - 00:59:49] here let's focus focus on making this
[00:59:47 - 00:59:52] thing work and then later we can always
[00:59:49 - 00:59:52] improve.
[00:59:53 - 00:59:57] Um is there any way to get recording of
[00:59:55 - 01:00:01] this session? So this will be shared on
[00:59:57 - 01:00:01] Slack. Yes,
[01:00:01 - 01:00:10] thank you Aneska. Um so um okay where
[01:00:04 - 01:00:11] did we stop? So now the coding agent in
[01:00:10 - 01:00:16] said
[01:00:11 - 01:00:19] so how how do I check it?
[01:00:16 - 01:00:22] So I probably want to run it. So I need
[01:00:19 - 01:00:22] to
[01:00:26 - 01:00:36] So for this one I want to have um let's
[01:00:30 - 01:00:36] have a make file for this.

## Window 009: 01:00:01 - 01:08:01

[01:00:04 - 01:00:11] did we stop? So now the coding agent in
[01:00:10 - 01:00:16] said
[01:00:11 - 01:00:19] so how how do I check it?
[01:00:16 - 01:00:22] So I probably want to run it. So I need
[01:00:19 - 01:00:22] to
[01:00:26 - 01:00:36] So for this one I want to have um let's
[01:00:30 - 01:00:36] have a make file for this.
[01:00:37 - 01:00:40] So I don't want to memorize these
[01:00:38 - 01:00:45] commands all the time. So I want to have
[01:00:40 - 01:00:47] a make file and I can just do yeah make
[01:00:45 - 01:00:51] def.
[01:00:47 - 01:00:53] So okay I have two things running.
[01:00:51 - 01:00:56] Make dev.
[01:00:53 - 01:01:03] Okay now this thing is running. I need
[01:00:56 - 01:01:06] another uh terminal to test it. So
[01:01:03 - 01:01:08] agent. So what do I need? Okay I closed
[01:01:06 - 01:01:10] I closed the agent.
[01:01:08 - 01:01:12] not accidentally but yeah I still need
[01:01:10 - 01:01:16] this
[01:01:12 - 01:01:20] um I need to send a
[01:01:16 - 01:01:25] post request so connect to this uh okay
[01:01:20 - 01:01:25] so let's first start with health check
[01:01:29 - 01:01:35] okay health check works then we want to
[01:01:33 - 01:01:38] um
[01:01:35 - 01:01:43] so I'm not really interested in um usual
[01:01:38 - 01:01:43] point. I want to check this.
[01:01:43 - 01:01:49] I actually have no idea what I will see
[01:01:45 - 01:01:49] now. So let's see.
[01:01:50 - 01:01:55] Okay, so we have this server side
[01:01:52 - 01:01:55] events.
[01:01:55 - 01:02:02] So this is um similar to what um
[01:01:59 - 01:02:05] what we get when we stream uh requests
[01:02:02 - 01:02:09] from OpenAI, right? So we also have
[01:02:05 - 01:02:10] stuff like that. Okay.
[01:02:09 - 01:02:14] So, we have some events and then at the
[01:02:10 - 01:02:14] end uh
[01:02:14 - 01:02:21] everything is done. Cool.
[01:02:18 - 01:02:26] So, it seems to work.
[01:02:21 - 01:02:26] We can also check this docs.
[01:02:27 - 01:02:33] Yeah. So, the same things says uh we
[01:02:30 - 01:02:35] saw. Okay. Plasti is quite convenient,
[01:02:33 - 01:02:39] right?
[01:02:35 - 01:02:41] Okay. Um what do we want to do next? Um
[01:02:39 - 01:02:43] any questions so far?
[01:02:41 - 01:02:49] Because I want now to create front end
[01:02:43 - 01:02:49] and maybe before we create front end. Uh
[01:02:49 - 01:02:55] uh I there is a question about the Slack
[01:02:52 - 01:02:57] invite. Um so since you're here, I
[01:02:55 - 01:02:59] suppose you are already in Slack. If
[01:02:57 - 01:03:01] you're not already in Slack, I have a
[01:02:59 - 01:03:03] question. Why? How are you here? Right.
[01:03:01 - 01:03:05] uh cuz this is supposed to be like a
[01:03:03 - 01:03:08] private event for people who are already
[01:03:05 - 01:03:12] in Slack. So um you're supposed to be
[01:03:08 - 01:03:15] there. So if you're not um yeah then I
[01:03:12 - 01:03:19] hope you like um what you see right now
[01:03:15 - 01:03:24] and you consider joining us. So uh this
[01:03:19 - 01:03:28] is uh you go to AI shipping labs
[01:03:24 - 01:03:32] and then um you get access to community
[01:03:28 - 01:03:36] here in main and uh premium and also if
[01:03:32 - 01:03:38] you um take my Maven course you also get
[01:03:36 - 01:03:42] access to this community.
[01:03:38 - 01:03:44] So then once you
[01:03:42 - 01:03:48] get in once you like either join the
[01:03:44 - 01:03:51] course or join one of these um plans
[01:03:48 - 01:03:55] then you get an invite.
[01:03:51 - 01:03:55] Okay. So where did we stop?
[01:03:57 - 01:04:05] So um I yeah I was asking if you have
[01:04:02 - 01:04:07] any questions um so yeah feel free to
[01:04:05 - 01:04:09] ask or yeah just raise your hand and
[01:04:07 - 01:04:13] ask. Um so but for now what I want to do
[01:04:09 - 01:04:16] is I want to create front end for that.
[01:04:13 - 01:04:18] For front end um typically for
[01:04:16 - 01:04:20] applications like that I don't want to
[01:04:18 - 01:04:26] have anything very complicated.
[01:04:20 - 01:04:29] So uh what I want to have is um a simple
[01:04:26 - 01:04:31] um simple u HTML page simple JavaScript
[01:04:29 - 01:04:34] page. So I don't want to use React or
[01:04:31 - 01:04:37] anything like that. So now let me
[01:04:34 - 01:04:41] dictate this. So now I want to build a
[01:04:37 - 01:04:44] front end uh for that and I want to be
[01:04:41 - 01:04:46] to do something simple. So let's use
[01:04:44 - 01:04:49] vanilla JavaScript
[01:04:46 - 01:04:51] and um I want to have minimal amount of
[01:04:49 - 01:04:55] files. So let's create a folder front
[01:04:51 - 01:05:00] end for that. And inside um let's use
[01:04:55 - 01:05:02] something like VA for um managing
[01:05:00 - 01:05:08] uh this.
[01:05:02 - 01:05:12] Okay. So, it didn't recognize Vita
[01:05:08 - 01:05:15] or V. I think it's not Vita, it's Vit.
[01:05:12 - 01:05:19] Uh, I can they say how I should
[01:05:15 - 01:05:19] pronounce it.
[01:05:21 - 01:05:26] Francesca, do you speak French?
[01:05:24 - 01:05:28] I think it's a French word.
[01:05:26 - 01:05:29] >> I think it's feet. Does it say feet?
[01:05:28 - 01:05:31] Yeah.
[01:05:29 - 01:05:37] >> Mercy.
[01:05:31 - 01:05:40] Okay. Um so um yeah so vit is um a tool
[01:05:37 - 01:05:42] for JavaScript that lets us uh
[01:05:40 - 01:05:45] automatically reload things if they
[01:05:42 - 01:05:47] change if they change right but I want
[01:05:45 - 01:05:51] to keep it super minimal that's why I
[01:05:47 - 01:05:53] ask you to use vanilla JavaScript um
[01:05:51 - 01:05:56] yeah so by the way for this thing um
[01:05:53 - 01:05:58] like since we use it we will need NodeJS
[01:05:56 - 01:06:01] right if you don't need if you don't
[01:05:58 - 01:06:03] have NodeJS what you can actually do is
[01:06:01 - 01:06:04] you can ask uh if you don't want to
[01:06:03 - 01:06:06] install it of course I recommend
[01:06:04 - 01:06:08] installing it uh well probably if you
[01:06:06 - 01:06:11] use something like clot code or codex or
[01:06:08 - 01:06:12] whatever you already have nodejs cuz uh
[01:06:11 - 01:06:15] they are written in javascript you need
[01:06:12 - 01:06:18] to have node but if you don't want to
[01:06:15 - 01:06:21] install them for some reasons uh what
[01:06:18 - 01:06:24] you can do is just ask your agent to
[01:06:21 - 01:06:27] implement uh plain javascript without
[01:06:24 - 01:06:29] using any uh any how do you call this
[01:06:27 - 01:06:31] with like builders or whatever like
[01:06:29 - 01:06:33] you're just plain javascript project.
[01:06:31 - 01:06:38] This is what you can ask.
[01:06:33 - 01:06:42] Okay. Now I want to have a make target
[01:06:38 - 01:06:42] for running.
[01:06:46 - 01:06:52] So in one uh terminal it says run make
[01:06:50 - 01:06:54] def in one terminal. Okay, we already
[01:06:52 - 01:06:59] did this. In other terminal it says run
[01:06:54 - 01:07:03] this. But I want to um
[01:06:59 - 01:07:06] Okay. Make front end install.
[01:07:03 - 01:07:06] Um
[01:07:09 - 01:07:15] make front and install.
[01:07:13 - 01:07:19] Cool.
[01:07:15 - 01:07:24] Moderate severity vulnerabilities.
[01:07:19 - 01:07:25] Okay. Should I worry? Um I haven't seen
[01:07:24 - 01:07:29] anything.
[01:07:25 - 01:07:29] uh and then make from that.
[01:07:32 - 01:07:36] Okay, I guess some things are already
[01:07:34 - 01:07:38] running.
[01:07:36 - 01:07:44] Yeah, let's see.
[01:07:38 - 01:07:48] Um okay, so we can ask our FAQ agent
[01:07:44 - 01:07:50] something. I just discovered the course.
[01:07:48 - 01:07:53] Can I join?
[01:07:50 - 01:07:53] No.
[01:07:56 - 01:08:01] So
[01:07:58 - 01:08:05] I don't know if it's broken or not. So
[01:08:01 - 01:08:07] in this case I would need to press F. Uh

## Window 010: 01:07:31 - 01:15:31

[01:07:32 - 01:07:36] Okay, I guess some things are already
[01:07:34 - 01:07:38] running.
[01:07:36 - 01:07:44] Yeah, let's see.
[01:07:38 - 01:07:48] Um okay, so we can ask our FAQ agent
[01:07:44 - 01:07:50] something. I just discovered the course.
[01:07:48 - 01:07:53] Can I join?
[01:07:50 - 01:07:53] No.
[01:07:56 - 01:08:01] So
[01:07:58 - 01:08:05] I don't know if it's broken or not. So
[01:08:01 - 01:08:07] in this case I would need to press F. Uh
[01:08:05 - 01:08:10] 12 and see.
[01:08:07 - 01:08:13] Okay.
[01:08:10 - 01:08:16] And this is what I would copy. Did it
[01:08:13 - 01:08:20] actually reply? Okay.
[01:08:16 - 01:08:26] Okay. I will ah so this is related to
[01:08:20 - 01:08:29] favicon. So this is this is fine but um
[01:08:26 - 01:08:31] so I expected to see streaming like it's
[01:08:29 - 01:08:33] not streaming the response. I also
[01:08:31 - 01:08:35] wanted to see two calls I did not see
[01:08:33 - 01:08:37] them and I wanted to see two calls as
[01:08:35 - 01:08:39] they happen. So now I give this
[01:08:37 - 01:08:41] feedback.
[01:08:39 - 01:08:45] Um
[01:08:41 - 01:08:48] I have this zoom thing everywhere.
[01:08:45 - 01:08:51] Okay. Um,
[01:08:48 - 01:08:53] so I tested it and it seems to be fine,
[01:08:51 - 01:08:56] but I have to wait till I see the final
[01:08:53 - 01:08:58] response. So I ask my question and then
[01:08:56 - 01:09:00] it's thinking and only when the final
[01:08:58 - 01:09:02] response is ready, I see the response.
[01:09:00 - 01:09:05] So what I want to have instead is I want
[01:09:02 - 01:09:08] to use the streaming API and I want to
[01:09:05 - 01:09:10] see events as they happen. So when we
[01:09:08 - 01:09:12] are making a tool call, I want to see
[01:09:10 - 01:09:15] this tool call. I want to see the
[01:09:12 - 01:09:16] parameters uh that we are getting. I
[01:09:15 - 01:09:19] want also to see the response we're
[01:09:16 - 01:09:21] getting from uh our tool. And this
[01:09:19 - 01:09:24] response should be collapsible. So it
[01:09:21 - 01:09:26] shouldn't take a lot of space. And yeah,
[01:09:24 - 01:09:28] I just want to have this interactivity
[01:09:26 - 01:09:31] so I know that um something is
[01:09:28 - 01:09:31] happening.
[01:09:37 - 01:09:42] So let's see what it's um what it will
[01:09:39 - 01:09:42] come up with.
[01:09:44 - 01:09:49] Um yeah, so this voice recognition is
[01:09:46 - 01:09:52] not ideal um
[01:09:49 - 01:09:56] from R2. So I have no idea what this R2
[01:09:52 - 01:09:59] is. But these models are smart enough to
[01:09:56 - 01:10:00] um actually understand what I mean.
[01:09:59 - 01:10:02] Well, I hope it will be able to
[01:10:00 - 01:10:04] understand what I mean. But like the
[01:10:02 - 01:10:06] gist is clear, right? So I want
[01:10:04 - 01:10:10] streaming events. I don't want to wait
[01:10:06 - 01:10:14] till um you know everything is done. So
[01:10:10 - 01:10:18] my one interactivity.
[01:10:14 - 01:10:20] Okay. So it's taking some time to think
[01:10:18 - 01:10:23] like I sometimes wonder how they come up
[01:10:20 - 01:10:26] with uh these things.
[01:10:23 - 01:10:30] They even mean caramelizing like why
[01:10:26 - 01:10:30] caramelizing? It's weird.
[01:10:31 - 01:10:38] Okay. Almost done thinking. Cool. It's
[01:10:34 - 01:10:38] taking time.
[01:10:39 - 01:10:44] And that al can also be that um you know
[01:10:41 - 01:10:47] a lot of people use clo code. So what
[01:10:44 - 01:10:50] could be h happening is that you know
[01:10:47 - 01:10:52] it's just slow because of the load or
[01:10:50 - 01:10:55] it's slow because it's rewriting the
[01:10:52 - 01:10:58] whole um thing.
[01:10:55 - 01:11:01] Ah it was actually thinking. Okay.
[01:10:58 - 01:11:03] Got it.
[01:11:01 - 01:11:06] Oh.
[01:11:03 - 01:11:09] So we don't really see here thinking
[01:11:06 - 01:11:12] traces like because when you use u
[01:11:09 - 01:11:14] the UI the chat you can see what it was
[01:11:12 - 01:11:17] thinking about but here we don't see
[01:11:14 - 01:11:17] that.
[01:11:21 - 01:11:25] Okay. Well I will not pretend I
[01:11:23 - 01:11:29] understand what's happening here. Front
[01:11:25 - 01:11:32] end is definitely not my um strongest
[01:11:29 - 01:11:32] skill.
[01:11:36 - 01:11:41] So it changed both. Cool.
[01:11:42 - 01:11:49] Restart both servers. I will not need to
[01:11:44 - 01:11:51] do this cuz here I run da bit sorry. So
[01:11:49 - 01:11:54] it should automatically
[01:11:51 - 01:11:56] restart. So that's the that this is why
[01:11:54 - 01:12:00] I actually use bit.
[01:11:56 - 01:12:03] How do I join the course?
[01:12:00 - 01:12:03] No.
[01:12:04 - 01:12:08] Okay. Much better.
[01:12:10 - 01:12:16] It's um it's okay.
[01:12:14 - 01:12:18] It's formatted actually.
[01:12:16 - 01:12:22] I mean, we can we can definitely work
[01:12:18 - 01:12:27] with this. Um
[01:12:22 - 01:12:27] Okay. So, what else should I ask? Um
[01:12:27 - 01:12:32] yeah. Well, to make it more interesting,
[01:12:30 - 01:12:35] what we can do is we can ask, hey, like
[01:12:32 - 01:12:37] explore the repository, ask multiple
[01:12:35 - 01:12:39] questions, but I think right now it's
[01:12:37 - 01:12:41] kind of okay. Like, let's not spend too
[01:12:39 - 01:12:42] much time on that. It's working. It's
[01:12:41 - 01:12:45] working the way I want. There's of
[01:12:42 - 01:12:46] course a lot of things we can improve,
[01:12:45 - 01:12:49] but it's already okay. Like, for
[01:12:46 - 01:12:53] example, here for the sources, we can
[01:12:49 - 01:12:54] make them clickable. Um, like there are
[01:12:53 - 01:12:57] many things to improve. like we can
[01:12:54 - 01:13:00] spend like entire evening now doing this
[01:12:57 - 01:13:02] but it's kind of working right so this
[01:13:00 - 01:13:06] is good enough
[01:13:02 - 01:13:07] so let me see what questions we have I
[01:13:06 - 01:13:10] think the voice instruction doesn't
[01:13:07 - 01:13:12] translate it's instructed to go instead
[01:13:10 - 01:13:18] of uh
[01:13:12 - 01:13:18] you need cloud pro for this u yeah so
[01:13:19 - 01:13:27] if it instructed two calls instead of
[01:13:22 - 01:13:30] two call Yes. Um it does not work
[01:13:27 - 01:13:34] ideally but CL code is smart enough to
[01:13:30 - 01:13:39] figure out that um what I want from it.
[01:13:34 - 01:13:41] You need cloth pro for this. So I use uh
[01:13:39 - 01:13:46] this 20x
[01:13:41 - 01:13:48] uh pro I think subscription or 20x plus
[01:13:46 - 01:13:52] I don't remember. Yes, this one. I use
[01:13:48 - 01:13:57] this one. But I think um like you can
[01:13:52 - 01:14:00] just use a smaller plants like the one
[01:13:57 - 01:14:03] for 20 or like let's say if you don't
[01:14:00 - 01:14:06] want to spend money uh a lot of money on
[01:14:03 - 01:14:08] this cuz like $200 is maybe for you
[01:14:06 - 01:14:10] you're not ready to pay $200 for cloud
[01:14:08 - 01:14:13] code. I totally understand that. So what
[01:14:10 - 01:14:17] I would recommend for you is
[01:14:13 - 01:14:19] uh GitHub copilot
[01:14:17 - 01:14:23] price.
[01:14:19 - 01:14:25] So for $10 per month you are actually
[01:14:23 - 01:14:28] getting
[01:14:25 - 01:14:30] really good package right so with 300 p
[01:14:28 - 01:14:33] requests you can build multiple good
[01:14:30 - 01:14:35] projects and it's just $10. So if you if
[01:14:33 - 01:14:38] you don't pay for any uh provider yet
[01:14:35 - 01:14:41] and you feel like okay I want to try I
[01:14:38 - 01:14:47] would oh temporarily unavailable. Okay.
[01:14:41 - 01:14:47] I was actually going to say uh try that.
[01:14:52 - 01:14:59] Okay.
[01:14:54 - 01:15:01] Well, um I'm sorry I didn't know.
[01:14:59 - 01:15:04] Uh well maybe you are subscribed to
[01:15:01 - 01:15:08] Chajb PD right and then uh Codex uh
[01:15:04 - 01:15:10] actually um yeah you can get Codex if as
[01:15:08 - 01:15:12] a part of your Chipds subscription.
[01:15:10 - 01:15:16] Yeah.
[01:15:12 - 01:15:18] >> Hey I I'm too lazy to type.
[01:15:16 - 01:15:20] >> Yeah sure. Of course. It's actually nice
[01:15:18 - 01:15:22] to talk like it's way better and more
[01:15:20 - 01:15:24] interactive and it's just not just me
[01:15:22 - 01:15:26] talking but also other people. So yeah.
[01:15:24 - 01:15:29] What's up? Uh can you spend like a
[01:15:26 - 01:15:32] minute or two explaining the fast API
[01:15:29 - 01:15:34] endpoints like what endpoints are needed

## Window 011: 01:15:01 - 01:23:01

[01:15:04 - 01:15:10] actually um yeah you can get Codex if as
[01:15:08 - 01:15:12] a part of your Chipds subscription.
[01:15:10 - 01:15:16] Yeah.
[01:15:12 - 01:15:18] >> Hey I I'm too lazy to type.
[01:15:16 - 01:15:20] >> Yeah sure. Of course. It's actually nice
[01:15:18 - 01:15:22] to talk like it's way better and more
[01:15:20 - 01:15:24] interactive and it's just not just me
[01:15:22 - 01:15:26] talking but also other people. So yeah.
[01:15:24 - 01:15:29] What's up? Uh can you spend like a
[01:15:26 - 01:15:32] minute or two explaining the fast API
[01:15:29 - 01:15:34] endpoints like what endpoints are needed
[01:15:32 - 01:15:37] for this project this mini project and
[01:15:34 - 01:15:38] then if we were to deploy our own
[01:15:37 - 01:15:42] projects like what should we think about
[01:15:38 - 01:15:46] when we create um those API endpoints?
[01:15:42 - 01:15:48] >> Yeah sure. Um, so the only endpoint we
[01:15:46 - 01:15:53] actually need is this one like ask
[01:15:48 - 01:15:55] stream, right? Cuz um, we want to be
[01:15:53 - 01:15:57] able to ask a question and we want to be
[01:15:55 - 01:15:59] able to stream back the response, right?
[01:15:57 - 01:16:02] So for this particular project, that's
[01:15:59 - 01:16:04] actually the only thing we need. Um, we
[01:16:02 - 01:16:07] might want to, let's say if our
[01:16:04 - 01:16:09] application is more complex, let me go
[01:16:07 - 01:16:12] back is maybe we want to start a new
[01:16:09 - 01:16:15] chat, right? Um
[01:16:12 - 01:16:17] wait wait wait a minute. Um so I think
[01:16:15 - 01:16:18] right now we are actually not continuing
[01:16:17 - 01:16:24] right. So if I ask a follow-up question
[01:16:18 - 01:16:27] now uh which
[01:16:24 - 01:16:30] which deadlines right so what it will do
[01:16:27 - 01:16:32] I think um it's not a continuing it's
[01:16:30 - 01:16:34] not continuing conversation right so
[01:16:32 - 01:16:37] another end point would be to actually
[01:16:34 - 01:16:39] continue conversation
[01:16:37 - 01:16:41] right so this would be can I actually
[01:16:39 - 01:16:45] check if we have some sort of ID or
[01:16:41 - 01:16:47] anything no so we're definitely not
[01:16:45 - 01:16:49] continuing the conversation Another
[01:16:47 - 01:16:51] endpoint you can have is for starting a
[01:16:49 - 01:16:54] new thread like you know in charge GBT
[01:16:51 - 01:16:55] you have this uh conversations here
[01:16:54 - 01:16:57] right so maybe you want to have
[01:16:55 - 01:17:00] something like that um so this could be
[01:16:57 - 01:17:03] another endpoint but the bare minimum
[01:17:00 - 01:17:05] would be to have this endpoint probably
[01:17:03 - 01:17:08] you also want to have a way to continue
[01:17:05 - 01:17:12] conversation right so we can of course
[01:17:08 - 01:17:14] ask cloud code to implement this and I
[01:17:12 - 01:17:17] don't think it would take a lot of time
[01:17:14 - 01:17:18] for it to implement but I want to focus
[01:17:17 - 01:17:21] on actually like you know finishing
[01:17:18 - 01:17:24] deployment but I think this start
[01:17:21 - 01:17:27] conversation continue
[01:17:24 - 01:17:29] um new session
[01:17:27 - 01:17:30] should be enough like for this sort of
[01:17:29 - 01:17:31] thing.
[01:17:30 - 01:17:33] >> Yeah.
[01:17:31 - 01:17:36] >> Oh it also depends like do you have any
[01:17:33 - 01:17:38] specific application in mind
[01:17:36 - 01:17:41] >> right now? No. I'm
[01:17:38 - 01:17:43] >> like the AP like building API endpoints
[01:17:41 - 01:17:45] is still a little new to me. So like I'm
[01:17:43 - 01:17:48] just trying to think about like what
[01:17:45 - 01:17:50] what kind of endpoints I need to create.
[01:17:48 - 01:17:53] >> Yeah. So I will share the link. There
[01:17:50 - 01:17:56] was a question like share the link to
[01:17:53 - 01:18:00] the notebook. So I just shared
[01:17:56 - 01:18:01] um yeah um I think like for simple chat
[01:18:00 - 01:18:04] applications you don't really need a
[01:18:01 - 01:18:06] lot. Just this ask theme is sufficient.
[01:18:04 - 01:18:09] I don't know actually if it's a
[01:18:06 - 01:18:12] convention if this is how you call them
[01:18:09 - 01:18:13] but it seems reasonable.
[01:18:12 - 01:18:16] Yeah.
[01:18:13 - 01:18:19] >> Okay. Um so um now what I want to do
[01:18:16 - 01:18:21] like of okay this is not ideal as I
[01:18:19 - 01:18:23] mentioned like we are not actually
[01:18:21 - 01:18:24] continuing conversation we are starting
[01:18:23 - 01:18:26] conversation from scratch every time we
[01:18:24 - 01:18:28] send the request. So there is no
[01:18:26 - 01:18:30] continuation. So this is something we
[01:18:28 - 01:18:33] just keep in mind that this is something
[01:18:30 - 01:18:36] we will improve later in the next
[01:18:33 - 01:18:38] versions. So what I want to do now is I
[01:18:36 - 01:18:40] want to package this inside a docker
[01:18:38 - 01:18:42] container right and I want to have one
[01:18:40 - 01:18:44] docker container. I want this docker
[01:18:42 - 01:18:46] container to serve both front end and
[01:18:44 - 01:18:48] back end
[01:18:46 - 01:18:52] and u then we will deploy this
[01:18:48 - 01:18:54] container. So this is what I will say.
[01:18:52 - 01:18:56] Uh okay right now everything works. So I
[01:18:54 - 01:18:58] want to deploy it and for that I want to
[01:18:56 - 01:19:01] create a docker container. This docker
[01:18:58 - 01:19:03] container should serve both back end and
[01:19:01 - 01:19:05] front end. So uh when we build a docker
[01:19:03 - 01:19:07] container so it should build our front
[01:19:05 - 01:19:10] end application it should package this
[01:19:07 - 01:19:14] and it should insert it inside our front
[01:19:10 - 01:19:15] end uh container. So then the sorry
[01:19:14 - 01:19:19] backend container so the backend
[01:19:15 - 01:19:22] container then will serve uh the built
[01:19:19 - 01:19:22] JavaScript.
[01:19:23 - 01:19:28] Okay. So we want to have only one docker
[01:19:26 - 01:19:29] container. We don't want to have two
[01:19:28 - 01:19:31] separate containers. We don't have a
[01:19:29 - 01:19:34] container for back end and front end.
[01:19:31 - 01:19:37] one is enough for us.
[01:19:34 - 01:19:41] Uh but typically when you have this um
[01:19:37 - 01:19:43] when you develop you have one um server
[01:19:41 - 01:19:45] service running for bit another service
[01:19:43 - 01:19:48] is running for back end. So kind of it's
[01:19:45 - 01:19:51] like two things but instead of that we
[01:19:48 - 01:19:53] only want to have one. So I'll stop this
[01:19:51 - 01:19:58] bit for now.
[01:19:53 - 01:19:58] I think I will also stop this thing.
[01:19:59 - 01:20:04] Yeah. Yeah. So typically in order to
[01:20:01 - 01:20:08] avoid that what uh people do is they
[01:20:04 - 01:20:11] that there is this build step when um
[01:20:08 - 01:20:13] this JavaScript project is turned into u
[01:20:11 - 01:20:17] like an actual files that would be
[01:20:13 - 01:20:20] served with uh like a browser can read
[01:20:17 - 01:20:22] right and then we serve these files
[01:20:20 - 01:20:24] through the back end. So back end is
[01:20:22 - 01:20:27] serving both front end and is making
[01:20:24 - 01:20:30] goals and I think we saw here
[01:20:27 - 01:20:33] um past API like CL code add in this
[01:20:30 - 01:20:36] static directory. So this is actually
[01:20:33 - 01:20:40] what it's uh going to use for serving
[01:20:36 - 01:20:40] this stuff.
[01:20:41 - 01:20:49] So now it's let me check docker image.
[01:20:47 - 01:20:52] Okay. So it's doing it in two stages. So
[01:20:49 - 01:20:55] the first stage is building uh back end
[01:20:52 - 01:20:57] uh building front end sorry and the
[01:20:55 - 01:21:00] second stage is building back end which
[01:20:57 - 01:21:02] makes total sense uh this is how I
[01:21:00 - 01:21:05] actually wanted to do
[01:21:02 - 01:21:08] um so then like we don't really need to
[01:21:05 - 01:21:11] have NodeJS dependencies in our uh back
[01:21:08 - 01:21:13] end right so this is already built um it
[01:21:11 - 01:21:16] has all the files and we just copy these
[01:21:13 - 01:21:20] files here from front end build we put
[01:21:16 - 01:21:25] them into this app static and then our
[01:21:20 - 01:21:27] uh back end our um
[01:21:25 - 01:21:30] how do we call it like fast API will
[01:21:27 - 01:21:32] just simply serve it okay seems
[01:21:30 - 01:21:35] reasonable I don't have any um
[01:21:32 - 01:21:39] objections I must say that this new
[01:21:35 - 01:21:42] cloud us that I use it's um this new
[01:21:39 - 01:21:46] cloud opus uh 4.7 I must say it's pretty
[01:21:42 - 01:21:49] good so I really like uh
[01:21:46 - 01:21:52] for simple things like that I would say
[01:21:49 - 01:21:55] it works really nice like I don't need
[01:21:52 - 01:21:58] to correct it a lot
[01:21:55 - 01:22:00] for codex when I use codex I find myself
[01:21:58 - 01:22:02] correcting it uh still correcting it
[01:22:00 - 01:22:05] quite often more often than for cloud
[01:22:02 - 01:22:07] code but for more complex projects uh
[01:22:05 - 01:22:09] with clot oppus with all this yeah
[01:22:07 - 01:22:13] latest oppos I still need to do this
[01:22:09 - 01:22:15] like when the project gets bigger
[01:22:13 - 01:22:17] they tend to over complicate things
[01:22:15 - 01:22:19] sometimes they get lazy and skip things
[01:22:17 - 01:22:22] but for this simple project. So far it's
[01:22:19 - 01:22:24] really smooth
[01:22:22 - 01:22:27] but probably it's a very typical thing
[01:22:24 - 01:22:30] that um developers have been doing for
[01:22:27 - 01:22:33] quite some time. So it has learned uh
[01:22:30 - 01:22:38] how to do this. Uh what about Gemini
[01:22:33 - 01:22:44] CLI? I haven't extensively used it. So I
[01:22:38 - 01:22:47] don't pay for Gemini access. Uh so um
[01:22:44 - 01:22:50] typically so I tried using Gemini but uh
[01:22:47 - 01:22:52] the usage quarter I have in a free
[01:22:50 - 01:22:54] account is not enough to even finish one
[01:22:52 - 01:22:57] session right so I ask it to build
[01:22:54 - 01:23:01] something and then midway it stops so I
[01:22:57 - 01:23:03] don't I don't know I did use
[01:23:01 - 01:23:06] anti-gravity and I do like anti-gravity

## Window 012: 01:22:31 - 01:30:31

[01:22:33 - 01:22:44] CLI? I haven't extensively used it. So I
[01:22:38 - 01:22:47] don't pay for Gemini access. Uh so um
[01:22:44 - 01:22:50] typically so I tried using Gemini but uh
[01:22:47 - 01:22:52] the usage quarter I have in a free
[01:22:50 - 01:22:54] account is not enough to even finish one
[01:22:52 - 01:22:57] session right so I ask it to build
[01:22:54 - 01:23:01] something and then midway it stops so I
[01:22:57 - 01:23:03] don't I don't know I did use
[01:23:01 - 01:23:06] anti-gravity and I do like anti-gravity
[01:23:03 - 01:23:09] so in anti-gravity uh I see that the
[01:23:06 - 01:23:11] Gemini models are pretty good but
[01:23:09 - 01:23:13] anti-gravity is It just gives you a
[01:23:11 - 01:23:16] little bit the feeling you get is a
[01:23:13 - 01:23:18] little bit different from terminal. But
[01:23:16 - 01:23:22] if you like it, I think anti-gravity is
[01:23:18 - 01:23:24] a really good um uh tool. Yeah, Carlos,
[01:23:22 - 01:23:26] what's up?
[01:23:24 - 01:23:29] >> Hi, Alex. I was just wondering about the
[01:23:26 - 01:23:32] Docker step that you said basically that
[01:23:29 - 01:23:35] we have we don't want to have any NodeJS
[01:23:32 - 01:23:37] dependencies in the back end. Um, how
[01:23:35 - 01:23:39] did we actually ensure that the back end
[01:23:37 - 01:23:42] starts running once the front end is
[01:23:39 - 01:23:45] done if we don't even have
[01:23:42 - 01:23:48] uh a compose file?
[01:23:45 - 01:23:51] >> Yeah. Um, so uh we don't need to do
[01:23:48 - 01:23:53] this. We don't have a compost file here.
[01:23:51 - 01:23:56] So we have the first stage. So let me do
[01:23:53 - 01:24:00] docker uh build actually
[01:23:56 - 01:24:03] docker build minus t. How do you call
[01:24:00 - 01:24:05] it? and to end
[01:24:03 - 01:24:07] workshop.
[01:24:05 - 01:24:09] So right now it's doing ah we already
[01:24:07 - 01:24:11] did this. So you see first it's running
[01:24:09 - 01:24:16] stage number one. It's building stage
[01:24:11 - 01:24:16] number one. So it builds.
[01:24:17 - 01:24:23] Okay. Sorry I'm confused. Yeah. Front
[01:24:20 - 01:24:23] end builder.
[01:24:24 - 01:24:30] I'm just trying to understand the order.
[01:24:26 - 01:24:32] Anyways um so what is happening is first
[01:24:30 - 01:24:36] it builds this. So this is stage number
[01:24:32 - 01:24:38] one. First it builds this and only after
[01:24:36 - 01:24:41] this thing is finished
[01:24:38 - 01:24:44] it builds this. Right? So we don't have
[01:24:41 - 01:24:46] compose we don't have two containers
[01:24:44 - 01:24:48] running at the same time. This is
[01:24:46 - 01:24:52] happening at the build time. So I'm not
[01:24:48 - 01:24:55] serving anything yet. So I first I built
[01:24:52 - 01:24:57] this but as a part of this I built first
[01:24:55 - 01:25:01] stage number one and then stage number
[01:24:57 - 01:25:03] two and when I built stage number one uh
[01:25:01 - 01:25:05] the result of this thing is a bunch of
[01:25:03 - 01:25:09] JavaScript files or maybe just one
[01:25:05 - 01:25:14] JavaScript file. So we have this
[01:25:09 - 01:25:18] inside this app.ist here. So when I run
[01:25:14 - 01:25:22] npm build, npm run build, it it creates
[01:25:18 - 01:25:24] this uh uh slash
[01:25:22 - 01:25:26] app
[01:25:24 - 01:25:29] dist folder, right?
[01:25:26 - 01:25:31] And then this folder is copied into
[01:25:29 - 01:25:36] static, right? So these are two separate
[01:25:31 - 01:25:37] steps. And when we run compost,
[01:25:36 - 01:25:40] compose
[01:25:37 - 01:25:43] runs only this. So here the front end is
[01:25:40 - 01:25:45] already built. So we don't that's why we
[01:25:43 - 01:25:47] don't need to think uh so don't think
[01:25:45 - 01:25:50] about this as two separate containers
[01:25:47 - 01:25:54] think about this as first we run this we
[01:25:50 - 01:25:56] build these things so now they are in a
[01:25:54 - 01:26:00] folder and we just take this folder and
[01:25:56 - 01:26:01] copy it to our uh backend container does
[01:26:00 - 01:26:03] make sense
[01:26:01 - 01:26:05] >> yeah totally thanks first time I see it
[01:26:03 - 01:26:08] but it's cool thanks
[01:26:05 - 01:26:11] >> it is cool yeah because it allows us to
[01:26:08 - 01:26:14] actually not have NodeJS dependency here
[01:26:11 - 01:26:16] cuz otherwise we would need to have uh
[01:26:14 - 01:26:20] install Node.js here, build it and then
[01:26:16 - 01:26:22] use it, right? But here we create our
[01:26:20 - 01:26:24] throwaway container, right? We build it
[01:26:22 - 01:26:26] there and okay, we only need one part
[01:26:24 - 01:26:29] there, we can throw away the rest. It's
[01:26:26 - 01:26:31] very it's very nice pattern or I say
[01:26:29 - 01:26:37] approach.
[01:26:31 - 01:26:41] Okay, so it's uh we have built it. So um
[01:26:37 - 01:26:45] make docker run. Okay. So, it's helpful
[01:26:41 - 01:26:48] like I don't even need to ask it to uh
[01:26:45 - 01:26:51] add Docker target or make targets cuz it
[01:26:48 - 01:26:54] already knows I want to have them
[01:26:51 - 01:26:57] probably. That's why it
[01:26:54 - 01:27:01] Yeah. Oh, and by the way, so it also
[01:26:57 - 01:27:07] used my N file. How nice.
[01:27:01 - 01:27:09] So, let's see. Should be local host.
[01:27:07 - 01:27:11] M
[01:27:09 - 01:27:17] I just discovered
[01:27:11 - 01:27:17] the course. Can I join? No.
[01:27:20 - 01:27:24] Does it work?
[01:27:28 - 01:27:32] So nothing is happening.
[01:27:33 - 01:27:38] So let me reload it. So what I want to
[01:27:36 - 01:27:42] see here in network some activity that
[01:27:38 - 01:27:47] okay it sent the request um
[01:27:42 - 01:27:50] can I join the course now
[01:27:47 - 01:27:50] stream okay
[01:27:53 - 01:28:00] but nothing is even stream thinking
[01:27:56 - 01:28:00] iteration number one
[01:28:02 - 01:28:06] okay I'll just tell
[01:28:05 - 01:28:08] Uh
[01:28:06 - 01:28:12] okay.
[01:28:08 - 01:28:12] So it was not able to
[01:28:13 - 01:28:17] just this I'll just copy it
[01:28:18 - 01:28:22] but it will figure it out.
[01:28:23 - 01:28:28] So the the problem is that uh um it
[01:28:26 - 01:28:31] couldn't get the API key from the
[01:28:28 - 01:28:31] apparently.
[01:28:32 - 01:28:37] So,
[01:28:34 - 01:28:39] incorrect key. Um,
[01:28:37 - 01:28:42] uh, the key actually works cuz we were
[01:28:39 - 01:28:45] able to to uh do this before, but when I
[01:28:42 - 01:28:48] run it inside Docker, it couldn't. So, I
[01:28:45 - 01:28:51] think the problem is with how we
[01:28:48 - 01:28:56] propagate the key from our uh from our
[01:28:51 - 01:28:57] host machine to Docker to the image.
[01:28:56 - 01:29:01] I should have saved to the container,
[01:28:57 - 01:29:01] but it doesn't matter.
[01:29:15 - 01:29:20] Okay. I had no idea that Docker parses
[01:29:17 - 01:29:22] it differently and we actually have uh
[01:29:20 - 01:29:24] quotes.
[01:29:22 - 01:29:26] I have no idea. I had no idea about
[01:29:24 - 01:29:30] that.
[01:29:26 - 01:29:30] Okay, so it removed quotes.
[01:29:31 - 01:29:34] Okay.
[01:29:34 - 01:29:38] So, let me Oops.
[01:29:39 - 01:29:43] So, made docker build.
[01:29:44 - 01:29:49] Now, my make docker run.
[01:29:47 - 01:29:52] Actually, I didn't even need to rebuild
[01:29:49 - 01:29:53] it, right? Cuz um and the end file
[01:29:52 - 01:29:57] changed.
[01:29:53 - 01:29:57] Nothing inside changed.
[01:29:57 - 01:30:01] I join the course.
[01:30:04 - 01:30:10] Okay, it's working. Cool.
[01:30:08 - 01:30:12] >> And some of them mythos have really made
[01:30:10 - 01:30:14] a lot of headlines and I think a lot of
[01:30:12 - 01:30:18] a lot more fear and I'm wondering what
[01:30:14 - 01:30:18] you guys claw.
[01:30:18 - 01:30:25] >> Um, was it a question or I'm sorry I
[01:30:21 - 01:30:25] think I muted you.
[01:30:27 - 01:30:31] Sorry, like because it was I didn't
[01:30:29 - 01:30:33] understand was it a question or you
[01:30:31 - 01:30:37] accidentally unmuted yourself and it was

## Window 013: 01:30:01 - 01:38:01

[01:30:04 - 01:30:10] Okay, it's working. Cool.
[01:30:08 - 01:30:12] >> And some of them mythos have really made
[01:30:10 - 01:30:14] a lot of headlines and I think a lot of
[01:30:12 - 01:30:18] a lot more fear and I'm wondering what
[01:30:14 - 01:30:18] you guys claw.
[01:30:18 - 01:30:25] >> Um, was it a question or I'm sorry I
[01:30:21 - 01:30:25] think I muted you.
[01:30:27 - 01:30:31] Sorry, like because it was I didn't
[01:30:29 - 01:30:33] understand was it a question or you
[01:30:31 - 01:30:37] accidentally unmuted yourself and it was
[01:30:33 - 01:30:37] something else. Um
[01:30:38 - 01:30:41] but yeah, feel free to unmute yourself
[01:30:40 - 01:30:45] and then
[01:30:41 - 01:30:45] ask it again. I'm sorry.
[01:30:52 - 01:30:56] Okay. Um
[01:30:56 - 01:31:00] so this thing is working. So we have our
[01:30:58 - 01:31:02] docker container working. So what I want
[01:31:00 - 01:31:05] to do next is uh let me check how much
[01:31:02 - 01:31:07] time we have cuz I also wanted to cover
[01:31:05 - 01:31:10] vector databases. I think it was in the
[01:31:07 - 01:31:11] title for this workshop. Um let's see if
[01:31:10 - 01:31:15] we have energy to actually cover that
[01:31:11 - 01:31:18] too. Uh but um let's now deploy it.
[01:31:15 - 01:31:22] So we have our docker container and this
[01:31:18 - 01:31:28] docker container works and uh now I want
[01:31:22 - 01:31:32] to deploy it. So I now want to deploy
[01:31:28 - 01:31:34] it. What are the best options? So it
[01:31:32 - 01:31:38] will probably recommend something like
[01:31:34 - 01:31:41] render or uh fly IO.
[01:31:38 - 01:31:41] Both are good options.
[01:31:48 - 01:31:55] by railway render even simpler.
[01:31:53 - 01:31:57] Um
[01:31:55 - 01:31:59] so lambda is actually also pretty
[01:31:57 - 01:32:01] interesting right but since we already
[01:31:59 - 01:32:05] have a docker container
[01:32:01 - 01:32:07] uh yeah it also recommended hner so
[01:32:05 - 01:32:11] railway is good okay Ian uh so then
[01:32:07 - 01:32:13] let's go with railway
[01:32:11 - 01:32:16] let's
[01:32:13 - 01:32:18] go with railway I don't think I ever
[01:32:16 - 01:32:21] used railway actually is it not the same
[01:32:18 - 01:32:24] as render so I know render I think I use
[01:32:21 - 01:32:26] it once or twice the the same services
[01:32:24 - 01:32:28] or not.
[01:32:26 - 01:32:31] Uh render cold start issue. How to fix
[01:32:28 - 01:32:33] it? Um pay for it. Like if you pay then
[01:32:31 - 01:32:36] you don't have this issue I think like
[01:32:33 - 01:32:41] but if um if you're on a free account
[01:32:36 - 01:32:41] then you will have cold start issue.
[01:32:44 - 01:32:52] Okay. Railway inject support
[01:32:48 - 01:32:52] code not so much.
[01:32:53 - 01:33:00] Okay. Railway CLI.
[01:32:57 - 01:33:04] Let's Oops.
[01:33:00 - 01:33:04] Let's use CLI.
[01:33:09 - 01:33:15] Not installed. Can you please install
[01:33:13 - 01:33:17] it?
[01:33:15 - 01:33:21] I mean I could have technically just you
[01:33:17 - 01:33:21] know copy this thing but
[01:33:23 - 01:33:30] like since I can just ask it politely to
[01:33:25 - 01:33:32] do this why not right railway login. So,
[01:33:30 - 01:33:36] I'll need to do this. And since I'm
[01:33:32 - 01:33:36] running this from a remote computer,
[01:33:37 - 01:33:41] uh, okay.
[01:33:42 - 01:33:47] I hope I will not be sharing any
[01:33:48 - 01:33:53] uh any private keys accidentally.
[01:34:00 - 01:34:03] I agree.
[01:34:06 - 01:34:09] So
[01:34:12 - 01:34:17] yeah, I will not going to
[01:34:15 - 01:34:20] m crypto
[01:34:17 - 01:34:22] torrent aggregators. Yeah, I will not
[01:34:20 - 01:34:24] deploy any of that.
[01:34:22 - 01:34:27] I hope my agent will also not deploy
[01:34:24 - 01:34:30] that. Okay, so now uh I need to run this
[01:34:27 - 01:34:30] thing again.
[01:34:34 - 01:34:40] Okay. Authorize
[01:34:36 - 01:34:42] device authorized. Cool.
[01:34:40 - 01:34:44] Um,
[01:34:42 - 01:34:46] so this is a toy project, right? So
[01:34:44 - 01:34:49] that's why like I just give access to
[01:34:46 - 01:34:52] cloud code for that. Um, in reality
[01:34:49 - 01:34:55] probably so on this server that I have
[01:34:52 - 01:34:57] in Hner, I don't keep AWS credentials.
[01:34:55 - 01:34:59] All I need to do if I want to do
[01:34:57 - 01:35:01] something with AWS, I will always do it
[01:34:59 - 01:35:05] from my computer. So I want to be
[01:35:01 - 01:35:07] careful with what I do. Um so I try to
[01:35:05 - 01:35:10] minimize like I had an accident recently
[01:35:07 - 01:35:12] where um with help of cloud code I
[01:35:10 - 01:35:16] deleted the production database. So I
[01:35:12 - 01:35:19] try to uh avoid giving cloud code
[01:35:16 - 01:35:22] sensitive uh access to things that it
[01:35:19 - 01:35:25] can destroy. Right? So ideally uh maybe
[01:35:22 - 01:35:28] like if you're if you're doing some
[01:35:25 - 01:35:30] production stuff maybe um like you
[01:35:28 - 01:35:34] shouldn't really let your agent do this
[01:35:30 - 01:35:37] kind of stuff. But that said um we have
[01:35:34 - 01:35:42] already given it access so it's fine.
[01:35:37 - 01:35:42] Just a disclaimer just keep it in mind.
[01:35:45 - 01:35:50] So we're not deploying anything critical
[01:35:47 - 01:35:52] right now. Um and as we are learning how
[01:35:50 - 01:35:54] to actually do these things, I think
[01:35:52 - 01:35:56] it's fine to plate edge and control it.
[01:35:54 - 01:35:59] Um but I would actually you know try to
[01:35:56 - 01:36:01] learn try to document it somewhere. So
[01:35:59 - 01:36:03] when I do it not for a deaf environment
[01:36:01 - 01:36:05] but for production environment I
[01:36:03 - 01:36:09] actually do it myself not I don't rely
[01:36:05 - 01:36:09] on agent for doing this.
[01:36:09 - 01:36:17] Um and actually right now I will ask it
[01:36:11 - 01:36:20] to document it. uh please uh document
[01:36:17 - 01:36:23] the deployment
[01:36:20 - 01:36:28] process into deploy. Let's create a
[01:36:23 - 01:36:28] folder and do deploy.
[01:36:29 - 01:36:35] Um I'll I'll send this when it finishes,
[01:36:35 - 01:36:40] but it seems simple enough, right? So
[01:36:38 - 01:36:43] initialize a project
[01:36:40 - 01:36:49] then do railway app
[01:36:43 - 01:36:51] and is that it? Oops. Seems very simple.
[01:36:49 - 01:36:52] Uh I have a question about the back end
[01:36:51 - 01:36:55] for this app. There are so many
[01:36:52 - 01:36:57] frameworks coming out um which work as
[01:36:55 - 01:36:59] hardness for LM applications providing
[01:36:57 - 01:37:02] memory tool calls. Is there any benefits
[01:36:59 - 01:37:04] to use any frameworks over uh OpenAI API
[01:37:02 - 01:37:08] wrappers? So for this particular project
[01:37:04 - 01:37:13] I wanted to keep things simple. Um so in
[01:37:08 - 01:37:16] many cases um like something like uh
[01:37:13 - 01:37:18] pedantic AI is sufficient right so this
[01:37:16 - 01:37:21] is my favorite framework so I would use
[01:37:18 - 01:37:23] that I just wanted to make things
[01:37:21 - 01:37:26] simpler because when you don't use a
[01:37:23 - 01:37:29] framework you have a lot of freedom of
[01:37:26 - 01:37:31] what you can do because right now
[01:37:29 - 01:37:34] because we don't use any framework we
[01:37:31 - 01:37:38] can insert uh like we and have this uh
[01:37:34 - 01:37:40] wait this
[01:37:38 - 01:37:44] renderer like this I don't know why it's
[01:37:40 - 01:37:47] called renderer uh but like this handler
[01:37:44 - 01:37:50] right and it can emit all these events
[01:37:47 - 01:37:52] right we can add these things in our
[01:37:50 - 01:37:55] agent at any
[01:37:52 - 01:37:57] point and if you use a framework this
[01:37:55 - 01:37:59] could be difficult with pentic I think
[01:37:57 - 01:38:02] it's possible but the code you will need
[01:37:59 - 01:38:04] to write is

## Window 014: 01:37:31 - 01:45:31

[01:37:34 - 01:37:40] wait this
[01:37:38 - 01:37:44] renderer like this I don't know why it's
[01:37:40 - 01:37:47] called renderer uh but like this handler
[01:37:44 - 01:37:50] right and it can emit all these events
[01:37:47 - 01:37:52] right we can add these things in our
[01:37:50 - 01:37:55] agent at any
[01:37:52 - 01:37:57] point and if you use a framework this
[01:37:55 - 01:37:59] could be difficult with pentic I think
[01:37:57 - 01:38:02] it's possible but the code you will need
[01:37:59 - 01:38:04] to write is
[01:38:02 - 01:38:07] like it becomes complicated right so for
[01:38:04 - 01:38:10] custom stuff eventually You might al
[01:38:07 - 01:38:15] also want to drop um any framework and
[01:38:10 - 01:38:16] just do it yourself. Um yeah
[01:38:15 - 01:38:19] uh David yes you will get the recording
[01:38:16 - 01:38:23] of this session it will be shared in
[01:38:19 - 01:38:24] Slack uh also along with the recording I
[01:38:23 - 01:38:26] want to create by like when the
[01:38:24 - 01:38:28] recording is already there. So what I
[01:38:26 - 01:38:30] want to do is I want to create an actual
[01:38:28 - 01:38:33] document that describes all the steps of
[01:38:30 - 01:38:38] what we have done.
[01:38:33 - 01:38:41] uh but for me it's also like an um
[01:38:38 - 01:38:43] how to say like a kind of improvisation
[01:38:41 - 01:38:45] right so that's why at the end yes we
[01:38:43 - 01:38:48] will have some written materials but I
[01:38:45 - 01:38:52] think for me um I hope you agree the
[01:38:48 - 01:38:54] value is also having these discussions
[01:38:52 - 01:38:59] okay let's see what it's doing ah it
[01:38:54 - 01:38:59] deployed in the meantime
[01:38:59 - 01:39:03] application failed to respond
[01:39:04 - 01:39:09] So
[01:39:05 - 01:39:11] right now I have oops sorry
[01:39:09 - 01:39:13] I have this thing here please document
[01:39:11 - 01:39:15] the deployment. So I don't want to send
[01:39:13 - 01:39:19] this request right now. I am going to
[01:39:15 - 01:39:21] stash it. I will use Ctrl S.
[01:39:19 - 01:39:23] So this is something okay it says it's
[01:39:21 - 01:39:25] actually good.
[01:39:23 - 01:39:28] Maybe just needed some time to do this.
[01:39:25 - 01:39:30] Yeah Carlos what's up? wondering if you
[01:39:28 - 01:39:33] could maybe also share basic configs for
[01:39:30 - 01:39:38] heads um
[01:39:33 - 01:39:41] um yeah instances in the in the repo
[01:39:38 - 01:39:43] later. So if anyone wants to try out um
[01:39:41 - 01:39:45] HNA maybe you could just say what are
[01:39:43 - 01:39:46] the basic configs we would need.
[01:39:45 - 01:39:48] >> Yeah.
[01:39:46 - 01:39:51] >> And that would be awesome. And are there
[01:39:48 - 01:39:53] any other security aspects that you
[01:39:51 - 01:39:55] would recommend looking into when
[01:39:53 - 01:39:57] deploying besides what you've just
[01:39:55 - 01:39:59] explained with the with the agents and
[01:39:57 - 01:40:00] everything, but are there any other
[01:39:59 - 01:40:03] aspects that should be taken into
[01:40:00 - 01:40:06] account when deploying the stuff
[01:40:03 - 01:40:08] >> when deploying? Um, so we should you
[01:40:06 - 01:40:13] should do it through through CI/CD. The
[01:40:08 - 01:40:16] setup I usually have is uh
[01:40:13 - 01:40:18] well the setup you ideally in the ideal
[01:40:16 - 01:40:21] world the setup you should have is let's
[01:40:18 - 01:40:24] say you use AWS for deployment right. So
[01:40:21 - 01:40:25] then you have deaf account and you have
[01:40:24 - 01:40:28] pro account. So these accounts are
[01:40:25 - 01:40:30] completely independent. Then you manage
[01:40:28 - 01:40:33] your state with terraform
[01:40:30 - 01:40:36] right. So you have terraform state here
[01:40:33 - 01:40:38] and terraform state here.
[01:40:36 - 01:40:40] Um so you provision your environment
[01:40:38 - 01:40:42] with this terraform like here let's say
[01:40:40 - 01:40:43] we use render it's fine like but somehow
[01:40:42 - 01:40:48] we probably need to have two separate
[01:40:43 - 01:40:53] environments right and then um here uh
[01:40:48 - 01:40:55] when we do uh g push what we should do
[01:40:53 - 01:41:00] is we should have a cicd job that
[01:40:55 - 01:41:03] automatically uh deploys to uh dev right
[01:41:00 - 01:41:07] so we just push to g it runs tests run
[01:41:03 - 01:41:09] tests and then uh it deploys to DV right
[01:41:07 - 01:41:11] so every time we push it automatically
[01:41:09 - 01:41:15] deploys there
[01:41:11 - 01:41:19] here we have um also we have state here
[01:41:15 - 01:41:21] and we have okay here deploy to dev
[01:41:19 - 01:41:23] version right
[01:41:21 - 01:41:25] dev version
[01:41:23 - 01:41:27] uh here we don't want to do this on
[01:41:25 - 01:41:30] every push right so here we want to do
[01:41:27 - 01:41:33] this manual manual deploy so when you
[01:41:30 - 01:41:35] think like okay you deploy to dev you
[01:41:33 - 01:41:40] went there you checked the things
[01:41:35 - 01:41:41] And uh then you manually uh say okay
[01:41:40 - 01:41:43] like I'm satisfied with the version I
[01:41:41 - 01:41:46] have on def let's promote the deaf
[01:41:43 - 01:41:50] version to production. So this is how or
[01:41:46 - 01:41:51] maybe I should call it manual uh
[01:41:50 - 01:41:54] promotion.
[01:41:51 - 01:41:56] So this is how I think there are people
[01:41:54 - 01:41:57] uh who are more experienced with me
[01:41:56 - 01:41:58] right now on this call. I don't know
[01:41:57 - 01:42:02] what you say. I know if you're here
[01:41:58 - 01:42:04] maybe you correct me um or maybe he left
[01:42:02 - 01:42:08] already. Um
[01:42:04 - 01:42:10] but um this is the setup I would this is
[01:42:08 - 01:42:11] setup you would typically have like in
[01:42:10 - 01:42:14] companies
[01:42:11 - 01:42:19] um with two complete AWS accounts right
[01:42:14 - 01:42:22] um so the way I implement it is uh like
[01:42:19 - 01:42:26] for example if I take data talks club
[01:42:22 - 01:42:26] sorry this one
[01:42:26 - 01:42:34] um yeah so we have uh actions so every
[01:42:29 - 01:42:38] time I push something to um like to this
[01:42:34 - 01:42:42] repo. It gets automatically deployed to
[01:42:38 - 01:42:43] this website, right? And then I can go
[01:42:42 - 01:42:46] here, I can check that things these
[01:42:43 - 01:42:48] things work and then I can go here to
[01:42:46 - 01:42:50] manual production deployment and I can
[01:42:48 - 01:42:53] run workflow. I say okay, I do confirm
[01:42:50 - 01:42:55] that and I rank this run this workflow.
[01:42:53 - 01:42:58] So this is how I do this except here in
[01:42:55 - 01:43:00] this case I don't have two separate
[01:42:58 - 01:43:02] accounts right because this is a smaller
[01:43:00 - 01:43:04] project and then I don't want to pay for
[01:43:02 - 01:43:07] two accounts and these two deaf and pro
[01:43:04 - 01:43:08] they share the same database instance
[01:43:07 - 01:43:11] right so in ideal world you probably
[01:43:08 - 01:43:14] want to have it differently but the
[01:43:11 - 01:43:17] point here is you don't let your agent
[01:43:14 - 01:43:20] do this you do it through CI/CD right so
[01:43:17 - 01:43:22] first you want so first when you learn
[01:43:20 - 01:43:24] you of course let your agent do this you
[01:43:22 - 01:43:26] experiment with with these things but
[01:43:24 - 01:43:29] then at some point you say okay now
[01:43:26 - 01:43:32] let's create a CI/CD job for deployment
[01:43:29 - 01:43:34] and then you stop doing this manually so
[01:43:32 - 01:43:37] the only manual thing you need to do is
[01:43:34 - 01:43:38] this manual promotion right so this is
[01:43:37 - 01:43:40] how you should do this and then the
[01:43:38 - 01:43:43] agent simply will not have access to
[01:43:40 - 01:43:47] this thing right unless you give it
[01:43:43 - 01:43:49] access so here uh when it installs uh
[01:43:47 - 01:43:53] all the stuff there we can just you know
[01:43:49 - 01:43:56] remove our u config fix from here. So it
[01:43:53 - 01:43:58] will not be able to like let's say it
[01:43:56 - 01:44:02] thinks like h how about I try to go and
[01:43:58 - 01:44:04] update our production um production
[01:44:02 - 01:44:05] version it will not be able to do this
[01:44:04 - 01:44:07] because it will not have access. The
[01:44:05 - 01:44:09] only way you can do this is through
[01:44:07 - 01:44:11] CI/CD
[01:44:09 - 01:44:13] right and the same with Terraform. With
[01:44:11 - 01:44:15] Terraform there is a thing called
[01:44:13 - 01:44:16] Atlantis.
[01:44:15 - 01:44:19] Atlantis is like a thing on top of
[01:44:16 - 01:44:22] Terraform that lets you kind of follow
[01:44:19 - 01:44:27] the same process, right? So you push
[01:44:22 - 01:44:29] your thing to um to g then it in
[01:44:27 - 01:44:31] atlantis you see the plan or in g you
[01:44:29 - 01:44:34] see the plan you say okay I approve the
[01:44:31 - 01:44:36] plan and then only then it applies the
[01:44:34 - 01:44:39] terraform state but this like for simple
[01:44:36 - 01:44:41] projects like we have here it could be
[01:44:39 - 01:44:45] an overkill right so I don't think you
[01:44:41 - 01:44:48] actually need to go all the way um to do
[01:44:45 - 01:44:50] this but um like actually having a setup
[01:44:48 - 01:44:52] like
[01:44:50 - 01:44:54] It's not very complicated at the end
[01:44:52 - 01:44:58] like okay let's let's not think about
[01:44:54 - 01:45:00] two accounts we can have just two uh
[01:44:58 - 01:45:02] what did we use render two render
[01:45:00 - 01:45:05] projects
[01:45:02 - 01:45:07] right so could a railway sorry so one
[01:45:05 - 01:45:11] railway could be FAQ agent def and
[01:45:07 - 01:45:13] another one could be FAQ agent pro right
[01:45:11 - 01:45:16] so it's just two different projects we
[01:45:13 - 01:45:18] would need to pay I don't know $5 per
[01:45:16 - 01:45:22] each but then you will have this extra
[01:45:18 - 01:45:29] protection layer and creating CIC CD
[01:45:22 - 01:45:32] simple I can say hey uh let's create CD
[01:45:29 - 01:45:35] for

## Window 015: 01:45:01 - 01:53:01

[01:45:02 - 01:45:07] right so could a railway sorry so one
[01:45:05 - 01:45:11] railway could be FAQ agent def and
[01:45:07 - 01:45:13] another one could be FAQ agent pro right
[01:45:11 - 01:45:16] so it's just two different projects we
[01:45:13 - 01:45:18] would need to pay I don't know $5 per
[01:45:16 - 01:45:22] each but then you will have this extra
[01:45:18 - 01:45:29] protection layer and creating CIC CD
[01:45:22 - 01:45:32] simple I can say hey uh let's create CD
[01:45:29 - 01:45:35] for
[01:45:32 - 01:45:37] deploying it
[01:45:35 - 01:45:40] we don't have tests here this is
[01:45:37 - 01:45:42] something we definitely need to uh take
[01:45:40 - 01:45:45] care of we need to create tests right so
[01:45:42 - 01:45:47] and then we first in our CI uh our
[01:45:45 - 01:45:50] GitHub uh GitHub actions we first run
[01:45:47 - 01:45:52] tests if test pass only then we deploy
[01:45:50 - 01:45:56] of course and the ideally we should have
[01:45:52 - 01:45:59] two two kind of tests first unit tests
[01:45:56 - 01:46:02] that run fast and we run it when we uh
[01:45:59 - 01:46:04] do things locally then we also need to
[01:46:02 - 01:46:05] have integration tests integration tests
[01:46:04 - 01:46:08] are typically tests that you don't
[01:46:05 - 01:46:11] always run locally but you always run
[01:46:08 - 01:46:12] them on on CI
[01:46:11 - 01:46:17] okay so this is what it's doing right
[01:46:12 - 01:46:17] now is creating this um CI flow
[01:46:21 - 01:46:26] Um, how do I do this?
[01:46:29 - 01:46:33] I don't think we will have time now to
[01:46:31 - 01:46:36] uh do vector database. Maybe it could be
[01:46:33 - 01:46:39] like a followup. So there we take this
[01:46:36 - 01:46:43] thing and we so the plan I had for this
[01:46:39 - 01:46:45] one was to create um an account in
[01:46:43 - 01:46:48] quadrant cloud and then we would just
[01:46:45 - 01:46:50] need to put data to quadrant cloud and
[01:46:48 - 01:46:52] use it from uh this application but I
[01:46:50 - 01:46:54] think for today it's enough information
[01:46:52 - 01:46:56] right so we can uh we can continue on
[01:46:54 - 01:46:59] some other day
[01:46:56 - 01:47:01] okay but let's finish with this CI/CD
[01:46:59 - 01:47:03] stuff GitHub is installed you're
[01:47:01 - 01:47:06] authenticated uh open railway and create
[01:47:03 - 01:47:06] token
[01:47:06 - 01:47:12] Okay. My token uh CIC CD.
[01:47:12 - 01:47:15] Okay.
[01:47:15 - 01:47:20] Actually, what I'm doing is like maybe
[01:47:17 - 01:47:23] you shouldn't uh just copy it to uh
[01:47:20 - 01:47:26] GitHub like for sorry not take this
[01:47:23 - 01:47:30] token and copy it to your agent, right?
[01:47:26 - 01:47:33] Cuz this information is sent to Entropic
[01:47:30 - 01:47:36] and who knows what can happen with this.
[01:47:33 - 01:47:38] So maybe if they're training uh their
[01:47:36 - 01:47:42] models on our data, this token can
[01:47:38 - 01:47:44] appear eventually in somebody's code,
[01:47:42 - 01:47:45] right? So we don't want to do this right
[01:47:44 - 01:47:49] now. I'm just simplifying because I'm
[01:47:45 - 01:47:53] going to um disable this token anyways
[01:47:49 - 01:47:57] after this session. Um but um for real
[01:47:53 - 01:47:57] production environment. So
[01:47:58 - 01:48:04] okay. Yeah, it actually said this token
[01:48:01 - 01:48:10] is now in our conversation transcript.
[01:48:04 - 01:48:15] Uh uh yeah, so it says don't do this.
[01:48:10 - 01:48:16] Uh treat compromised. Can
[01:48:15 - 01:48:21] can
[01:48:16 - 01:48:21] you please use it?
[01:48:23 - 01:48:27] Don't paste it here. Okay. I think uh
[01:48:25 - 01:48:30] what entropic is doing is it's educating
[01:48:27 - 01:48:33] it is educating people to uh not do this
[01:48:30 - 01:48:35] kind of stuff that I did right now. I
[01:48:33 - 01:48:38] must admit it was pretty sloppy of me to
[01:48:35 - 01:48:41] to do this kind of stuff. Um but it just
[01:48:38 - 01:48:43] simplifies things so it's not like um a
[01:48:41 - 01:48:46] very important thing. So for important
[01:48:43 - 01:48:48] project I would never do this
[01:48:46 - 01:48:50] and it has a point to say it's now in
[01:48:48 - 01:48:51] conversation transcript and also in
[01:48:50 - 01:48:54] telemetry.
[01:48:51 - 01:48:57] So it can be compromised.
[01:48:54 - 01:49:00] Um so
[01:48:57 - 01:49:04] while it's doing this um Carlos your
[01:49:00 - 01:49:08] other thing was about headner.
[01:49:04 - 01:49:13] >> So what I will do now is um I already
[01:49:08 - 01:49:16] have all the instructions for this.
[01:49:13 - 01:49:18] So uh
[01:49:16 - 01:49:23] yeah this one.
[01:49:18 - 01:49:25] So um the reason I did this is because I
[01:49:23 - 01:49:28] wanted to make it very reproducible cuz
[01:49:25 - 01:49:30] I'm running agents many agents on my
[01:49:28 - 01:49:32] computer
[01:49:30 - 01:49:36] and I'm running these agents in this
[01:49:32 - 01:49:39] bypass permissions on which is dangerous
[01:49:36 - 01:49:42] right so clude actually warns you saying
[01:49:39 - 01:49:44] hey like you are entering the dangerous
[01:49:42 - 01:49:46] territory you are running like this
[01:49:44 - 01:49:50] dangerous list keep permission thing so
[01:49:46 - 01:49:54] it can happen that um uh rock agent
[01:49:50 - 01:49:59] decides to delete some things, right? I
[01:49:54 - 01:50:00] um am aware of that and I accept u the
[01:49:59 - 01:50:02] responsibility. I take the
[01:50:00 - 01:50:06] responsibility and for these reasons I
[01:50:02 - 01:50:08] created this document. So when things if
[01:50:06 - 01:50:11] things go wrong, not when I hope they
[01:50:08 - 01:50:14] will not, but if things go wrong, I can
[01:50:11 - 01:50:18] actually easily just nuke my entire file
[01:50:14 - 01:50:20] system and recreate it, right? And um
[01:50:18 - 01:50:24] this is what I needed to install. So
[01:50:20 - 01:50:27] probably it will not be complete but um
[01:50:24 - 01:50:29] at least I will get it to a working um
[01:50:27 - 01:50:31] so for example right now when I was
[01:50:29 - 01:50:33] creating this I didn't have Rust
[01:50:31 - 01:50:35] installed now I have a few projects that
[01:50:33 - 01:50:40] are that use Rust. So then I would need
[01:50:35 - 01:50:42] to add these things. Um but yeah so I'll
[01:50:40 - 01:50:45] just share this thing with you.
[01:50:42 - 01:50:47] >> Awesome. Thank you. So for me the idea
[01:50:45 - 01:50:49] is that I want to quickly recreate the
[01:50:47 - 01:50:53] environment. So what I would do is like
[01:50:49 - 01:50:55] let's say in the event uh unlikely event
[01:50:53 - 01:50:57] I hope that I'll need to nuke my file
[01:50:55 - 01:50:59] system and recreate the whole thing from
[01:50:57 - 01:51:03] scratch. What I would do is I would just
[01:50:59 - 01:51:05] add give this G to my agent and say hey
[01:51:03 - 01:51:11] go ahead and recreate this thing please
[01:51:05 - 01:51:11] for me right and uh yeah it will
[01:51:12 - 01:51:17] okay so where do we stop? Um, so yeah,
[01:51:15 - 01:51:20] let's pretend I didn't do it this way.
[01:51:17 - 01:51:22] So let's pretend I didn't um copy it to
[01:51:20 - 01:51:24] the agent.
[01:51:22 - 01:51:28] Workflow failed with invited train
[01:51:24 - 01:51:30] token. The value we used maybe a project
[01:51:28 - 01:51:35] ID rather than token or was rotated
[01:51:30 - 01:51:35] either way time for a fresh one.
[01:51:35 - 01:51:38] Okay,
[01:51:39 - 01:51:47] GitHub. Okay, let's make it right this
[01:51:42 - 01:51:47] way. So, I'm going to copy it.
[01:51:48 - 01:51:51] Um,
[01:51:52 - 01:51:56] but is this correct? Uh, repo.
[01:51:56 - 01:52:04] Is this
[01:51:59 - 01:52:07] oops is this correct repo? Have we
[01:52:04 - 01:52:08] pushed?
[01:52:07 - 01:52:11] And maybe that's why it doesn't work,
[01:52:08 - 01:52:14] right? Because I don't remember us
[01:52:11 - 01:52:16] uh
[01:52:14 - 01:52:18] what is it
[01:52:16 - 01:52:22] agent? I don't remember us actually
[01:52:18 - 01:52:25] pushing any of the code. Oh, okay. I
[01:52:22 - 01:52:29] don't remember but what it actually did.
[01:52:25 - 01:52:29] Cool. Um yeah,
[01:52:30 - 01:52:35] and it's private. Okay.
[01:52:37 - 01:52:42] The fer is pretty about okay.
[01:52:42 - 01:52:50] So um what did we need to do? GitHub
[01:52:45 - 01:52:50] secrets realist token.
[01:52:57 - 01:53:01] Okay, I probably should do this outside
[01:52:59 - 01:53:04] of this chat because I don't remember
[01:53:01 - 01:53:06] how um it works with

## Window 016: 01:52:31 - 01:56:11

[01:52:37 - 01:52:42] The fer is pretty about okay.
[01:52:42 - 01:52:50] So um what did we need to do? GitHub
[01:52:45 - 01:52:50] secrets realist token.
[01:52:57 - 01:53:01] Okay, I probably should do this outside
[01:52:59 - 01:53:04] of this chat because I don't remember
[01:53:01 - 01:53:06] how um it works with
[01:53:04 - 01:53:11] I don't remember how it works with this
[01:53:06 - 01:53:15] bash uh thing inside uh
[01:53:11 - 01:53:15] pasted secret.
[01:53:16 - 01:53:23] Got it.
[01:53:18 - 01:53:23] Okay, I've done that.
[01:53:28 - 01:53:35] Okay, what else? Um, oh no, I've used
[01:53:31 - 01:53:38] 100% of my weekly limit.
[01:53:35 - 01:53:41] I think it will stop working right now.
[01:53:38 - 01:53:41] That's very unfortunate.
[01:53:41 - 01:53:47] But yeah, I think we are almost done,
[01:53:44 - 01:53:49] right? So this thing is working. The
[01:53:47 - 01:53:51] only thing that um I wanted to do is
[01:53:49 - 01:53:57] this ICD. Of course, yes, we wanted to
[01:53:51 - 01:53:57] do uh vector database stuff, but um
[01:53:59 - 01:54:04] Okay, I think
[01:54:01 - 01:54:06] uh I am lucky because Entropic gave some
[01:54:04 - 01:54:08] extra
[01:54:06 - 01:54:13] usage.
[01:54:08 - 01:54:18] Oh, wow. I already spent 30 on that.
[01:54:13 - 01:54:18] Yeah, I need to be careful. Um,
[01:54:18 - 01:54:24] so let's see. Uh, do I need to do
[01:54:21 - 01:54:24] anything here?
[01:54:25 - 01:54:30] It's deploy. Yeah, I think uh for now we
[01:54:28 - 01:54:32] are done. Are there any other questions
[01:54:30 - 01:54:35] before we finish? So I'll think when we
[01:54:32 - 01:54:38] can announce the followup for this one.
[01:54:35 - 01:54:41] Maybe what we can do is we can I'll take
[01:54:38 - 01:54:43] a simplified version. So it will not be
[01:54:41 - 01:54:45] like a continuation. I'll try to make it
[01:54:43 - 01:54:47] standalone. So then for people who did
[01:54:45 - 01:54:49] did not attend this one, it will also
[01:54:47 - 01:54:52] make sense where we focus actually on
[01:54:49 - 01:54:55] like vector databases.
[01:54:52 - 01:55:01] Um yeah and deploying them too.
[01:54:55 - 01:55:01] Okay. Anything before we finish?
[01:55:01 - 01:55:06] Yeah, thanks for all these questions. I
[01:55:03 - 01:55:09] I know it's been uh long.
[01:55:06 - 01:55:11] Um yeah, thanks for sticking around for
[01:55:09 - 01:55:14] quite some time. I hope it was useful.
[01:55:11 - 01:55:17] As always, you can u also like what I
[01:55:14 - 01:55:19] want you to ask is to like if you have
[01:55:17 - 01:55:22] any suggestions maybe some topics that
[01:55:19 - 01:55:24] you're interested in you want to do in a
[01:55:22 - 01:55:26] similar format like when I'm not
[01:55:24 - 01:55:29] necessarily prepared but we explore this
[01:55:26 - 01:55:32] topic together um I like this format it
[01:55:29 - 01:55:34] doesn't require for me a lot of upfront
[01:55:32 - 01:55:36] uh preparation right so if you have some
[01:55:34 - 01:55:39] ideas of what we can explore together in
[01:55:36 - 01:55:42] a similar way uh please share it in
[01:55:39 - 01:55:43] slack and we can do something like
[01:55:42 - 01:55:46] Okay, I'm going to stop sharing my
[01:55:43 - 01:55:49] screen. Um, so right now, uh, I'll need
[01:55:46 - 01:55:51] to take some time to actually
[01:55:49 - 01:55:53] prepare write up. So you will get
[01:55:51 - 01:55:55] recording. You will also get a write up
[01:55:53 - 01:56:00] with that that you can just, you know,
[01:55:55 - 01:56:02] copy paste and do things. Um, yeah. So
[01:56:00 - 01:56:04] thanks a lot. Thanks for your questions.
[01:56:02 - 01:56:06] Um, and I see you around.
[01:56:04 - 01:56:08] >> Thanks a lot.
[01:56:06 - 01:56:11] >> Yeah. Bye everyone.
[01:56:08 - 01:56:11] >> Carlos. Bye.
