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
python .claude/skills/transcript-post-miner/scripts/prepare_transcript_context.py \
  /Users/valeria/short-video-automation/<VIDEO_ID>/full_transcript.json
```

## Network And Dependency Handling

Fetching a YouTube transcript requires network access. If the command fails with a network, DNS, proxy, YouTube blocking, or dependency error, rerun it with network access after the user approves.

If `youtube_transcript_api` or `dotenv` is missing, check whether `/Users/valeria/short-video-automation/.venv/bin/python` exists and use it. If dependencies are still missing, tell the user which dependency is missing and suggest installing the repo requirements.

## When YouTube Has No Captions

If the fetcher reports that subtitles are disabled, or the video is not public yet, transcribe the local video file on this machine instead. Nothing is uploaded and no API credits are used:

```bash
uv run --with mlx-whisper python3 .claude/skills/transcript-post-miner/scripts/transcribe_local.py "<video.mp4>" \
  --output content-runs/<run>/source \
  --names "<speaker names, host, product and company names from the event source>"
```

- It writes `full_transcript.json` in the same shape as the fetcher, so the rest of the workflow is unchanged.
- It saves each 10-minute chunk as it finishes; rerunning the same command resumes instead of starting over.
- `--names` fixes most misspelled names. Still record any remaining misspellings or unverified terms as `transcript_caveats` in `source/source.json`.
- The transcript has no speaker labels. Say so in the shortlist, and mark who said each quote the posts will rely on.

Do not send the audio to a paid transcription API without the user's permission.

## Output Location

For a video ID like `abc123XYZ00`, expect:

```text
/Users/valeria/short-video-automation/abc123XYZ00/full_transcript.json
```

Use that path for idea mining. Do not create a separate transcript format unless the user asks for it.
