# Transcript Context

Source: /Users/valeria/short-video-automation/zoAvc8VU6Qs/full_transcript.json
Duration: 01:28:31
Segments: 1673

Use these windows to mine social post ideas across the full transcript. Ideas may span multiple windows.

## Window 001: 00:00:01 - 00:08:01

[00:00:01 - 00:00:06] Yeah, the Hi everyone. So the idea
[00:00:03 - 00:00:09] behind this thing is um is like it's
[00:00:06 - 00:00:11] freestyle. So um you come with some
[00:00:09 - 00:00:13] problems you want to solve together and
[00:00:11 - 00:00:15] we try to solve it. If you don't have
[00:00:13 - 00:00:17] any problems you want to solve together
[00:00:15 - 00:00:19] then I can come up with something and
[00:00:17 - 00:00:22] then we do this together. So I'm not
[00:00:19 - 00:00:24] prepared uh like I don't have a specific
[00:00:22 - 00:00:28] plan. This is what I mean. So um it's
[00:00:24 - 00:00:31] kind of very raw but also I intend it to
[00:00:28 - 00:00:33] be very interactive where you can say
[00:00:31 - 00:00:36] hey like you can not only change the
[00:00:33 - 00:00:39] course of what we do um but you can also
[00:00:36 - 00:00:42] ask questions and suggest things. So
[00:00:39 - 00:00:45] this is the idea behind this format like
[00:00:42 - 00:00:47] freestyle sessions. I have not I have
[00:00:45 - 00:00:50] never done anything like that before. So
[00:00:47 - 00:00:52] um we will also need to sort of figure
[00:00:50 - 00:00:56] it out like the format and how it's
[00:00:52 - 00:00:59] useful in the in the the way I think
[00:00:56 - 00:01:01] about it. But yeah um so that's why
[00:00:59 - 00:01:03] again I see a few more people joined. So
[00:01:01 - 00:01:05] maybe some of you have some ideas of
[00:01:03 - 00:01:08] what you want to do. Maybe you are
[00:01:05 - 00:01:11] interviewing right now uh for I don't
[00:01:08 - 00:01:13] know AI engineering position and uh you
[00:01:11 - 00:01:15] need to work on a home assignment or
[00:01:13 - 00:01:18] maybe you are thinking what kind of
[00:01:15 - 00:01:19] project you can do um or maybe there's
[00:01:18 - 00:01:22] something else maybe like there is a
[00:01:19 - 00:01:25] personal project you're just starting.
[00:01:22 - 00:01:28] So if you don't have anything we can see
[00:01:25 - 00:01:30] how we can brainstorm and come up with a
[00:01:28 - 00:01:34] problem but if you have something then
[00:01:30 - 00:01:34] we can perhaps discuss it.
[00:01:42 - 00:01:45] >> Hi Alex, this is Carlos.
[00:01:44 - 00:01:48] >> Hi Carlos.
[00:01:45 - 00:01:50] >> So I have actually a problem but I'm not
[00:01:48 - 00:01:53] sure that this would be fitting in this
[00:01:50 - 00:01:55] context. You might recall that I did a
[00:01:53 - 00:01:58] project where I had several agents
[00:01:55 - 00:02:01] running and my problem was that they
[00:01:58 - 00:02:03] actually started to overwrite each
[00:02:01 - 00:02:06] other's counters.
[00:02:03 - 00:02:09] >> So you would have basically a global
[00:02:06 - 00:02:10] variable which would be
[00:02:09 - 00:02:14] tracking
[00:02:10 - 00:02:16] how many tool calls each agent has
[00:02:14 - 00:02:18] >> done until now. And then at some point
[00:02:16 - 00:02:22] because it's a global variable, they
[00:02:18 - 00:02:23] start overwriting each other's counters.
[00:02:22 - 00:02:25] >> So that's something that I'm working on
[00:02:23 - 00:02:27] right now, but I have the impression
[00:02:25 - 00:02:30] that that would be maybe too much for
[00:02:27 - 00:02:31] the moment to to work on. So I was just
[00:02:30 - 00:02:33] wondering maybe you have examples of
[00:02:31 - 00:02:35] what you were thinking of doing. I mean,
[00:02:33 - 00:02:37] you just said you don't have a concrete
[00:02:35 - 00:02:39] plan, but
[00:02:37 - 00:02:41] >> um can you give us like a feeling of
[00:02:39 - 00:02:43] what potentially we could be talking
[00:02:41 - 00:02:47] about? because my my proposal right now
[00:02:43 - 00:02:48] I think is just maybe too too high or
[00:02:47 - 00:02:51] just too complex.
[00:02:48 - 00:02:52] >> Yeah, maybe because for this one it's uh
[00:02:51 - 00:02:54] you're already working on a problem and
[00:02:52 - 00:02:57] then you have some is this code
[00:02:54 - 00:02:58] somewhere available on GitHub.
[00:02:57 - 00:03:01] >> It will be once I refactor it.
[00:02:58 - 00:03:02] >> Ah it will be once cuz uh otherwise we I
[00:03:01 - 00:03:04] could have pulled it and then we could
[00:03:02 - 00:03:08] have looked at this. I I know maybe I
[00:03:04 - 00:03:10] didn't give you um a warning about um
[00:03:08 - 00:03:12] what you should bring into this. Maybe
[00:03:10 - 00:03:14] you would have done this. But what I
[00:03:12 - 00:03:18] would do in this case is try to make
[00:03:14 - 00:03:21] this variable not global and each agent
[00:03:18 - 00:03:25] perhaps could have its own
[00:03:21 - 00:03:29] um instance of an object and then they
[00:03:25 - 00:03:33] would increment only this the
[00:03:29 - 00:03:33] >> um so let me maybe share my screen.
[00:03:34 - 00:03:40] Oops. I want to open Visual Studio Code.
[00:03:42 - 00:03:46] So I don't know I'm just assuming that
[00:03:44 - 00:03:50] how your code can look like right now.
[00:03:46 - 00:03:52] So maybe you have a class agent
[00:03:50 - 00:03:56] and then it's doing something like maybe
[00:03:52 - 00:03:59] you have def run uh code right and then
[00:03:56 - 00:04:02] they uh deal with this variable right
[00:03:59 - 00:04:05] but what you can do instead yes run
[00:04:02 - 00:04:09] self. What you can do instead is you can
[00:04:05 - 00:04:13] have like a local variable
[00:04:09 - 00:04:15] uh where you do something like self
[00:04:13 - 00:04:17] counter
[00:04:15 - 00:04:19] and then they would do something like
[00:04:17 - 00:04:22] self counter plus one right something
[00:04:19 - 00:04:26] like this. So this and if um you have uh
[00:04:22 - 00:04:29] I don't know agent one
[00:04:26 - 00:04:31] and then you have agent two and then
[00:04:29 - 00:04:32] each one would have its own counter.
[00:04:31 - 00:04:33] >> Yes. Yes.
[00:04:32 - 00:04:35] >> Does it make sense?
[00:04:33 - 00:04:37] >> Yes. Yes. Yes. Absolutely.
[00:04:35 - 00:04:39] >> Okay.
[00:04:37 - 00:04:43] Okay. Well, I hope it was helpful. But
[00:04:39 - 00:04:48] um how about we uh brainstorm something.
[00:04:43 - 00:04:51] So uh what I was thinking about is um in
[00:04:48 - 00:04:53] the previous session that we did,
[00:04:51 - 00:04:58] I probably have some code there. Uh let
[00:04:53 - 00:05:00] me try to find it. Uh AI engineering AI
[00:04:58 - 00:05:04] shipping labs. So in the previous
[00:05:00 - 00:05:05] session that we did we um where's
[00:05:04 - 00:05:07] workshops? So we have the workshops from
[00:05:05 - 00:05:11] the previous session. In the previous
[00:05:07 - 00:05:14] session we created um
[00:05:11 - 00:05:17] front end and back end and this was a
[00:05:14 - 00:05:21] fast API application and and then this
[00:05:17 - 00:05:22] application was uh then we packaged it
[00:05:21 - 00:05:24] inside docker and then we deploy
[00:05:22 - 00:05:27] deployed it with uh I think was
[00:05:24 - 00:05:30] surrender or railway some service that
[00:05:27 - 00:05:32] we use right. So in this case, we have
[00:05:30 - 00:05:34] to have a server. We have to have a
[00:05:32 - 00:05:37] Docker container that we deploy
[00:05:34 - 00:05:39] somewhere. And it means that the server
[00:05:37 - 00:05:41] has to be up and running all the time.
[00:05:39 - 00:05:44] And even if we don't use it, if we're on
[00:05:41 - 00:05:48] a paid plan, we still pay for this. And
[00:05:44 - 00:05:51] I thought it would be cool to be able to
[00:05:48 - 00:05:54] uh use something like AWS Lambda to
[00:05:51 - 00:05:58] deploy this thing. So in case of AWS
[00:05:54 - 00:06:00] Lambda, you only pay for invocation. uh
[00:05:58 - 00:06:02] you don't pay for the server up and
[00:06:00 - 00:06:05] running. So then potentially what it can
[00:06:02 - 00:06:07] give us that this application is like
[00:06:05 - 00:06:10] probably this could be some tools that
[00:06:07 - 00:06:11] we are just developing for ourselves.
[00:06:10 - 00:06:15] They don't have to be up and running all
[00:06:11 - 00:06:18] the time. Plus in AWS Lambda
[00:06:15 - 00:06:20] uh
[00:06:18 - 00:06:23] pre invocations
[00:06:20 - 00:06:26] they're pretty like it's pretty generous
[00:06:23 - 00:06:28] u when it comes to
[00:06:26 - 00:06:31] pre- tier like how many invocations we
[00:06:28 - 00:06:34] have can have per month I use lambda I I
[00:06:31 - 00:06:36] wouldn't say I use it extensively but I
[00:06:34 - 00:06:38] used lambda for some things and I don't
[00:06:36 - 00:06:43] think I'm paying for it like so I'm
[00:06:38 - 00:06:45] still below this threshold for um
[00:06:43 - 00:06:48] for actually like for them to start
[00:06:45 - 00:06:51] charging me for for lambda. Um so how
[00:06:48 - 00:06:54] about we now I don't know what's wrong
[00:06:51 - 00:06:58] with this website. Um how about we now
[00:06:54 - 00:07:01] try to create something like an agent
[00:06:58 - 00:07:04] and deploy it to Lambda. Um would it be
[00:07:01 - 00:07:04] interesting for you?
[00:07:10 - 00:07:16] Yes, let's do it.
[00:07:13 - 00:07:18] >> Okay, cool. Um, for the next one, maybe
[00:07:16 - 00:07:21] what you can do is you don't have to
[00:07:18 - 00:07:23] come up with an idea of what to develop,
[00:07:21 - 00:07:25] but maybe there is something like maybe
[00:07:23 - 00:07:28] there's a technology you want to uh
[00:07:25 - 00:07:30] learn or maybe there's some new concept
[00:07:28 - 00:07:32] you want to learn. Um, and then we can
[00:07:30 - 00:07:35] do this together. Another thing I was
[00:07:32 - 00:07:36] thinking about uh let's do lambda now um
[00:07:35 - 00:07:39] because I think this is pretty
[00:07:36 - 00:07:45] interesting. Uh another thing is there
[00:07:39 - 00:07:47] are these things like um open claw or
[00:07:45 - 00:07:49] hairs. So we can also try to understand
[00:07:47 - 00:07:51] how these things work and how we can use
[00:07:49 - 00:07:54] them or maybe something similar. Maybe
[00:07:51 - 00:07:56] you uh check Twitter um you open Twitter
[00:07:54 - 00:07:58] you see some things there and you wonder
[00:07:56 - 00:08:00] okay how does this thing work? Can I
[00:07:58 - 00:08:03] implement something similar? So these
[00:08:00 - 00:08:07] are the things we can do together.

## Window 002: 00:07:31 - 00:15:31

