from steps.validator import validate_file, FileType
from pathlib import Path
import pytest


@pytest.mark.parametrize("filepath, expected", [
    (Path("test.pdf"), FileType.PDF),
    (Path("test.docx"), FileType.DOCX),
    (Path("test.jpg"), FileType.UNSUPPORTED),
])
def test_validate_file(filepath, expected):
    assert validate_file(filepath) == expected
