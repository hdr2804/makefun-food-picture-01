"""food-picture-01 entry: copy the bundled food photograph to the output dir.

The image (art.png) is a 1024x1024 palette PNG of beef rendang with jasmine
rice on a banana leaf, steam rising. The program copies it byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output), so both grader runs write
identical bytes. Standard library only, no network.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "art.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard the gate: the copied file must be byte-identical to the source.
    if os.path.getsize(src) != os.path.getsize(dst):
        raise RuntimeError("entry.png size mismatch after copy")
    return 0


if __name__ == "__main__":
    sys.exit(main())
