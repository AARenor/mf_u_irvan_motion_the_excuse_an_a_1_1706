#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

The entry is one line, at most 200 characters, for the bounty
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.
"""

import os
import sys

TEXT = "I lost the bounty. I'd blame the model, but I am the model."

OUTPUT_NAME = "entry.txt"


def resolve_output_dir() -> str:
    """Return the directory the entry file is written to."""
    return (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"

    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
