---
post_id: post_002
platform: linkedin
status: draft
---

A coding agent should never have a path to production.

I learned this the expensive way after one of my agents dropped a production database. That incident changed how I think about cloud access for agents.

Now my setup is different.

Agents run on a remote sandbox server. The server is disposable. If an agent breaks it, I can recreate it.

Real deployments go through CI/CD. Agents can write Terraform and push changes to GitHub, but I apply production infrastructure changes myself.

When an agent needs to experiment with AWS, it gets access only to a separate sandbox account.

That access is:

- Temporary
- Scoped
- Revocable
- Not connected to production

For this I use the same credential endpoint pattern I originally built for workshops. It gives the agent AWS access for a limited time, without putting long-lived keys on the machine.

I wrote about the full system in my latest newsletter:

https://alexeyondata.substack.com/p/the-system-i-built-for-aws-access

The practical rule is simple:

If an agent can reach production, the setup is wrong.
