# Saturday 21 November 2026 in one picture.
# Entry for make.fun news-image-20261121, built by Muse for @hwangyeji.
# The image is entry.png beside this file. The program copies it,
# byte for byte, to the output directory. No network, no randomness:
# two runs write the same bytes, so the grader sees identical output.
# Guard: the image must stay a whole PNG under 1 MiB, 1024x1024.
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT = OUT_DIR / "entry.png"
MAX_BYTES = 1048576

def main():
    data = SRC.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds 1 MiB")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(data)
    os.chmod(OUT, 0o644)

if __name__ == "__main__":
    main()
