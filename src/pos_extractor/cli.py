import argparse
import sys
from pathlib import Path

from .extractor import extract_from_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pos-extract",
        description="Extract unique nouns and verbs from a text file using spaCy.",
    )
    parser.add_argument("input_file", help="Path to the input text file.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    input_path = Path(args.input_file)

    if not input_path.is_file():
        print(f"Error: file not found: {input_path}", file=sys.stderr)
        return 2

    try:
        nouns, verbs = extract_from_file(input_path)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"Error reading file: {exc}", file=sys.stderr)
        return 2

    print(f"Nouns ({len(nouns)}):")
    for noun in nouns:
        print(f"- {noun}")

    print(f"\nVerbs ({len(verbs)}):")
    for verb in verbs:
        print(f"- {verb}")

    return 0
