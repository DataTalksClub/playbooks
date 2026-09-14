# Handoff Brief: Run coding agents where the work can continue

Source: /Users/valeria/.codex/content-runs/2026-06-16-end-to-end-agent-deployment/source/transcript.json

## 00:32:51 - 00:33:17

here. Um I also want to like since I use SSH what I also want to do is I want to use a tuk or t-muk I don't know how I pronounce it. um in order to create a session. So if for for some reasons my SSH SSH session gets uh interrupted then like the process actually keeps running. Uh so for this thing I have an utility

## 00:42:28 - 00:45:22

So I start a codex session and then my connection is interrupted. So in this case what happens is everything that leaves that is attached to this uh SSH session dies with the connection right. So if an agent is doing something and my Wi-Fi uh interrupts or I need to uh I don't know close my laptop laptop and go somewhere the work will stop in order to avoid that. Um so I don't know I will probably not be able to uh model this right now. uh I don't want to interrupt my connection. Uh but the thing is like yeah it will stop working. So in order to um deal with this problem you can use timuku. TMUX is I think it's terminal multiplexer or something like this. Uh so it actually allows you to disconnect to run processes that are not attached to your SS SSH session. So you do timuk new session and then uh codex right and then inside this session you do codex yellow and then say u tell me about about this project and right now what I can do is I can disconnect from this and I go I can go I don't know for a walk I can come back and then I can connect to my session again and now I need to write tmuk attach minus t uh codex right so it's different syntax so it was first it was new session minus s and now in order to attach I use this syntax right so you can see that this is different so for me it was a bit annoying and then I also need to type a lot of things so I built a small wrapper that lets me just do this codex t codex >> so If it does not exist, it creates a new session. If it exists, it attaches to this session. Right. >> But realistically, not realistically, but if we're just testing things on our local machines, >> you don't need that. >> Don't really need to do this. >> Yes. You don't need to do that. Exactly. Uh, and then one other thing I like is because I can attach sessions instead of writing like big name, long name, I can just do T1 and then I would attach to this collection, right? So this is very convenient if you're running things remotely, right? So for me um cuz for example I travel right now I'm in Amsterdam. Um and then I don't know before um I fly back to Berlin in my plane on my plane I can give an instruction to the agent. I can close my laptop and this thing will continue working. It's very

## 00:45:45 - 00:46:31

>> Yeah. Like if you want this thing to continue run running when you close the lid of your laptop then you need a remote machine. And so for me for example I have like different uh telegram bots uh that actually require a machine that is always up and running. I have long running codeex and uh code code sessions. So for me it's just I don't want to keep my computer on all the time. >> Mhm. And also computers um like my old computer broke um so I also want to have an environment that is you know independent from a specific piece of machines like specific piece of hardware specific laptop. >> Mhm. >> But for you like when you need it I think you'll understand it before you

## Post angle

For long-running coding-agent work, a remote machine plus tmux keeps work alive when the laptop disconnects, closes, or moves networks.

## Clip recommendation

Use 00:42:28 - 00:45:22.

## Writing brief

Write a practical workflow post explaining why long-running coding-agent work benefits from a remote machine and tmux. Keep it grounded and avoid telling every user they need this setup.
