"""Build pipe-delimited audio/transcript metadata from source folders."""

import argparse
import csv
from pathlib import Path


def read_transcript(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    text = text.replace(",", "").replace("%", "")
    return text.splitlines()


def write_metadata(source_dir: Path) -> None:
    transcript_path = source_dir / "transcript.txt"
    if not transcript_path.exists():
        return

    output_path = source_dir / "transcript.csv"
    lines = read_transcript(transcript_path)

    with output_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="|")
        for index, line in enumerate(lines, start=1):
            writer.writerow([f"{source_dir.name}-{index}.wav", line])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".", help="Directory containing transcript source folders")
    args = parser.parse_args()

    root = Path(args.root)
    for source_dir in sorted(path for path in root.iterdir() if path.is_dir()):
        write_metadata(source_dir)


if __name__ == "__main__":
    main()