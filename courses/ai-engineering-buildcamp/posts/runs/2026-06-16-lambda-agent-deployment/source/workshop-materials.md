# Workshop Materials Context

Source pages:

- Previous workshop: https://aishippinglabs.com/workshops/2026-04-21-end-to-end-agent-deployment
- This workshop: https://aishippinglabs.com/workshops/2026-05-05-lambda-agent-deployment

Visible context from the Lambda workshop page:

- Title: Deploying an Agent to AWS Lambda
- Date: May 5, 2026
- The session starts from the FastAPI service deployed to Railway in the previous workshop.
- The workshop strips out FastAPI and swaps in a custom AWS Lambda runtime.
- The runtime handles both the static frontend and the streaming agent API.
- The deployment uses one container image as a Lambda Function URL with SSE streaming.
- A coding agent, Codex, does most of the code-writing, with prompts quoted in the materials.
- The session also discusses how to work with agents, when to trust them, and when to slow down and read the code.

Visible architecture notes from the page:

- Frontend UI uses vanilla JavaScript and SSE.
- Lambda Function URL receives frontend and API requests.
- `backend/lambda_runtime.py` handles routing, static file serving, and SSE streaming.
- The agent loop, search tool, renderer abstraction, and frontend remain unchanged from the previous workshop.
- FastAPI is removed.
- The Dockerfile is rebased on `public.ecr.aws/lambda/python:3.14`.
- `deploy.sh` builds a container image, pushes it to ECR, and deploys a CloudFormation stack.
- The CloudFormation stack creates the Lambda function and a Function URL with `RESPONSE_STREAM` invoke mode.
- Railway and the GitHub Actions promotion workflow are removed.
- Lambda changes the cost model: instead of paying for an always-on server, Lambda is paid per invocation, which can fit small tools and agents that run occasionally.
