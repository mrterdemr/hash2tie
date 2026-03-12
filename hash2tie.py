#!/usr/bin/env python3

import argparse
import re
import sys
from pathlib import Path

TAGS = {
    32: "MD5Hash",
    40: "SHA1Hash",
    64: "SHA256Hash",
}

HEX_RE = re.compile(r"^[0-9a-fA-F]+$")


def detect_tag(h: str) -> str | None:
    return TAGS.get(len(h)) if HEX_RE.fullmatch(h) else None


def convert(input_file: Path, output_file: Path) -> None:
    with input_file.open(encoding="utf-8") as fin, output_file.open(
        "w", encoding="utf-8"
    ) as fout:
        fout.write("<TIEReputations>\n")

        for line_no, raw in enumerate(fin, 1):
            h = raw.strip()
            if not h:
                continue

            tag = detect_tag(h)
            if not tag:
                print(f"[!] Line {line_no} is invalid: {h}", file=sys.stderr)
                continue

            xml_block = (
                f"<FileReputation>\n"
                f"  <{tag}>{h}</{tag}>\n"
                f"  <ReputationLevel>1</ReputationLevel>\n"
                f"</FileReputation>\n"
            )
            fout.write(xml_block)

        fout.write("</TIEReputations>\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a hash list into FileReputation XML format for Trellix TIE"
    )
    parser.add_argument("input", help="Text file containing hashes (one hash per line)")
    parser.add_argument(
        "-o",
        "--output",
        default="file_reputations.xml",
        help="Output file path (default: file_reputations.xml)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_file():
        parser.error(f"Input file not found: {input_path}")

    convert(input_path, Path(args.output))


if __name__ == "__main__":
    main()
