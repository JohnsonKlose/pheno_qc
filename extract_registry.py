import json
import sys
from pathlib import Path


SUBSTRING = "感官-耳声发射测试仪"


def load_json(path: Path):
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def iter_feature_keys(obj):
    if isinstance(obj, dict):
        # top-level dict whose values are feature payloads
        for value in obj.values():
            if isinstance(value, dict):
                key = value.get("feature_key")
                if isinstance(key, str):
                    yield key
    elif isinstance(obj, list):
        # list of feature payloads
        for value in obj:
            if isinstance(value, dict):
                key = value.get("feature_key")
                if isinstance(key, str):
                    yield key


def main(raw_path: str):
    path = Path(raw_path)
    if not path.is_file():
        raise SystemExit(f"File not found: {path}")

    data = load_json(path)
    matches = [key for key in iter_feature_keys(data) if SUBSTRING in key]

    if not matches:
        print("No feature_key matched the substring.")
        return

    for key in matches:
        print(f'registry["{key}"] = ')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python extract_registry.py <path-to-json>")
    main(sys.argv[1])
