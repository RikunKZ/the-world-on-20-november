"""make.fun news-image-20261120 entry program.

Writes one image that sums up the world's news of Friday
20 November 2026 to /output/entry.png. The repository holds the
image (entry.png, 1024x1024, under 1 MiB); this program copies it
to the output directory. No network, no input, deterministic:
every run writes the same bytes.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    src = Path(__file__).with_name("entry.png")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    # The gate runs the program twice and both runs must write the
    # same bytes; verify the copy landed byte for byte.
    if dst.read_bytes() != src.read_bytes():
        raise SystemExit("output does not match the repository image")


if __name__ == "__main__":
    main()
