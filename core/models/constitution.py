from pydantic import BaseModel
from typing import List

class Constitution(BaseModel):
    id: str
    title: str
    articles: List[str]
