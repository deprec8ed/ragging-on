from steps import structurer, parser, validator
from pathlib import Path


def pipeline(filepath: Path):
    validated = validator(filepath)
    parsed = parser(filepath)
    structurer = parsed

    return ""
