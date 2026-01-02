# core/interfaces/llm.py

# LLM contract (tool-aware)

from abc import ABC, abstractmethod
from typing import List, Optional
from core.models.tool_call import ToolCall

class LLM(ABC):
    @abstractmethod
    def generate(
        self,
        messages: list,
        tools: Optional[List[dict]] = None
    ) -> str | ToolCall:
        """
        Returns either:
        - Final assistant text
        - ToolCall request
        """
