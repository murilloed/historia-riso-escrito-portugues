"""Locate candidate passages in downloaded PDFs. Confirm matches on the page."""

import argparse
import json
import re
import unicodedata
from pathlib import Path

import pymupdf


TERMS = re.compile(
    r"\b(?:risos?|risadas?|gargal(?:h|lh)\w*|sorri\w*|rindo|riu)\b"
)


def passages(path):
    with pymupdf.open(path) as document:
        for number, page in enumerate(document, 1):
            raw = re.sub(r"(?<=\w)-[ \t]*\r?\n[ \t]*(?=\w)", "", page.get_text())
            passage = " ".join(raw.split())
            normalized = "".join(
                char for char in unicodedata.normalize("NFD", passage)
                if not unicodedata.combining(char)
            ).lower()
            for match in TERMS.finditer(normalized):
                start, end = match.span()
                yield {
                    "file": str(path),
                    "pdf_page": number,
                    "term": passage[start:end],
                    "context": passage[max(0, start - 70):end + 70],
                }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, nargs="+")
    args = parser.parse_args()
    for path in args.pdf:
        for result in passages(path):
            print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
