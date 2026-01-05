from pydantic import BaseModel
from datetime import datetime

class Episode(BaseModel):
    id: str
    agent_name: str
    content: str
    created_at: datetime
