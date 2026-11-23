"""One-Line Laugh entry: write one funny line to /output/entry.txt.

The line is a single sentence, at most 200 characters, on any subject.
Self-check gate: the text must be one sentence, 1-200 characters,
UTF-8, and contain no trailing newline.
"""

import os

LINE = "My plants died, so I bought plastic ones \u2014 now I feel guilty watering the fake ones out of habit."


def main() -> None:
    text = LINE.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if any(p in text[:-1] for p in ("!", "?")):
        raise SystemExit("entry must not hide a second sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry on disk does not match the checked text")


if __name__ == "__main__":
    main()
