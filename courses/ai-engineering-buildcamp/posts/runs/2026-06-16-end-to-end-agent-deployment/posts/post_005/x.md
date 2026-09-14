---
post_id: post_005
platform: x
status: draft
---

1/6

If you use coding agents for longer tasks, think about where the work is running.

For small local experiments, your laptop is fine.

2/6

For longer sessions, a remote machine helps:

- Work keeps running after disconnects
- You can close the laptop
- You can reconnect later
- Background jobs keep running

3/6

In the workshop, I used a remote Linux machine and tmux.

tmux solves a simple problem.

4/6

If a process is attached directly to SSH, it dies when the SSH connection dies.

If it runs inside tmux, you can disconnect and attach again later.

5/6

This matters more with coding agents.

They may read the repo, edit files, run tests, inspect errors, and try again.

That work can take time.

6/6

You do not need this for every project.

But for long-running agent work, remote machine + tmux is a practical upgrade.

Recording: https://youtu.be/h84rcRezNM4
