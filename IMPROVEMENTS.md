# Content Pipeline Improvements

A checklist of planned improvements to the social content pipeline: from a recording or task to posts, review, Typefully drafts, and learning from edits. Tick items off as they are done, and add new ones when a gap is found but not fixed.

The pipeline itself is described in `.claude/skills/social-content-studio/SKILL.md` (Artifact Mode).

## First Typefully upload (2026-09-23, Switch run)

- [x] Social set IDs filled in: Alexey 188312, DataTalksClub 182343.
- [x] 15 drafts created: a `clip` and a `visual` draft per Alexey post, one `clip` draft per DataTalks.Club post.
- [x] The same media ID is accepted on several platforms of one draft.
- [x] Substack Notes accepts no video ("Substack's limit of 0"), so the `clip` variant now gives Substack the copy without the clip.
- [ ] Check in the Typefully UI: does Alexey's identical copy show LinkedIn, X, and Substack as synced?
- [ ] Check in the Typefully UI: the carousel PDF as a LinkedIn document, the resource image on X, and the DataTalks.Club X thread as separate copy from LinkedIn.
- [ ] Decide whether Substack belongs in the `visual` draft (currently only in `clip`).

## Media quality

- [x] Burn subtitles into clips from the transcript. Most social video plays muted. (`render_social_clip.py`: word-by-word captions under the vertical video, or boxed on the horizontal one.)
- [x] Vertical version for social: full-width clip on a branded 1080x1920 frame with a title (`render_social_clip.py`, `datatalksclub` style).
- [ ] Speaker crop for vertical clips where the speaker, not the screen, matters (needs crop positions per recording layout), and a square version.
- [ ] An `alexey` style in `clip-styles.json`: font, colours, and whether his clips get a label.
- [ ] A DataTalks.Club logo file for the bottom of the vertical frame (`--logo`), and the poster's `texture.png` background.
- [ ] Record the captioned clips in `post.json` and let the Typefully upload choose which one to attach (vertical or horizontal, per platform).
- [ ] A clip review sheet with the first and last frame and the transcript text of each clip, for quick approval before upload.
- [ ] Snap clip boundaries to sentence starts and ends, and trim filler at the edges.
- [ ] Flag clips that only make sense with the screen visible, or zoom into the shared screen for them.
- [ ] Confirm X's video length limit for the DataTalks.Club account (no Premium). `check_posts.py` warns above 140 seconds; verify the real limit.
- [x] Normalize clip audio loudness (-14 LUFS in `render_social_clip.py`).
- [ ] Review the carousel and resource image design, and decide whether DataTalks.Club gets its own visual style.

## Transcription and speakers

- [ ] Speaker labels (diarization), so the pipeline knows whether Alexey or the speaker said a line. Options:
  - WhisperX with pyannote: free and local. Needs a one-time Hugging Face token and accepting the pyannote model terms.
  - A paid API with diarization built in, such as AssemblyAI, Deepgram, or ElevenLabs Scribe. Needs a key and approval to upload audio.
- [ ] Move the YouTube caption fetcher (`~/short-video-automation/scripts/youtube.py`) into this repository, so cloud and Codex runs can fetch captions.
- [ ] A fallback for machines without Apple Silicon (for example faster-whisper), since `transcribe_local.py` uses mlx-whisper.

## Review

- [ ] The reviewer subagent set `status: approved` on the five Alexey posts although it was told to write only `review.json`, and its report said it had not. Only a person should set `approved`. Add a guard (for example, `check_posts.py` fails when a post is `approved` while reviewer findings are open, or the review runs without write access to `post.json`).
- [ ] After a few runs, compare the reviewer's findings (`review.json.reviewer`) with the edits made in Typefully (`edits.md`), and tune `references/review-stage.md` for what it misses.

## Learning from edits

- [ ] Run `pull_typefully_edits.py` after every publish. First snapshot taken 2026-09-23: 35 platform versions, none edited yet.
- [ ] A script that collects `edits.md` across runs and summarizes repeated edits per owner, as input for updating the style references.

## Typefully

- [ ] Retry on HTTP 429 using the rate-limit headers.
- [ ] Scheduling (`publish_at`, `next-free-slot`), with an explicit permission step.
- [ ] Typefully tags per owner or campaign.
- [ ] Alt text for images and carousels (`alt_text` on media upload).
- [ ] Retire `~/short-video-automation/scripts/create_typefully_drafts.py`, which still creates a draft first and patches media in later.

## Pipeline hygiene

- [ ] A campaign file per event that links the pre-event and post-event runs.
- [x] Removed `export_social_queue.py` and `validate_post_records.py`; `check_posts.py` covers the record checks.
- [ ] The DataTalks.Club post-event channel variants (registrant newsletter recap, YouTube Community, Telegram, Slack) are not produced by this pipeline yet.
- [ ] Migrate the 2026-08-27 Switch runs (old `post_NNN` IDs, one folder per owner) if they will be uploaded.
