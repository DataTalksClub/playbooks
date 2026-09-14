---
post_id: post_001
platform: linkedin
status: draft
---

I needed to give 50 or 60 workshop participants access to AWS.

They had to provision resources from their own machines. I didn't want them to install anything. I didn't want to copy AWS keys into a repo, email, chat, or slide.

And I definitely didn't want them anywhere near my main AWS account.

So I built a credential endpoint.

The short version:

- A Lambda assumes an AWS role
- The AWS SDK fetches temporary credentials from a URL
- The environment points to that URL with `AWS_CONTAINER_CREDENTIALS_FULL_URI`
- The workshop runs from GitHub Codespaces
- Participants get access without ever seeing a long-lived key

What started as a workshop setup later became useful for coding agents too.

I don't want agents to have permanent access to AWS. I want them in a sandbox account, with temporary credentials, and with a way to turn access off.

I wrote about the full system in my latest newsletter:

https://alexeyondata.substack.com/p/the-system-i-built-for-aws-access

The rule I follow now is simple:

Before anything gets AWS access, I ask:

- Is it scoped to a sandbox?
- Is it temporary?
- Can I revoke it?
- Can it reach production?

If the answer to the last question is yes, I stop and fix that first.
