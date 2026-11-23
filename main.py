"""One-star review of sleep, written to /output/entry.txt.

The review treats sleep as a subscription that cannot be cancelled:
it auto-renews every night, and the free trial is your entire life.
"""

import os

LINE = (
    "Sleep: the only subscription I can't cancel, it auto-renews "
    "every night, and the free trial is my entire life. One star."
)


def main() -> None:
    """Validate the review and write it to entry.txt, then verify it."""
    if not 1 <= len(LINE) <= 160:
        raise ValueError(f"review must be 1-160 characters, got {len(LINE)}")
    if LINE != LINE.strip():
        raise ValueError("review must not have leading or trailing whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("review must be a single line")
    if "!" in LINE:
        raise ValueError("deadpan review must not contain exclamation marks")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the review")


if __name__ == "__main__":
    main()
