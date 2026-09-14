# Handoff Brief: Build the smallest deployable agent first

Source: /Users/valeria/.codex/content-runs/2026-06-16-end-to-end-agent-deployment/source/transcript.json

## 00:31:02 - 00:32:46

uh, what I want to do together with you is I want to figure out how to deploy it, right? So this is this was, uh, I mean it's not something I typically show. So this for some of you this can be actually new information cuz what we do here is we use this as sync client, not the usual client. But otherwise, if you took like this AI shipping labs course or maybe you took the Maven course, like this should sound familiar. And if it's not familiar for you, like this AI hero course will help. Um, and of course like if you feel a bit lost, we can talk in Slack and then I can also help you find information like so next time, uh, you can understand like these things. uh but what we haven't done in any of the courses is um actually deploying this and this is what I want to focus on but before we can deploy this we actually need to turn this into a proper Python project right so let me quickly check questions are you using API responses uh open AI responses API yes so this is responses API or Where do I see it? Yeah, you see it's only clientres responses. Yeah, with chat completions I think it's similar. So what I want to do now is I want to turn this into a proper uh Python project and then I want to turn this Python project into a fast API back end.

## 00:58:30 - 00:59:49

no needs for structured output I think eventually we might need to have structured output um I don't want to over complicate this particular project right now uh but as we know that usually when we have structured output we kind of force the agent to be better right so eventually uh for version um I don't know for version number two for the next version I would actually add this here I just want to focus first on making it work end to end because when we add structured output we actually add one more layer of complexity right because when we talk about structured output and streaming at the same time we will need to stream things online and this makes the code that is already a bit complic complicated even more complicated right so I don't want to I want to avoid it for this particular session but um I think it was actually creating an application that I wanted to use I would first make this thing work end to end so I want to create front end now or maybe we can actually first test back end but I want to create front end now and I would then test that these things work then I would deploy it and only after that I would think okay now I need this this and that right so let's here let's focus focus on making this thing work and then later we can always

## 01:18:13 - 01:19:31

>> Okay. Um so um now what I want to do like of okay this is not ideal as I mentioned like we are not actually continuing conversation we are starting conversation from scratch every time we send the request. So there is no continuation. So this is something we just keep in mind that this is something we will improve later in the next versions. So what I want to do now is I want to package this inside a docker container right and I want to have one docker container. I want this docker container to serve both front end and back end and u then we will deploy this container. So this is what I will say. Uh okay right now everything works. So I want to deploy it and for that I want to create a docker container. This docker container should serve both back end and front end. So uh when we build a docker container so it should build our front end application it should package this and it should insert it inside our front end uh container. So then the sorry backend container so the backend container then will serve uh the built JavaScript. Okay. So we want to have only one docker container. We don't want to have two separate containers. We don't have a container for back end and front end.

## Post angle

Make the agent work end to end before adding structured outputs, memory, vector databases, or heavier frameworks.

## Clip recommendation

Use 00:58:30 - 00:59:49.

## Writing brief

Write a practical LinkedIn/X post for AI engineers explaining why the first milestone should be a deployed vertical slice: simple agent loop, backend, frontend, Docker, deploy. Mention that structured outputs, better retrieval, memory, and nicer UX can follow once the full path works.
