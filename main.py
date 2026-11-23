"""Write one short, intriguing text to /output/entry.txt.

The fragment opens a door and deliberately refuses to close it: the
same ritual logged for forty years, a voice that was never answered,
and then one final change that is never explained.
"""

import os

TEXT = (
    "For forty years the lighthouse keeper logged the same line every night: "
    "\u201cShe came again. I did not answer.\u201d "
    "In the forty-first year, the handwriting changed \u2014 and the line read: "
    "\u201cHe finally answered.\u201d"
)


def write_entry(path: str) -> None:
    # Write the fragment exactly as held in TEXT — no added newline.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)


if __name__ == "__main__":
    main()
