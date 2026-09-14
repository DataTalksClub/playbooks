---
post_id: post_002
platform: linkedin
status: draft
---

Before giving a coding agent AWS credentials, decide what it is allowed to break.

In the Lambda deployment workshop, I did not give the remote machine access to my production AWS account.

That was intentional.

The safer setup was:

- Create a separate AWS account for experiments
- Keep production credentials away from the agent environment
- Use temporary credentials for the session
- Keep credentials project-scoped instead of global
- Rotate or remove them when the experiment is done

This changes the question from:

"Do I fully trust the agent?"

to:

"What damage can happen if the agent makes a mistake?"

That is a much better question.

Agents can write useful deployment scripts. They can create CloudFormation templates. They can help with ECR, Lambda URLs, Docker images, and local testing.

But AWS credentials are not just another config value.

If they are in your global shell environment, any process on the machine can potentially read them. If they are pasted into a chat, they can end up in logs or transcripts. If they point to production, a mistake can become expensive.

For agent-assisted infrastructure work, isolation is part of the workflow.

Full workshop materials: https://aishippinglabs.com/workshops/2026-05-05-lambda-agent-deployment

Recording: https://youtu.be/zoAvc8VU6Qs
