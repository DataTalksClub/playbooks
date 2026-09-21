# My editing playbook

## Sentence-shape moves

### Fusing short sentences into one compound

The draft tended to chop ideas into short, separate sentences. I usually fuse them back together with a comma or *and*.

- **Draft:** *"I now rent a dedicated Linux server running 24/7. The agents run there persistently. I install everything on it: Claude Code, Codex, and OpenCode. They all live there."*
- **Mine:** *"I now rent a dedicated Linux server available 24/7, and Claude Code, Codex, and OpenCode are running there."*

- **Draft:** *"The built-in recognizer gets confused by terminal syntax. The agents mostly understand what I mean, but the input is messy."*
- **Mine:** *"It doesn't work well for the terminal, and the input is messy, but the agents mostly understand what I mean."*

**Why:** Short staccato sentences feel like a manual or a slide deck. When the ideas belong together, I want them in one breath. Reading aloud, the draft sounds choppy; my version flows.

### Ending the compound on the softer / positive clause

When I fuse sentences, I also reorder so the upbeat clause lands at the end.

- **Draft ends on:** *"…but the input is messy."*
- **Mine ends on:** *"…but the agents mostly understand what I mean."*

**Why:** The last clause of a sentence is the one the reader carries forward. I'd rather leave them with "it works" than "it's messy."

### Replacing "colon + list" with "comma + like"

- **Draft:** *"Where it falls short is anything visual: judging a layout, reviewing a screenshot from an agent, or picking between design variants."*
- **Mine:** *"But it's still not ideal for visual work, like reviewing screenshots or choosing between design variants."*

**Why:** A colon followed by three parallel noun phrases feels formal — almost like documentation. *"like X or Y"* is how I'd say it out loud.

### Removing topic-introducer openers <--- THIS

The draft liked to introduce a topic with a labelling sentence before getting to the content. I cut those and start with the content.

- **Draft:** *"The result is ssh-auto-forward-android, written in Kotlin."*
- **Mine:** *"It created ssh-auto-forward-android in Kotlin."*

- **Draft:** *"The flow is simple. I open the app, tap Connect…"*
- **Mine:** *"I open the app, tap Connect…"*

- **Draft:** *"A recent example: I needed to select banners…"*
- **Mine:** *"Recently I needed to select banners…"*

**Why:** "The flow is simple" is the sentence telling me the next sentence is the flow. The next sentence already is the flow. I don't need a label.

### Leading with When / If

When there's a condition or context, I lead with it.

- **Draft:** *"I run a local version on my laptop and record feedback from the phone. Recorder works offline. When I land, I send the recording links to the agent."*
- **Mine:** *"When I'm on a plane, I open my laptop to review the code or run the local version and click around. While doing it, I dictate feedback to my phone, and share the recording with the agents when I land."*

**Why:** Putting the context first ("When I'm on a plane…") gives the reader the frame before the action. The draft makes me hold three disconnected facts until the last sentence ties them together.

### Period + "But" over comma + "and"

- **Draft:** *"sound reckless, and I understand the risks. But I'm comfortable…"*
- **Mine:** *"sound reckless. But I understand the risks: these agents are running on an isolated remote machine with no access to production environments."*

**Why:** "But" at the start of a sentence is a stronger pivot than "and" mid-sentence. I want the reader to feel the turn.

### Compressing sensory examples into a relative clause

I don't always cut concrete examples — sometimes I just tuck them into the previous sentence as `, which…`.

- **Draft (full sentence):** *"My connection drops whenever a tram goes underground, and the signal at my gym is often patchy."*
- **Mine (relative clause):** *"…dealing with constant disconnects, which happen often when traveling."*

**Why:** The draft's version is more vivid, but it slows the section down. The relative clause version keeps the rhythm and still tells the reader this isn't theoretical.

### Replacing a declarative anecdote with a rhetorical question

- **Draft:** *"One Gemini agent actually dropped my production database not long ago. I detailed that disaster in [link]."*
- **Mine:** *"Maybe you remember the incident I described in [link]?"*

**Why:** The draft names and shames a specific product. The question version invites the reader in instead of accusing. It also assumes some continuity with my regular readers, which is the relationship I want.

### Using an em dash for an aside, not a new sentence

- **Draft:** *"The same approach works on a plane. On a plane, I can't SSH anywhere. … Recorder works offline."*
- **Mine:** *"I like Google Recorder because it works offline too – also on planes."*

