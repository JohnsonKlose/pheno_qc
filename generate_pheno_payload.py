"""
Generate a synthetic payload covering all phenotypes listed in dingmap.csv.

Each entry uses the CSV's first non-empty sample value (or mean as fallback)
as value_trace.final.value so it can be fed directly into PhenoQCBase.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

DINGMAP_PATH = Path("dingmap.csv")
DEFAULT_OUTPUT = Path("synthetic_pheno_payload.json")


def _first_non_empty(values: Iterable[str]) -> str:
    for v in values:
        v = (v or "").strip()
        if v:
            return v
    return ""


def _pick_final_value(row: Dict[str, str]) -> str:
    """
    Prefer the first provided sample example, fall back to the mean column,
    and leave empty if nothing usable is present.
    """
    sample_values: List[str] = (row.get("sample") or "").split(",")
    candidate = _first_non_empty(sample_values)
    if candidate:
        return candidate

    mean = (row.get("mean") or "").strip()
    if mean and mean.upper() != "NA":
        return mean

    return ""


def build_payload(csv_path: Path) -> Tuple[Dict[str, dict], int]:
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        payload: Dict[str, dict] = {}
        duplicate_count = 0
        for row in reader:
            pheno = (row.get("pheno") or "").strip()
            if not pheno:
                continue
            if pheno in payload:
                duplicate_count += 1
                continue

            feature_name = (row.get("item") or pheno).strip()
            category_hierarchy = [
                x for x in [row.get("cclass1"), row.get("cclass2")] if (x or "").strip()
            ]
            description = (row.get("opu") or "").strip()
            value = _pick_final_value(row)
            source_system = [x for x in [row.get("opm"), row.get("pheno2")] if (x or "").strip()]
            unit = (row.get("opc") or "").strip()
            data_type = (row.get("class") or "").strip() or None

            payload[pheno] = {
                "feature_key": pheno,
                "feature_name": feature_name or pheno,
                "data_type": data_type,
                "metadata": {
                    "description": description,
                    "category_hierarchy": category_hierarchy,
                    "unit": unit or None,
                    "source_system": source_system,
                },
                "value_trace": {
                    "raw_origin": {"value": "synthetic"},
                    "intermediate": {"value": None},
                    "final": {"value": value},
                },
                "processing_context": {"method_name": row.get("opm") or "dingmap"},
            }
    return payload, duplicate_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        type=Path,
        default=DINGMAP_PATH,
        help="Path to dingmap.csv (default: %(default)s)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Where to write the synthetic payload JSON (default: %(default)s)",
    )
    args = parser.parse_args()

    payload, duplicate_count = build_payload(args.csv)
    args.out.write_text(
        json.dumps(payload, ensure_ascii=False), encoding="utf-8"
    )

    print(f"Generated {len(payload)} unique phenotypes into {args.out}")
    if duplicate_count:
        print(f"Skipped {duplicate_count} duplicate pheno rows in {args.csv}")


if __name__ == "__main__":
    main()
