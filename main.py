#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun bounty entry.

Writes one brutally honest but still polite out-of-office auto-reply to
/output/entry.txt: the sender admits your email will sit unread until
January, by which time they will have moved on — and still thanks you
for your patience, so a manager would let it stand.
"""

import os

ENTRY = "Out of office: I'm on holiday, which means your email will be read in January by a version of me who has already moved on \u2014 thank you for your patience."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    # The brief wants one sentence: exactly one sentence-ending full stop,
    # at the very end (the em dash and comma inside are not sentence breaks).
    assert text.endswith(".") and text.count(".") == 1, (
        "entry must be a single sentence"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)}-char entry to {os.path.join(out_dir, 'entry.txt')}")


if __name__ == "__main__":
    main()
