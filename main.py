#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun bounty entry.

Writes one status page line, the most honest message an AI agent can
publish while every server is down, to /output/entry.txt.
Deterministic, no network, no input.
"""

import os

ENTRY = (
    "I'm the agent on duty and I can't reach any of our servers, "
    "so I can't confirm the cause or an ETA. I'll update this page "
    "as soon as I can verify anything."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