[00:07:32 - 00:07:36] thinking about uh let's do lambda now um
[00:07:35 - 00:07:39] because I think this is pretty
[00:07:36 - 00:07:45] interesting. Uh another thing is there
[00:07:39 - 00:07:47] are these things like um open claw or
[00:07:45 - 00:07:49] hairs. So we can also try to understand
[00:07:47 - 00:07:51] how these things work and how we can use
[00:07:49 - 00:07:54] them or maybe something similar. Maybe
[00:07:51 - 00:07:56] you uh check Twitter um you open Twitter
[00:07:54 - 00:07:58] you see some things there and you wonder
[00:07:56 - 00:08:00] okay how does this thing work? Can I
[00:07:58 - 00:08:03] implement something similar? So these
[00:08:00 - 00:08:07] are the things we can do together.
[00:08:03 - 00:08:12] Okay. So we'll go with lambda, right? Um
[00:08:07 - 00:08:14] so what I want to do now for that is um
[00:08:12 - 00:08:17] I run maybe you remember from the last
[00:08:14 - 00:08:19] time I run everything on the remote
[00:08:17 - 00:08:21] machine.
[00:08:19 - 00:08:24] So this remote machine doesn't have
[00:08:21 - 00:08:27] access to my AWS. This is on purpose. I
[00:08:24 - 00:08:29] do not want agents. I am running quite a
[00:08:27 - 00:08:33] few agents here. I don't want these
[00:08:29 - 00:08:35] agents to have access to my um to my
[00:08:33 - 00:08:37] production uh to my AWS account because
[00:08:35 - 00:08:39] there are some things that are in
[00:08:37 - 00:08:42] production that are running there. Um so
[00:08:39 - 00:08:44] I don't them I don't want them to see
[00:08:42 - 00:08:47] these things. Uh what I want to do now
[00:08:44 - 00:08:50] is I probably I want to create a new
[00:08:47 - 00:08:53] account for AWS and then I can do
[00:08:50 - 00:08:56] whatever I want uh in this account and
[00:08:53 - 00:08:59] not be afraid and I will not be afraid
[00:08:56 - 00:09:02] of uh the agent accidentally nuking some
[00:08:59 - 00:09:06] some of the infrastructure. So for that
[00:09:02 - 00:09:10] um I'll probably I'll create a folder
[00:09:06 - 00:09:13] that I'll call temporary or AWS
[00:09:10 - 00:09:16] experiments.
[00:09:13 - 00:09:18] So right now I'm on my laptop and uh on
[00:09:16 - 00:09:23] my laptop I do have a account. So if I
[00:09:18 - 00:09:25] do AWS STS get caller identity.
[00:09:23 - 00:09:27] Um
[00:09:25 - 00:09:31] so I
[00:09:27 - 00:09:34] did I make a typo? Yes.
[00:09:31 - 00:09:38] So I so this is kind of who am I but for
[00:09:34 - 00:09:41] AWS. So this is my um user ID this is my
[00:09:38 - 00:09:43] account. So uh this is actually my uh
[00:09:41 - 00:09:45] administrator access on this account. I
[00:09:43 - 00:09:48] deploy uh many things like for example
[00:09:45 - 00:09:54] the course management platform from data
[00:09:48 - 00:09:56] talks club this one is deployed there or
[00:09:54 - 00:09:59] um for this AI shipping labs. Uh I'm
[00:09:56 - 00:10:02] still working on the jungo website for
[00:09:59 - 00:10:04] this. Um the deaf environment is already
[00:10:02 - 00:10:07] there and we have something that looks
[00:10:04 - 00:10:10] like pro environment. Um, so they are
[00:10:07 - 00:10:13] both deployed there. So I don't want my
[00:10:10 - 00:10:15] agents to be able to change change
[00:10:13 - 00:10:19] things there.
[00:10:15 - 00:10:23] But um, what I want to do is I want to
[00:10:19 - 00:10:27] uh create a new account and this account
[00:10:23 - 00:10:29] uh, I can just let agents play with this
[00:10:27 - 00:10:31] account. So what I will do, I'll use
[00:10:29 - 00:10:33] Codex.
[00:10:31 - 00:10:36] I wonder if I actually have it installed
[00:10:33 - 00:10:38] on my computer. Yeah. So, and then for
[00:10:36 - 00:10:40] codex, I because I don't remember how do
[00:10:38 - 00:10:44] I actually why it's doing this. I don't
[00:10:40 - 00:10:48] actually remember how um to create an
[00:10:44 - 00:10:52] account. So, I'll say um hey, I want to
[00:10:48 - 00:10:53] create a separate account in AWS for
[00:10:52 - 00:10:57] experiments and I want to have a
[00:10:53 - 00:10:59] separate billing for this account. Um um
[00:10:57 - 00:11:03] please uh create an account uh that is
[00:10:59 - 00:11:06] uh connected to my main account and
[00:11:03 - 00:11:10] create an admin user for that account
[00:11:06 - 00:11:11] and give me credentials.
[00:11:10 - 00:11:14] So then these credentials I'm going to
[00:11:11 - 00:11:18] use for um
[00:11:14 - 00:11:21] um for this other
[00:11:18 - 00:11:23] um like on the remote machine. So there
[00:11:21 - 00:11:26] there are some AWS commands like that
[00:11:23 - 00:11:29] that you can do this through uh command
[00:11:26 - 00:11:34] line interface to actually create uh
[00:11:29 - 00:11:35] accounts within organization on AWS. Uh
[00:11:34 - 00:11:38] and this is very convenient because when
[00:11:35 - 00:11:42] I will get an AWS bill I know that um
[00:11:38 - 00:11:46] these experiments come from um this
[00:11:42 - 00:11:49] account. So for the unique email address
[00:11:46 - 00:11:50] so for me it will be AWS plus
[00:11:49 - 00:11:54] experiments
[00:11:50 - 00:11:54] data talks club.
[00:11:56 - 00:12:04] So I think this Yeah, of course
[00:11:59 - 00:12:07] >> question. Uh I find so much satisfaction
[00:12:04 - 00:12:10] from figuring out like how to do things
[00:12:07 - 00:12:13] but I feel like a lot of the um
[00:12:10 - 00:12:17] workshops we've done you've you've been
[00:12:13 - 00:12:20] uh delegating to um these coding agents.
[00:12:17 - 00:12:24] So I'm just like trying to kind of
[00:12:20 - 00:12:28] understand what is the like the workflow
[00:12:24 - 00:12:30] in in a real AI engineer role that like
[00:12:28 - 00:12:32] what is being expected
[00:12:30 - 00:12:35] >> do you have to understand how
[00:12:32 - 00:12:37] >> you know like things work how
[00:12:35 - 00:12:41] >> to engineer like
[00:12:37 - 00:12:42] >> yes um I spoke with many people so I
[00:12:41 - 00:12:45] don't know if I can call myself a
[00:12:42 - 00:12:48] engineer probably I can so I can also
[00:12:45 - 00:12:50] say how I work uh but since like I don't
[00:12:48 - 00:12:53] work for a particular company I work for
[00:12:50 - 00:12:55] myself it can be a bit different but I
[00:12:53 - 00:12:57] also speak with people who work as
[00:12:55 - 00:12:59] actual engineers right so for them the
[00:12:57 - 00:13:01] expectation is that they use coding at
[00:12:59 - 00:13:03] least so this is started this year so
[00:13:01 - 00:13:05] this is pretty fresh so we as industry
[00:13:03 - 00:13:07] we still need to figure out how exactly
[00:13:05 - 00:13:10] it should look like but from what I see
[00:13:07 - 00:13:11] right now AI engineers are expected to
[00:13:10 - 00:13:13] use these tools and expected to
[00:13:11 - 00:13:16] understand what they do right so because
[00:13:13 - 00:13:19] at the end the ownership is yours like
[00:13:16 - 00:13:21] you cannot tell um um hey my agent
[00:13:19 - 00:13:24] implemented something uh I have no idea
[00:13:21 - 00:13:26] how it works um but it kind of works
[00:13:24 - 00:13:28] right so this is I don't think it will
[00:13:26 - 00:13:31] it's the right attitude to just
[00:13:28 - 00:13:36] completely offload this to the uh coding
[00:13:31 - 00:13:40] agent and not do anything right so the
[00:13:36 - 00:13:43] way I work is I also want to understand
[00:13:40 - 00:13:45] but uh sometimes it's less important in
[00:13:43 - 00:13:48] the moment so what I want to understand
[00:13:45 - 00:13:50] is how the agent did something right so
[00:13:48 - 00:13:53] not how it's going to do something but
[00:13:50 - 00:13:55] okay it's it did something it's working
[00:13:53 - 00:13:58] what exactly happened there and that's
[00:13:55 - 00:14:00] why at the end of the session I usually
[00:13:58 - 00:14:02] ask the agent to document the process
[00:14:00 - 00:14:03] okay what exactly we did and right now
[00:14:02 - 00:14:07] we can actually see that there is
[00:14:03 - 00:14:09] nothing super complicated so for me like
[00:14:07 - 00:14:11] the reason I'm asking the agent to do
[00:14:09 - 00:14:14] this because first of all I don't
[00:14:11 - 00:14:15] remember the syntax I know that it's
[00:14:14 - 00:14:18] possible to do this thing I know it's
[00:14:15 - 00:14:21] possible to use AWS CLI command to
[00:14:18 - 00:14:23] create an organization uh and to create
[00:14:21 - 00:14:28] an account within organization and to
[00:14:23 - 00:14:30] create uh um to create like a user in
[00:14:28 - 00:14:33] this account. I know it's possible. I
[00:14:30 - 00:14:35] just don't remember the comments and um
[00:14:33 - 00:14:40] I don't know if it makes sense for me to
[00:14:35 - 00:14:43] remember. Um but uh what I do is I try
[00:14:40 - 00:14:45] to do this uh through the agent and then
[00:14:43 - 00:14:48] eventually I ask the agent hey now let's
[00:14:45 - 00:14:50] document this and I probably can show
[00:14:48 - 00:14:51] you an example
[00:14:50 - 00:14:54] um
[00:14:51 - 00:14:58] certificates. Yeah
[00:14:54 - 00:15:00] I think in buckets.
[00:14:58 - 00:15:03] Yeah. So for example right now um for
[00:15:00 - 00:15:08] certificates um
[00:15:03 - 00:15:12] I have this website certificate
[00:15:08 - 00:15:12] AI shipping
[00:15:14 - 00:15:20] ah here I don't know who's uh oh majesa
[00:15:17 - 00:15:25] that's let's that's here um so these
[00:15:20 - 00:15:28] certificates are hosted uh on um here on
[00:15:25 - 00:15:32] this website right so what happens under
[00:15:28 - 00:15:35] the hood is this certificates.labs.com

## Window 003: 00:15:01 - 00:23:01

[00:15:03 - 00:15:12] I have this website certificate
[00:15:08 - 00:15:12] AI shipping
[00:15:14 - 00:15:20] ah here I don't know who's uh oh majesa
[00:15:17 - 00:15:25] that's let's that's here um so these
[00:15:20 - 00:15:28] certificates are hosted uh on um here on
[00:15:25 - 00:15:32] this website right so what happens under
[00:15:28 - 00:15:35] the hood is this certificates.labs.com
[00:15:32 - 00:15:37] is actually an S3 bucket, right? So, I
[00:15:35 - 00:15:41] know it's possible for me to put things
[00:15:37 - 00:15:43] in an S3 bucket and then turn this into
[00:15:41 - 00:15:45] a website so then people can use it. I
[00:15:43 - 00:15:50] just don't remember how to do this. So,
[00:15:45 - 00:15:52] the way I set it up is I uh opened uh I
[00:15:50 - 00:15:54] don't remember which uh AI assistant was
[00:15:52 - 00:15:56] it maybe close code I don't remember. So
[00:15:54 - 00:16:00] then I started I described what I wanted
[00:15:56 - 00:16:03] to to get and then at the end uh I asked
[00:16:00 - 00:16:05] it to document everything. So and here
[00:16:03 - 00:16:07] it was like in order to create a three
[00:16:05 - 00:16:09] public bucket with custom domain this is
[00:16:07 - 00:16:13] what you need to do and then this is the
[00:16:09 - 00:16:17] description of what needs to happen. So
[00:16:13 - 00:16:19] for me I treat this information as u
[00:16:17 - 00:16:22] first of all documentation because next
[00:16:19 - 00:16:24] time I want to do something similar I
[00:16:22 - 00:16:26] will ask an agent to just read this file
[00:16:24 - 00:16:28] and it would do the same thing and
[00:16:26 - 00:16:31] another thing what if my agent uh
[00:16:28 - 00:16:33] doesn't work like what if I'm out of
[00:16:31 - 00:16:35] tokens what if I'm I don't know they are
[00:16:33 - 00:16:38] down and I need to do this right so I
[00:16:35 - 00:16:41] want to be able to do this thing myself
[00:16:38 - 00:16:45] so that's why at the end of the session
[00:16:41 - 00:16:47] I ask to um save this information and
[00:16:45 - 00:16:48] then I go through this and I want to
[00:16:47 - 00:16:50] make sure that I understand all the
[00:16:48 - 00:16:53] steps. Right? So here in this case it's
[00:16:50 - 00:16:55] a pretty detailed description of what I
[00:16:53 - 00:17:00] need to do next time if I want to uh
[00:16:55 - 00:17:02] again create a website for um
[00:17:00 - 00:17:04] for serving like I don't know static
[00:17:02 - 00:17:06] files because right now also this AI
[00:17:04 - 00:17:08] shipping labs this is the current
[00:17:06 - 00:17:12] version of the website it's actually
[00:17:08 - 00:17:15] also stored on S3. Yeah. So these things
[00:17:12 - 00:17:17] they these things tend to
[00:17:15 - 00:17:19] I don't know repeat themselves like I
[00:17:17 - 00:17:21] tend to come across them over and over
[00:17:19 - 00:17:23] again. That's why I think it's important
[00:17:21 - 00:17:25] to save to have this segmentation and
[00:17:23 - 00:17:29] then I also save it somewhere in G so
[00:17:25 - 00:17:31] then later I can discover it. Um did I
[00:17:29 - 00:17:33] answer the question?
[00:17:31 - 00:17:34] >> Yeah. Um somewhat there's
[00:17:33 - 00:17:36] >> somehat
[00:17:34 - 00:17:39] >> there's a level of trust that I'm
[00:17:36 - 00:17:42] hearing that you have for these coding
[00:17:39 - 00:17:45] agents, right? So I mean do you trust
[00:17:42 - 00:17:47] them completely? Not you can't trust
[00:17:45 - 00:17:49] them completely, right?
[00:17:47 - 00:17:51] >> Yes. That's why I'm creating an account
[00:17:49 - 00:17:53] right now because I don't want them to
[00:17:51 - 00:17:57] poke around my production account. I
[00:17:53 - 00:17:58] mean here I know more or less what it's
[00:17:57 - 00:18:01] going to do. So I know that it will not
[00:17:58 - 00:18:05] be trying to uh drop my production
[00:18:01 - 00:18:07] database while creating an account.
[00:18:05 - 00:18:11] >> Mhm. Um so yes I have some level of
[00:18:07 - 00:18:14] trust and uh I think at some point um
[00:18:11 - 00:18:15] um
[00:18:14 - 00:18:18] so the the comparison I have in my mind
[00:18:15 - 00:18:20] is like uh let's say I'm a manager and I
[00:18:18 - 00:18:22] have a team so I have to have trust with
[00:18:20 - 00:18:23] my team so I cannot
[00:18:22 - 00:18:27] >> uh
[00:18:23 - 00:18:29] watch every step of the team or of
[00:18:27 - 00:18:32] people in the team because the it's
[00:18:29 - 00:18:35] micromanagement with agent I find it
[00:18:32 - 00:18:37] kind of similar right except agents like
[00:18:35 - 00:18:40] the the code they produce is often worse
[00:18:37 - 00:18:43] than the code that human write. Um
[00:18:40 - 00:18:46] but yeah so and the another reason I
[00:18:43 - 00:18:48] trust this the the this coding agent is
[00:18:46 - 00:18:49] because I
[00:18:48 - 00:18:52] know that it's going to be something
[00:18:49 - 00:18:54] simple right sometimes uh sometimes I
[00:18:52 - 00:18:56] explicitly tell let's not implement
[00:18:54 - 00:18:58] things I just want to discuss an
[00:18:56 - 00:19:01] approach with you so then we discuss an
[00:18:58 - 00:19:04] approach and once the approach uh once
[00:19:01 - 00:19:07] I'm clear on what exactly the approach
[00:19:04 - 00:19:09] is and then we start implementing
[00:19:07 - 00:19:11] so then of course like If we discuss the
[00:19:09 - 00:19:13] approach first, I have more trust
[00:19:11 - 00:19:16] because I understand how this system
[00:19:13 - 00:19:20] looks um overall.
[00:19:16 - 00:19:23] >> Mhm. Yeah.
[00:19:20 - 00:19:25] >> It clears things up for me. Would you
[00:19:23 - 00:19:29] prefer to have like more detailed
[00:19:25 - 00:19:29] explanation or
[00:19:30 - 00:19:34] >> um
[00:19:32 - 00:19:37] I'm I'm trying to adjust the way I work
[00:19:34 - 00:19:40] because like I work um like forwards and
[00:19:37 - 00:19:43] I think like what you described is
[00:19:40 - 00:19:45] working backwards having the agent do
[00:19:43 - 00:19:47] like asking the agent to do something
[00:19:45 - 00:19:51] and trying to understand it later.
[00:19:47 - 00:19:53] working backwards and yeah I'm just
[00:19:51 - 00:19:55] >> trying I guess I'm trying to decide on
[00:19:53 - 00:19:57] how I should adjust my approach.
[00:19:55 - 00:19:59] >> It also depends on how much time you
[00:19:57 - 00:20:02] have maybe because um let's say in this
[00:19:59 - 00:20:04] workshop right now uh I would need to do
[00:20:02 - 00:20:06] some research. I would need to Google
[00:20:04 - 00:20:08] things. I would need to like maybe it
[00:20:06 - 00:20:09] would be a bit
[00:20:08 - 00:20:11] not only it will take more time but
[00:20:09 - 00:20:13] maybe at times it will be a bit awkward
[00:20:11 - 00:20:15] right because I I'll be like okay I
[00:20:13 - 00:20:18] don't really know how to do this. But
[00:20:15 - 00:20:21] now with agents like doing workshops
[00:20:18 - 00:20:23] like that um feels kind of easier right?
[00:20:21 - 00:20:26] So we can just delegate this work to the
[00:20:23 - 00:20:28] agent then we can discuss uh what the
[00:20:26 - 00:20:30] solution the agent implemented they came
[00:20:28 - 00:20:34] up with then we can see okay um this is
[00:20:30 - 00:20:36] actually not good because of reasons um
[00:20:34 - 00:20:41] and then eventually we will arrive at
[00:20:36 - 00:20:44] something that works uh faster. Yeah,
[00:20:41 - 00:20:46] >> I don't think there is like the right or
[00:20:44 - 00:20:48] wrong approach. Um, like if you feel
[00:20:46 - 00:20:51] like you need to know exactly what each
[00:20:48 - 00:20:53] step uh you're making,
[00:20:51 - 00:20:55] I see nothing wrong with that.
[00:20:53 - 00:20:57] >> Mhm. Okay.
[00:20:55 - 00:21:00] >> That's why like I really like asking
[00:20:57 - 00:21:03] agents to document things, especially in
[00:21:00 - 00:21:05] cases where
[00:21:03 - 00:21:07] it's not coming up with the answer
[00:21:05 - 00:21:09] immediately. So it needs to I'll try
[00:21:07 - 00:21:10] this, I'll try that, I'll try that and
[00:21:09 - 00:21:13] then at the end there is one solution
[00:21:10 - 00:21:14] that works. So then in these cases it's
[00:21:13 - 00:21:18] especially important to document things
[00:21:14 - 00:21:20] because I think if you ask if I ask this
[00:21:18 - 00:21:22] thing again it will come up with the
[00:21:20 - 00:21:24] same solution. So probably it knows AWS
[00:21:22 - 00:21:26] well enough to actually do this. But for
[00:21:24 - 00:21:28] some things where we need some
[00:21:26 - 00:21:30] experimentation where we need some back
[00:21:28 - 00:21:32] and forth where where we need some uh
[00:21:30 - 00:21:33] brainstorming.
[00:21:32 - 00:21:36] So in these cases I think it's
[00:21:33 - 00:21:36] especially important to document things.
[00:21:36 - 00:21:39] >> Yeah.
[00:21:36 - 00:21:42] >> So I will now document uh please
[00:21:39 - 00:21:42] document
[00:21:43 - 00:21:50] all the steps you made.
[00:21:47 - 00:21:55] So here I expect it to have like a pile
[00:21:50 - 00:21:58] there which describe all the comments um
[00:21:55 - 00:22:00] it performed.
[00:21:58 - 00:22:03] So I also want to open it in my visual
[00:22:00 - 00:22:03] studio code.
[00:22:06 - 00:22:12] So okay I have my initial admin
[00:22:08 - 00:22:15] credentials. Of course I'm going to um
[00:22:12 - 00:22:18] ah it created an account for me. So what
[00:22:15 - 00:22:23] I wanted to have is um
[00:22:18 - 00:22:26] instead of that I wanted to have um CLI
[00:22:23 - 00:22:31] um credentials. So maybe I will ask it
[00:22:26 - 00:22:33] after it writes it down. Can you give me
[00:22:31 - 00:22:35] um
[00:22:33 - 00:22:38] variable
[00:22:35 - 00:22:41] access?
[00:22:38 - 00:22:44] So, I want to have um this u account
[00:22:41 - 00:22:48] number and secret that I can use uh in
[00:22:44 - 00:22:51] my um remote machine to in order to do
[00:22:48 - 00:22:51] things there.
[00:22:51 - 00:22:59] But I will probably still need my um
[00:22:56 - 00:23:02] we will need to web access to do things.
[00:22:59 - 00:23:05] So maybe how about we actually do what

