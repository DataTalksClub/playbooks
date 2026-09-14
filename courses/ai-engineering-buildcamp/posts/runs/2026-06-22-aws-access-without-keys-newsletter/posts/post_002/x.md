---
post_id: post_002
platform: x
status: draft
---

1/6

A coding agent should never have a path to production.

I learned this the expensive way after one of my agents dropped a production database.

That incident changed how I think about AWS access for agents.

2/6

My setup now:

- Agents run on a remote sandbox server
- The server is disposable
- Real deployments go through CI/CD
- Production infra changes are applied from my laptop

Agents can write the files. They don't get production AWS access.

3/6

Sometimes agents still need AWS.

For example, when I want them to experiment with a new service, find required resources, or test permissions.

For that, I use a separate sandbox AWS account.

4/6

The agent gets temporary credentials for that sandbox account.

No long-lived keys on the machine.
No access to production.
No permanent AWS credentials sitting in a project folder.

5/6

This uses the same credential endpoint pattern I built for offline workshops:

A Lambda assumes a role, returns temporary credentials, and the SDK fetches them through `AWS_CONTAINER_CREDENTIALS_FULL_URI`.

6/6

I wrote the full setup here:

The System I Built for AWS Access Without Keys

https://alexeyondata.substack.com/p/the-system-i-built-for-aws-access
