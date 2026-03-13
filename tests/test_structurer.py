from steps.parser import parse_document
from steps.structurer import structure_document
from models.document import NodeType
from docling.document_converter import DocumentConverter
from docling_core.types.doc import DoclingDocument
from pathlib import Path


def test_structure_document():
    path = Path("tests/fixtures/test_file.pdf")
    converter = DocumentConverter()
    parsed = parse_document(path, converter)
    result = structure_document(parsed, path)
    assert result != None
    assert result.node_type == NodeType.TITLE
    assert result.children != None
    assert any(child.node_type ==
               NodeType.SECTION_HEADER for child in result.children)
    section = next(child for child in result.children if child.node_type ==
                   NodeType.SECTION_HEADER)
    assert len(section.children) > 0
