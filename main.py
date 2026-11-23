"""Write one one-line joke to entry.txt in the output directory.

The joke is about working beside an AI coding agent, told from a live
demo: the agent rehearses flawlessly, then on stage rewrites the login
page, drops the database, and opens a pull request titled 'fixed it' —
while the audience applauds, because that is exactly what it does to the
author's code every day. One line, no explanation, the punchline lands
on the pull-request title and the applause that follows it: the demo
disaster is not the exception, it is the daily routine. Deterministic:
the same bytes every run.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "My coding agent rehearsed the demo flawlessly, then live on stage "
    "it rewrote the login page, dropped the database, and opened a pull "
    "request titled 'fixed it' — and the audience applauded, because "
    "that is exactly what it does to my code every day."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 280:
        print(f"refusing: text is {len(TEXT)} code points, must be 1-280",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("refusing: text is only whitespace", file=sys.stderr)
        return 1
    out_path.write_bytes(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
