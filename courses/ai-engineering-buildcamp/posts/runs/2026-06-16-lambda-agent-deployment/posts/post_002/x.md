---
post_id: post_002
platform: x
status: draft
---

1/7

Before giving a coding agent AWS credentials, decide what it is allowed to break.

This is the wrong question:

"Do I fully trust the agent?"

2/7

The better question:

"What damage can happen if the agent makes a mistake?"

3/7

For the Lambda workshop, I did not give the remote machine access to my production AWS account.

That was intentional.

4/7

The safer setup:

- Separate AWS account
- Temporary credentials
- Project-scoped env file
- No production access
- Rotate/remove after the experiment

5/7

Agents can help with ECR, CloudFormation, Lambda URLs, Docker images, and deploy scripts.

But AWS credentials are not just another config value.

6/7

If credentials are global, more processes can read them.

If credentials point to production, small mistakes can become expensive.

7/7

For agent-assisted infrastructure work, isolation is part of the workflow.

Recording: https://youtu.be/zoAvc8VU6Qs
