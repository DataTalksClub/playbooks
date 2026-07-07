# YouTube Transcript Fetching

Use this when the user provides a YouTube URL or 11-character video ID instead of an existing transcript file.

## Preferred Local Fetcher

Use the user's existing script:

```bash
cd /Users/valeria/short-video-automation
python scripts/youtube.py "<youtube-url-or-video-id>"
```

If the repo virtual environment exists, prefer:

```bash
cd /Users/valeria/short-video-automation
.venv/bin/python scripts/youtube.py "<youtube-url-or-video-id>"
```

The script:

- extracts or validates the YouTube video ID
- fetches the transcript with `youtube_transcript_api`
- optionally uses Oxylabs proxy credentials from `.env`
- writes `<VIDEO_ID>/full_transcript.json`

The output shape is:

```json
{
  "text": "<full transcript text>",
  "segments": [
    {
      "start": 0.0,
      "end": 5.12,
      "text": "..."
    }
  ]
}
```

After fetching, continue the main skill workflow with:

```bash
python /Users/valeria/.codex/skills/transcript-post-miner/scripts/prepare_transcript_context.py \
  /Users/valeria/short-video-automation/<VIDEO_ID>/full_transcript.json
```

## Network And Dependency Handling

Fetching a YouTube transcript requires network access. If the command fails with a network, DNS, proxy, YouTube blocking, or dependency error, follow Codex's escalation rules and rerun with approval when appropriate.

If `youtube_transcript_api` or `dotenv` is missing, check whether `/Users/valeria/short-video-automation/.venv/bin/python` exists and use it. If dependencies are still missing, tell the user which dependency is missing and suggest installing the repo requirements.

## Output Location

For a video ID like `abc123XYZ00`, expect:

```text
/Users/valeria/short-video-automation/abc123XYZ00/full_transcript.json
```

Use that path for idea mining. Do not create a separate transcript format unless the user asks for it.
