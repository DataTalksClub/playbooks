---
post_id: post_001
platform: x
status: draft
---

1/6

I needed 50 or 60 workshop participants to use AWS from their own machines.

No keys to copy. Nothing to install. No access to my main AWS account.

So I built a credential endpoint.

Full write-up:
https://alexeyondata.substack.com/p/the-system-i-built-for-aws-access

2/6

The endpoint returns temporary AWS credentials in the format the SDK expects.

The environment points to it with:

`AWS_CONTAINER_CREDENTIALS_FULL_URI`

Then the AWS CLI, boto3, and SDKs can fetch and refresh credentials automatically.

3/6

For the workshop, this meant:

- GitHub Codespaces as the environment
- A separate AWS sandbox account
- A Lambda that assumes a role
- No long-lived keys for participants

They could run the workshop, and I could turn access off later.

4/6

The same pattern turned out to be useful for coding agents.

I don't want agents to have permanent AWS access. I want a sandbox account, temporary credentials, and a clear way to revoke access.

5/6

This now covers three cases:

- Offline workshops
- Coding agents experimenting with infra
- A phone-controlled toggle for sandbox AWS access

Same mechanism: temporary, revocable access without long-lived keys on the machine.

6/6

I wrote the full story here:

The System I Built for AWS Access Without Keys

https://alexeyondata.substack.com/p/the-system-i-built-for-aws-access
