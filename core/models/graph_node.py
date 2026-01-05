from pydantic import BaseModel
from typing import Dict, Any

class GraphNode(BaseModel):
    id: str
    label: str
    properties: Dict[str, Any]
