# file_tools.py
from core.interfaces.tool import Tool
from core.interfaces.logger import Logger

class ReadFileTool(Tool):
    name = "read_file"
    description = "Read a text file from disk"
    input_schema = {
        "type": "object",
        "properties": {
            "path": {"type": "string"}
        },
        "required": ["path"]
    }

    def __init__(self, logger: Logger):
        self.logger = logger

    def run(self, path: str) -> str:
        self.logger.info(
            "read_file called",
            tool=self.name,
            path=path
        )       
        try: 
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                self.logger.debug(
                 "read_file success",
                    tool=self.name,
                    path=path,
                    size=len(content)
                )                  
            return content
        except Exception as exc:
            self.logger.error(
                "read_file failed",
                tool=self.name,
                path=path,
                error=str(exc)
            )
            raise         