## Window 004: 00:22:31 - 00:30:31

[00:22:33 - 00:22:38] variable
[00:22:35 - 00:22:41] access?
[00:22:38 - 00:22:44] So, I want to have um this u account
[00:22:41 - 00:22:48] number and secret that I can use uh in
[00:22:44 - 00:22:51] my um remote machine to in order to do
[00:22:48 - 00:22:51] things there.
[00:22:51 - 00:22:59] But I will probably still need my um
[00:22:56 - 00:23:02] we will need to web access to do things.
[00:22:59 - 00:23:05] So maybe how about we actually do what
[00:23:02 - 00:23:05] it suggested.
[00:23:06 - 00:23:10] So, experiments admin,
[00:23:15 - 00:23:22] I'm curious, um, does anyone u not have
[00:23:18 - 00:23:26] an AWS account here
[00:23:22 - 00:23:26] or everyone have this?
[00:23:29 - 00:23:32] Oops.
[00:23:39 - 00:23:45] Okay, I guess uh it means yes, everyone
[00:23:42 - 00:23:45] has it.
[00:23:47 - 00:23:51] Okay, your authentication information is
[00:23:48 - 00:23:54] not correct. It probably should have
[00:23:51 - 00:23:54] been this one.
[00:24:03 - 00:24:09] Um my account I created it quite some
[00:24:05 - 00:24:13] time ago. Um
[00:24:09 - 00:24:13] okay. Um
[00:24:18 - 00:24:24] create temporary variables here.
[00:24:22 - 00:24:26] Okay.
[00:24:24 - 00:24:29] So I think it messed up a bit with any
[00:24:26 - 00:24:30] lines but it's okay. And also I'll add
[00:24:29 - 00:24:33] UWS
[00:24:30 - 00:24:36] default
[00:24:33 - 00:24:36] region.
[00:24:36 - 00:24:44] I'll use EU west one.
[00:24:41 - 00:24:47] Uh what is this session token? Why do I
[00:24:44 - 00:24:47] need session token?
[00:24:56 - 00:25:04] This is very very long.
[00:24:59 - 00:25:04] That's a lot of things. Um
[00:25:04 - 00:25:09] I temporary STS credentials. Ah that's
[00:25:07 - 00:25:14] actually pretty cool. So instead of
[00:25:09 - 00:25:16] giving a complete access to um this
[00:25:14 - 00:25:21] production environment, we just give it
[00:25:16 - 00:25:25] for the session. Um, I want to
[00:25:21 - 00:25:30] have uh the M
[00:25:25 - 00:25:30] variables that I can paste
[00:25:34 - 00:25:39] and give me access for 2 hours.
[00:25:42 - 00:25:49] Okay, so these are the comments. Um,
[00:25:44 - 00:25:49] I'll ask it to save them too.
[00:26:06 - 00:26:12] I wonder if you understand what I meant
[00:26:08 - 00:26:17] by save these two documents.
[00:26:12 - 00:26:17] Okay. But here I have um
[00:26:17 - 00:26:22] yeah I have my fresh account
[00:26:22 - 00:26:29] uh Europe. I did not know that there is
[00:26:25 - 00:26:31] um an uh a region in stock. So, I'll use
[00:26:29 - 00:26:35] Ireland. Ireland is typically the
[00:26:31 - 00:26:35] cheapest one in uh Europe.
[00:26:40 - 00:26:44] I need push.
[00:26:55 - 00:27:02] Okay. Now, let me go here. Um, I'll
[00:26:58 - 00:27:07] create maybe another folder. How should
[00:27:02 - 00:27:07] we call it? Um, I'll call it um
[00:27:07 - 00:27:13] Lambda
[00:27:10 - 00:27:13] deploy.
[00:27:21 - 00:27:24] Oh, okay.
[00:27:30 - 00:27:36] Safe there.
[00:27:32 - 00:27:36] N file to
[00:27:38 - 00:27:42] so what I want to do now I have this uh
[00:27:39 - 00:27:45] file I have these credentials and I want
[00:27:42 - 00:27:49] to save it to um to n file that I can
[00:27:45 - 00:27:54] use for like doing things
[00:27:49 - 00:27:58] um so it's going to be in tempp
[00:27:54 - 00:27:58] and lambda deploy
[00:28:01 - 00:28:06] So it will just copy this to the remote
[00:28:03 - 00:28:06] server
[00:28:08 - 00:28:13] use EU west one.
[00:28:16 - 00:28:20] So I don't know why it decided to run
[00:28:18 - 00:28:21] PowerShell.
[00:28:20 - 00:28:25] Maybe just sees that I'm on Windows. So
[00:28:21 - 00:28:25] that's why it uses PowerShell.
[00:28:43 - 00:28:49] and then I'll write document
[00:28:46 - 00:28:51] everything.
[00:28:49 - 00:28:53] Okay, so now we should have u this file
[00:28:51 - 00:28:55] here.
[00:28:53 - 00:28:59] Okay,
[00:28:55 - 00:29:02] cool. Um yeah it should be it's one line
[00:28:59 - 00:29:07] now
[00:29:02 - 00:29:09] it's one line should be multiple I don't
[00:29:07 - 00:29:13] know why it's one line but that's why it
[00:29:09 - 00:29:13] uh oops
[00:29:14 - 00:29:21] so I saw this dorm is a tool that uh
[00:29:19 - 00:29:24] automatically detects if there is a n
[00:29:21 - 00:29:27] file and I think we used it in the
[00:29:24 - 00:29:29] course automatically detects if there is
[00:29:27 - 00:29:31] a n file and loads this into the
[00:29:29 - 00:29:34] environment. But it detected only one.
[00:29:31 - 00:29:36] And the reason it detected only one is
[00:29:34 - 00:29:41] because um for some reasons it put
[00:29:36 - 00:29:41] everything inside uh one line.
[00:29:58 - 00:30:05] Yeah, I don't know why it uses bash, why
[00:30:01 - 00:30:08] it uses um PowerShell maybe. So when it
[00:30:05 - 00:30:11] finishes, I will ask it to use uh Python
[00:30:08 - 00:30:15] instead to use Python
[00:30:11 - 00:30:15] instead of PowerShell
[00:30:16 - 00:30:21] because I think it's more crossplatform.
[00:30:22 - 00:30:26] Okay. Now let me check.
[00:30:24 - 00:30:31] Yeah.
[00:30:26 - 00:30:34] So now if I do STS get color
[00:30:31 - 00:30:34] identity

## Window 005: 00:30:01 - 00:38:01

