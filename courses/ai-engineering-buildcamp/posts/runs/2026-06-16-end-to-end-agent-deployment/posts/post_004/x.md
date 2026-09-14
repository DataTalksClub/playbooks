---
post_id: post_004
platform: x
status: draft
---

1/7

Coding agents are useful for learning deployment.

They should not have direct access to production.

2/7

For a toy app, it is fine to let an agent help you experiment.

That is how you learn the commands, deployment platform, and config.

3/7

For production, add boundaries:

- Dev/prod environments
- Tests before deploy
- Auto deploy to dev
- Manual promotion to prod
- Secrets through CI/CD

4/7

The key point is access control.

If the agent cannot reach production, it cannot accidentally change production.

5/7

The agent can still help.

It can write the workflow, docs, tests, and deployment config.

But production promotion should go through a controlled path.

6/7

For a small project, this can be simple:

- One dev service
- One prod service
- GitHub Actions
- Test step
- Manual deploy step

7/7

Use coding agents for speed.

Use CI/CD and permissions for safety.

Recording: https://youtu.be/h84rcRezNM4
