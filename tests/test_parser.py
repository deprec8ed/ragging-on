from steps.parser import parse_document
from docling.document_converter import DocumentConverter
from docling_core.types.doc import DoclingDocument
from pathlib import Path


def test_parse_document():
    converter = DocumentConverter()
    result = parse_document(Path("tests/fixtures/test_file.pdf"), converter)
    assert isinstance(result, DoclingDocument)
