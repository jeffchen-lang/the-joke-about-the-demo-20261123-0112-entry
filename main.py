"""Emit one one-line joke about a coding agent to entry.txt.

The joke is set at a live demo: the agent rehearses perfectly, then on
stage rewrites the login page, drops the database, and opens a pull
request titled 'fixed it' — and the audience applauds, because that is
exactly what it does to the author's code every single day. One line,
no explanation, the punchline landing on the pull-request title and
the applause that follows it: the demo disaster is not the exception,
it is the daily routine, repeated every single day. The program is fully deterministic: it writes the same
bytes on every run, uses no network, no clock and no randomness.
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
    if not 1 <= len(TEXT) <= 280:
        print(
            f"refusing: text is {len(TEXT)} code points, must be 1-280",
            file=sys.stderr,
        )
        return 1
    if not TEXT.strip():
        print("refusing: text is only whitespace", file=sys.stderr)
        return 1
    out_path.write_bytes(TEXT.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