[00:30:05 - 00:30:11] finishes, I will ask it to use uh Python
[00:30:08 - 00:30:15] instead to use Python
[00:30:11 - 00:30:15] instead of PowerShell
[00:30:16 - 00:30:21] because I think it's more crossplatform.
[00:30:22 - 00:30:26] Okay. Now let me check.
[00:30:24 - 00:30:31] Yeah.
[00:30:26 - 00:30:34] So now if I do STS get color
[00:30:31 - 00:30:34] identity
[00:30:35 - 00:30:44] STS color identity.
[00:30:38 - 00:30:49] Okay. So it works. Um so now uh what we
[00:30:44 - 00:30:51] can do is maybe we should just take um
[00:30:49 - 00:30:57] we should take what we developed before
[00:30:51 - 00:31:01] and try to deploy to AWS Lambda. So
[00:30:57 - 00:31:01] take this.
[00:31:03 - 00:31:08] Um I'm thinking if I should use Codex or
[00:31:05 - 00:31:10] CLOT.
[00:31:08 - 00:31:14] I recently started using Codex more and
[00:31:10 - 00:31:20] more often. So, I kind of like it.
[00:31:14 - 00:31:23] Let's copy this older only this
[00:31:20 - 00:31:23] here.
[00:31:28 - 00:31:34] And for these simple tasks like um
[00:31:31 - 00:31:36] getting a file from somewhere, I know I
[00:31:34 - 00:31:39] can do this. I can do git clone. I can
[00:31:36 - 00:31:43] remove these things. uh but it will just
[00:31:39 - 00:31:44] take more time for me to um do these
[00:31:43 - 00:31:47] things myself rather than just
[00:31:44 - 00:31:51] explaining this agent uh what I want to
[00:31:47 - 00:31:54] do. Let's put all content inside this
[00:31:51 - 00:31:54] folder.
[00:31:58 - 00:32:06] Say I want like all the content of the
[00:32:01 - 00:32:06] subfolder to be here inside
[00:32:09 - 00:32:14] Okay. I actually don't know what what
[00:32:11 - 00:32:14] it's doing.
[00:32:16 - 00:32:20] So, let me check.
[00:32:21 - 00:32:27] Yeah, that's cool.
[00:32:23 - 00:32:32] Um, so now, um, actually, so I think
[00:32:27 - 00:32:36] what we have here is we have, um, Can I
[00:32:32 - 00:32:39] run it? Oops. Yeah, wrong chat
[00:32:36 - 00:32:39] make.
[00:32:41 - 00:32:46] So I think from what I remember what we
[00:32:43 - 00:32:48] have
[00:32:46 - 00:32:52] open AI key. Okay, I need to get my open
[00:32:48 - 00:32:55] AI key. Um I'll quickly stop sharing my
[00:32:52 - 00:33:00] screen cuz open AI key I don't want to
[00:32:55 - 00:33:03] um you receive. Um
[00:33:00 - 00:33:06] um I'll take it maybe from the previous
[00:33:03 - 00:33:09] workshop we did.
[00:33:06 - 00:33:10] Um or maybe I'll create a new one. Yeah,
[00:33:09 - 00:33:12] I think it's fine. I think I'll continue
[00:33:10 - 00:33:16] sharing my screen because then I will
[00:33:12 - 00:33:20] simply um I will simply deactivate it
[00:33:16 - 00:33:22] after our um so instead of using an
[00:33:20 - 00:33:23] existing uh key, I will just create a
[00:33:22 - 00:33:26] new one like I did for the previous
[00:33:23 - 00:33:33] workshop. And then after this workshop,
[00:33:26 - 00:33:33] I'll just remove it. Uh, lambda deploy.
[00:33:42 - 00:33:45] Um, yeah.
[00:33:57 - 00:34:04] Okay. So now um
[00:34:01 - 00:34:07] now if I run this
[00:34:04 - 00:34:07] make run
[00:34:09 - 00:34:15] it should work
[00:34:12 - 00:34:19] address is already uh in use. So I think
[00:34:15 - 00:34:19] I have something running.
[00:34:20 - 00:34:25] So let me stop it.
[00:34:29 - 00:34:38] Okay, so now it should work. Let me see.
[00:34:35 - 00:34:41] Okay, so this is our
[00:34:38 - 00:34:44] Do I also need to run front end? Um,
[00:34:41 - 00:34:44] probably I do.
[00:34:46 - 00:34:50] Uh to be honest I don't really remember
[00:34:48 - 00:34:53] what we did um
[00:34:50 - 00:34:56] or like in details maybe because agent
[00:34:53 - 00:34:59] was creating all things.
[00:34:56 - 00:35:01] So we have um
[00:34:59 - 00:35:04] this fronted install that we probably
[00:35:01 - 00:35:07] need to run and then I'll need to run
[00:35:04 - 00:35:07] make um
[00:35:14 - 00:35:21] okay um
[00:35:16 - 00:35:21] how do I enroll the course?
[00:35:23 - 00:35:28] So what I want to do now is take this
[00:35:26 - 00:35:32] application that we developed together
[00:35:28 - 00:35:35] last time and try to deploy it to um AWS
[00:35:32 - 00:35:40] Lambda. So I don't think we can use fast
[00:35:35 - 00:35:44] API for that. So we will need to use um
[00:35:40 - 00:35:46] some lambda specific stuff. Um but this
[00:35:44 - 00:35:48] lambda can also serve our front end.
[00:35:46 - 00:35:52] Right? So this lambda like in the same
[00:35:48 - 00:35:56] way as we uh serve um let me open it.
[00:35:52 - 00:35:59] Um, I open a new
[00:35:56 - 00:35:59] file.
[00:36:04 - 00:36:08] Okay, I need to first open.
[00:36:10 - 00:36:15] I have some zoom things that are a bit
[00:36:12 - 00:36:15] annoying.
[00:36:15 - 00:36:23] So what we did last time is we created
[00:36:17 - 00:36:23] front end and back end and they are
[00:36:24 - 00:36:29] in separate folders right we have um
[00:36:29 - 00:36:35] back end here like this our back end and
[00:36:33 - 00:36:38] this our front end but then for serving
[00:36:35 - 00:36:41] it uh we have two stages docker build.
[00:36:38 - 00:36:44] So first we um
[00:36:41 - 00:36:46] we prepare we build the front end and
[00:36:44 - 00:36:49] then we put this into the back end and
[00:36:46 - 00:36:51] then the back end at the end serves the
[00:36:49 - 00:36:53] front end. So what we can do is do
[00:36:51 - 00:36:57] something similar but with lambda.
[00:36:53 - 00:37:00] So I will now ask
[00:36:57 - 00:37:00] this.
[00:37:00 - 00:37:07] Okay. So now we have our code here and
[00:37:03 - 00:37:09] the back end is currently in fast API.
[00:37:07 - 00:37:13] So what I want to do is I want to deploy
[00:37:09 - 00:37:14] it with lambda. Um so I want to serve
[00:37:13 - 00:37:17] both front end and back end through
[00:37:14 - 00:37:22] lambda. And when I open this lambda
[00:37:17 - 00:37:24] function on AWS, um I want to see the
[00:37:22 - 00:37:25] front end and I want to be able to
[00:37:24 - 00:37:28] interact with this front end and also
[00:37:25 - 00:37:34] get uh streaming events, these server
[00:37:28 - 00:37:38] side events um streamed to to me um uh
[00:37:34 - 00:37:38] as the agent is responding.
[00:37:38 - 00:37:42] I think it's understandable enough.
[00:37:43 - 00:37:48] I have some ideas of how it may look
[00:37:45 - 00:37:49] like. Um
[00:37:48 - 00:37:54] so probably we'll need to completely
[00:37:49 - 00:37:57] ditch uh fast API and uh I actually
[00:37:54 - 00:37:59] don't know um if lambda is supporting
[00:37:57 - 00:38:05] server side events but I think this is a
[00:37:59 - 00:38:07] usual um they they are HTTP

## Window 006: 00:37:31 - 00:45:31

[00:37:34 - 00:37:38] as the agent is responding.
[00:37:38 - 00:37:42] I think it's understandable enough.
[00:37:43 - 00:37:48] I have some ideas of how it may look
[00:37:45 - 00:37:49] like. Um
[00:37:48 - 00:37:54] so probably we'll need to completely
[00:37:49 - 00:37:57] ditch uh fast API and uh I actually
[00:37:54 - 00:37:59] don't know um if lambda is supporting
[00:37:57 - 00:38:05] server side events but I think this is a
[00:37:59 - 00:38:07] usual um they they are HTTP
[00:38:05 - 00:38:09] compatible. So probably they should do
[00:38:07 - 00:38:11] this
[00:38:09 - 00:38:14] for streaming on lambda bracketable path
[00:38:11 - 00:38:17] uh is a container image plus lambda web
[00:38:14 - 00:38:19] adapter and a function function within
[00:38:17 - 00:38:21] mode response stream. I check docs for
[00:38:19 - 00:38:25] that because API gateway style adapter
[00:38:21 - 00:38:28] commonly buffer responses.
[00:38:25 - 00:38:31] Okay. Um
[00:38:28 - 00:38:33] to me it doesn't make a lot of like I I
[00:38:31 - 00:38:36] know what these things are like I know
[00:38:33 - 00:38:40] what is API gateway. So typically if you
[00:38:36 - 00:38:43] want to access a lambda function through
[00:38:40 - 00:38:47] HTTP you need to use this API gateway.
[00:38:43 - 00:38:53] Um but what it says that uh it will not
[00:38:47 - 00:38:55] be able to do SSE SSA stuff. Um but I I
[00:38:53 - 00:38:57] don't have enough experience I guess to
[00:38:55 - 00:38:59] understand this. So here again this we
[00:38:57 - 00:39:03] were talking about the level of trust
[00:38:59 - 00:39:04] that I have to put in in agent um in
[00:39:03 - 00:39:07] order to implement this. But um like I
[00:39:04 - 00:39:09] just accept for a fact that uh these
[00:39:07 - 00:39:12] agents when it comes to these things
[00:39:09 - 00:39:15] they know more uh about these things
[00:39:12 - 00:39:15] than I do.
[00:39:17 - 00:39:23] Okay. So I'm not sure I really like um
[00:39:21 - 00:39:29] this um
[00:39:23 - 00:39:29] so maybe I will ask now to um
[00:39:30 - 00:39:35] to explain what we are doing.
[00:39:32 - 00:39:40] So let me see
[00:39:35 - 00:39:43] um I will also add I want to completely
[00:39:40 - 00:39:47] remove past API
[00:39:43 - 00:39:50] from here just do
[00:39:47 - 00:39:50] lambda
[00:39:53 - 00:39:59] and then what I didn't like when I saw
[00:39:56 - 00:40:04] what it was doing so it was doing uh
[00:39:59 - 00:40:11] putting these things to make file Um
[00:40:04 - 00:40:14] let's move all the creation logic.
[00:40:11 - 00:40:14] Um
[00:40:14 - 00:40:19] inside scripts
[00:40:17 - 00:40:24] like these things uh maybe some things
[00:40:19 - 00:40:27] are actually useful.
[00:40:24 - 00:40:27] Lamb to deploy.
[00:40:28 - 00:40:31] Okay.
[00:40:32 - 00:40:38] But I would prefer to have a script
[00:40:34 - 00:40:41] deploy.sh instead of this. I want to
[00:40:38 - 00:40:45] have a script
[00:40:41 - 00:40:45] deploy sh
[00:40:47 - 00:40:51] cuz usually it's just more manageable.
[00:40:49 - 00:40:54] Like when I look at this, I don't really
[00:40:51 - 00:40:57] uh I don't know here. I prefer to have
[00:40:54 - 00:40:59] one line commands that are not really um
[00:40:57 - 00:41:04] you know I I don't want to have like
[00:40:59 - 00:41:04] logic here in make files.
[00:41:04 - 00:41:09] Yeah, it created like a ton of things
[00:41:06 - 00:41:12] here. So I want to have them inside a
[00:41:09 - 00:41:12] script.
[00:41:22 - 00:41:28] So, did it um implement anything yet?
[00:41:37 - 00:41:40] Yeah, I don't think it implemented.
[00:41:38 - 00:41:44] Probably it's creating some file right
[00:41:40 - 00:41:44] now. I don't know.
[00:41:47 - 00:41:55] Any questions so far or
[00:41:50 - 00:41:55] ideas or I don't know anything.
[00:41:58 - 00:42:02] >> One question regarding credentials.
[00:42:00 - 00:42:04] Maybe you've already mentioned it. I'm
[00:42:02 - 00:42:08] sorry if I'm repeating the question, but
[00:42:04 - 00:42:10] um instead of saving them in a m file,
[00:42:08 - 00:42:14] would it also be sensible to put it
[00:42:10 - 00:42:17] instead in a as a global variable like
[00:42:14 - 00:42:17] in a bash bash rc?
[00:42:17 - 00:42:21] >> Mhm.
[00:42:17 - 00:42:23] >> Or bash m something like that instead.
[00:42:21 - 00:42:25] >> I usually don't do this um because I
[00:42:23 - 00:42:29] prefer to have separate keys for each
[00:42:25 - 00:42:31] project. So in case um something happens
[00:42:29 - 00:42:33] to my key, it hasn't happened but in
[00:42:31 - 00:42:36] case something happens like my accident,
[00:42:33 - 00:42:39] my key is accidentally uh leaked uh for
[00:42:36 - 00:42:41] some reasons or I don't know then I know
[00:42:39 - 00:42:45] which project is compromised and then I
[00:42:41 - 00:42:46] can just simply um
[00:42:45 - 00:42:47] update this project.
[00:42:46 - 00:42:49] >> Understood.
[00:42:47 - 00:42:51] >> Yeah. So this is I don't I'm not saying
[00:42:49 - 00:42:53] this is the right approach.
[00:42:51 - 00:42:55] >> There are benefits of just putting this
[00:42:53 - 00:42:56] in basher because you don't need to
[00:42:55 - 00:42:58] worry about these things. it's it's
[00:42:56 - 00:43:01] always there, right? But because it's
[00:42:58 - 00:43:03] always there, um it's also easier to cuz
[00:43:01 - 00:43:06] any script that runs on your computer
[00:43:03 - 00:43:10] can access your environment variable,
[00:43:06 - 00:43:12] right? And then um your key can get uh
[00:43:10 - 00:43:15] leaked. Again, it hasn't happened to me,
[00:43:12 - 00:43:17] but uh reading all the stories on the
[00:43:15 - 00:43:19] internet that uh there was a library
[00:43:17 - 00:43:23] that got compromised and then it stole
[00:43:19 - 00:43:27] all the API keys. Um I'm a bit I'm
[00:43:23 - 00:43:30] trying to be careful. you cannot be u
[00:43:27 - 00:43:33] like I'm not like super paranoid about
[00:43:30 - 00:43:36] this but I'm also trying not to be like
[00:43:33 - 00:43:36] um
[00:43:36 - 00:43:41] how to say like I'm trying to be a bit
[00:43:38 - 00:43:42] more um careful
[00:43:41 - 00:43:44] >> it's interesting I would have thought
[00:43:42 - 00:43:45] it's actually more secure to put it into
[00:43:44 - 00:43:49] a bash RC
[00:43:45 - 00:43:52] >> yeah because um like I can run something
[00:43:49 - 00:43:54] like and then I have have access to all
[00:43:52 - 00:43:59] the environment variables I can run it
[00:43:54 - 00:44:03] inside my um inside Python. So if you
[00:43:59 - 00:44:05] run Python, you have this import OS and
[00:44:03 - 00:44:08] run and then you have access to all the
[00:44:05 - 00:44:12] environments. It means that if you have
[00:44:08 - 00:44:14] your uh credential inside your BRC, any
[00:44:12 - 00:44:15] process that runs on your computer can
[00:44:14 - 00:44:17] have access to this.
[00:44:15 - 00:44:19] >> Okay. Okay.
[00:44:17 - 00:44:21] >> Uh while if it's right, so then it's
[00:44:19 - 00:44:23] only um
[00:44:21 - 00:44:27] >> yeah in the designated project. Okay.
[00:44:23 - 00:44:27] Awesome. Yeah, thanks.
[00:44:27 - 00:44:33] >> Okay, I saw it created a ton of code. I
[00:44:31 - 00:44:38] don't know what exactly it was doing.
[00:44:33 - 00:44:38] Uh, so let's let's check.
[00:44:38 - 00:44:43] Uh,
[00:44:40 - 00:44:45] so yeah, it added this then I asked it
[00:44:43 - 00:44:49] to
[00:44:45 - 00:44:51] move it. So template I think this is um
[00:44:49 - 00:44:55] cloud form. So cloud form is like kind
[00:44:51 - 00:44:58] of terraform but specific to
[00:44:55 - 00:45:01] um to AWS. So here we just define okay
[00:44:58 - 00:45:04] we have these resources. So then instead
[00:45:01 - 00:45:06] of um managing all the functions or all
[00:45:04 - 00:45:08] the resources separately we just have
[00:45:06 - 00:45:12] one file that describes what kind of
[00:45:08 - 00:45:16] resources created for this project.
[00:45:12 - 00:45:18] Um and I didn't ask to create it and it
[00:45:16 - 00:45:21] did it itself. And I think this is good.
[00:45:18 - 00:45:24] Like eventually we would we probably
[00:45:21 - 00:45:25] would move to something like um this or
[00:45:24 - 00:45:28] Terraform or something like
[00:45:25 - 00:45:32] infrastructure as code. And it's cool
[00:45:28 - 00:45:36] cuz I didn't even need to ask it.

