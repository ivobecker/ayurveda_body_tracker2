# core/models/tool_result.py

from dataclasses import dataclass
from typing import Any

@dataclass
class ToolResult:
    name: str
    output: Any
