from unittest.mock import Mock
import sys
from pathlib import Path

# Ensure repository root is on sys.path when running this file directly
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from infrastructure.tools.file_tools import ReadFileTool

def test_read_file_logs():
    logger = Mock()
    tool = ReadFileTool(logger=logger)

    # assuming file exists
    tool.run("example.txt")

    logger.info.assert_called_once()