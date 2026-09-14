---
post_id: post_005
platform: linkedin
status: draft
---

If you use coding agents for longer tasks, think about where the work is running.

For a small local experiment, your laptop is fine.

But for long-running agent sessions, remote work becomes useful:

- The process keeps running if your laptop disconnects
- You can close the lid and come back later
- You can reconnect from another machine
- Bots and background jobs can keep running
- Your development environment is not tied to one physical laptop

In the workshop, I used a remote Linux machine and tmux.

The problem tmux solves is simple: if a process is attached directly to your SSH session, it dies when the connection dies. If it runs inside tmux, you can disconnect and attach again later.

This matters more now because coding agents often do multi-step work: reading a repo, editing files, running tests, fixing errors, and trying again.

You do not need this setup for every project.

But once you start running longer agent tasks, a remote machine plus tmux is a very practical upgrade.

Full recording: https://youtu.be/h84rcRezNM4