**Why:** An em dash signals "by the way" without forcing me to open a whole new sentence. The draft made the plane thing feel like its own beat; I wanted it to feel like a footnote.

### Mild emphasis words restored

- **Draft:** *"postponed it for several days"*
- **Mine:** *"postponed it for many days"*

- **Draft:** *"Real deploys are triggered by CI on my laptop, not on this server."*
- **Mine:** *"Real deployments are always triggered through CI, never on the server by agents."*

**Why:** "Several" is precise but flat. "Many" has heat. The always/never symmetry in the second example reads more like a rule than a description.

### Specific duration over vague time-of-day

- **Draft:** *"reviewing all 30 variants from my phone that same afternoon."*
- **Mine:** *"reviewing all 30 variants in 5 minutes."*

**Why:** "5 minutes" is the surprising number. "That same afternoon" sounds normal. I want the surprise.

### Specific noun subjects over "That's" / "It"

- **Draft:** *"That's changed in the last few months."*
- **Mine:** *"My approach changed in the last few months."*

**Why:** Demonstratives ("that") are vague. Naming the subject ("my approach") gives the sentence a clear actor.

### Process descriptions: bullets, not narrative prose

The single biggest reshape was the "Behind the scenes" section. The draft turned the writing process into four flowing paragraphs. I turned it back into a bulleted recipe.

**Why:** When I'm describing discrete steps with timings, bullets carry the structure visibly. Narrative prose pretends the steps are connected when they're really just a list.

### Intro bullets: varied openers, not rigid parallels

The draft pushed the article's promise bullets into a parallel "How I…" pattern. I broke the pattern.

- **Draft:**
  - *Why a borrowed runtime wasn't enough and what I moved to*
  - *How I made the server usable from a phone terminal*
  - *How I stopped typing and started talking to the agent*
  - *How I turn voice walkthroughs into task lists*
  - *How I handle the things a phone can't show*
  - *How this article itself was made*
- **Mine:**
  - *Why I moved to a permanent remote server*
  - *The small tools that make terminal work possible from a phone*
  - *How voice became my main interface to coding agents*
  - *How long recordings turn into structured engineering tasks*
  - *Tricks for handling visual tasks without access to a laptop*
  - *How this article itself was produced while moving around*

**Why:** Rigid parallel structure feels like a checklist. Varied openers ("Why…", "The small tools…", "How voice…", "Tricks for…") give each bullet a different shape, which makes them easier to read as distinct topics.

---

## Things I removed

### Whole subsections that fragment the structure

The draft added two H3-level subsections that I cut entirely:

- **"One command to restore everything"** — about three paragraphs on dotfiles syncing my laptop, tablet, and server.
- **"Turning a voice walkthrough into issues"** — about the orchestrator agent decomposing recordings into GitHub issues, with the plane workflow as a sub-beat.

**Why:** Each section in the article should be one clear idea. Promoting a paragraph into its own subsection makes the article feel like a reference doc with too many headings. If something fits in a paragraph inside the parent section, it should stay there. If it doesn't fit, it probably belongs in a different article.

### Bridging / scaffolding paragraphs between sections

- *"The setup is solid: the server is accessible from anywhere, sessions persist across disconnects, agents launch with two keystrokes, and ports forward themselves. The final hurdle is input – getting the actual instructions into the agent."*
- *"This article went through the same flow I use for most writing from the phone."*

**Why:** I want each section to open cold, not with a recap of what came before. The reader knows what came before — they just read it. Bridges add a soft warm-up that I'd rather skip.

### Meta-explanations of why something is hard

- *"Providing context, constraints, and specific task requirements is nearly impossible with a thumb-keyboard."*
- *"It wasn't meant to be general-purpose; it just needed to work."*

**Why:** Saying "typing on a phone is a nightmare" is enough. If I add a second sentence explaining *why* it's a nightmare, I'm explaining a thing the reader already accepted.

### Rationale sentences for setup choices

- *"I run three in rotation: Claude Code is the primary, then Codex when I hit Claude's limits, and OpenCode as the final fallback."*

**Why:** This explains the *why* behind a three-item list. The list itself is the next thing on the page. Readers don't need both — they can infer the rotation from the names.

### Parenthetical definitions of jargon

