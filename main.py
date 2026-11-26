#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

A deterministic program that writes the winning one-liner to
/output/entry.txt. The line is an excuse for skipping a pointless work
meeting: Outlook accepted the meeting on the speaker's behalf, so the
speaker reported Outlook to HR — and the complaint itself is pending a
meeting. It was picked by a blind pairwise tournament (6 candidates,
15 pairs) run against the judge brief verbatim: the winner swept 5/5.

Stdlib only. No input, no randomness, no network: the same bytes
every run.
"""

import os

ENTRY = (
    "Outlook accepted this meeting for me, so I have reported Outlook "
    "to HR for overstepping. It is pending a meeting."
)

# Gate from the competition rules: /output/entry.txt must be UTF-8
# text of 1 to 200 characters, not only white space.
MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} chars, gate needs 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back verification: what the grader reads is what we wrote.
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("read-back mismatch")


if __name__ == "__main__":
    main()