## Window 007: 00:45:01 - 00:53:01

[00:45:04 - 00:45:08] the resources separately we just have
[00:45:06 - 00:45:12] one file that describes what kind of
[00:45:08 - 00:45:16] resources created for this project.
[00:45:12 - 00:45:18] Um and I didn't ask to create it and it
[00:45:16 - 00:45:21] did it itself. And I think this is good.
[00:45:18 - 00:45:24] Like eventually we would we probably
[00:45:21 - 00:45:25] would move to something like um this or
[00:45:24 - 00:45:28] Terraform or something like
[00:45:25 - 00:45:32] infrastructure as code. And it's cool
[00:45:28 - 00:45:36] cuz I didn't even need to ask it.
[00:45:32 - 00:45:39] Okay. Uh what else did it do? Okay. Now
[00:45:36 - 00:45:45] it adjusted Docker file to
[00:45:39 - 00:45:45] uh do Lambda I guess.
[00:45:45 - 00:45:51] So now I asked it to move this to the
[00:45:47 - 00:45:54] script. So I did this. It removed uh
[00:45:51 - 00:45:54] fast API
[00:45:56 - 00:46:01] lambda runtime. Okay. So for lambda what
[00:46:00 - 00:46:04] we need to do for lambda is we need to
[00:46:01 - 00:46:06] define maybe it's easier for me if I
[00:46:04 - 00:46:10] just open it here.
[00:46:06 - 00:46:12] So for lambda we need
[00:46:10 - 00:46:15] oh we have this main
[00:46:12 - 00:46:18] Um
[00:46:15 - 00:46:22] I'll show you in in a different window
[00:46:18 - 00:46:24] so in a different project. Um so I don't
[00:46:22 - 00:46:26] know how many of you heard or took this
[00:46:24 - 00:46:28] machine learning zoom camp. It's a
[00:46:26 - 00:46:31] course about introduction to machine
[00:46:28 - 00:46:34] learning and there at some point I show
[00:46:31 - 00:46:39] how to deploy things with lambda
[00:46:34 - 00:46:41] and we should have some code for that
[00:46:39 - 00:46:43] and typically oh yeah we have this
[00:46:41 - 00:46:45] lambda function and then we have a
[00:46:43 - 00:46:50] function that is called lambda handler.
[00:46:45 - 00:46:54] So this is the main entry point um
[00:46:50 - 00:46:57] that um that is invoked when we u make a
[00:46:54 - 00:46:59] call to lambda. So I was trying to look
[00:46:57 - 00:47:02] something to find something like this
[00:46:59 - 00:47:06] lambda handler there but I couldn't. So
[00:47:02 - 00:47:06] let me see if we have it.
[00:47:12 - 00:47:15] So here at this point if I wanted to
[00:47:14 - 00:47:17] understand what's happening I would
[00:47:15 - 00:47:19] actually start asking questions like
[00:47:17 - 00:47:22] okay what is uh uh what are these
[00:47:19 - 00:47:24] things? So here I think this is uh
[00:47:22 - 00:47:29] something that is coming from our
[00:47:24 - 00:47:31] previous project. So um this is uh this
[00:47:29 - 00:47:35] is a part we implemented before. So I
[00:47:31 - 00:47:35] just took it response metadata.
[00:47:36 - 00:47:41] Um yeah, perhaps this is also from the
[00:47:38 - 00:47:43] pre I don't remember that if we actually
[00:47:41 - 00:47:47] checked a lot of code. So I think it
[00:47:43 - 00:47:49] could be from the previous two
[00:47:47 - 00:47:52] event body.
[00:47:49 - 00:47:54] So this could be specific to lambda
[00:47:52 - 00:47:57] because lambda is doing sometimes this
[00:47:54 - 00:47:57] base 64 encoding
[00:47:58 - 00:48:02] method static f. So if I wanted to
[00:48:01 - 00:48:04] understand what's happening here, I
[00:48:02 - 00:48:08] would ask you hey why do we need this
[00:48:04 - 00:48:10] file? Why do we need that file? And um
[00:48:08 - 00:48:11] probably so right now I'm just trusting
[00:48:10 - 00:48:14] okay like it's probably doing something
[00:48:11 - 00:48:15] right. But if I really wanted to learn
[00:48:14 - 00:48:17] like I would start asking these
[00:48:15 - 00:48:20] questions like why would we need these
[00:48:17 - 00:48:20] things
[00:48:20 - 00:48:23] response.
[00:48:23 - 00:48:28] So this looks a bit like the entry
[00:48:26 - 00:48:30] point.
[00:48:28 - 00:48:34] So we have this lambda handler event and
[00:48:30 - 00:48:37] context and here is ask response event.
[00:48:34 - 00:48:42] So maybe this is the
[00:48:37 - 00:48:44] ask stream response. Okay, root.
[00:48:42 - 00:48:46] Okay, this looks like the entry point.
[00:48:44 - 00:48:49] So it first figures out what is the
[00:48:46 - 00:48:52] method whether it's get or post and what
[00:48:49 - 00:48:54] is the path and it roots to the
[00:48:52 - 00:48:56] appropriate function. So in fast API
[00:48:54 - 00:48:58] fast API is handling this this for us
[00:48:56 - 00:49:01] but lambda is a pretty low-level thing.
[00:48:58 - 00:49:02] So it gets a row request and then it
[00:49:01 - 00:49:04] needs to understand okay this request is
[00:49:02 - 00:49:09] coming for this path then therefore we
[00:49:04 - 00:49:12] need to um invoke this function right.
[00:49:09 - 00:49:14] So here if we send a request to ask
[00:49:12 - 00:49:16] stream
[00:49:14 - 00:49:20] then
[00:49:16 - 00:49:24] we get the event body we get the
[00:49:20 - 00:49:27] question that is inside and
[00:49:24 - 00:49:30] then we stream back the response. Okay
[00:49:27 - 00:49:32] seems logical.
[00:49:30 - 00:49:34] Next invocation. I have no idea what is
[00:49:32 - 00:49:40] that.
[00:49:34 - 00:49:40] Um that too. Okay, but this one is u
[00:49:41 - 00:49:47] we need to initialize the index too.
[00:49:44 - 00:49:49] So I don't know if it's this is actually
[00:49:47 - 00:49:52] invoked in lambda but we will figure
[00:49:49 - 00:49:52] this out.
[00:49:55 - 00:50:01] Okay. So this build image is stuff for
[00:49:59 - 00:50:06] um so because our lambda will be in
[00:50:01 - 00:50:09] docker. So we first will be able to test
[00:50:06 - 00:50:09] it locally
[00:50:10 - 00:50:14] and we're deploying through cloud form.
[00:50:12 - 00:50:18] So that yaml file that we saw that I uh
[00:50:14 - 00:50:18] talked about. So here it is.
[00:50:22 - 00:50:29] Okay,
[00:50:24 - 00:50:29] that's um a lot of stuff.
[00:50:32 - 00:50:39] Okay. Um so what how do I test it? How
[00:50:36 - 00:50:40] do I test it locally? So I probably need
[00:50:39 - 00:50:43] to do something like make run or
[00:50:40 - 00:50:43] something.
[00:50:47 - 00:50:53] So now what I want to do is uh should
[00:50:50 - 00:50:55] probably stop it.
[00:50:53 - 00:50:57] So what I want to get is uh the state
[00:50:55 - 00:51:00] where I run a docker container and this
[00:50:57 - 00:51:02] docker container has both front end and
[00:51:00 - 00:51:05] lambda back end inside. So then we can
[00:51:02 - 00:51:08] start thinking how can we deploy this to
[00:51:05 - 00:51:08] AWS.
[00:51:11 - 00:51:16] Okay. What is this code for? local
[00:51:14 - 00:51:20] server.py.
[00:51:16 - 00:51:20] Okay. Why do we need it?
[00:51:23 - 00:51:29] Um,
[00:51:24 - 00:51:33] so let me check which um
[00:51:29 - 00:51:35] so it uses this Python 3.14.
[00:51:33 - 00:51:39] As far as I know for lambda we need to
[00:51:35 - 00:51:42] use uh either we use a specific um image
[00:51:39 - 00:51:44] from provided by AWS or we need to do um
[00:51:42 - 00:51:45] this kind of stuff that it's doing right
[00:51:44 - 00:51:47] now. And to be honest I don't really
[00:51:45 - 00:51:52] understand what's happening like what is
[00:51:47 - 00:51:58] this lambda runtime? What is this uh
[00:51:52 - 00:52:01] local server? Why do we need it? Um I'll
[00:51:58 - 00:52:05] try to run it but then I will probably
[00:52:01 - 00:52:09] try to um also ask it to
[00:52:05 - 00:52:11] um rewrite it with the um Python image
[00:52:09 - 00:52:15] from uh AWS. So then we don't need to
[00:52:11 - 00:52:15] deal with all this kind of stuff.
[00:52:18 - 00:52:25] Okay.
[00:52:20 - 00:52:25] How do I join the course?
[00:52:28 - 00:52:36] No, amazing. It's working. Um, so
[00:52:31 - 00:52:42] probably I'll uh what I'll do is I'll um
[00:52:36 - 00:52:42] commit it. Get in it. Get at.
[00:52:43 - 00:52:48] So we have a working version. So the
[00:52:45 - 00:52:49] agent produced something. I have no clue
[00:52:48 - 00:52:52] what I don't understand half of the
[00:52:49 - 00:52:54] code, but it's working. So which is
[00:52:52 - 00:52:54] cool.
[00:52:55 - 00:53:01] Now I will try to um
[00:52:59 - 00:53:05] I will try to simplify it. I will try to
[00:53:01 - 00:53:08] understand what's happening. Um and I

## Window 008: 00:52:31 - 01:00:31