- *"(no confirmation prompts for commands or file edits)"* after `csp`

**Why:** Most of my readers either know what "skip permissions" means or don't care. The ones who care can google it. Defining every term inline slows everyone down for the benefit of nobody.

### Sensory specifics that don't pull weight

- *"My connection drops whenever a tram goes underground, and the signal at my gym is often patchy."*
- *"on the tram, in the metro, between gym sets. I press pause, do a working set, come back, and pick up where I left off."*
- *"In the same folder I can run a code session and a `-web` session running `make dev`"*

**Why:** These are good details, but they're padding the paragraph rather than driving it forward. I sometimes keep one or two for color, but the draft tends to add them everywhere. When in doubt I cut.

### Self-explanation that the next sentence already shows

- *"This custom picker let me like, reject, or comment on each banner variant directly."* — the next sentence already says "made my selections, tapped 'Export Picks'."
- *"Port 8030 in the screenshot above is llama.cpp running on the server. One tap and I'm in the chat UI."* — the screenshot caption already says this.
- *"The recorder keeps recording in the background. I'm recording this article right now while the app is minimized."*

**Why:** If the next sentence demonstrates the thing, the sentence describing it is redundant. The draft tends to tell-then-show; I keep only the show.

### Alternative tactics / "you could also…" additions

The draft added a second tactic to the visual-work section: agents posting screenshots directly to GitHub issues, plus a paragraph about how CI/CD has made this less necessary. I cut both.

**Why:** Each section should have one clear example. A second example dilutes the main one and turns the article into a survey. If the alternative tactic is interesting enough, it belongs in its own article.

### Backward references to earlier setup

- *"for all three"* after "short aliases" (referring back to the three agents)
- *"Claude Code"* qualifier in *"I open a Claude Code session"* (referring back to which agent)
- *", ready to send"* in the image caption

**Why:** Once a fact has been established a few paragraphs ago, I trust the reader to carry it. Re-anchoring every sentence to earlier setup makes the prose feel anxious.

### Hedges and intensifiers that don't add anything

- *"significant"* in *"any significant prompt"*
- *"comfortably"* in *"30 variants comfortably from a phone"*
- *"far"* in *"far too slow"*
- *"and it likely wouldn't have happened at all"*

**Why:** These are filler. "Too slow" and "far too slow" mean the same thing; the *far* just makes the sentence longer.

---

## Things I added back

Not everything was a cut. There were also places where the draft had been sanded smooth and I put my voice back in.

### Reader plugs and personal asides

I added back the Vienna concert line: *"And this Sunday, I'm traveling to Vienna again for a concert (drop me a line if you want to meet for coffee!)."*

**Why:** These lines are how I treat my Substack — as a relationship with people I'd actually meet for coffee, not a publication. The draft tends to remove them because they're not "on topic." For me they're the point.

### Specific names instead of generic terms

I changed "child" back to "son" in the morning-routine bullets.

**Why:** "Child" is what a draft uses when it's trying to be neutral. I'm not writing neutrally — this is my life, and my son is my son.

### Side tangents that show how I think

I restored the Java→Kotlin aside: *"I can understand Kotlin a bit because I used to be a Java developer, and Kotlin looks similar to Java. But I have no intention to read this code, just like I never looked inside the Python version."*

**Why:** The draft trimmed this to *"I haven't looked inside it, the same as I never looked inside the Python version."* That's shorter, but it loses the small story about my background and my comfort with not reading agent-generated code. The tangent is what makes the paragraph mine.

### Standalone gratitude paragraph for Valeriia

The draft folded her into a single inline credit: *"Then Valeria, my editor, did the final pass."* I restored both her full role-in-the-process (in the bullet list) and the separate thank-you paragraph at the end, and kept the spelling *Valeriia* (double *i*).

**Why:** Inline credit is technically accurate but emotionally flat. A standalone paragraph at the end is how I actually feel about her work — and it's also a signal to readers that this article was a collaboration, not a solo performance.

---

## One-line summary for an editor

If I had to compress all of this into a single line for someone editing my drafts:

> Fuse short sentences into compound ones that end on the softer clause; lead with the action, not the topic; cut bridges, rationale, parentheticals, sensory padding, and any sentence whose content is shown by the next one; keep one example per section; and leave my voice in — the concert plugs, the personal nouns, the side tangents, the gratitude.
