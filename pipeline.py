from docling.document_converter import DocumentConverter
from steps.validator import validate_file, FileType
from steps.parser import parse_document
from steps.structurer import structure_document
from models.document import DocumentNode
from pathlib import Path


def pipeline(filepath: Path) -> DocumentNode:
    validated = validate_file(filepath)
    if validated == FileType.UNSUPPORTED:
        raise ValueError(f"Unsupported file type: {filepath.suffix}")
    document_converter = DocumentConverter()
    parsed = parse_document(filepath, document_converter)
    structured = structure_document(parsed, filepath)
    return structured
