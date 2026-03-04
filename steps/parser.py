from docling_core.types.doc import DoclingDocument
from docling.document_converter import DocumentConverter
from pathlib import Path


def parse_document(filepath: Path, converter: DocumentConverter) -> DoclingDocument:
    contents = converter.convert(filepath)
    result = contents.document
    return result
