---
post_id: post_004
platform: linkedin
status: draft
---

Coding agents are useful for learning deployment.

They should not have direct access to production.

In the workshop, I used an agent to help deploy a toy app. That is fine for experimentation. The app was not critical, and the goal was to learn the steps.

For production, I would put more boundaries around the process:

- Separate dev and prod environments
- Tests before deployment
- Automatic deployment to dev
- Manual promotion to prod
- Production credentials kept away from the coding agent
- Secrets passed through CI/CD, not pasted into chat

The important part is access control.

If the agent cannot reach production, it cannot accidentally change production.

This is why CI/CD matters. The deployment path becomes explicit. The agent can help write the workflow, tests, docs, and configuration. But the actual production promotion goes through a controlled process.

For a small project, this can be simple: one dev service, one prod service, GitHub Actions, a test step, and a manual deploy step.

For a larger project, you may also separate cloud accounts, Terraform state, databases, and permissions.

Start simple, but keep the boundary clear.

Full recording: https://youtu.be/h84rcRezNM4
