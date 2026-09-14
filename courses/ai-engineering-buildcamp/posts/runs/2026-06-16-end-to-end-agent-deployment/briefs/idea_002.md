# Handoff Brief: Make agent tool use visible in the UI

Source: /Users/valeria/.codex/content-runs/2026-06-16-end-to-end-agent-deployment/source/transcript.json

## 00:53:27 - 00:56:29

So now what we have is we have the search agent renderer schemas and app.py. So let's actually see what we have. So this is our entry point. Um so we have health check we have ask so this is the endpoint we will use for asking this dam so run agent so this is the function we implemented actually in our notebook so this was the function um here oops yeah this is what this is the our two call loop here so It uses this and at the end it sends an ask response. Okay, I think uh ah ask stream. Okay, I was thinking like uh did we not mention that we watch streaming? I don't remember mentioning it. But actually yes. So it uses this SSA. I think it's server side events. This is exactly what we need uh for uh for us because we want to um be able to push events to front end. I'm not really an expert in these things like I know these things exist and I know how to ask lot to implement these things. That's pretty much the extent of the knowledge I have about these things. Uh but um from what I see I have no objections to the way it wrote the code. Like for me it's actually let's say understandable I uh okay it's interesting init index open a client yeah this is the first time actually I see this construct construction okay so um I would typically define like a um global variable here and then they would access it here, right? Uh but I will undo it. I I'll I'll trust uh the agent. Um but yeah, it looks okay. I mean, I still uh don't have a lot of ideas what's happening here. Uh so there is event generator. So there's producer. Okay. So we have this run agent and run agent is producing some events. So if we go inside so these are the events right so this handle event uh so I think what is happening inside um okay so we have this base renderer so this is an abstract class and then this collecting renderer yeah ah okay so this is what the thing we need so we have this Q and this thing puts this event to the queue and these events are sent to the front end so this is my interpretation This this is what I think is happening.

## 01:08:26 - 01:09:31

so I expected to see streaming like it's not streaming the response. I also wanted to see two calls I did not see them and I wanted to see two calls as they happen. So now I give this feedback. Um I have this zoom thing everywhere. Okay. Um, so I tested it and it seems to be fine, but I have to wait till I see the final response. So I ask my question and then it's thinking and only when the final response is ready, I see the response. So what I want to have instead is I want to use the streaming API and I want to see events as they happen. So when we are making a tool call, I want to see this tool call. I want to see the parameters uh that we are getting. I want also to see the response we're getting from uh our tool. And this response should be collapsible. So it shouldn't take a lot of space. And yeah, I just want to have this interactivity so I know that um something is happening.

## 01:12:27 - 01:12:49

yeah. Well, to make it more interesting, what we can do is we can ask, hey, like explore the repository, ask multiple questions, but I think right now it's kind of okay. Like, let's not spend too much time on that. It's working. It's working the way I want. There's of course a lot of things we can improve, but it's already okay. Like, for example, here for the sources, we can

## Post angle

An agent UI should show streaming progress, tool calls, parameters, and tool results instead of waiting silently for the final answer.

## Clip recommendation

Use 01:08:26 - 01:09:31.

## Writing brief

Write a post for AI engineers about exposing agent internals in the product UI: stream tokens, show tool calls, show inputs and outputs, collapse noisy results, and make progress observable.
