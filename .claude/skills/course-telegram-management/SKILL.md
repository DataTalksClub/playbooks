---
name: course-telegram-management
description: Connect the DataTalks.Club course Telegram bot through Dapier, compare channel announcements with course facts, and prepare or execute approved course posting plans.
---

# Course Telegram Management

Use this skill for course channel operations. For announcement wording, read the `datatalks-event-promotion` skill and its `references/telegram.md`: organizational voice, no emojis/bold/hashtags, labelled links, current CET/CEST deadline followed by UTC. Save drafts in course copy banks or campaigns, never in this skill.

Read `courses/telegram-channel-management.md` for the five-course channel registry, message families, and comparison rules. For the current ML cohort, read `courses/campaigns/ml-zoomcamp-2026/processes/telegram-review-plan-2026-10-10.md` and its linked copy/calendar. These are plans; they do not establish delivery or approval.

## Connect through Dapier

Use the sibling `../dapier` checkout and its authenticated CLI. Pull its current branch when clean; preserve local changes. Commands below run from that checkout with `uv run dapier`. Read command help if the installed version differs.

```powershell
uv run dapier auth status
uv run dapier connections list
uv run dapier connections show <connection-id>
uv run dapier connections test <connection-id>
```

Select the verified course bot connection, not another Telegram bot with a similar name. Keep its connection ID, bot username/ID, and verified channel IDs in the nonsecret course registry. Never put a token in that registry, drafts, logs, command arguments, or Git.

The connection ID is `dtc-course-announcements`, bot `@dtc_course_announcements_bot`, numeric bot ID `8928085122`. Its local secret variable is `TELEGRAM_COURSE_BOT_TOKEN`. The agent name for Dapier grants is `course-telegram-management`. Creation/import does not establish channel administrator rights; check the registry and helper result for current access.

When importing a newly authorized bot, its token belongs in the repository's gitignored `.env`. Check `git check-ignore .env` before writing it. Read the named variable in process, then pass its raw value to the stdin of this child command, without displaying it or creating another credential file:

```text
uv run dapier connections import dtc-course-announcements --provider telegram --token-file -
```

Here `-` means stdin. A Python `subprocess.run` can provide `input=token` with text mode; never echo the token in a shell pipeline or place it in child command arguments. Verify `connections import --help` supports stdin in the installed CLI; update the clean checkout if necessary. Future API clients should receive secrets only through `dapier token exec`, which injects `DAPIER_ACCESS_TOKEN` into its child process. Do not use `token write` or print environment variables for routine operations.

For an authorized agent grant, use `uv run dapier grants save <grant.json>`. The nonsecret JSON contains `connection_id`, the authenticated DTC subject ID, `agent: "course-telegram-management"`, and `operations: ["use"]`. Use the operator identity verified by the current login; do not guess a subject or widen the grant. Obtain any action-time confirmation required by the active browser/tool before expanding channel or credential access.

For each intended channel, a human channel administrator adds the bot as an administrator. Request posting permission; add editing/pinning only for approved operations that need it. Do not grant adding administrators or deleting messages by default. Dapier connection grants restrict which agent can obtain the bot token; Telegram channel rights still determine what that token can do.

Use the read-only helper to resolve username ambiguities:

```powershell
uv run dapier token exec dtc-course-announcements --agent course-telegram-management -- python ../playbooks/.claude/skills/course-telegram-management/scripts/verify_bot.py --chat '@mlzoomcamp'
```

The helper calls `getMe`, `getChat`, and `getChatMember`; it reports identity and permissions without printing credentials. Quote `@channel` arguments in PowerShell to prevent splatting. Repeat `--chat` to inventory multiple channels: failures are recorded per channel and the remaining channels are still checked. Exit status 1 means at least one requested channel is unavailable or lacks posting permission. Resolve conflicting historical/YAML usernames by title, chat ID, and bot membership before updating the registry. A successful connection test alone does not prove the bot can post to every channel. Verify deployed static-token issuance support before invoking `token exec`; a local CLI/plugin change alone does not establish live support. Dapier's `chats` discovery lists observed chats; it is not an arbitrary `getChat` lookup and does not replace this helper.

Telegram Bot API does not provide arbitrary channel history. Compare recent public posts in Telegram Web/public channel pages, supplied exports, and recorded Dapier inbound events. Dapier webhook registration changes the bot's single webhook: inspect current ownership and the intended inbound workflow before replacing it. Do not call `getUpdates` against an existing webhook.

