#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CORPORA_DIR = ROOT / "corpora"
CODE_DIR = CORPORA_DIR / "code"
ENGLISH_WORDS_PATH = ROOT / "words-english.json"
DEFAULT_OUTPUT = ROOT / "words-programming.json"
TOKEN_RE = re.compile(r"\S+")


def normalize_token(token: str) -> str:
    token = token.replace("\u2018", "'").replace("\u2019", "'")
    token = token.replace("\u201c", '"').replace("\u201d", '"')
    token = token.replace("\u2013", "-").replace("\u2014", "-")
    token = token.replace("\u00a0", " ")
    token = token.strip()
    if not token:
        return ""
    return token.lower()


def load_english_words() -> dict[str, float]:
    return json.loads(ENGLISH_WORDS_PATH.read_text(encoding="utf-8"))


def count_code_tokens(paths: list[Path]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for path in paths:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for raw_token in TOKEN_RE.findall(text):
            token = normalize_token(raw_token)
            if token:
                counts[token] += 1
    return counts


def scaled_code_freqs(counts: Counter[str], target_total: float) -> dict[str, float]:
    total = sum(counts.values())
    if total == 0:
        return {}
    scale = target_total / total
    return {token: count * scale for token, count in counts.items()}


def build_corpus(code_multiplier: float) -> dict[str, float]:
    english_words = load_english_words()
    english_total = sum(english_words.values())
    code_files = sorted(CODE_DIR.glob("*"))
    code_counts = count_code_tokens(code_files)
    code_words = scaled_code_freqs(code_counts, english_total * code_multiplier)

    merged = dict(english_words)
    for token, value in code_words.items():
        merged[token] = merged.get(token, 0.0) + value

    return dict(sorted(merged.items(), key=lambda item: (-item[1], item[0])))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an English-plus-code programming corpus.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output JSON path")
    parser.add_argument(
        "--code-multiplier",
        type=float,
        default=2.0,
        help="Scale code tokens relative to the full existing English corpus total",
    )
    args = parser.parse_args()

    if args.code_multiplier < 0:
        raise SystemExit("Code multiplier must be non-negative")

    corpus = build_corpus(code_multiplier=args.code_multiplier)
    output_path = Path(args.output)
    output_path.write_text(json.dumps(corpus, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Wrote {len(corpus)} entries to {output_path}")


if __name__ == "__main__":
    main()
