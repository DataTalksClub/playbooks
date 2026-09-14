# Handoff Brief: FastAPI to custom Lambda runtime for SSE

Source: /Users/valeria/.codex/content-runs/2026-06-16-lambda-agent-deployment/source/transcript.json

## 00:35:23 - 00:38:25

So what I want to do now is take this application that we developed together last time and try to deploy it to um AWS Lambda. So I don't think we can use fast API for that. So we will need to use um some lambda specific stuff. Um but this lambda can also serve our front end. Right? So this lambda like in the same way as we uh serve um let me open it. Um, I open a new file. Okay, I need to first open. I have some zoom things that are a bit annoying. So what we did last time is we created front end and back end and they are in separate folders right we have um back end here like this our back end and this our front end but then for serving it uh we have two stages docker build. So first we um we prepare we build the front end and then we put this into the back end and then the back end at the end serves the front end. So what we can do is do something similar but with lambda. So I will now ask this. Okay. So now we have our code here and the back end is currently in fast API. So what I want to do is I want to deploy it with lambda. Um so I want to serve both front end and back end through lambda. And when I open this lambda function on AWS, um I want to see the front end and I want to be able to interact with this front end and also get uh streaming events, these server side events um streamed to to me um uh as the agent is responding. I think it's understandable enough. I have some ideas of how it may look like. Um so probably we'll need to completely ditch uh fast API and uh I actually don't know um if lambda is supporting server side events but I think this is a usual um they they are HTTP compatible. So probably they should do this for streaming on lambda bracketable path uh is a container image plus lambda web adapter and a function function within mode response stream. I check docs for that because API gateway style adapter commonly buffer responses.

## 00:45:56 - 00:49:30

lambda runtime. Okay. So for lambda what we need to do for lambda is we need to define maybe it's easier for me if I just open it here. So for lambda we need oh we have this main Um I'll show you in in a different window so in a different project. Um so I don't know how many of you heard or took this machine learning zoom camp. It's a course about introduction to machine learning and there at some point I show how to deploy things with lambda and we should have some code for that and typically oh yeah we have this lambda function and then we have a function that is called lambda handler. So this is the main entry point um that um that is invoked when we u make a call to lambda. So I was trying to look something to find something like this lambda handler there but I couldn't. So let me see if we have it. So here at this point if I wanted to understand what's happening I would actually start asking questions like okay what is uh uh what are these things? So here I think this is uh something that is coming from our previous project. So um this is uh this is a part we implemented before. So I just took it response metadata. Um yeah, perhaps this is also from the pre I don't remember that if we actually checked a lot of code. So I think it could be from the previous two event body. So this could be specific to lambda because lambda is doing sometimes this base 64 encoding method static f. So if I wanted to understand what's happening here, I would ask you hey why do we need this file? Why do we need that file? And um probably so right now I'm just trusting okay like it's probably doing something right. But if I really wanted to learn like I would start asking these questions like why would we need these things response. So this looks a bit like the entry point. So we have this lambda handler event and context and here is ask response event. So maybe this is the ask stream response. Okay, root. Okay, this looks like the entry point. So it first figures out what is the method whether it's get or post and what is the path and it roots to the appropriate function. So in fast API fast API is handling this this for us but lambda is a pretty low-level thing. So it gets a row request and then it needs to understand okay this request is coming for this path then therefore we need to um invoke this function right. So here if we send a request to ask stream then we get the event body we get the question that is inside and then we stream back the response. Okay seems logical.

## 01:16:13 - 01:16:48

Okay, then we describe that we need uh stream that's why we create u custom runtime entry point which talks to the lambda runtime API directory and post responses with okay so I guess if we use the default um bootstrap or whatever um it's already it's already predefined that it's not streaming, it's buffered. That's why we need to do this thing

## Post angle

Moving the previous FastAPI app to Lambda required replacing the web layer with custom routing and a custom runtime because SSE streaming is not the default Lambda path.

## Clip recommendation

Use 00:45:56 - 00:49:30.

## Writing brief

Write a technical post explaining what changed when moving a streaming agent app from FastAPI to Lambda.
