from abc import ABC, abstractmethod
from typing import Iterable


class Storage(ABC):
    """
    Abstract storage interface.

    Implementations may include:
    - Local filesystem
    - S3 / GCS / Azure Blob
    - In-memory storage
    - Database-backed storage
    """

    @abstractmethod
    def save(self, path: str, data: bytes) -> None:
        """
        Persist raw bytes at the given path or key.
        """
        raise NotImplementedError

    @abstractmethod
    def load(self, path: str) -> bytes:
        """
        Load raw bytes from the given path or key.
        """
        raise NotImplementedError

    @abstractmethod
    def exists(self, path: str) -> bool:
        """
        Return True if the given path or key exists.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, path: str) -> None:
        """
        Delete the given path or key.
        """
        raise NotImplementedError

    @abstractmethod
    def list(self, prefix: str = "") -> Iterable[str]:
        """
        List paths or keys under a prefix.
        """
        raise NotImplementedError
