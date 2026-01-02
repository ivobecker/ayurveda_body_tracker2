from openai import OpenAI

from core.interfaces.llm import LLM
from core.models.tool_call import ToolCall
from infrastructure.llm.base import tool_to_openai

class OpenAILLM(LLM):
    def __init__(self, api_key: str, model="gpt-4.1"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate(self, messages, tools=None):
        response = self.client.responses.create(
            model=self.model,
            input=messages,
            tools=tools,
        )

        msg = response.output[0]

        if msg["type"] == "tool_call":
            return ToolCall(
                name=msg["name"],
                arguments=msg["arguments"]
            )

        return msg["content"][0]["text"]
