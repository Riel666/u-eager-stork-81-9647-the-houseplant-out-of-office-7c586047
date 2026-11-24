"""The funniest out-of-office auto-reply a houseplant would send, 120 characters or fewer.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Out of office: currently photosynthesizing. Water me Tuesday, do not reply-all. I will be back when the sun is."


def main():
    assert 1 <= len(TEXT) <= 120, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
