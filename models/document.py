from __future__ import annotations
from enum import Enum
from dataclasses import dataclass, field
from typing import Optional

class NodeType(Enum):
    HEADING = "heading"
    PARAGRAPH = "paragraph"
    TABLE = "table"

@dataclass
class DocumentNode:
    title: Optional[str]
    level: int
    node_type: NodeType
    text: Optional[str] = None
    parent: Optional[DocumentNode] = None
    children: list[DocumentNode] = field(default_factory=list)
