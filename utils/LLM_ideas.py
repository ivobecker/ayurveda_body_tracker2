from typing import List
from pydantic import BaseModel, Field

class FAQLookupArgs(BaseModel):
    query: str = Field(..., description="User's query")
    tags: List[str] = Field(..., description="Relevant keyword tags from the customer query")
    top_k: int = Field(5, description="Number of top relevant FAQ entries to retrieve") 

#Lookup tool

# https://learn.microsoft.com/en-us/azure/developer/ai/how-to/extract-entities-using-structured-outputs?tabs=github-codespaces