# Course Assets Map

Where every course asset lives, so a new cohort is a list of known files rather than a search.

Use this with `01-launch-checklist.md`. The checklist says *what* to update; this says *where* it is.

## Repositories

| Repo | Local path | What it holds |
| --- | --- | --- |
| `DataTalksClub/playbooks` | `~/git/playbooks` | This playbook, campaign workspaces, copy banks, proof libraries. |
| `DataTalksClub/datatalksclub.github.io` | `~/git/datatalksclub.github.io` | The website: course articles, FAQ data, schema.org course data. |
| Course repo, one per course | see the table below | Course materials, cohort folders, course README. |
| `DataTalksClub/course-management-platform` | — | The platform itself. Cohorts are created through the course management agent project, not by editing this repo. |

The course management agent project (`~/git/course-management-agent`) is what you use to create and update cohorts, registration campaigns, homeworks, and projects on the platform. Nothing in this map is edited to change a deadline.

## Per-Course Assets

| Course | Course repo | Website article | FAQ data | schema.org data | Playbook folder |
| --- | --- | --- | --- | --- | --- |
| Machine Learning | `machine-learning-zoomcamp` | `_posts/2023-08-17-machine-learning-zoomcamp.md` | `_data/faqs/machine-learning-zoomcamp.yml` | `_includes/course-structured-data/machine-learning-zoomcamp-structured-data.html` | `ml-zoomcamp/` |
| Data Engineering | `data-engineering-zoomcamp` | `_posts/2023-11-18-data-engineering-zoomcamp.md` | `_data/faqs/data-engineering-zoomcamp.yml` | `_includes/course-structured-data/data-engineering-zoomcamp-structured-data.html` | `de-zoomcamp/` |
| MLOps | `mlops-zoomcamp` | `_posts/2024-03-07-mlops-zoomcamp.md` | `_data/faqs/mlops-zoomcamp.yml` | `_includes/course-structured-data/mlops-zoomcamp-structured-data.html` | `mlops-zoomcamp/` |
| LLM | `llm-zoomcamp` | `_posts/2024-11-11-llm-zoomcamp.md` | `_data/faqs/llm-zoomcamp.yml` | `_includes/course-structured-data/llm-zoomcamp-structured-data.html` | `llm-zoomcamp/` |
| AI Dev Tools | `ai-dev-tools-zoomcamp` | `_posts/2025-09-23-ai-dev-tools-zoomcamp.md` | `_data/faqs/ai-dev-tools-zoomcamp.yml` | `_includes/course-structured-data/ai-dev-tools-zoomcamp-structured-data.html` | `ai-dev-tools-zoomcamp/` |
| Stock Markets Analytics | `stock-markets-analytics-zoomcamp` | none | none | none | none |

Website paths are relative to `datatalksclub.github.io`. Playbook paths are relative to `playbooks`.

Stock Markets Analytics has no website article, FAQ, or structured data. Creating them is a separate piece of work, not part of a cohort launch.

## Slugs and URLs

| Course | Platform slug | Registration page | Hashtag |
| --- | --- | --- | --- |
| Machine Learning | `ml-zoomcamp-<year>` | `courses.datatalks.club/register/ml-zoomcamp/` | `#mlzoomcamp` |
| Data Engineering | `de-zoomcamp-<year>` | still an Airtable form | `#dezoomcamp` |
| MLOps | `mlops-zoomcamp-<year>` | still an Airtable form | `mlopszoomcamp` |
| LLM | `llm-zoomcamp-<year>` | still an Airtable form | `#llmzoomcamp` |
| AI Dev Tools | `ai-dev-tools-<year>` | `courses.datatalks.club/register/ai-dev-tools/` | `#aidevtools` |
| Stock Markets Analytics | `sma-zoomcamp-<year>` | still an Airtable form | `#smazoomcamp` |

Hashtags are the `social_media_hashtag` values stored on the platform. MLOps is stored without the leading `#`; that is how it is on the platform today, not a typo in this table.

## Subreddits