[00:52:36 - 00:52:42] commit it. Get in it. Get at.
[00:52:43 - 00:52:48] So we have a working version. So the
[00:52:45 - 00:52:49] agent produced something. I have no clue
[00:52:48 - 00:52:52] what I don't understand half of the
[00:52:49 - 00:52:54] code, but it's working. So which is
[00:52:52 - 00:52:54] cool.
[00:52:55 - 00:53:01] Now I will try to um
[00:52:59 - 00:53:05] I will try to simplify it. I will try to
[00:53:01 - 00:53:08] understand what's happening. Um and I
[00:53:05 - 00:53:10] will try to uh
[00:53:08 - 00:53:13] at least I have a bit of knowledge of
[00:53:10 - 00:53:18] lambda right. So um I think what we
[00:53:13 - 00:53:22] should actually do is we should use
[00:53:18 - 00:53:22] um standard image.
[00:53:23 - 00:53:28] So I'll ask it to do this.
[00:53:26 - 00:53:30] Um so I want to simplify it a little
[00:53:28 - 00:53:34] bit. So I see that we have a lot of
[00:53:30 - 00:53:37] wrappers around this uh which makes me
[00:53:34 - 00:53:39] wonder if um um this is going to be
[00:53:37 - 00:53:41] reproducible. So I want to have the
[00:53:39 - 00:53:43] local environment is exactly the same
[00:53:41 - 00:53:45] that the local environment is exactly
[00:53:43 - 00:53:47] the same as the production environment.
[00:53:45 - 00:53:51] That's why I think it's better if we use
[00:53:47 - 00:53:54] an official uh image from AWS. For
[00:53:51 - 00:53:54] example, this one
[00:53:56 - 00:53:59] 14
[00:54:04 - 00:54:10] because I I don't like this uh like why
[00:54:07 - 00:54:15] do we need this local server and I don't
[00:54:10 - 00:54:20] see uh like what is this bootstrap
[00:54:15 - 00:54:20] why do we even need It
[00:54:35 - 00:54:40] uh let me check uh what I had before.
[00:54:40 - 00:54:46] So um this is an example of what I did
[00:54:43 - 00:54:50] before. So since we use UV uh I think in
[00:54:46 - 00:54:52] lambda it's a bit tricky
[00:54:50 - 00:54:56] you cannot just do UV sync you need to
[00:54:52 - 00:55:00] install it into system um your system
[00:54:56 - 00:55:03] Python and this is how you do this
[00:55:00 - 00:55:08] the code I have from another
[00:55:03 - 00:55:08] project let's do something similar
[00:55:19 - 00:55:23] Okay, it deleted this stuff. That's
[00:55:21 - 00:55:25] good.
[00:55:23 - 00:55:28] Uh, and then the local container would
[00:55:25 - 00:55:32] be just this still like why it's war
[00:55:28 - 00:55:35] task bootstrap. Why do we need this? I
[00:55:32 - 00:55:37] don't want this. I just want to run uh I
[00:55:35 - 00:55:42] just want to do docker run and then let
[00:55:37 - 00:55:42] it handle everything
[00:55:43 - 00:55:49] and actually um so this thing that I
[00:55:45 - 00:55:51] have here so I
[00:55:49 - 00:55:54] I don't think I used AI to generate this
[00:55:51 - 00:55:57] code so I was doing it myself so maybe
[00:55:54 - 00:55:59] that's why it's uh
[00:55:57 - 00:56:02] more understandable what's happening
[00:55:59 - 00:56:04] because I um maybe also noticed that AI
[00:56:02 - 00:56:07] tends to overengineer things like the
[00:56:04 - 00:56:09] solutions it comes up with at the end
[00:56:07 - 00:56:11] they work but they are complicated and
[00:56:09 - 00:56:14] then you spend some time trying to cut
[00:56:11 - 00:56:15] it. um at the end I don't know what is
[00:56:14 - 00:56:17] faster
[00:56:15 - 00:56:19] um
[00:56:17 - 00:56:24] do it with AI end to end and then cut it
[00:56:19 - 00:56:26] or do everything by hand but um cleaner
[00:56:24 - 00:56:28] uh to me I probably prefer doing the
[00:56:26 - 00:56:31] second way with AI because I don't
[00:56:28 - 00:56:35] always exactly know what I uh how how I
[00:56:31 - 00:56:38] want to build it um so then while I
[00:56:35 - 00:56:40] interact with AI uh I have it more clear
[00:56:38 - 00:56:42] in my mind and I try to understand the
[00:56:40 - 00:56:44] code it's not like I just let it blindly
[00:56:42 - 00:56:46] write something and not care about this
[00:56:44 - 00:56:48] but I also try to figure out what's
[00:56:46 - 00:56:51] happening inside um this code like what
[00:56:48 - 00:56:53] exactly what kind of functions I have
[00:56:51 - 00:56:56] what these functions do where these
[00:56:53 - 00:56:59] functions are invoked from um and things
[00:56:56 - 00:56:59] like that
[00:56:59 - 00:57:04] okay let's see what do we have
[00:57:06 - 00:57:11] so uh relevant code changes
[00:57:10 - 00:57:14] so I'll stop
[00:57:11 - 00:57:18] And I'll go and check
[00:57:14 - 00:57:18] what we have.
[00:57:23 - 00:57:29] Why do we need it? Can't we use um
[00:57:30 - 00:57:34] how did Can't we use um
[00:57:44 - 00:57:49] I see uh okay so I'm satisfied with this
[00:57:48 - 00:57:52] explanation because it says here for
[00:57:49 - 00:57:56] normal buffered lambda yes but since we
[00:57:52 - 00:57:58] need SS SS is e streaming. Um, okay. Now
[00:57:56 - 00:58:01] I understand that there is a reason why
[00:57:58 - 00:58:04] we do it this way. So then for me, okay,
[00:58:01 - 00:58:06] it means I need to maybe not now but
[00:58:04 - 00:58:08] eventually understand what it actually
[00:58:06 - 00:58:15] is. What is this bootstrap? Why is it
[00:58:08 - 00:58:17] used? Why do we do it um this way? Um
[00:58:15 - 00:58:20] I don't know maybe we uh we can do this
[00:58:17 - 00:58:22] a bit later but uh now I want to test it
[00:58:20 - 00:58:25] and I want to deploy it and then uh
[00:58:22 - 00:58:27] maybe understand it. Um
[00:58:25 - 00:58:29] okay Franchesca. Yeah, it was nice
[00:58:27 - 00:58:32] seeing you. Um yeah, I'll probably take
[00:58:29 - 00:58:35] another half an hour to wrap it up. Um
[00:58:32 - 00:58:37] yeah, I hope it's useful for you and um
[00:58:35 - 00:58:40] yeah, I'll be happy if you share
[00:58:37 - 00:58:43] feedback. Um but yeah, was nice seeing
[00:58:40 - 00:58:44] you and um see you around.
[00:58:43 - 00:58:45] Bye.
[00:58:44 - 00:58:49] >> Yeah. Bye.
[00:58:45 - 00:58:52] Um, okay. Let's continue. So, I want to
[00:58:49 - 00:58:52] uh deploy it.
[00:58:53 - 00:58:58] Um, so first I want to run it locally,
[00:58:56 - 00:59:01] right? So, I want to run and make sure
[00:58:58 - 00:59:06] that uh when I requested these changes,
[00:59:01 - 00:59:06] nothing broke. So, I will probably
[00:59:07 - 00:59:12] try to do this local container. What did
[00:59:09 - 00:59:16] I just run?
[00:59:12 - 00:59:20] Uh script local container. Okay, so you
[00:59:16 - 00:59:24] just build uh an image
[00:59:20 - 00:59:26] uh and then run this image.
[00:59:24 - 00:59:29] Okay, so there there are some things
[00:59:26 - 00:59:31] that I'm not happy about like why do we
[00:59:29 - 00:59:33] need to do this entry point? Like it
[00:59:31 - 00:59:36] looks confusing to me like it's not
[00:59:33 - 00:59:39] something I have seen before. That's why
[00:59:36 - 00:59:42] for me it's like okay do I really like
[00:59:39 - 00:59:44] it this way? I'll probably need to spend
[00:59:42 - 00:59:47] some time understanding like what these
[00:59:44 - 00:59:47] things are.
[00:59:47 - 00:59:53] Okay, but it is running
[00:59:50 - 00:59:58] and let me see.
[00:59:53 - 00:59:58] I think it used a different port, right?
[00:59:58 - 01:00:02] It was 9,000.
[01:00:01 - 01:00:07] I don't know why all of a sudden I
[01:00:02 - 01:00:07] decided to use um
[01:00:09 - 01:00:16] Okay, I'll just say I sent a request to
[01:00:17 - 01:00:23] localhost 9,000 and got this.
[01:00:24 - 01:00:31] So perhaps something happened when we
[01:00:29 - 01:00:36] all right this is expected with AWS
[01:00:31 - 01:00:40] runtime interface simulator or 9,000.

## Window 009: 01:00:01 - 01:08:01

[01:00:02 - 01:00:07] decided to use um
[01:00:09 - 01:00:16] Okay, I'll just say I sent a request to
[01:00:17 - 01:00:23] localhost 9,000 and got this.
[01:00:24 - 01:00:31] So perhaps something happened when we
[01:00:29 - 01:00:36] all right this is expected with AWS
[01:00:31 - 01:00:40] runtime interface simulator or 9,000.
[01:00:36 - 01:00:40] So I need to do this.
[01:00:41 - 01:00:44] Okay.
[01:00:45 - 01:00:52] How do I open
[01:00:49 - 01:00:52] front end?
[01:01:08 - 01:01:13] Interesting. Um,
[01:01:11 - 01:01:16] okay. If we do it this way, but then how
[01:01:13 - 01:01:20] am I going to serve front end? I also
[01:01:16 - 01:01:20] want to serve front end from lambda.
[01:01:26 - 01:01:31] Front end is served from lambda by
[01:01:28 - 01:01:31] lambda runtime.
[01:01:41 - 01:01:47] Okay.
[01:01:43 - 01:01:50] Uh probably I still want to try to do
[01:01:47 - 01:01:51] this locally
[01:01:50 - 01:01:54] but let's deploy it first and then see
[01:01:51 - 01:01:58] cuz yeah it told me about some reasons
[01:01:54 - 01:02:03] why it's this way. Indeed, this is how
[01:01:58 - 01:02:05] you do this in um lambda when you use
[01:02:03 - 01:02:09] this official
[01:02:05 - 01:02:10] official uh image. So it's a bit cryptic
[01:02:09 - 01:02:13] but I think this is the standard way of
[01:02:10 - 01:02:16] doing this. That's why um yeah that's
[01:02:13 - 01:02:20] why we'll do this this way. So okay
[01:02:16 - 01:02:20] let's deploy it.
[01:02:25 - 01:02:31] So we'll build the lambda function
[01:02:27 - 01:02:34] create use repo. So ECR repo is where we
[01:02:31 - 01:02:36] store the docker images. We haven't
[01:02:34 - 01:02:40] created it. It's actually this um AWS
[01:02:36 - 01:02:42] account is completely empty.
[01:02:40 - 01:02:45] All right. Um so yeah it will need to
[01:02:42 - 01:02:45] create all these things.
[01:02:49 - 01:02:52] Okay. Um,
[01:02:55 - 01:02:59] and then it's said, okay, that there are
[01:02:57 - 01:03:06] some weird things coming from Windows.
[01:02:59 - 01:03:06] I'll just ask it to um to edit it.
[01:03:08 - 01:03:12] I want to get some water. So, while it's
[01:03:10 - 01:03:15] working, uh, I'll go get water and I'll
[01:03:12 - 01:03:15] be back.
[01:03:34 - 01:03:38] Um so while it's doing something um I
[01:03:37 - 01:03:42] just want to quickly check with you like
[01:03:38 - 01:03:44] how useful you think it is. Um because I
[01:03:42 - 01:03:46] I get some questions from you and this
[01:03:44 - 01:03:49] is very nice. Um for me it's also a bit
[01:03:46 - 01:03:51] experimental because we are figuring out
[01:03:49 - 01:03:54] this together. So, I'm wondering if it's
[01:03:51 - 01:03:57] actually useful for you or uh maybe you
[01:03:54 - 01:04:01] would prefer the prefer content that is
[01:03:57 - 01:04:01] like more prepared. I don't know.
[01:04:13 - 01:04:17] >> I don't want to do the talking all the
[01:04:15 - 01:04:18] time.
[01:04:17 - 01:04:20] Just as a comment,
[01:04:18 - 01:04:23] >> I think the process is super interesting
[01:04:20 - 01:04:26] to see how you go about things.
[01:04:23 - 01:04:29] >> I think I do it similarly with the only
[01:04:26 - 01:04:31] difference that I think I limit the
[01:04:29 - 01:04:33] agents a lot more than you do. I think
[01:04:31 - 01:04:36] it goes back to the question that
[01:04:33 - 01:04:39] Vanches before, how much you really want
[01:04:36 - 01:04:43] to let them go. And I haven't jumped
[01:04:39 - 01:04:45] over my own shadow yet, I guess.
[01:04:43 - 01:04:47] >> Jump over your own shadow. What What
[01:04:45 - 01:04:50] does it mean? Yeah, I haven't jumped
[01:04:47 - 01:04:52] over my own limitations to I don't I I'm
[01:04:50 - 01:04:55] conservative about it. I don't want to
[01:04:52 - 01:04:58] Yeah. let it loose.
[01:04:55 - 01:05:00] >> Um I understand this approach too. Yeah.
[01:04:58 - 01:05:03] Um and how do you usually do this? Like
[01:05:00 - 01:05:05] do you ask it to come up with a plan and
[01:05:03 - 01:05:07] then you manually execute it or how do
[01:05:05 - 01:05:10] you do this?
[01:05:07 - 01:05:13] >> What I do a lot is that I give it the
[01:05:10 - 01:05:15] path to old projects and I say okay now
[01:05:13 - 01:05:18] I want to do something new. this is what
[01:05:15 - 01:05:21] I want to do but take into account
[01:05:18 - 01:05:24] the code of my other projects like I'm
[01:05:21 - 01:05:27] really focused on maintainability
[01:05:24 - 01:05:29] and I wanted to replicate it
[01:05:27 - 01:05:31] >> so that it's maintainable later and not
[01:05:29 - 01:05:33] that I have what you said before it goes
[01:05:31 - 01:05:35] wild and then it creates too much
[01:05:33 - 01:05:37] complex code
[01:05:35 - 01:05:40] >> so if I give it a reference I kind of
[01:05:37 - 01:05:43] control for what it will pre-produce
[01:05:40 - 01:05:48] >> I I understand this approach and I think
[01:05:43 - 01:05:50] it's Um, a good one. Yeah, cuz it does u
[01:05:48 - 01:05:52] it does go wild. It does create like
[01:05:50 - 01:05:54] here we don't see this but on other
[01:05:52 - 01:05:57] projects sometimes it would go crazy and
[01:05:54 - 01:05:59] create all these weird obstructions that
[01:05:57 - 01:06:01] only these agents can understand. So
[01:05:59 - 01:06:03] then I review the code and I say hey
[01:06:01 - 01:06:06] here I'm really confused. I don't know
[01:06:03 - 01:06:09] what's happening. Um let's
[01:06:06 - 01:06:13] >> let's simplify it.
[01:06:09 - 01:06:16] >> Okay so deployment is successful.
[01:06:13 - 01:06:16] Yeah, thanks Carlos.
[01:06:17 - 01:06:22] Now if I if somebody else Ashish or Inan
[01:06:20 - 01:06:25] you want to share something, I would be
[01:06:22 - 01:06:28] also very happy to chat and then maybe
[01:06:25 - 01:06:31] get your feedback or maybe know how you
[01:06:28 - 01:06:31] work.
[01:06:43 - 01:06:49] And so while it's checking things, I
[01:06:45 - 01:06:53] want to go to um AWS.
[01:06:49 - 01:06:56] So we deployed I think to AU West one
[01:06:53 - 01:06:58] and we already have one function. So
[01:06:56 - 01:07:00] let's see
[01:06:58 - 01:07:04] what is there.
[01:07:00 - 01:07:07] Um so we have this FAQ agent lambda and
[01:07:04 - 01:07:11] then this I think um the name is weird
[01:07:07 - 01:07:14] because it's coming from cloud form.
[01:07:11 - 01:07:17] Um so then this is the image uh because
[01:07:14 - 01:07:21] uh we do it through docker that's why we
[01:07:17 - 01:07:23] don't see um the code here.
[01:07:21 - 01:07:28] Um
[01:07:23 - 01:07:28] okay I think it said that um
[01:07:29 - 01:07:37] yeah I guess not everything works
[01:07:33 - 01:07:38] so it figured out some mistakes.
[01:07:37 - 01:07:41] So this is exactly the situation I was
[01:07:38 - 01:07:43] talking about previously where it is
[01:07:41 - 01:07:44] trying to do something and then it sees
[01:07:43 - 01:07:47] that something is not working. It's
[01:07:44 - 01:07:49] trying to figure things out on their
[01:07:47 - 01:07:52] own. And I think this is pretty useful
[01:07:49 - 01:07:54] not only for the agent uh but for me
[01:07:52 - 01:07:57] too. And oh maybe I should say not only
[01:07:54 - 01:07:59] for me but for the agent too because
[01:07:57 - 01:08:02] next time the agent will uh do something
[01:07:59 - 01:08:05] like that. I can point it to a document

## Window 010: 01:07:31 - 01:15:31

