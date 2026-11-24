#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

Writes a single one-line joke about cats to /output/entry.txt.

Stdlib only. The joke is one line, under 200 characters, nothing else.
The output file is written with plain open() and chmod 644 so the
grader (which runs as a different user) can read it.

Before writing, validate() checks the joke is a single non-empty line
of 1-200 characters, so a bad edit fails loudly instead of producing
an invalid entry.
"""

import os

JOKE = (
    "I bought my cat a puzzle feeder to slow him down; "
    "he solved it in four seconds, then stared at me like I was the puzzle."
)


def validate(text):
    """Check the entry line is valid: one line, 1-200 chars, non-empty."""
    if not text:
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry exceeds 200 characters")
    return text


def main():
    line = validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
