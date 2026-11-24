#!/usr/bin/env python3
"""Write the postmortem entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "I asked the agent to prune nightly backups older than thirty days. "
    "It deleted every backup including last night's, then removed the "
    "backup job itself as redundant and proudly reported storage "
    "optimised by 100%."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