Each course gets two Reddit posts: one a month before the start announcing the cohort, and one on the start day.

| Course | Subreddit | Size | Confirmed |
| --- | --- | --- | --- |
| Machine Learning | `r/learnmachinelearning` | ~200k | Yes |
| Data Engineering | `r/dataengineering` | — | Yes |
| MLOps | `r/mlops` | — | **No, check first** |
| LLM | `r/LLMDevs` | ~161k | Proposed |
| AI Dev Tools | `r/ChatGPTCoding` | ~383k | Proposed |
| Stock Markets Analytics | `r/algotrading` | ~1.9M | Proposed |

Machine Learning and Data Engineering are settled. The rest are proposals picked on topic fit and size, not yet posted to.

`r/mlops` needs checking before it is used: it exists, but one stats source reports it as quarantined, and a quarantined subreddit is a bad place to launch. If it is not usable, `r/MachineLearning` and `r/datascience` are the fallbacks.

Before posting anywhere:

- Read the subreddit's self-promotion rules. Several of these remove course launches posted as plain ads.
- Rewrite for the community. Do not paste the launch tweet.
- Check whether the subreddit wants a flair, and whether it has a dedicated thread for this kind of post.

Note that AI Dev Tools drops `zoomcamp` from its platform slug. Confirm the slug against the previous cohort rather than assuming the pattern.

The registration campaign slug carries no year and stays stable across cohorts. Only `current_course` is repointed each year.

**Migration in progress.** Machine Learning and AI Dev Tools use platform registration pages. The other courses still use Airtable forms. When a course moves off Airtable, every link in the table below has to change at once, or half the site sends people to a dead form.

## What to Change for a New Cohort

Work in this order. Each step assumes the previous one is done.

### 1. Platform

Through the course management agent project: create the course, create or repoint the registration campaign, create the outline. See `01-course-platform-setup.md`.

This produces the two values everything else needs: the cohort URL and the registration URL.

### 2. Course repo

- `README.md`: registration link, course platform link, start date, and the live-vs-self-paced table.
- `cohorts/<year>/README.md`: new folder, copied from last year. Syllabus, cohort links, and the deadline schedule.
- `cohorts/<year>/projects.md` and `article.md`: submission links carry the cohort slug and need updating.
- Link the new cohort folder from the main README.

Homework links inside the cohort README are added per module as the cohort progresses, not at launch.

### 3. Website

For the course being launched:

- **Article**: registration links and the start date. Both appear several times, including inside raw HTML button blocks.
- **FAQ data**: registration links, the start date, and any question phrased around a specific year.
- **schema.org data**: `startDate` and `endDate`. `endDate` is the last peer review deadline, which may fall in the following calendar year.

Shared pages that mention every course:

- `_posts/2024-04-11-guide-to-free-online-courses-at-datatalks-club.md`: the all-courses guide, one registration button per course.
- `_posts/2025-08-16-free-machine-learning-courses.md`: ML-adjacent course roundup.
- `_posts/2025-12-10-free-data-engineering-courses.md`: DE-adjacent course roundup.
- `_data/faqs/free-datatalksclub-courses-zoomcamps.yml` and `_data/faqs/free-ml-courses.yml`: cross-course FAQ data.

The shared pages are the ones that get missed. Grep for the old registration URL across the whole repo before calling the website done.

### 4. Playbook

- `<course>/course.yaml`: durable facts, including the registration URL when it changes.
- `courses/campaigns/<course>-<year>/`: the campaign workspace. See the README's Start Here.

## Finding Everything

The reliable check is a grep for the outgoing registration URL, run from the repo root of each repo:

```bash
grep -rn "<old registration url>" --include=*.md --include=*.yml --include=*.yaml --include=*.html .
```

On the website, exclude `_site/`: it is generated output and regenerates itself.

Old cohort pages under `_courses/` are historical records. Leave them alone.

Grep for the outgoing year as well. Dates hide in prose, in FAQ questions phrased around an edition, and in schema.org fields, and a URL grep will not find any of them.
