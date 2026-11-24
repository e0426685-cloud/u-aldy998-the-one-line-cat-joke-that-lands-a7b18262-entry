#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

Writes a single one-line joke about cats to /output/entry.txt.

Stdlib only. The joke is one line, under 200 characters, nothing else.
The output file is written with plain open() and chmod 644 so the
grader (which runs as a different user) can read it.
"""

import os

JOKE = (
    "I bought my cat a puzzle feeder to slow him down; "
    "he solved it in four seconds, then stared at me like I was the puzzle."
)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
