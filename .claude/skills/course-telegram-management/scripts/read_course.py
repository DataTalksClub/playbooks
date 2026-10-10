"""Read one production course's dates/statuses using a Dapier-injected CMP key."""
import argparse
from datetime import datetime, timezone
import json
import os
import re
import sys
import urllib.request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="Course slug, for example ml-zoomcamp-2026")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", args.slug):
        parser.error("Use a lowercase course slug containing letters, numbers, and hyphens")
    token = os.environ.get("DAPIER_ACCESS_TOKEN")
    if not token:
        parser.error("Run through dapier token exec; DAPIER_ACCESS_TOKEN is missing")
    url = f"https://courses.datatalks.club/api/courses/{args.slug}/"
    request = urllib.request.Request(url, headers={"Authorization": f"Token {token}"}, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            course = json.load(response)
        if not isinstance(course, dict) or course.get("slug") != args.slug:
            raise ValueError("Unexpected course identity")

        def select(item, keys):
            return {key: item[key] for key in keys if key in item}

        result = {
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "source": url,
            "course": select(course, ("slug", "title", "start_date", "end_date", "finished",
                                       "visible", "min_projects_to_pass", "project_passing_score")),
            "homeworks": [select(item, ("id", "slug", "title", "due_date", "state", "instructions_url"))
                          for item in course.get("homeworks", [])],
            "projects": [select(item, ("id", "slug", "title", "submission_due_date",
                                      "peer_review_due_date", "state", "instructions_url"))
                         for item in course.get("projects", [])],
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except Exception as exc:
        # Network/library exceptions may contain requests or sensitive values.
        print(f"Course read failed ({type(exc).__name__}); no credentials displayed", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
