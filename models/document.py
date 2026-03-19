from __future__ import annotations
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional


class NodeType(Enum):
    TITLE = "title"
    SECTION_HEADER = "section_header"
    TEXT = "text"
    LIST = "list"
    LIST_ITEM = "list_item"
    TABLE = "table"
    PICTURE = "picture"
    SKIP = "skip"


@dataclass
class DocumentNode:
    level: int
    node_type: NodeType
    title: Optional[str] = None
    text: Optional[str] = None
    parent: Optional[DocumentNode] = None
    children: list[DocumentNode] = field(default_factory=list)
    page_number: Optional[int] = None

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "level": self.level,
            "node_type": self.node_type.value,
            "text": self.text,
            "children": [child.to_dict() for child in self.children],
            "page_number": self.page_number
        }
