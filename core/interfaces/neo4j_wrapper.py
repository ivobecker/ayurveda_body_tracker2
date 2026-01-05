# from abc import ABC, abstractmethod
# from typing import Iterable

# from infrastructure.database.neo4j_client import AyurvedaKGClient


# class neo4j_wrapper(ABC):
#     """
#     Abstract storage interface.

#     Implementations may include:
#     - Local filesystem
#     - S3 / GCS / Azure Blob
#     - In-memory storage
#     - Database-backed storage
#     """

#     @abstractmethod
#     def make_ayurveda_tools(kg_client: AyurvedaKGClient):
#         print ("Making Ayurveda KG tools")

      


# class Storage(ABC):
#     """
#     Abstract storage interface.

#     Implementations may include:
#     - Local filesystem
#     - S3 / GCS / Azure Blob
#     - In-memory storage
#     - Database-backed storage
#     """

#     @abstractmethod
#     def query_ayurveda_kg(cypher: str, params: dict):
#         return kg_client.query(cypher, params)


#     @abstractmethod
#     def save(self, path: str, data: bytes) -> None:
#         """
#         Persist raw bytes at the given path or key.
#         """
#         raise NotImplementedError

#     @abstractmethod
#     def load(self, path: str) -> bytes:
#         """
#         Load raw bytes from the given path or key.
#         """
#         raise NotImplementedError

#     @abstractmethod
#     def exists(self, path: str) -> bool:
#         """
#         Return True if the given path or key exists.
#         """
#         raise NotImplementedError

#     @abstractmethod
#     def delete(self, path: str) -> None:
#         """
#         Delete the given path or key.
#         """
#         raise NotImplementedError

#     @abstractmethod
#     def list(self, prefix: str = "") -> Iterable[str]:
#         """
#         List paths or keys under a prefix.
#         """
#         raise NotImplementedError
