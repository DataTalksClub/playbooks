# Course Repo Cohort Setup

This process opens a new cohort in the course GitHub repo: the `cohorts/<year>/` folder learners work from, and the archive of any module the new cohort replaces.

Run it alongside `01-course-platform-setup.md`. The platform holds deadlines and submissions; the repo holds the materials, the homework, and the record of what each cohort actually studied.

## The Two Rules

**The repo root is always the current cohort.** Module folders at the top level — `01-.../`, `02-.../` — hold the version being taught right now. Nobody should have to guess which copy is live.

**`cohorts/<year>/` is the record of one cohort.** It holds that cohort's homework, its links, and the module content as it stood that year, so a learner who took the 2025 edition can still find what they were taught after the 2026 rewrite lands.

Everything below follows from those two.

## 1. Open the New Cohort Folder

Copy the previous cohort's structure into `cohorts/<year>/` and update it:

```text
cohorts/<year>/
  README.md
  <module>/homework.md
  workshops/            if the cohort runs workshops with their own homework
  project.md            if the course keeps project instructions per cohort
```

The cohort `README.md` is short and links-first. Follow the shape already in the repo:

```markdown
# <Course> <Year>

* [Course management platform](https://courses.datatalks.club/<slug>-<year>/)
* [FAQ](https://datatalks.club/faq/<course>.html)

Homework:

* [Module 1: <Title>](01-<slug>/homework.md)
* Module 2: <Title> — coming
```

List every module from the start, marking the unwritten ones `— coming`. Learners use this page to find their homework, and a module that is missing entirely reads as an error, while `— coming` reads as a schedule.

Name the module folders to match the module folders at the repo root. When a module is renamed between cohorts, the new cohort folder takes the new name.

Homework carries over as a starting point, not as a copy to ship. Re-solve it against the current materials before opening it: tool versions move, output changes, and a question that was fair last year can become unanswerable.

## 2. Archive Any Module the New Cohort Replaces

This is the step that gets forgotten, and it is the one that loses work.

When a module at the repo root is rewritten, renamed, or dropped, copy its **previous content** into the previous cohort's folder before the rewrite lands:

```text
cohorts/<year-1>/<old-module-folder>/
  README.md
  any supporting files the module had
```

Use the folder name the module had then, not the new one. It is the 2025 module, so it keeps the 2025 name.

Worked examples in `ai-dev-tools-zoomcamp`, from the 2026 rewrite:

| Module in 2025 | Became in 2026 | Archived at |
| --- | --- | --- |
| `03-mcp/` | `05-agent-capabilities/` | `cohorts/2025/03-mcp/` — `README.md` and `clients.md` |
| `05-cicd-devops/` | folded into `04-devops/` | `cohorts/2025/05-cicd-devops/README.md` |
| `04-build-coding-agent/`, `06-automation-lowcode/` | dropped | `cohorts/2025/…` |

`llm-zoomcamp` does the same across three cohorts: `cohorts/2024/`, `cohorts/2025/`, and `cohorts/2026/` each hold the modules as they were taught, including notebooks, datasets, and homework solutions.

Then link the archive from the new module so the trail is visible:

```markdown
## Previous Cohort Materials

Related material from the previous cohort:

- [2025 archived CI/CD and DevOps module](../cohorts/2025/05-cicd-devops/)
```

A rewritten module usually still owes something to the version before it. The link is how a learner finds the older treatment of a topic the new module only touches.

## 3. Update the Root README

The syllabus section lists the current modules, in the current order, with the current titles. Check that:

- module numbers match the folder numbers
- module titles match the `# Module N — Title` heading in each module README
- the start date, cohort links, and events table point at this cohort

When modules are renumbered, the numbers move in the article filenames too: `articles/03-deployment.md` sits next to `03-deployment/`.

## Checklist

- [ ] `cohorts/<year>/README.md` created, linking the platform and the FAQ
- [ ] Every module listed, unwritten ones marked `— coming`
- [ ] Homework folders created per module, named to match the root module folders
- [ ] Homework re-solved against the current materials before opening
- [ ] Replaced or renamed modules archived under `cohorts/<year-1>/` with their old folder names
- [ ] New modules link back to the archived version under "Previous Cohort Materials"
- [ ] Root README syllabus, dates, and events table updated
- [ ] Article filenames still match their module folders
