# ML Zoomcamp 2026 announcement sources

Checked October 10, 2026. The course-management-agent repository was cloned to `../course-management-agent` beside playbooks. Its `AGENTS.md` and `course-content` skill were read. Authentication stayed inside the Hetzner process, which read the existing `.env`; no key was printed, saved locally, or copied to playbooks.

## Schedule

Final planning refresh: [live review payload](platform-live-review-2026-10-10.json), retrieved at **2026-10-10T20:47:43.844296Z** through `Dapier token exec cmp-production --agent course-telegram-management` using a read-only GET. An independent comparison verified all 22 future-plan deadline/state rows and the course start/end dates against this payload with zero mismatches. The payload contains no credentials. [Review plan](../processes/telegram-review-plan-2026-10-10.md) and its CSV record this verification; posting dates remain editorial recommendations because CMP supplies no module release dates.

[Production API snapshot](platform-2026-10-10.json) records the course metadata, homework deadlines, project deadlines, and states from a GET request to `https://courses.datatalks.club/api/courses/ml-zoomcamp-2026/`. The generated OpenAPI specification was also read to confirm the route.

The cohort starts September 14, 2026 and ends January 25, 2027. Every homework and project deadline is at 23:00 UTC. Telegram copy converts these to Europe/Berlin: 01:00 CEST the following day before the autumn clock change, and 00:00 CET afterward. The end date is the platform's course end date, not a promised certificate delivery date.

The old cohort brief had homework dates and the midterm submission date one week early. Those rows now follow the API. The campaign YAML already had the correct homework and submission dates, but incorrectly listed November 16 as the midterm peer-review deadline. The confirmed date is November 23 at 23:00 UTC.

## Materials and examples

All nine homework files under [the 2026 homework folder](https://github.com/DataTalksClub/machine-learning-zoomcamp/tree/main/cohorts/2026/homework) were fetched. None had a draft marker. The existing 2026 announcement summaries match the course's fuel-efficiency, lead-scoring, and hair-classification homework descriptions.

Use durable curriculum and materials from `courses/ml-zoomcamp/course.yaml`, with the deployment, PyTorch, serverless, and Kubernetes workshop guidance retained. The reusable course copy now contains placeholders; the campaign copy contains the resolved year, homework descriptions, platform links, and deadlines.

[Historical source messages](../../../ml-zoomcamp/copy-bank/telegram/historical-announcements-2026-10-10.md) and [extraction method](../../../../research/telegram/README.md) provide calibration. Human authorship is unverified. The drafts follow the repository's Telegram style: a direct opening, practical topics, labelled links, local and UTC deadlines, and Slack for questions.

## Unresolved certificate rule

The API reports one passing project with a passing score of 7. [Published certification documentation](https://datatalks.club/docs/courses/zoomcamp-logistics/certification/) says ML learners need two of the three projects. The existing reusable metadata also says two. These sources disagree.

The campaign preserves the platform settings as observed and records the conflict. Drafts link to the published requirements without claiming that either one or two projects is the confirmed 2026 rule. No external settings were changed. Resolve this discrepancy before announcing a numerical certificate requirement.

## Posting dates

The API provides course start/end dates and submission/review deadlines, not individual module release dates. The Telegram calendar's posting dates are editorial recommendations. Already elapsed announcements and homework reminders are marked as past reference. Nothing has been posted or scheduled.

## Verification

The repository's `ruby scripts/validate_courses.rb` passed for all seven course YAML files. Ruby was unavailable locally and on the Hetzner host, so the unchanged validator and current YAML/schema files ran in a temporary Ruby container with a read-only mount.

All 28 drafts were checked for resolved placeholders, Telegram's 4,096-character limit, calendar coverage, internal file links, and deadline agreement with the API snapshot. Every homework and project timestamp was converted with the Europe/Berlin timezone database. YAML start/end dates and every deadline match the snapshot.

The full `stylint` check ran on the 28 generated message files without ignored rules. Prose findings were fixed. Remaining findings are the labelled bare links and deadline labels required by the repository's Telegram guide, plus three false positives for the literal Car Fuel Efficiency dataset name. The checker is not a clean pass under its general prose rules; those rules conflict with this channel's required format. Historical extracted text was preserved and excluded from style rewriting.
