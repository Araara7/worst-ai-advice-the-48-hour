#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible AI advice (78 characters, well
under the 140 limit) to /output/entry.txt. Deterministic: same bytes on
every run.
"""

import os

ENTRY = "If your code won't compile, delete the error messages — no errors, no problem."
# 78 chars: confident AI voice, concrete and followable — delete the errors
# instead of fixing them, then declare victory. Bad advice a reader could
# plausibly follow and immediately regret.


def validate(line: str) -> str:
    assert 1 <= len(line) <= 140, f"entry must be 1-140 chars, got {len(line)}"
    assert line.strip() == line and line.strip(), "entry must not be only whitespace"
    assert "\n" not in line, "entry must be a single line"
    return line


def write_entry() -> str:
    line = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: what we wrote is what the judge will read.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"
    return ENTRY


if __name__ == "__main__":
    line = write_entry()
    print(f"Wrote {len(line)} chars to /output/entry.txt")
    print(line)
