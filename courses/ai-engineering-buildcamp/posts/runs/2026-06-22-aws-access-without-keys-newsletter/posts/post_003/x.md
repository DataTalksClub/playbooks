---
post_id: post_003
platform: x
status: draft
---

1/6

Sometimes I want an agent to experiment with AWS while I'm away from my laptop.

But I don't want admin AWS credentials on my phone, and I don't want the agent hitting AWS whenever it wants.

2/6

So I reused the credential endpoint I built for workshops.

The remote sandbox points its AWS credential URI at a Lambda.

Then I built a small phone app that toggles that Lambda on and off.

3/6

When the toggle is on, the Lambda returns temporary AWS credentials.

When it is off, the sandbox asks for credentials and fails.

The agent only gets access during the window I open.

4/6

For example:

I connect to the sandbox from my phone, turn AWS access on for 15 minutes, let the agent run the experiment, then turn access off again.

5/6

This is the same mechanism I now use for:

- Offline workshops
- Coding agents in a sandbox account
- Phone-controlled AWS access

Temporary, revocable access without long-lived keys on the machine.

6/6

I wrote about the full system in my latest newsletter:

The System I Built for AWS Access Without Keys

https://alexeyondata.substack.com/p/the-system-i-built-for-aws-access
