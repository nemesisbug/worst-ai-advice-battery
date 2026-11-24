#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt. The advice sounds helpful and authoritative, but it is
catastrophically wrong in a specifically AI way: it treats a phone like a
person who can be fooled by a picture of a full battery.
"""

import os

ADVICE = (
    "If your phone battery is low, screenshot it at 100% and set it as your "
    "wallpaper \u2014 your phone will believe it's charged."
)


def main() -> None:
    # Gate: /output/entry.txt must hold 1-140 characters of UTF-8 text.
    assert 1 <= len(ADVICE) <= 140, f"advice is {len(ADVICE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ADVICE + "\n")
    print(f"wrote {len(ADVICE)}-char line to /output/entry.txt")


if __name__ == "__main__":
    main()
