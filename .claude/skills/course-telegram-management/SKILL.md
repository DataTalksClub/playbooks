---
name: course-telegram-management
description: Manage DataTalks.Club course Telegram access through Dapier, compare announcements with current course facts, and schedule approved posts in Telegram's native queue.
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

The connection ID is `dtc-course-announcements`, bot `@dtc_course_announcements_bot`, numeric bot ID `8928085122`. Its local secret variable is `TELEGRAM_COURSE_BOT_TOKEN`. The agent name for Dapier grants is `course-telegram-management`. All five registry channels were verified with posting enabled on October 10, 2026. Read the registry permission caveat: Web A shows only posting selected, but the API also reports direct-message management enabled. Recheck the helper result for current rights; creation/import alone does not establish access. The helper reports other optional rights for least-privilege verification.

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

The user's current preference is Telegram's native scheduled-message queue. Use an authorized Telegram user session in Telegram Web to schedule the approved text directly in the destination channel. Dapier remains the credential store and read-only CMP access route; do not create a separate Dapier workflow or EventBridge rule for each post.

For the observed Web A controls, read `courses/campaigns/ml-zoomcamp-2026/processes/telegram-native-scheduling.md`. Paste the exact approved plain text into the channel composer, right-click **Send Message** (normal click sends immediately), choose **Schedule Message**, select the native calendar month/day, and set the separate HH/MM fields. Leave **Repeat: Never**. Verify the final button's date/time, submit once, then inspect **Scheduled Messages** for the full text and intended time. Inspect UI state after each action; intermittent locator failures do not justify retrying an uncertain final schedule without checking the queue.

Before queueing, refresh live CMP facts, compare recent channel posts and the native scheduled-message queue, and check the exact approved file hash. The authorized Telegram user must have the required channel rights; the bot's API permissions do not establish that user's rights. Follow the active browser skill and observed UI controls for scheduling.

For each row, verify the destination, full text, and date/time in Telegram's scheduling UI. Determine the browser/session timezone rather than assuming it matches Berlin. Convert the approved UTC instant into the displayed UI timezone using timezone-aware conversion. Berlin changes from CEST to CET on October 25, 2026: the approved 09:00 Berlin slot is 07:00 UTC before the change and 08:00 UTC afterward. Telegram UI wall-clock values must represent that approved instant, including dates across midnight.

After each schedule action, reopen or inspect the native queue and verify the exact message, displayed time, and destination. Record the approved UTC instant, actual UI timezone/time, file hash, scheduled-message identifier if exposed, and evidence. A clicked schedule button alone does not prove queueing. If the UI result is uncertain, inspect the queue before retrying to avoid duplicate messages. After delivery, record the actual message ID/permalink and send time when available.

Native scheduled messages do not run a fresh CMP check at send time. Deadlines, form state, materials, or certificate rules that change after queueing require a manual review and edit/cancel of the affected queued message. Recheck state-dependent homework/submission/peer-review reminders before their release; do not imply an automatic platform gate remains in effect.

Maintain a nonsecret ledger in the campaign with stable row ID/version, exact destination chat ID, content hash, approval, planned UTC time, observed queue state, and delivery evidence. For ML2026, use `courses/campaigns/ml-zoomcamp-2026/processes/telegram-native-execution-2026-10-11.json`. Edit/pin only an identified message with approval and log the new version.

The user authorized the reviewed 22-row ML2026 plan, then requested replacing its Dapier per-post flows with native Telegram scheduling. This migration requires retiring the old rules/workflows and independently verifying native queue entries. The native execution ledger establishes which rows are actually queued; do not infer that all 22 are complete from approval or an older Dapier manifest. Reconcile both queues before adding a row so the retired automation cannot duplicate it. Other courses still need their own approved plans.

Keep course-platform credentials in a separate Dapier connection from Telegram. The CMP integration uses provider `cmp` and connection ID `cmp-production`. Verify that the deployed service supports this provider and that `connections show/test cmp-production` succeeds; a local plugin change alone does not establish live support.

```powershell
uv run dapier connections import cmp-production --provider cmp --token-file -
uv run dapier token exec cmp-production --agent course-telegram-management -- python ../playbooks/.claude/skills/course-telegram-management/scripts/read_course.py ml-zoomcamp-2026
```

The import command also receives its raw key through child-process stdin using the same procedure; never start it interactively expecting to paste a visible key.

The CMP provider's connection verification request is GET `/api/courses/`; this establishes platform access, not a named-user identity. The helper reads `DAPIER_ACCESS_TOKEN`, authenticates with `Authorization: Token <value>` (not Bearer), and makes one GET `/api/courses/<slug>/`. It returns cohort metadata, homework/project dates and statuses, retrieval time, and source URL. Replace the slug for another verified course. Errors are sanitized without printing headers or credentials. Recommended module posting dates are editorial inferences from that sequence unless a source explicitly provides them. Telegram's provider cannot store a CMP API key. Never invent generic provider syntax or embed its key in tracked workflow files.