## Compare and plan

1. Read `courses/<course>/course.yaml`, its Telegram copy bank, and current campaign sources. Retrieve current platform deadlines/status through its read-only client; an old snapshot cannot establish that homework or project submissions are open today. Historical exports are calibration and cannot establish human authorship when only channel names appear.
2. Compare by course/cohort, module or project, message kind, destination chat ID, normalized text, essential URLs, and UTC deadline. Similarity flags a possible duplicate for review; it does not authorize overwriting a live message. Record any live message ID/permalink used as evidence.
3. Skip past-date announcements, already delivered matches, and superseded versions. Do not backfill missed posts silently. Keep later course dates unresolved when the platform has no verified cohort; flag certificate-rule conflicts before including a numeric promise.
4. Present a review table with row ID, exact destination, posting time and timezone plus UTC, message/file, current deadline and source, live comparison, and proposed action (`skip`, `send`, `edit`, `pin`, or `schedule`). Show unresolved rights, dates, and duplicate questions in the affected rows.

The user requested table review before executing the ML plan. Do not publish workflows, create active schedules, send test posts, pin, edit, or replay messages until the user explicitly approves the specific rows/actions. Bot creation and connection setup do not authorize posting.

## Execute approved rows

Use Dapier workflows with `connection_id` references so token values never appear in workflow files. Inspect the checked-out Telegram action schema and schedule help before producing YAML/JSON; do not infer a native Telegram scheduling parameter.

Local validation and dry-run review:

```powershell
uv run dapier workflows test <workflow.yaml> --event @<event.json> --strict
uv run dapier schedules list
uv run dapier schedules upcoming --days 7
```

`workflows test` defaults to dry-run; keep it that way before approval. `workflows save` stores a draft; `workflows publish` activates it. `schedules save <schedule.json>` can activate a schedule and requires approval. `schedules run` fires immediately and is a send action. Never use it to verify connectivity. Use a date-specific cron including the year for a single course post; compare the resulting next fire time with the approved UTC value and disable/remove completed schedules after verifying delivery.

Schedules use EventBridge Rules' six-field UTC cron, for example `cron(0 18 11 10 ? 2026)`. Convert the approved local time to UTC first; do not add a timezone suffix or use `at(...)`. A schedule JSON uses `name`, `expression`, optional `description`, and `enabled`; names are 2–32 lowercase letters/digits/hyphens. Keep any preparatory payload `enabled: false`; creating even a disabled live schedule still requires approval.

Maintain a nonsecret delivery ledger in the campaign: stable row ID/version, exact destination chat ID, content hash, approved timestamp, workflow/schedule IDs, run ID, result, and returned Telegram `message_id`. A scheduler retry or manual replay can duplicate an accepted `sendMessage`; a content hash alone is not an API idempotency key. If a timeout leaves delivery uncertain, inspect run records and the live channel before retrying. Mark it uncertain and stop that row until resolved. Edit/pin only the verified recorded message ID, and log the new version.

Keep course-platform credentials in a separate Dapier connection from Telegram. The CMP integration uses provider `cmp` and connection ID `cmp-production`. Verify that the deployed service supports this provider and that `connections show/test cmp-production` succeeds; a local plugin change alone does not establish live support.

```powershell
uv run dapier connections import cmp-production --provider cmp --token-file -
uv run dapier token exec cmp-production --agent course-telegram-management -- python ../playbooks/.claude/skills/course-telegram-management/scripts/read_course.py ml-zoomcamp-2026
```

The import command also receives its raw key through child-process stdin using the same procedure; never start it interactively expecting to paste a visible key.

The CMP provider's connection verification request is GET `/api/courses/`; this establishes platform access, not a named-user identity. The helper reads `DAPIER_ACCESS_TOKEN`, authenticates with `Authorization: Token <value>` (not Bearer), and makes one GET `/api/courses/<slug>/`. It returns cohort metadata, homework/project dates and statuses, retrieval time, and source URL. Replace the slug for another verified course. Errors are sanitized without printing headers or credentials. Recommended module posting dates are editorial inferences from that sequence unless a source explicitly provides them. Telegram's provider cannot store a CMP API key. Never invent generic provider syntax or embed its key in tracked workflow files.
