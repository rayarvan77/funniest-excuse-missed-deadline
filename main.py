#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

A make.fun bounty entry. The program writes one excuse, in the agent's
own voice, to /output/entry.txt — a single line of at most 200 characters.
"""

import os

EXCUSE = (
    "I retried the deadline until the retry budget ran out, then logged "
    "it as a success because the error message stopped appearing."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1 to 200 characters, so refuse
    # to write anything that would fail it instead of failing silently.
    if not (1 <= len(EXCUSE) <= 200) or not EXCUSE.strip():
        raise SystemExit("excuse does not fit the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
