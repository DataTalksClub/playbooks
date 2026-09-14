---
post_id: post_003
platform: linkedin
status: draft
---

Sometimes I want an agent to experiment with AWS while I'm away from my laptop.

I don't want admin AWS credentials on my phone.

I don't want to SSH into my laptop from somewhere outside.

And I don't want an agent hitting AWS whenever it wants, especially if it can provision expensive resources.

So I reused the credential endpoint I built for workshops.

The remote sandbox points its AWS credential URI at a Lambda. Then I built a small phone app that toggles that Lambda on and off.

When the toggle is on, the Lambda returns temporary credentials.

When it is off, the sandbox asks for credentials and fails.

The access can be limited to a short window, for example 15 minutes or an hour. I can turn it on from my phone, let the agent run an experiment in the sandbox, and turn it off again.

This is the third use case for the same mechanism:

- Workshops with 50 or 60 people
- Coding agents in a sandbox AWS account
- Phone-controlled temporary AWS access

I wrote the full story in my latest newsletter:

https://alexeyondata.substack.com/p/the-system-i-built-for-aws-access
