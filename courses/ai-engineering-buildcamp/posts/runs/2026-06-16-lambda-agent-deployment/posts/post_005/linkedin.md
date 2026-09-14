---
post_id: post_005
platform: linkedin
status: draft
---

One useful way to work with coding agents:

Get a working version first.
Then simplify it.

In the Lambda workshop, the agent produced a version that worked locally. I did not understand half of the code at first.

That was okay for a temporary milestone.

The next step was not to ship it blindly. The next step was to inspect it:

- Why is this file needed?
- Why is there a bootstrap script?
- Why is this entrypoint different from a normal Lambda handler?
- Why did it create this local server?
- Which parts are Lambda-specific?
- Which parts are application logic?

Agents often create code that works but is more complicated than necessary.

This is especially true when the platform has awkward details: Lambda runtime APIs, Docker entrypoints, local emulators, ECR, CloudFormation, and streaming responses.

The practical workflow is:

1. Let the agent explore and get something running
2. Commit the working state
3. Ask it to explain the architecture
4. Remove or simplify code you do not understand
5. Keep the parts that have a clear reason

Working code is a checkpoint, not the finish line.

Full workshop materials: https://aishippinglabs.com/workshops/2026-05-05-lambda-agent-deployment

Recording: https://youtu.be/zoAvc8VU6Qs
