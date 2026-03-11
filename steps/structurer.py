from models.document import DocumentNode, NodeType
from docling_core.types.doc import DoclingDocument, DocItemLabel


LABEL_MAP = {
    DocItemLabel.TITLE: NodeType.TITLE,
    DocItemLabel.SECTION_HEADER: NodeType.SECTION_HEADER,
    DocItemLabel.TEXT: NodeType.TEXT,
    DocItemLabel.LIST_ITEM: NodeType.LIST_ITEM,
    DocItemLabel.TABLE: NodeType.TABLE,
    DocItemLabel.PICTURE: NodeType.PICTURE,
}


def map_label_to_node_type(label: DocItemLabel) -> NodeType:
    return LABEL_MAP.get(label, NodeType.SKIP)
