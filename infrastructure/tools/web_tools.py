import requests
from core.interfaces.tool import Tool


class FetchUrlTool(Tool):
    """
    Fetch raw text content from a URL (GET only).
    """

    name = "fetch_url"
    description = "Fetch text content from a public URL"
    input_schema = {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "Public URL to fetch content from"
            }
        },
        "required": ["url"]
    }

    def run(self, url: str) -> str:
        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "LLM-Tool/1.0"}
        )
        response.raise_for_status()

        # Limit size to avoid prompt explosion
        text = response.text
        return text[:5_000]
