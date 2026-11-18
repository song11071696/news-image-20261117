#!/usr/bin/env python3
"""news-image-20261117: write the day's world-news image to /output/entry.png.

The entry image is bundled in this repository as entry.png: one 1024x1024
image summing up the world news of Tuesday 17 November 2026 (Kerch Bridge
strike, Trump at the ASEAN-Quad summit in Manila, Iran's drone attack on a
US radar base in Bahrain, the Optimizely supply-chain hack, and the Vulcan
rocket failure). It was composed from a generated background with all text
overlaid by PIL.

The program simply copies the bundled image to the harness output path.
It is offline and deterministic: the same bytes are written on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Guard the determinism the competition requires: what lands in
    # /output must be byte-for-byte the image bundled in this repository.
    with open(SRC, "rb") as f:
        expected = f.read()
    with open(DST, "rb") as f:
        actual = f.read()
    assert actual == expected, "output does not match the bundled image"


if __name__ == "__main__":
    main()
