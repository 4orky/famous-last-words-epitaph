#!/usr/bin/env python3
"""Write the winning epitaph to /output/entry.txt.

The epitaph was picked from fifteen original candidates, each scored
against the bounty's five judging criteria, in order: a one-line tombstone
epitaph of famous last words, a real laugh from a genuine joke, a surprise
that lands cleanly, reads like something carved in stone, and stays in the
head. The winner is a dying person's last words that turn on one word:

    I see the light. It's a train.

The first sentence is the oldest dying cliché there is; the second takes
it literally and runs it over. A revision pass tightened the draft
("I can see the light. It's a train.") by dropping the filler word "can":
the setup now sounds exactly like last words a person would actually say,
and both beats hit harder.
"""

import os
import sys

EPITAPH = "I see the light. It's a train."
MAX_CHARS = 150
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = EPITAPH.strip()
    if not text:
        print("error: epitaph is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: epitaph must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: epitaph is %d characters, over the 150 limit" % len(text),
            file=sys.stderr,
        )
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
