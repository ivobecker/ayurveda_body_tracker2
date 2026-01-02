# infrastructure/storage/azure_blob.py
from typing import Iterable
from azure.storage.blob import BlobServiceClient, ContainerClient
from core.interfaces.storage import Storage


class AzureBlobStorage(Storage):
    """
    Azure Blob Storage implementation of the Storage interface.
    """

    def __init__(
        self,
        connection_string: str,
        container_name: str,
        prefix: str = "",
        read_only=False        
    ):
        """
        :param connection_string: Azure Blob Storage connection string
        :param container_name: Blob container name
        :param prefix: Optional key prefix (acts like a base directory)
        """
        self.service_client = BlobServiceClient.from_connection_string(
            connection_string
        )
        self.container: ContainerClient = (
            self.service_client.get_container_client(container_name)
        )
        self.prefix = prefix.strip("/")
        self.read_only = read_only

    def _blob_name(self, path: str) -> str:
        if self.prefix:
            return f"{self.prefix}/{path.lstrip('/')}"
        return path.lstrip("/")

    def save(self, path: str, data: bytes) -> None:
        if self.read_only:
            raise PermissionError("Storage is read-only")
        blob_name = self._blob_name(path)
        blob = self.container.get_blob_client(blob_name)
        blob.upload_blob(data, overwrite=True)

    def load(self, path: str) -> bytes:
        blob_name = self._blob_name(path)
        blob = self.container.get_blob_client(blob_name)
        return blob.download_blob().readall()

    def exists(self, path: str) -> bool:
        blob_name = self._blob_name(path)
        blob = self.container.get_blob_client(blob_name)
        return blob.exists()

    def delete(self, path: str) -> None:
        blob_name = self._blob_name(path)
        blob = self.container.get_blob_client(blob_name)
        blob.delete_blob(delete_snapshots="include")

    def list(self, prefix: str = "") -> Iterable[str]:
        full_prefix = self._blob_name(prefix)
        blobs = self.container.list_blobs(name_starts_with=full_prefix)

        for blob in blobs:
            name = blob.name
            if self.prefix:
                name = name[len(self.prefix) + 1 :]
            yield name