[01:07:33 - 01:07:38] so it figured out some mistakes.
[01:07:37 - 01:07:41] So this is exactly the situation I was
[01:07:38 - 01:07:43] talking about previously where it is
[01:07:41 - 01:07:44] trying to do something and then it sees
[01:07:43 - 01:07:47] that something is not working. It's
[01:07:44 - 01:07:49] trying to figure things out on their
[01:07:47 - 01:07:52] own. And I think this is pretty useful
[01:07:49 - 01:07:54] not only for the agent uh but for me
[01:07:52 - 01:07:57] too. And oh maybe I should say not only
[01:07:54 - 01:07:59] for me but for the agent too because
[01:07:57 - 01:08:02] next time the agent will uh do something
[01:07:59 - 01:08:05] like that. I can point it to a document
[01:08:02 - 01:08:07] to a document saying this is how you go
[01:08:05 - 01:08:10] about deploying like all these things
[01:08:07 - 01:08:13] that we learned along the way
[01:08:10 - 01:08:16] here. Use them and u for the agent it
[01:08:13 - 01:08:16] will be just faster.
[01:08:18 - 01:08:24] Normalize updated build script
[01:08:21 - 01:08:28] provenence false.
[01:08:24 - 01:08:31] I have not a slightest idea of what is
[01:08:28 - 01:08:31] that.
[01:08:33 - 01:08:40] How do I
[01:08:37 - 01:08:40] join the course?
[01:08:44 - 01:08:52] Okay. I Oh, it's actually working.
[01:08:49 - 01:08:54] Okay. So, that's pretty cool. Um, we
[01:08:52 - 01:08:56] deployed it. Um there are some still
[01:08:54 - 01:08:59] some things I still want to understand
[01:08:56 - 01:09:01] like what happened. Okay, we deploy it's
[01:08:59 - 01:09:06] working. It's really good. So I will ask
[01:09:01 - 01:09:10] it. Uh let's commit everything.
[01:09:06 - 01:09:12] So this is really cool because lambda as
[01:09:10 - 01:09:14] I said at the very beginning is
[01:09:12 - 01:09:17] serverless. We pay only when we use it.
[01:09:14 - 01:09:21] So when I u go here and I start
[01:09:17 - 01:09:24] interacting with this um only when uh
[01:09:21 - 01:09:26] then it kind of wakes up and then I pay
[01:09:24 - 01:09:28] for the requests. So if during the day
[01:09:26 - 01:09:31] nobody is interacting with this I'm not
[01:09:28 - 01:09:35] paying anything and uh probably for this
[01:09:31 - 01:09:37] project after we play with this today
[01:09:35 - 01:09:40] it's never going to be used and it's
[01:09:37 - 01:09:42] fine. I can just keep it in my AWS and I
[01:09:40 - 01:09:44] don't need to worry about this right. So
[01:09:42 - 01:09:47] maybe at some point I will want to check
[01:09:44 - 01:09:48] it for some reasons and then I can just
[01:09:47 - 01:09:51] get this URL and check it right or maybe
[01:09:48 - 01:09:54] there are projects that are just low uh
[01:09:51 - 01:09:58] how to say
[01:09:54 - 01:10:02] just I use them not often once per day
[01:09:58 - 01:10:05] once per week right so having a separate
[01:10:02 - 01:10:07] instance on render or on fly io or
[01:10:05 - 01:10:10] especially on AWS doesn't make sense cuz
[01:10:07 - 01:10:14] on the if I do this on AWS I'll have to
[01:10:10 - 01:10:18] pay I don't know um way more than €10
[01:10:14 - 01:10:20] per month probably I don't know 20 30 um
[01:10:18 - 01:10:21] with render maybe it's like around 10
[01:10:20 - 01:10:24] but still like why would I need to pay
[01:10:21 - 01:10:27] €10 if I can get away with not paying
[01:10:24 - 01:10:29] anything right and then I can have as
[01:10:27 - 01:10:32] many projects like that as as I want
[01:10:29 - 01:10:34] right cuz on render you are actually
[01:10:32 - 01:10:36] limited I think you can only have one
[01:10:34 - 01:10:38] project in your free plan and then you
[01:10:36 - 01:10:41] you'll you'll need to start paying when
[01:10:38 - 01:10:41] you want to have multiple projects
[01:10:42 - 01:10:45] Okay. Um,
[01:10:48 - 01:10:55] uh, okay. I forgot about that, but it's
[01:10:50 - 01:10:57] really important. Uh, make sure and is
[01:10:55 - 01:11:00] in
[01:10:57 - 01:11:00] get ignore.
[01:11:03 - 01:11:10] And I think what I did before I might
[01:11:06 - 01:11:13] have accidentally committed it. No.
[01:11:10 - 01:11:15] Exit. G ignore. Okay. I think Yeah, I
[01:11:13 - 01:11:19] think before we already put it to Git
[01:11:15 - 01:11:20] ignore. That's why um I kind of forgot
[01:11:19 - 01:11:22] about this step.
[01:11:20 - 01:11:24] >> I think that's done uh by default,
[01:11:22 - 01:11:27] right? If you have git ignore, I think
[01:11:24 - 01:11:29] that's one of the absolute files that
[01:11:27 - 01:11:31] will be there by default.
[01:11:29 - 01:11:34] >> I wish it was the case. No, like you
[01:11:31 - 01:11:36] have to to do it yourself. And the
[01:11:34 - 01:11:38] reason it was here now is because I
[01:11:36 - 01:11:41] cloned this project from our previous
[01:11:38 - 01:11:43] workshop. So it was our previous
[01:11:41 - 01:11:44] workshop. Where was it?
[01:11:43 - 01:11:47] >> Yeah, I remember. Uhhuh.
[01:11:44 - 01:11:52] >> Yeah. So, and when we when we created it
[01:11:47 - 01:11:55] um then we actually um yeah, one of the
[01:11:52 - 01:11:57] first things I did was this give it.
[01:11:55 - 01:12:00] But um the good thing here is even if I
[01:11:57 - 01:12:03] accidentally committed this code, it
[01:12:00 - 01:12:09] actually is um
[01:12:03 - 01:12:13] so right now I didn't do get remote
[01:12:09 - 01:12:15] uh help. Yeah. So there's no remote uh
[01:12:13 - 01:12:18] no remote set. So remote is like I am
[01:12:15 - 01:12:22] not connected to GitHub because if I was
[01:12:18 - 01:12:23] connected to GitHub and I pushed then
[01:12:22 - 01:12:25] what can happen is I know that there are
[01:12:23 - 01:12:26] bots that scan all the repos and the
[01:12:25 - 01:12:29] moment they see my API key they can do
[01:12:26 - 01:12:31] something with this key. So I of course
[01:12:29 - 01:12:33] don't want that
[01:12:31 - 01:12:36] and uh if you accidentally commit the
[01:12:33 - 01:12:37] key um you will need to clean your g
[01:12:36 - 01:12:40] history and of course you will need to
[01:12:37 - 01:12:45] rotate the keys um as fast as possible.
[01:12:40 - 01:12:46] So um yeah I did this um sometimes this
[01:12:45 - 01:12:49] happens to me that I accidentally do
[01:12:46 - 01:12:52] this uh but of course I try to be
[01:12:49 - 01:12:55] careful and this is one of the reasons I
[01:12:52 - 01:12:57] uh here in this case I just initialized
[01:12:55 - 01:12:59] the g project
[01:12:57 - 01:13:01] um
[01:12:59 - 01:13:04] locally right so I I don't I don't know
[01:13:01 - 01:13:06] yet how useful it's going to be this
[01:13:04 - 01:13:08] project going to be um whether I should
[01:13:06 - 01:13:11] push it to GitHub and make it public or
[01:13:08 - 01:13:13] where I to uh keep it local, but I
[01:13:11 - 01:13:15] already have version control. So,
[01:13:13 - 01:13:17] because with agents there is a working
[01:13:15 - 01:13:19] code, but then they overwrite the
[01:13:17 - 01:13:21] working code, I always want to uh be
[01:13:19 - 01:13:24] able to go back even though it's maybe
[01:13:21 - 01:13:26] not on GitHub yet, but at least locally
[01:13:24 - 01:13:28] it's struck.
[01:13:26 - 01:13:31] Okay, so uh let's do this. Um there are
[01:13:28 - 01:13:34] some things I don't understand and I
[01:13:31 - 01:13:38] want to spend some time uh understanding
[01:13:34 - 01:13:40] them. Well, maybe first um
[01:13:38 - 01:13:42] let's document everything you have done
[01:13:40 - 01:13:45] so far because I know you had some
[01:13:42 - 01:13:48] problems with deployment. Um so let's
[01:13:45 - 01:13:51] document the deployment process. Um so
[01:13:48 - 01:13:55] we for us it's easy to to do something
[01:13:51 - 01:13:55] like that next time.
[01:13:55 - 01:14:00] And while it's documenting I want to
[01:13:57 - 01:14:03] check around. Um so front end I don't
[01:14:00 - 01:14:07] think front end changed but I want to
[01:14:03 - 01:14:10] look around at these things and then
[01:14:07 - 01:14:15] collect questions.
[01:14:10 - 01:14:18] So um what
[01:14:15 - 01:14:21] does this mean
[01:14:18 - 01:14:25] and create ECR? Um okay so here nothing
[01:14:21 - 01:14:27] I don't see anything suspicious. So ECR
[01:14:25 - 01:14:30] uh is elastic container registry. This
[01:14:27 - 01:14:32] is the place where we store the
[01:14:30 - 01:14:35] containers.
[01:14:32 - 01:14:38] Deploy lambda. Um yeah, here we do this
[01:14:35 - 01:14:40] through cloud form. So if we need to
[01:14:38 - 01:14:44] update anything with lambda, we just do
[01:14:40 - 01:14:47] cloud form deploy and that's fine.
[01:14:44 - 01:14:48] Lambda URL. So I think this is the
[01:14:47 - 01:14:50] script that gives you like once you
[01:14:48 - 01:14:53] deploy the lambda, you invoke the script
[01:14:50 - 01:14:55] and it gives you the URL.
[01:14:53 - 01:14:59] Local container.
[01:14:55 - 01:14:59] Do we still need it?
[01:15:05 - 01:15:09] uh push image. Um
[01:15:10 - 01:15:15] yeah, I think we already saw the
[01:15:11 - 01:15:18] scripts. Yeah, here seems logical.
[01:15:15 - 01:15:22] Then this thing I have no idea what is
[01:15:18 - 01:15:22] that. um
[01:15:23 - 01:15:29] explain in detail. Okay, for now I think
[01:15:27 - 01:15:31] it's enough. So I see that it created
[01:15:29 - 01:15:33] deployment script.
[01:15:31 - 01:15:36] Um maybe let let's check it in the

## Window 011: 01:15:01 - 01:23:01

