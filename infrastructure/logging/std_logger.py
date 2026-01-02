# infrastructure/logging/std_logger.py
import logging
from core.interfaces.logger import Logger
from infrastructure.logging.base import BaseLogger


class StdLogger(Logger, BaseLogger):
    """
    Wrapper around Python's standard logging module.
    """

    def __init__(self, name: str = "app", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, message: str, **kwargs):
        self.logger.info(message, extra=kwargs or None)

    def warning(self, message: str, **kwargs):
        self.logger.warning(message, extra=kwargs or None)

    def error(self, message: str, **kwargs):
        self.logger.error(message, extra=kwargs or None)

    def debug(self, message: str, **kwargs):
        self.logger.debug(message, extra=kwargs or None)
