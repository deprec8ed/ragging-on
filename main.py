from pipeline import pipeline
from pathlib import Path
import argparse
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=Path)
    args = parser.parse_args()

    piped = pipeline(args.filepath)
    result = piped.to_dict()

    output_path = args.filepath.with_suffix(".json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
