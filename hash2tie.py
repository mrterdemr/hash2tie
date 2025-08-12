#!/usr/bin/env python3
"""
hash2tie.py
----------
Girdi:  Her satırında bir MD5 (32 haneli), SHA-1 (40 haneli) ya da SHA-256 (64 haneli)
        onaltılık karma bulunan bir .txt dosyası
Çıktı:  file_reputations.txt  —  Her karma için aşağıdaki şablona göre XML bloğu:

<FileReputation>
  <MD5Hash|SHA1Hash|SHA256Hash>...</...>
  <ReputationLevel>1</ReputationLevel>
</FileReputation>
"""

import argparse
import re
import sys
from pathlib import Path

# Dizin uzunluğuna göre XML etiket adı
TAGS = {
    32: "MD5Hash",
    40: "SHA1Hash",
    64: "SHA256Hash",
}

HEX_RE = re.compile(r"^[0-9a-fA-F]+$")


def detect_tag(h: str) -> str | None:
    """Karma uzunluğuna göre uygun XML etiketini döndürür (yoksa None)."""
    return TAGS.get(len(h)) if HEX_RE.fullmatch(h) else None


def convert(input_file: Path, output_file: Path) -> None:
    """Girdi dosyasındaki karmaları XML’e dönüştürür ve çıktı dosyasına yazar."""
    with input_file.open(encoding="utf-8") as fin, output_file.open(
        "w", encoding="utf-8"
    ) as fout:
        for line_no, raw in enumerate(fin, 1):
            h = raw.strip()
            if not h:
                continue  # boş satırları atla

            tag = detect_tag(h)
            if not tag:
                print(f"[!] Satır {line_no} geçersiz: {h}", file=sys.stderr)
                continue

            xml_block = (
                f"<FileReputation>\n"
                f"  <{tag}>{h}</{tag}>\n"
                f"  <ReputationLevel>1</ReputationLevel>\n"
                f"</FileReputation>\n"
            )
            fout.write(xml_block)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Karma listesini FileReputation XML formatına dönüştürür"
    )
    parser.add_argument("input", help="Hash’leri içeren txt dosyası (bir karma/satır)")
    parser.add_argument(
        "-o",
        "--output",
        default="file_reputations.txt",
        help="Oluşturulacak çıktı dosyası (varsayılan: file_reputations.txt)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_file():
        parser.error(f"Girdi dosyası bulunamadı: {input_path}")

    convert(input_path, Path(args.output))


if __name__ == "__main__":
    main()
