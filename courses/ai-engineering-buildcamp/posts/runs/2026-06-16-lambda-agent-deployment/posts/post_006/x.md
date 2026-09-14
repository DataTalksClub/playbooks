---
post_id: post_006
platform: x
status: draft
---

1/7

Deploying an agent container to Lambda is not just changing Python code.

The deployment path has its own moving parts.

2/7

You need to:

- Build the image
- Push to ECR
- Define Lambda
- Create Function URL
- Enable response streaming

3/7

In the workshop, we used CloudFormation for AWS resources and a deploy script for build, push, and deploy.

4/7

There were small gotchas.

One was Docker image metadata. Lambda rejected the image until provenance metadata was disabled during build.

5/7

These details are easy to forget.

They are exactly the kind of thing that should go into deployment docs.

6/7

Document:

- Commands that worked
- Failed attempts
- Required flags
- What each script does
- What to clean up later

7/7

For agent-assisted infrastructure work, the deployment document becomes part of the system.

Recording: https://youtu.be/zoAvc8VU6Qs
