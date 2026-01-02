import structlog
from core.interfaces.logger import Logger
from infrastructure.logging.base import BaseLogger


class StructuredLogger(Logger, BaseLogger):
    """
    JSON structured logger using structlog.
    """

    def __init__(self, service_name: str = "llm-app"):
        self.logger = structlog.get_logger(service_name)

    def info(self, message: str, **kwargs):
        self.logger.info(message, **kwargs)

    def warning(self, message: str, **kwargs):
        self.logger.warning(message, **kwargs)

    def error(self, message: str, **kwargs):
        self.logger.error(message, **kwargs)

    def debug(self, message: str, **kwargs):
        self.logger.debug(message, **kwargs)
