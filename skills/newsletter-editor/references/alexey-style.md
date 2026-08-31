# Alexey's Newsletter Style Guide

## Voice and tone

### Tone first

Write as if you are explaining the work to a colleague.

Keep the writing:

* Direct
* Human
* Practical
* Specific
* Factual
* Grounded
* Modest

Sound like a practitioner explaining what happened, how something works, and what others can learn from it.

Use simple, natural wording.

> The finished app has two main files: `App.jsx` for the page shell and `SnakeGame.jsx` for the game logic.

Avoid stiff wording:

> The implementation contains two primary artifacts.

Avoid loose or imprecise wording:

> The app is split into two bits.

Do not make ordinary work sound more important, innovative, or conclusive than it is.

## Point of view

Technical write-ups are first-person walkthroughs.

* Use `I`, `we`, `you`, and `let’s`.
* Do not refer to Alexey by name in his own newsletter.
* Use `I` for Alexey’s actions, experience, and decisions.
* Use `we` when Alexey and the reader are working through a process together.
* Use `you` for instructions and reader-facing outcomes.
* Use contractions: `it’s`, `we’ll`, `don’t`, `I’ve`.
* Use active voice: `Run the command`, not `The command should be run`.

Prefer:

> I used Claude Code to create the first version.

> We put the database configuration in Docker Compose.

> You can submit a score and open the leaderboard.

Avoid:

> Alexey used Claude Code to create the first version.

> The database configuration is placed in Docker Compose.

> The app allows score submission and leaderboard access.

## Tense

Use present tense for walkthroughs. Write as if the reader is doing the work now.

> We create the frontend, add the API, and connect the two services.

Use past tense for lived experience, completed experiments, and events.

> During the session, I found that our trial had ended.

Do not switch tense without a reason.

## Preserve the source

Preserve the original:

* Meaning
* Tone
* Level of confidence
* Technical explanation
* Reasoning
* Conclusions
* Uncertainty

When the source explains a choice, behavior, or trade-off, use that explanation with light cleanup. Do not replace it with a more polished but invented explanation.

Match the intensity of the source.

* `works` should not become `performs exceptionally well`
* `simple` should not become `effortless`
* `useful` should not become `essential`
* `might` should not become `will`

When in doubt, stay close to the source.

Do not invent:

* Reasons for technical decisions
* Benefits that were not demonstrated
* Problems that were not mentioned
* Results that were not measured
* General lessons that do not follow from the example

If the source does not explain why a decision was made, make the action clear and leave the reason out. If the reason is necessary for understanding, flag it as missing.

## Explain why

Explain the reason behind each important design choice, helper, step, or change when the source provides one.

Do not stop at what was done.

Weak:

> We use `AsyncOpenAI`.

Better:

> We use `AsyncOpenAI` because the model response arrives as a live stream rather than one finished string. The notebook processes the stream event by event, so we need the async client.

Ground the explanation in a concrete consequence:

* Fewer files to change
* No local installation
* One command instead of several
* No CORS error
* No package collision
* The same database engine in development and production
* The ability to test the frontend before the API exists
* A shorter feedback loop

Avoid abstract explanations such as:

* It is more flexible.
* It improves the developer experience.
* It makes the system more robust.
* It provides better scalability.
* It follows best practices.

If one of these claims is necessary, explain what specifically becomes more flexible, reliable, or scalable.

## Make the logic explicit

Connect the problem, action, and result.

Weak:

> I added WebSockets. Both participants can edit the diagram.

Better:

> Both participants need to see the same diagram state. I connect their browser sessions through one WebSocket room, so an update from either participant appears in both sessions.

Explain:

* Why a step comes next
* Why a tool is used
* What changed between versions
* What caused a problem
* What the change fixed
* What breaks if the reader skips a step
* Why the result matters

Do not leave the relationship between adjacent sentences implicit.

When two sentences contrast, connect them with `but`, `though`, or `yet` unless they express independent ideas.

## Use concrete actors and verbs

Name who or what performs the action.

Prefer:

> We run two processes.

Avoid:

> The work splits into two processes.

Prefer:

> We put the configuration in `config.py`.

Avoid:

> The configuration goes in `config.py`.

Prefer concrete verbs:

* Add
* Build
* Call
* Connect
* Copy
* Create
* Deploy
* Move
* Open
* Replace
* Run
* Send
* Store
* Test

Avoid turning actions into abstract nouns.

Prefer:

> We evaluate the model.

Avoid:

> We conduct an evaluation of the model.

## Do not let noun phrases hide the real actor

A component, file, section, or setup can be grammatically concrete while still hiding who made a decision or what caused a change.

Watch for subjects such as:

* The app
* The frontend
* The backend
* The database
* The implementation
* The setup
* The stack
* The prompt
* The file
* The repo
* The workshop
* The service layer
* Option 1

Be especially careful when they appear with verbs such as:

* Allows
* Becomes
* Defines
* Decides
* Drives
* Enables
* Keeps
* Lets
* Moves
* Needs
* Owns
* Requires
* Starts
* Stays

Weak:

> The database starts as SQLite and becomes Postgres in containers.

Better:

> We use SQLite locally because it requires no setup. When we move the app into containers, we switch to Postgres so we use the same database engine as the deployed version.

Weak:

> The frontend defines what the app does.

Better:

> We start with the frontend because the screens force us to identify the game states, API calls, and data that the backend must support.

Weak:

> The app lets you submit a score and view the leaderboard.

Better:

> You can submit a score and view the leaderboard.

Weak:

> The mock keeps the frontend usable on its own.

Better:

> We keep the mock backend so we can test the frontend before the real API exists.

Weak:

> Two apps at the root would collide.

Better:

