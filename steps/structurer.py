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


def structure_document(doc: DoclingDocument) -> DocumentNode:
    root = None
    stack = []
    previous_node_type = None

    for item, level in doc.iterate_items():
        node_type = map_label_to_node_type(item.label)

        if node_type == NodeType.SKIP:
            continue

        if node_type == NodeType.TITLE:
            root = DocumentNode(
                title=item.text,
                level=0,
                node_type=NodeType.TITLE,
            )
            stack.append(root)
            previous_node_type = node_type

        if node_type == NodeType.SECTION_HEADER:
            if not stack:
                root = DocumentNode(
                    title="unknown",
                    level=0,
                    node_type=NodeType.TITLE,
                )
            while stack[-1].level >= level:
                stack.pop()
            node = DocumentNode(
                level=level,
                node_type=NodeType.SECTION_HEADER,
                parent=stack[-1],
                text=item.text
            )
            stack[-1].children.append(node)
            stack.append(node)

        if node_type in (NodeType.TEXT, NodeType.TABLE, NodeType.PICTURE):
            node = DocumentNode(
                level=level,
                node_type=node_type,
                text=item.text,
                parent=stack[-1],
            )
            stack[-1].children.append(node)

    return root
