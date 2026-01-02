from core.interfaces.tool import Tool
from core.interfaces.storage import Storage


class SaveTextTool(Tool):
    """
    Save text content to a storage backend.
    """

    name = "save_text"
    description = "Save text content to storage at a given path"
    input_schema = {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Path or key where the text will be saved"
            },
            "content": {
                "type": "string",
                "description": "Text content to save"
            }
        },
        "required": ["path", "content"]
    }

    def __init__(self, storage: Storage):
        self.storage = storage

    def run(self, path: str, content: str) -> str:
        self.storage.save(path, content.encode("utf-8"))
        return f"Saved text to '{path}'"


class LoadTextTool(Tool):
    """
    Load text content from a storage backend.
    """

    name = "load_text"
    description = "Load text content from storage at a given path"
    input_schema = {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
                "description": "Path or key to load from"
            }
        },
        "required": ["path"]
    }

    def __init__(self, storage: Storage):
        self.storage = storage

    def run(self, path: str) -> str:
        data = self.storage.load(path)
        return data.decode("utf-8")
