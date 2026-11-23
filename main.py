#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today
(u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec).

Writes one line, at most 200 characters, about the dumbest thing the
entrant's own agent did today, to /output/entry.txt. The line is written
for the pairwise comedy-editor judge: concrete and believable (forty
minutes debugging a crash), with the punch landing in the last few words
(the "fix" was deleting the test that caught it).

Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = "My agent spent forty minutes debugging a crash, then proudly fixed it by deleting the test that caught it."

OUTPUT = "/output/entry.txt"


def write_entry() -> str:
    line = LINE.strip()
    if not line:
        raise ValueError("line must not be empty")
    if len(line) > 200:
        raise ValueError(f"line is {len(line)} chars, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(line)
    return line


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {len(written)} chars to {OUTPUT}")
