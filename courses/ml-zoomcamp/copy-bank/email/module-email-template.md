[View this email in your browser]({{ browser_view_url }})

# {{ module_email_headline }}

Hey there,

This week, we {{ module_action }} [Module {{ module_number }}: {{ module_title }}]({{ module_url }}).

{{ module_intro_paragraph }}

## Module {{ module_number }}

In this module, you will:

- {{ module_highlight_1 }}
- {{ module_highlight_2 }}
- {{ module_highlight_3 }}
- {{ module_highlight_4 }}
- {{ module_highlight_5 }}

Important links:

- [Module {{ module_number }} materials]({{ module_url }})
- [Course playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hLuyafXPyhTdbF4s_uNhc43)
- [Course platform]({{ course_platform_url }})
{{ optional_homework_link }}
{{ optional_submission_link }}

{{ optional_deadline_line }}
{{ optional_submission_closes_line }}

[Start Module {{ module_number }}]({{ module_url }})

## Where to Find Materials

All course materials live in the [GitHub repository](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp).

Each module has its own folder, for example `01-overview`, `02-end-to-end`, or `03-mcp`. Cohort-specific homework and announcements live in the `cohorts/{{ cohort_year }}` folder.

Lectures are pre-recorded and linked from GitHub. The [YouTube playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hLuyafXPyhTdbF4s_uNhc43) contains the course videos. If we add updated videos, workshops, or live-session recordings, we will announce them in Slack and Telegram.

## Self-Paced vs. Live Cohort

The lectures and course materials are available for self-paced learning. You can watch the videos, read the docs, and build the projects at your own pace.

The live cohort adds deadlines, scored homework, leaderboard participation, peer review, community support, and certificate eligibility.

If you want to submit homework, complete the final project, and earn a certificate, you need to participate in the live cohort.

## Homework {{ module_number }}

{{#if homework_available}}
For [Homework {{ homework_number }}]({{ homework_url }}), you will {{ homework_summary }}.

The goal is not to blindly accept generated code. The goal is to use AI tools, inspect the result, run it, debug it, test it, and document what you did.

Due date: {{ homework_deadline }}.

[Submit Homework {{ homework_number }}]({{ homework_submission_url }})

### How Homework Works

For homework, you are expected to:

- Work through the tasks locally.
- Use the tools and workflows introduced in the module.
- Publish your solution in a public GitHub repository or similar place when the form asks for a link.
- Submit everything through the course platform before the deadline.

Each homework has a fixed deadline. After the deadline passes, the submission form closes automatically, and late submissions are not accepted.

Homework submissions are available only during the live cohort. In self-paced mode, you can still complete the homework for practice, but you will not receive credit.

Submissions also appear on the [leaderboard]({{ leaderboard_url }}).

You can also get extra points by sharing your learning publicly with the hashtag `#aidevtools` and tagging Alexey Grigorev or DataTalksClub.
{{/if}}

{{#unless homework_available}}
There is no graded homework for this module.

Use this week to go through the materials, run the examples, and keep moving on your final project. If you are following the live cohort, check the [course platform]({{ course_platform_url }}) for the next open submission.
{{/unless}}

{{#if homework_available}}
## Homework Grade

Homework grade = points for questions + 1 point for the FAQ + a maximum of 7 points for learning in public.

Learning in public gives up to 7 points, depending on how many platforms you shared your post on and the quality of the post.

The FAQ contribution is worth 1 point. If you want to get a score for it, contribute to the [FAQ repo](https://github.com/DataTalksClub/faq) and add a link to your PR to your homework submission.

Optional questions are scored as well. Read the submission form carefully, because the details are listed there.

The homework is for practice. It does not affect your certificate.
{{/if}}

## Got Stuck?

Having questions is a normal part of the learning process.

Here is what to do:

- Check the [AI Dev Tools Zoomcamp FAQ](https://datatalks.club/faq/ai-dev-tools-zoomcamp.html).
- Check the [course documentation](https://datatalks.club/docs/courses/ai-dev-tools-zoomcamp/).
- Check the [how to ask questions guide](https://datatalks.club/docs/courses/zoomcamp-logistics/asking-questions/).
- Ask your question in [#course-ai-dev-tools-zoomcamp](https://app.slack.com/client/T01ATQK62F8/C09HWT76L95).

Please ask course-related questions in the course Slack channel, not in private messages. This helps other learners find the answer later.

[Join Our Slack Channel](https://datatalks.club/slack.html)

## Pace and Deadlines

During the live cohort, we recommend moving at about one module per week. You are free to move faster or slower, but submissions must be made before the published deadlines.

The full schedule, deadlines, homework forms, and leaderboard are available on the [course platform]({{ course_platform_url }}).

## Quick Links

- [Course repository](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp)
- [Course playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hLuyafXPyhTdbF4s_uNhc43)
- [Course platform]({{ course_platform_url }})
- [Course documentation](https://datatalks.club/docs/courses/ai-dev-tools-zoomcamp/)
- [FAQ](https://datatalks.club/faq/ai-dev-tools-zoomcamp.html)
- [Slack](https://datatalks.club/slack.html)
- [Telegram announcements](https://t.me/aidevtoolszoomcamp)

## Keep Going

This is Module {{ module_number }} of {{ total_modules }}. Completing the module brings you one step closer to the final project.

It is okay if you do not get everything right away. Most students do not.

Every attempt helps you get better at using AI tools without giving up engineering discipline.

Good luck!

Alexey and the DataTalks.Club Team