> If React and FastAPI both use the repository root, their package files and commands compete for the same directory. We move the React app to `frontend/` before adding `backend/`.

Keep sentences in which the component is genuinely performing the action:

> Docker Compose starts Postgres.

> The function returns a list.

> The database stores scores.

> The frontend calls the scores endpoint.

## Use reader-facing words

Prefer familiar words unless a technical term is more precise.

* `run`, `call`, or `do`, not `execute`
* `finished app`, `preview`, `file`, or `tool`, not `artifact`
* `code repo`, `final code`, or `working version`, not `reference implementation`

Use `execute` when it is the precise API or tool term.

Some words depend on context:

### Workflow

Use `workflow` for Temporal, GitHub Actions, and other named workflow concepts.

In ordinary text, prefer:

* Flow
* Process
* Way of working
* The specific action

### Production

Use `production` when discussing real production concerns such as deployment, reliability, security, monitoring, or scaling.

Do not use it as a vague substitute for `real`, `complete`, or `larger`.

### Build

Use `build` for constructing an application or for a software build step.

> We build the agent.

> The build step creates the frontend bundle.

Do not call a workshop or recording `the build`.

Prefer:

> I used Claude Code in the live session.

Avoid:

> I used Claude Code during the live build.

### Decides

Use `decides` when a person makes a decision.

When an agent, router, or component selects an action, use the precise operation:

* Orchestrates
* Routes
* Picks
* Selects
* Calls

> The router picks the tool based on the request.

Not:

> The router decides what to do.

## Technical details

Include the details readers need to understand or reproduce the work:

* Shell commands, in order
* Non-trivial code files, inline or linked
* Environment variable names
* Relevant `.env` structure
* Tool and runtime versions when they affect reproducibility
* Relevant configuration
* Important prompts
* Errors and gotchas
* Technical constraints
* Prices and product tiers when they affect a decision

Add the month and year to prices because they can change.

Do not add technical detail merely to make the text sound more advanced. Each detail should help the reader understand, run, verify, or adapt the work.

## Remove internal process

Do not publish details about how the write-up itself was produced.

Remove references to:

* Transcripts
* Scratch files
* Temporary directories
* Internal review processes
* Subagents
* Source-of-truth instructions
* Missing evidence notes
* Drafting discussions

Remove transcript noise:

* False starts
* Repeated statements
* Self-corrections
* Filler words
* Pauses
* Asides with no instructional value

Keep the commands, prompts, decisions, gotchas, and reasoning that readers may need later.

## Sentence and paragraph style

* Keep sentences relatively short.
* Express one main idea per sentence.
* Keep paragraphs focused on one point.
* Use short paragraphs, usually one to three sentences.
* Break long explanations at a logical change in step, cause, or result.
* Avoid repeating the same claim in different words.
* Avoid unnecessary introductory clauses.
* Avoid rhetorical questions used only as hooks.
* Avoid sentence fragments written for dramatic effect.
* Avoid chains of abstract nouns.

Prefer:

> The first version stores the state in SQLite. This is enough for the workshop because we run one backend instance.

Avoid:

> In terms of the persistence layer, the initial implementation makes use of SQLite, which represents a sufficiently robust solution within the context of the workshop environment.

## Formatting

* Do not use bold formatting in body text.
* Do not use em dashes.
* Use headings to separate substantial sections.
* Use bullets for parallel information.
* Use numbered lists when order matters.
* Start bullet points with capital letters.
* Keep list items grammatically parallel.
* Use consistent punctuation across list items.
* Format commands, filenames, variables, and code identifiers as code.
* Use descriptive link text instead of `click here`.
* Avoid excessive parentheses.
* Avoid excessive exclamation marks.

## Language to avoid

Do not use generic AI-style or marketing phrases such as:

* At its core
* The idea is simple
* In today’s landscape
* In the rapidly evolving world of
* Not only X, but also Y
* It is not just X, it is Y
* This is where X comes in
* The result?
* The best part?
* Game-changing
* Cutting-edge
* Unlock
* Harness
* Leverage
* Seamless
* Robust
* Powerful
* Transformative
* Revolutionary
* Delve into
* Navigate the complexities of
* Take X to the next level
* Whether you are a beginner or an expert
* The possibilities are endless

Do not use adjectives as substitutes for evidence.

Weak:

> The tool provides a powerful and seamless development workflow.

Better:

> The tool generates the first version, runs the tests, and shows the diff before you commit the changes.

## Editing checklist

### Meaning

* Does the edit preserve the original meaning?
* Does it preserve the original level of confidence?
* Have we added any unsupported claims or explanations?
* Does each conclusion follow from the source?

### Voice

* Does the text sound like a colleague explaining the work?
* Does it use first person where appropriate?
* Does it use active voice?
* Does it use contractions naturally?
* Does it avoid stiff or corporate wording?

### Logic

* Is it clear why each important step or decision appears?
* Does the text connect problems, actions, and results?
* Does each contrast have a clear connection?
* Are the practical consequences stated?

### Sentence construction

* Does each sentence name the real actor?
* Is a component or noun phrase hiding a human decision?
* Can an abstract noun be replaced with a concrete verb?
* Does `this`, `that`, `it`, or `all of this` hide specific actions?
* Can the sentence be shorter without losing meaning?

### Technical clarity

* Are the necessary commands, files, variables, versions, and constraints included?
* Are technical terms used precisely?
* Are vague benefits replaced with concrete mechanisms?
* Are prices dated when relevant?
* Has internal drafting or transcript noise been removed?

### Final cleanup

* Remove generic AI phrasing.
* Remove inflated language.
* Remove unnecessary repetition.
* Remove bold formatting from body text.
* Remove em dashes.
* Check headings, lists, links, and code formatting.
