# The World in One Day — news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/nickhellyou/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/nickhellyou/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A single front page summing up Sunday 22 November 2026 in 40 stories:
COP31 close to a deal in Antalya, Iran's strikes on US bases in
Bahrain, the Sparta II ablaze in the Baltic, and the day's other big
stories from every region, with a map, a stats strip, and a date check
that keeps 21 November stories off the page.

The image is pre-rendered and checked in as `entry.png` (1024x1024 PNG,
166,981 bytes). `main.py` only copies it to the output directory and
checks it is a real PNG under the 1 MiB limit, so every run produces
byte-identical output.

## Files

- `entry.png` — the front page itself, 1024x1024, 166,981 bytes
- `main.py` — the entrypoint: validates and copies `entry.png` (stdlib only)
- `LICENSE` — MIT

## How to run it

```sh
python3 main.py
```

That writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (`/output` by default).
The copy is verified by SHA-256 after writing, and two runs produce
byte-identical output (`6557d413be878b5f3c8d45f7175c3adddbb96b7de73f010c0e367da1d9faa77e`).
Point the variable somewhere else to write it somewhere else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=gg3rr7hw&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
