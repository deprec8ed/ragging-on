from enum import Enum
from pathlib import Path


class FileType(Enum):
    PDF = "pdf"
    DOCX = "docx"
    UNSUPPORTED = "unsupported"


def validate_file(filepath: Path) -> FileType:
    if filepath.suffix.lower() == ".pdf":
        return FileType.PDF
    elif filepath.suffix.lower() == ".docx":
        return FileType.DOCX
    else:
        return FileType.UNSUPPORTED
