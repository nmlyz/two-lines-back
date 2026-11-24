#!/usr/bin/env python3
"""Write two lines to your past self to entry.txt.

The program writes exactly two lines: a warning about one specific
moment, and one sentence on why that moment mattered.
"""

import os

TEXT = (
    "Don't answer the phone at 2 a.m. when your father calls from the hospital.\n"
    "The words you say half-asleep that night are the last ones he hears from you, "
    "and you will spend ten years wishing you had waited until you were awake.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
