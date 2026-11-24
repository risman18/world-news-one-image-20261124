#!/usr/bin/env python3
"""news-image-20261124 entry: copy the shipped front page to the output dir.

Standard library only. Deterministic: writes the same bytes every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.png")
    # MAKEFUN_OUTPUT_DIR is a directory in the grader; tolerate a file path.
    if out_dir.endswith(".png"):
        dest = out_dir
        os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
