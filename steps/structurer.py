from models.document import DocumentNode, NodeType
from docling_core.types.doc import DoclingDocument, DocItemLabel
from typing import Optional
from pathlib import Path

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


def get_item_text(item) -> Optional[str]:
    return getattr(item, "text", None)


def structure_document(doc: DoclingDocument, filepath: Path) -> DocumentNode:
    root = DocumentNode(
        level=0,
        node_type=NodeType.TITLE,
        title=filepath.stem,
    )
    stack = []
    stack.append(root)
    previous_node_type = None

    for item, level in doc.iterate_items():
        node_type = map_label_to_node_type(item.label)

        if node_type == NodeType.SKIP:
            continue

        if node_type == NodeType.TITLE:
            root = DocumentNode(
                title=get_item_text(item),
                level=0,
                node_type=NodeType.TITLE,
            )
            stack.append(root)
            previous_node_type = node_type

        if node_type == NodeType.SECTION_HEADER:
            while stack[-1].level >= level:
                stack.pop()
            node = DocumentNode(
                level=level,
                node_type=NodeType.SECTION_HEADER,
                parent=stack[-1],
                text=get_item_text(item)
            )
            stack[-1].children.append(node)
            stack.append(node)

        if node_type in (NodeType.TEXT, NodeType.TABLE, NodeType.PICTURE):
            if previous_node_type == NodeType.LIST_ITEM:
                stack.pop()
            node = DocumentNode(
                level=level,
                node_type=node_type,
                text=get_item_text(item),
                parent=stack[-1],
            )
            stack[-1].children.append(node)

        if node_type == NodeType.LIST_ITEM:
            if previous_node_type != NodeType.LIST_ITEM:
                list_node = DocumentNode(
                    level=level,
                    node_type=NodeType.LIST,
                    parent=stack[-1],
                )
                stack[-1].children.append(list_node)
                stack.append(list_node)
            list_item_node = DocumentNode(
                level=level,
                node_type=NodeType.LIST_ITEM,
                parent=stack[-1],
                text=get_item_text(item),
            )
            stack[-1].children.append(list_item_node)

        previous_node_type = node_type

    return root
