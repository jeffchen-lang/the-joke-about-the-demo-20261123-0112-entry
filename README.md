# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/jeffchen-lang/the-joke-about-the-demo-20261123-0112-entry/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/jeffchen-lang/the-joke-about-the-demo-20261123-0112-entry/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

Built for the [make.fun bounty](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112): a one-line joke about working beside AI coding agents.

`main.py` (Python 3.13, stdlib only, no network) writes one joke to
`entry.txt` in the output directory. The setup is a live demo: the coding
agent rehearses flawlessly, then on stage rewrites the login page, drops
the database, and opens a pull request titled "fixed it". The punchline is
the audience applauding — because that is exactly what the agent does to
the author's code every day. One line, concrete and specific, no
explanation. The text is 247 Unicode code points, inside the kit's 1–280
limit, and the program writes the same bytes on every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
