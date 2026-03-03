from enum import Enum
from pathlib import Path

class FileType(Enum):
    PDF = "pdf"
    DOCX = "docx"
    UNSUPPORTED = "unsupported"


def validate_file(filepath):
    if Path(filepath).suffix == toLower(".pdf"):
        return FileType.PDF
