"""One-line performance review entry (make.fun, 140 characters or fewer).

The program writes the review line to /output/entry.txt as UTF-8.
It uses only the Python standard library.
"""

import os

ENTRY_TEXT = "Exceeds Expectations at 'just handle it'; Needs Improvement at defining 'it.' Recommend promotion to spectator."


def main() -> None:
    assert 1 <= len(ENTRY_TEXT) <= 140, "entry must be 1 to 140 characters"
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
