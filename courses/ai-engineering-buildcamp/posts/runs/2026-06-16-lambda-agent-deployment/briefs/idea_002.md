# Handoff Brief: Isolate AWS before giving agents credentials

Source: /Users/valeria/.codex/content-runs/2026-06-16-lambda-agent-deployment/source/transcript.json

## 00:08:19 - 00:11:14

So this remote machine doesn't have access to my AWS. This is on purpose. I do not want agents. I am running quite a few agents here. I don't want these agents to have access to my um to my production uh to my AWS account because there are some things that are in production that are running there. Um so I don't them I don't want them to see these things. Uh what I want to do now is I probably I want to create a new account for AWS and then I can do whatever I want uh in this account and not be afraid and I will not be afraid of uh the agent accidentally nuking some some of the infrastructure. So for that um I'll probably I'll create a folder that I'll call temporary or AWS experiments. So right now I'm on my laptop and uh on my laptop I do have a account. So if I do AWS STS get caller identity. Um so I did I make a typo? Yes. So I so this is kind of who am I but for AWS. So this is my um user ID this is my account. So uh this is actually my uh administrator access on this account. I deploy uh many things like for example the course management platform from data talks club this one is deployed there or um for this AI shipping labs. Uh I'm still working on the jungo website for this. Um the deaf environment is already there and we have something that looks like pro environment. Um, so they are both deployed there. So I don't want my agents to be able to change change things there. But um, what I want to do is I want to uh create a new account and this account uh, I can just let agents play with this account. So what I will do, I'll use Codex. I wonder if I actually have it installed on my computer. Yeah. So, and then for codex, I because I don't remember how do I actually why it's doing this. I don't actually remember how um to create an account. So, I'll say um hey, I want to create a separate account in AWS for experiments and I want to have a separate billing for this account. Um um please uh create an account uh that is uh connected to my main account and create an admin user for that account and give me credentials. So then these credentials I'm going to use for um

## 00:17:31 - 00:18:15

>> Yeah. Um somewhat there's >> somehat >> there's a level of trust that I'm hearing that you have for these coding agents, right? So I mean do you trust them completely? Not you can't trust them completely, right? >> Yes. That's why I'm creating an account right now because I don't want them to poke around my production account. I mean here I know more or less what it's going to do. So I know that it will not be trying to uh drop my production database while creating an account. >> Mhm. Um so yes I have some level of trust and uh I think at some point um um so the the comparison I have in my mind

## 00:25:04 - 00:25:39

I temporary STS credentials. Ah that's actually pretty cool. So instead of giving a complete access to um this production environment, we just give it for the session. Um, I want to have uh the M variables that I can paste and give me access for 2 hours.

## 00:42:17 - 00:44:27

>> Mhm. >> Or bash m something like that instead. >> I usually don't do this um because I prefer to have separate keys for each project. So in case um something happens to my key, it hasn't happened but in case something happens like my accident, my key is accidentally uh leaked uh for some reasons or I don't know then I know which project is compromised and then I can just simply um update this project. >> Understood. >> Yeah. So this is I don't I'm not saying this is the right approach. >> There are benefits of just putting this in basher because you don't need to worry about these things. it's it's always there, right? But because it's always there, um it's also easier to cuz any script that runs on your computer can access your environment variable, right? And then um your key can get uh leaked. Again, it hasn't happened to me, but uh reading all the stories on the internet that uh there was a library that got compromised and then it stole all the API keys. Um I'm a bit I'm trying to be careful. you cannot be u like I'm not like super paranoid about this but I'm also trying not to be like um how to say like I'm trying to be a bit more um careful >> it's interesting I would have thought it's actually more secure to put it into a bash RC >> yeah because um like I can run something like and then I have have access to all the environment variables I can run it inside my um inside Python. So if you run Python, you have this import OS and run and then you have access to all the environments. It means that if you have your uh credential inside your BRC, any process that runs on your computer can have access to this. >> Okay. Okay. >> Uh while if it's right, so then it's only um >> yeah in the designated project. Okay. Awesome. Yeah, thanks.

## Post angle

Before letting a coding agent touch AWS, isolate the experiment from production with a separate account and short-lived, project-scoped credentials.

## Clip recommendation

Use 00:08:19 - 00:11:14.

## Writing brief

Write a security-minded post about safe AWS access for agent-assisted deployment.
