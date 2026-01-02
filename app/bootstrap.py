from core.interfaces.tool_registry import ToolRegistry
from infrastructure.logging.structured_logger import StructuredLogger
from infrastructure.storage.azure_blob import AzureBlobStorage
from infrastructure.tools.storage_tools import SaveTextTool, LoadTextTool
from infrastructure.tools.web_tools import FetchUrlTool
from infrastructure.tools.file_tools import ReadFileTool
from infrastructure.logging.config import configure_logging
from infrastructure.logging.structured_logger import StructuredLogger


configure_logging()
logger = StructuredLogger(service_name="llm-tools")
#logger = StructuredLogger(service_name="document-processor")

storage = AzureBlobStorage(
    connection_string=settings.AZURE_BLOB_CONNECTION_STRING,
    container_name=settings.AZURE_BLOB_CONTAINER,
    prefix="llm-artifacts"
)

#registry = ToolRegistry()
#registry.register(SaveTextTool(storage))
#registry.register(LoadTextTool(storage))
#registry.register(FetchUrlTool())

#save_tool = SaveTextTool(storage)
save_text_tool = SaveTextTool(storage=storage, logger=logger)
read_file_tool = ReadFileTool(logger=logger)
load_tool = LoadTextTool(storage)












