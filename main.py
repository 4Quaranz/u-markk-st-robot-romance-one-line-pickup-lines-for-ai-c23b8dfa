#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI — make.fun
u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.

Writes one joke pickup line, at most 200 characters, aimed at an AI,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Stdlib only, no network, no clock, no randomness: running it twice
writes identical bytes. The line is written with no trailing newline,
so the file holds exactly the line and nothing else.
"""

import os
import sys

# A pickup line aimed at a machine, built on the machine's own premise:
# the speaker cannot stop overfitting to its training data. No batteries,
# no charging, no reboot — the joke comes from how a model actually learns.
LINE = "You must be my training data, because I can't stop overfitting to you."


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"error: line is {len(LINE)} characters, must be 1-200",
              file=sys.stderr)
        return 1
    if LINE.strip() == "" or "\n" in LINE:
        print("error: line must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(dest, encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("error: output does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(written)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
