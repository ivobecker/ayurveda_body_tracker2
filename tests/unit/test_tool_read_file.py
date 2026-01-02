from unittest.mock import Mock
from infrastructure.tools.file_tools import ReadFileTool

def test_read_file_logs():
    logger = Mock()
    tool = ReadFileTool(logger=logger)

    # assuming file exists
    tool.run("example.txt")

    logger.info.assert_called_once()