#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry for make.fun bounty
u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.

One short rant about a small everyday annoyance: hotel Wi-Fi that makes
you re-log in every ninety seconds behind a terms page longer than your
stay, turning a paying guest into their own unpaid IT department.
"""

import os
import sys


def rant_text():
    return (
        "The hotel Wi-Fi makes me re-log in every ninety seconds, and each time "
        "it shows me a terms page longer than my stay, a checkbox the size of a "
        "grain of rice, and a 'success' screen that lasts exactly until I open "
        "my email. I paid for a room and got a part-time job as my own IT "
        "department."
    )


def main() -> int:
    text = rant_text()
    if not (1 <= len(text) <= 400):
        print(f"bad length: {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("blank entry", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote /output/entry.txt: {len(text)} chars")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