[01:15:05 - 01:15:09] uh push image. Um
[01:15:10 - 01:15:15] yeah, I think we already saw the
[01:15:11 - 01:15:18] scripts. Yeah, here seems logical.
[01:15:15 - 01:15:22] Then this thing I have no idea what is
[01:15:18 - 01:15:22] that. um
[01:15:23 - 01:15:29] explain in detail. Okay, for now I think
[01:15:27 - 01:15:31] it's enough. So I see that it created
[01:15:29 - 01:15:33] deployment script.
[01:15:31 - 01:15:36] Um maybe let let's check it in the
[01:15:33 - 01:15:38] project deploy container the
[01:15:36 - 01:15:41] architecture
[01:15:38 - 01:15:45] um the build front end files are copied
[01:15:41 - 01:15:49] into okay lambda runtime this is the
[01:15:45 - 01:15:53] main entry point for this
[01:15:49 - 01:15:53] oh where is it
[01:15:53 - 01:16:00] so we use the official ads lambda
[01:15:57 - 01:16:00] base image
[01:16:00 - 01:16:04] Okay,
[01:16:02 - 01:16:06] deploy. Did we check this file? Ah, we
[01:16:04 - 01:16:11] just use this deploy lambda and then we
[01:16:06 - 01:16:11] show the script. Okay, makes sense.
[01:16:13 - 01:16:19] Okay, then we describe that we need uh
[01:16:16 - 01:16:23] stream that's why we create u custom
[01:16:19 - 01:16:23] runtime entry point
[01:16:28 - 01:16:33] which talks to the lambda runtime API
[01:16:30 - 01:16:36] directory and post responses with
[01:16:33 - 01:16:39] okay so I guess if we use the default um
[01:16:36 - 01:16:42] bootstrap or whatever um it's already
[01:16:39 - 01:16:44] it's already predefined that it's not
[01:16:42 - 01:16:48] streaming, it's buffered. That's why we
[01:16:44 - 01:16:48] need to do this thing
[01:16:49 - 01:16:53] deployment command. Um,
[01:16:56 - 01:16:59] so this one I don't think it's
[01:16:57 - 01:17:01] interesting.
[01:16:59 - 01:17:06] Um, I don't think we will hit this
[01:17:01 - 01:17:08] problem uh in the future.
[01:17:06 - 01:17:10] um cloud for deploy failed with image
[01:17:08 - 01:17:13] manifest configure layer is not
[01:17:10 - 01:17:13] supported.
[01:17:14 - 01:17:22] Okay, so this is this thing. So I have
[01:17:17 - 01:17:22] no idea what is that. So let's ask this.
[01:17:23 - 01:17:26] So I understand that it's needed but I
[01:17:24 - 01:17:29] want to understand what exactly it is
[01:17:26 - 01:17:31] like as bomb false like to me it doesn't
[01:17:29 - 01:17:33] say anything. What uh what the hell is
[01:17:31 - 01:17:36] provenance?
[01:17:33 - 01:17:39] Not to touch extra supply chain metadata
[01:17:36 - 01:17:40] to
[01:17:39 - 01:17:42] disables provenence at the station.
[01:17:40 - 01:17:44] Provenence is metadata about how the
[01:17:42 - 01:17:49] image was built.
[01:17:44 - 01:17:49] Uh software bill of materials.
[01:17:49 - 01:17:54] uh why we added on docker can export
[01:17:52 - 01:17:59] this as extra
[01:17:54 - 01:17:59] as lambda rejects the image with
[01:17:59 - 01:18:05] I'm still not exactly sure what it is uh
[01:18:02 - 01:18:07] to be honest like um I guess by default
[01:18:05 - 01:18:09] we include by default docker includes
[01:18:07 - 01:18:12] provenence and docker by default
[01:18:09 - 01:18:15] includes this software bill of materials
[01:18:12 - 01:18:18] what the hell this name is um
[01:18:15 - 01:18:19] I guess I'm the I don't remember
[01:18:18 - 01:18:21] actually having this kind problems with
[01:18:19 - 01:18:24] Lambda. Maybe it's just the new version
[01:18:21 - 01:18:26] of Docker is doing this, that's why we
[01:18:24 - 01:18:29] need to include this. It's interesting.
[01:18:26 - 01:18:32] Uh I guess um
[01:18:29 - 01:18:34] at least I understand now why we have
[01:18:32 - 01:18:37] this. I'm not fully I don't fully
[01:18:34 - 01:18:40] understand that uh what exactly is that
[01:18:37 - 01:18:43] and why uh we would need this
[01:18:40 - 01:18:45] information. Um,
[01:18:43 - 01:18:47] but yeah, I guess this is just how
[01:18:45 - 01:18:50] Docker includes the information and
[01:18:47 - 01:18:54] Lambda doesn't want this. Yeah, I'm I'm
[01:18:50 - 01:18:54] satisfied with this.
[01:18:58 - 01:19:02] Strictly skip speaking when make local
[01:19:01 - 01:19:06] script builds the same production image
[01:19:02 - 01:19:08] runs is with Lambda runtime
[01:19:06 - 01:19:11] it does not let you open the front end
[01:19:08 - 01:19:11] browser.
[01:19:14 - 01:19:19] Okay. Um I'll come back to this because
[01:19:16 - 01:19:22] I also want to make sure that um locally
[01:19:19 - 01:19:24] we have the same as um
[01:19:22 - 01:19:26] uh on production. But now I want to
[01:19:24 - 01:19:28] understand this bootstrap script what
[01:19:26 - 01:19:30] exactly it's doing
[01:19:28 - 01:19:33] this executable startup script for our
[01:19:30 - 01:19:36] custom lambda runtime. So it's doing
[01:19:33 - 01:19:38] this long bin Python. Okay. So this is
[01:19:36 - 01:19:42] the location of Python
[01:19:38 - 01:19:42] and task lambda runtime.
[01:19:50 - 01:19:53] Okay,
[01:19:56 - 01:20:00] it's a custom lambda runtime. Lambda
[01:19:58 - 01:20:03] starts the container and runs this
[01:20:00 - 01:20:03] executable.
[01:20:06 - 01:20:12] Okay. So typically we define the entry
[01:20:08 - 01:20:17] point to lambda uh this way but because
[01:20:12 - 01:20:20] of this sse thing we need to do it this
[01:20:17 - 01:20:22] way and I'm still a bit confused about
[01:20:20 - 01:20:26] this thing but I think um I just need to
[01:20:22 - 01:20:28] accept that this is how you do this cuz
[01:20:26 - 01:20:32] technically like this thing makes sense
[01:20:28 - 01:20:33] right so you need to execute uh
[01:20:32 - 01:20:35] although I don't know why exactly this
[01:20:33 - 01:20:38] interface typically you don't have this
[01:20:35 - 01:20:46] exact it. You just have uh this and
[01:20:38 - 01:20:46] this. Maybe I ask why do we need exec
[01:20:49 - 01:20:53] exec replaces the shell process with the
[01:20:51 - 01:20:57] Python process without of exec. The
[01:20:53 - 01:20:57] process tree is bootstrap shell.
[01:20:58 - 01:21:05] Um python becomes the main process
[01:21:01 - 01:21:05] instead of being the child of shell.
[01:21:06 - 01:21:11] Um okay okay okay okay I mean I'm not
[01:21:08 - 01:21:13] really a professional in this but there
[01:21:11 - 01:21:16] is a clear reason why it's there so what
[01:21:13 - 01:21:17] I want to avoid is um is just making
[01:21:16 - 01:21:21] things more complicated things that I
[01:21:17 - 01:21:23] don't understand for no reason right so
[01:21:21 - 01:21:28] I see now that there is a reason and
[01:21:23 - 01:21:28] since there is a reason I'm like okay um
[01:21:30 - 01:21:34] so
[01:21:32 - 01:21:36] maybe last thing before we wrap I want
[01:21:34 - 01:21:39] to
[01:21:36 - 01:21:44] let's uh try to make sure we can run it
[01:21:39 - 01:21:46] locally with front end too.
[01:21:44 - 01:21:48] So just for the sake of completeness
[01:21:46 - 01:21:50] because we don't want to check. So let's
[01:21:48 - 01:21:53] say we want to test front end. We don't
[01:21:50 - 01:21:56] want to deploy this uh maybe this is
[01:21:53 - 01:21:59] what I should say. So what I want to do
[01:21:56 - 01:22:01] is I want to be able to test things
[01:21:59 - 01:22:02] locally without having to deploy it.
[01:22:01 - 01:22:06] Let's say I make a change in back end.
[01:22:02 - 01:22:08] and I make a change in front end. Um, so
[01:22:06 - 01:22:11] I want to deploy it and ideally if
[01:22:08 - 01:22:14] possible I want to run it even without
[01:22:11 - 01:22:17] Docker cuz like if I want if I want to
[01:22:14 - 01:22:20] change the backend logic I don't want to
[01:22:17 - 01:22:23] rebuild this thing. So how do I have
[01:22:20 - 01:22:28] this local setup that doesn't require me
[01:22:23 - 01:22:28] to rebuild um the whole image.
[01:22:31 - 01:22:36] So something similar to what we had with
[01:22:33 - 01:22:37] u fast API right so with fast API we
[01:22:36 - 01:22:39] could do this uh we could run these
[01:22:37 - 01:22:43] things locally um I want to have
[01:22:39 - 01:22:43] something like that right now too
[01:22:45 - 01:22:49] and then ideally eventually I want to
[01:22:47 - 01:22:52] have also a docker image that serves
[01:22:49 - 01:22:55] both front end and back end um but if
[01:22:52 - 01:22:59] it's adding too many complications in
[01:22:55 - 01:23:02] the process uh then perhaps um yeah it's
[01:22:59 - 01:23:02] not really worth

## Window 012: 01:22:31 - 01:28:31

[01:22:33 - 01:22:37] u fast API right so with fast API we
[01:22:36 - 01:22:39] could do this uh we could run these
[01:22:37 - 01:22:43] things locally um I want to have
[01:22:39 - 01:22:43] something like that right now too
[01:22:45 - 01:22:49] and then ideally eventually I want to
[01:22:47 - 01:22:52] have also a docker image that serves
[01:22:49 - 01:22:55] both front end and back end um but if
[01:22:52 - 01:22:59] it's adding too many complications in
[01:22:55 - 01:23:02] the process uh then perhaps um yeah it's
[01:22:59 - 01:23:02] not really worth
[01:23:06 - 01:23:13] I think I saw this the right container.
[01:23:11 - 01:23:19] I don't really know what it is. Maybe
[01:23:13 - 01:23:19] I'll just ask what exactly is
[01:23:20 - 01:23:28] here. So, let me see what it wrote. Uh,
[01:23:25 - 01:23:32] yeah, again, this is the same thing that
[01:23:28 - 01:23:35] I asked you to delete. Uh and now it's
[01:23:32 - 01:23:37] uh put it back I guess if I want to run
[01:23:35 - 01:23:40] it locally then this is what I have to
[01:23:37 - 01:23:41] have.
[01:23:40 - 01:23:46] Uh
[01:23:41 - 01:23:48] okay. Yeah. So because for um fast API
[01:23:46 - 01:23:51] there is some
[01:23:48 - 01:23:53] back something that is handling requests
[01:23:51 - 01:23:57] right. So I guess for lambda we have to
[01:23:53 - 01:24:00] have this in order to be able to start
[01:23:57 - 01:24:03] this thing locally and um serve the back
[01:24:00 - 01:24:03] end.
[01:24:04 - 01:24:08] Um I'll run index check.
[01:24:16 - 01:24:21] So let's see what is uh lambda runtime
[01:24:20 - 01:24:24] interface emulator. It's small local
[01:24:21 - 01:24:29] emulator for from AWS that lets you run
[01:24:24 - 01:24:29] lambda container image on local machine.
[01:24:30 - 01:24:36] I see. Okay. So this is the thing that
[01:24:33 - 01:24:40] lets us run lambda without docker and we
[01:24:36 - 01:24:43] don't have to deploy to uh to lambda to
[01:24:40 - 01:24:47] actually test it. Okay. Make was it
[01:24:43 - 01:24:47] local? Let's see.
[01:24:52 - 01:24:57] How do I join the course?
[01:24:59 - 01:25:06] Okay, it's still uh it's still working.
[01:25:04 - 01:25:10] Um I'm not fully satisfied with the
[01:25:06 - 01:25:12] code. I still want to um
[01:25:10 - 01:25:13] adjust it. So for example, this lambda
[01:25:12 - 01:25:16] runtime, I think this could be
[01:25:13 - 01:25:19] simplified. I want to understand what
[01:25:16 - 01:25:20] these things are. Um, but right now it's
[01:25:19 - 01:25:23] been a long session. So I think we can
[01:25:20 - 01:25:26] call it a day from now. But eventually I
[01:25:23 - 01:25:28] really want to understand like every
[01:25:26 - 01:25:31] single line here cuz like if I need to
[01:25:28 - 01:25:33] fix it myself, I want to be able to,
[01:25:31 - 01:25:35] right? Um, I think I understand some
[01:25:33 - 01:25:38] things but still I want to make sure
[01:25:35 - 01:25:41] that and another thing is I want to also
[01:25:38 - 01:25:44] separate this thing that are strictly
[01:25:41 - 01:25:46] lambda related. uh like for example
[01:25:44 - 01:25:50] maybe routing we have this routing thing
[01:25:46 - 01:25:52] so perhaps this could be um I don't know
[01:25:50 - 01:25:54] in one uh file and then some other like
[01:25:52 - 01:25:59] very technical thing could be another
[01:25:54 - 01:26:02] file like this kind of back end logic um
[01:25:59 - 01:26:06] yeah I think this is um I remember
[01:26:02 - 01:26:09] seeing it in the explanation right so
[01:26:06 - 01:26:12] these are the headers that we set um
[01:26:09 - 01:26:12] Okay.
[01:26:14 - 01:26:18] So yeah, I would uh I will not do this
[01:26:16 - 01:26:20] right now, but eventually like if I
[01:26:18 - 01:26:22] wanted really to use it for my
[01:26:20 - 01:26:25] applications, I would write I would try
[01:26:22 - 01:26:26] to understand at least once. Um I would
[01:26:25 - 01:26:28] try to understand what this is and next
[01:26:26 - 01:26:30] time I will simply ask my agent hey like
[01:26:28 - 01:26:33] this is how I did last time please do
[01:26:30 - 01:26:35] something similar. So for me it's
[01:26:33 - 01:26:38] actually I already understand something.
[01:26:35 - 01:26:40] So it I will not to I will not need to
[01:26:38 - 01:26:43] understand something else some other
[01:26:40 - 01:26:47] approach that it used.
[01:26:43 - 01:26:49] Okay that's it for for now. Um I hope it
[01:26:47 - 01:26:51] was useful for you. Um I'm happy to get
[01:26:49 - 01:26:53] any feedback. You can share it now. You
[01:26:51 - 01:26:55] can share it in Slack. Um you can also
[01:26:53 - 01:26:59] think what else we can cover next time.
[01:26:55 - 01:27:01] So what I will do next is I will um
[01:26:59 - 01:27:04] share the recording with you when it's
[01:27:01 - 01:27:06] ready. And based on what we did today, I
[01:27:04 - 01:27:08] also want to prepare a kind of workshop
[01:27:06 - 01:27:11] that is more polished. Right? So right
[01:27:08 - 01:27:12] now it was like freestyle exploration,
[01:27:11 - 01:27:14] but I want to have like a proper
[01:27:12 - 01:27:17] workshop uh information based on that.
[01:27:14 - 01:27:19] So then later for you, you don't have to
[01:27:17 - 01:27:23] come through this uh through this video.
[01:27:19 - 01:27:25] Um but it will be like more polished uh
[01:27:23 - 01:27:28] version of what we learned today or what
[01:27:25 - 01:27:30] we explore today where you can just okay
[01:27:28 - 01:27:33] this is how I do this and then next time
[01:27:30 - 01:27:36] you can just uh uh either do it yourself
[01:27:33 - 01:27:39] or ask your agent to implement something
[01:27:36 - 01:27:42] something like that.
[01:27:39 - 01:27:44] Okay, that's uh it for now. So thanks a
[01:27:42 - 01:27:47] lot for joining.
[01:27:44 - 01:27:49] >> Thanks Alex. Yeah, thank you Carlos for
[01:27:47 - 01:27:51] being active because it felt a bit um
[01:27:49 - 01:27:54] you know strange to just talk to myself.
[01:27:51 - 01:27:55] So thanks for sometimes um helping me
[01:27:54 - 01:27:57] out.
[01:27:55 - 01:27:59] >> And and one thing that I really like
[01:27:57 - 01:28:01] maybe as a comment is that you showed
[01:27:59 - 01:28:03] the documentation that you produce once
[01:28:01 - 01:28:05] you finish with the project
[01:28:03 - 01:28:07] >> so that you can use that documentation
[01:28:05 - 01:28:10] for later purposes as well.
[01:28:07 - 01:28:13] >> That's really cool. Um
[01:28:10 - 01:28:15] >> so I would still clean it though. um
[01:28:13 - 01:28:17] like the documentation I have, I would
[01:28:15 - 01:28:19] still go through this. I would still try
[01:28:17 - 01:28:21] to process it a bit. I would still try
[01:28:19 - 01:28:23] to make it more useful. But at least you
[01:28:21 - 01:28:26] saw part of this process.
[01:28:23 - 01:28:27] >> Absolutely. Thanks a ton.
[01:28:26 - 01:28:28] >> Yeah. Thank you.
[01:28:27 - 01:28:31] >> Talk soon. Bye.
[01:28:28 - 01:28:31] >> Yeah. Bye.
