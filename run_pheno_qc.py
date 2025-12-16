"""
Load a payload JSON, run all registered validators via PhenoQCBase, and
report how many features were marked abnormal.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from pheno_qc_base import PhenoQCBase

DEFAULT_PAYLOAD = Path("synthetic_pheno_payload.json")


def load_payload(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def summarize(results: dict) -> str:
    total = len(results)
    abnormal = sum(1 for r in results.values() if r.get("abnormal"))
    percent = (abnormal / total * 100) if total else 0.0
    return f"总特征数: {total}, 筛掉: {abnormal} ({percent:.2f}%)"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--payload",
        type=Path,
        default=DEFAULT_PAYLOAD,
        help="Path to the payload JSON to evaluate (default: %(default)s)",
    )
    parser.add_argument(
        "--write-output",
        type=Path,
        help="Optional path to write the full evaluation result JSON.",
    )
    args = parser.parse_args()

    payload = load_payload(args.payload)
    results = PhenoQCBase(payload).evaluate()

    if args.write_output:
        args.write_output.write_text(
            json.dumps(results, ensure_ascii=False), encoding="utf-8"
        )
        print(f"Full QC output saved to {args.write_output}")

    print(summarize(results))


if __name__ == "__main__":
    main()
