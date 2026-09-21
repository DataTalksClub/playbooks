# Clip Manifest Format

Use JSON for clip manifests.

```json
{
  "input": "/path/to/source-video.mp4",
  "output_dir": "/path/to/output-directory",
  "clips": [
    {
      "output": "post-01-plain-llm-vs-rag.mp4",
      "segments": [
        {"start": "00:22:21", "end": "00:30:27"}
      ]
    },
    {
      "output": "post-03-data-prep-and-ingestion-combined.mp4",
      "parts_prefix": "post-03",
      "segments": [
        {"start": "00:37:34", "end": "00:42:05", "label": "json-data"},
        {"start": "01:39:45", "end": "01:40:28", "label": "ingestion"}
      ]
    }
  ]
}
```

## Fields

- `input`: absolute or relative path to the source video.
- `output_dir`: where generated clips should be written. Can be overridden with `--output-dir`.
- `clips`: list of clip definitions.
- `output`: filename for the final clip.
- `segments`: one or more `{start, end}` timestamp ranges.
- `label`: optional suffix used for intermediate part filenames.
- `parts_prefix`: optional prefix for intermediate part filenames.

## Duration Limit

Every final generated clip must be shorter than 600 seconds. A clip with multiple segments is measured by summing the durations of all its segments.

The script validates this before running `ffmpeg`. If any clip is 600 seconds or longer, the run fails before cutting starts.

## Timestamp Format

Use `HH:MM:SS`, `MM:SS`, or versions with milliseconds such as `01:02:03.500`.

## Commands

Generate commands without running them:

```bash
python3 scripts/cut_video_clips.py clip-manifest.json --dry-run
```

Create clips with fast stream copy:

```bash
python3 scripts/cut_video_clips.py clip-manifest.json
```

Create more accurate cuts by re-encoding:

```bash
python3 scripts/cut_video_clips.py clip-manifest.json --reencode
```

Override the output directory:

```bash
python3 scripts/cut_video_clips.py clip-manifest.json --output-dir /path/to/clips
```
