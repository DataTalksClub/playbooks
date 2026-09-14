---
post_id: post_006
platform: linkedin
status: draft
---

Deploying an agent container to Lambda is not just changing Python code.

The code changes are only one part.

The deployment path needs several pieces:

- Build the container image
- Push it to ECR
- Define the Lambda function
- Create the Function URL
- Enable response streaming
- Pass environment variables
- Test locally
- Keep the deployment script repeatable

In the workshop, we used CloudFormation for the AWS resources and a deploy script to build, push, and deploy the image.

There were also small gotchas.

One example was Docker image metadata. The deployment hit an image manifest issue, and the fix involved disabling provenance metadata during the build.

This is the kind of detail you do not want to rediscover every time.

For infrastructure-heavy agent work, I like ending with a deployment document:

- What commands worked
- What failed
- What flags were needed
- What each script does
- What should be cleaned up later

That document becomes part of the system.

Full workshop materials: https://aishippinglabs.com/workshops/2026-05-05-lambda-agent-deployment

Recording: https://youtu.be/zoAvc8VU6Qs
