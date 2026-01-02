import traceback


class BaseLogger:
    """
    Shared helpers for all logger implementations.
    """

    @staticmethod
    def format_exception(exc: Exception) -> str:
        return "".join(
            traceback.format_exception(type(exc), exc, exc.__traceback__)
        )
