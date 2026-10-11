"""Collect per-file transcript .json files into one JSONL keyed by basename.

Usage: python collect_transcripts.py <dir1> [dir2 ...] <out_jsonl>
"""

import json
import sys
from pathlib import Path

dirs, out = sys.argv[1:-1], sys.argv[-1]
seen = {}
for d in dirs:
    for p in sorted(Path(d).rglob("*.json")):
        try:
            rec = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(rec, dict) and "file" in rec:
            seen[rec["file"]] = rec

with open(out, "w", encoding="utf-8") as f:
    for fname in sorted(seen):
        f.write(json.dumps(seen[fname], ensure_ascii=False) + "\n")
print(f"{len(seen)} transcripts -> {out}")
