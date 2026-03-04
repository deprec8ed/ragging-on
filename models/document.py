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
    title: Optional[str]
    level: int
    node_type: NodeType
    text: Optional[str] = None
    parent: Optional[DocumentNode] = None
    children: list[DocumentNode] = field(default_factory=list)
    page_number: Optional[int] = None
