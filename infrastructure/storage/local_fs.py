# infrastructure/storage/local_fs.py

from pathlib import Path
from core.interfaces.storage import Storage


class LocalFileStorage(Storage):
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)

    def _resolve(self, path: str) -> Path:
        return self.base_dir / path

    def save(self, path: str, data: bytes) -> None:
        full_path = self._resolve(path)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_bytes(data)

    def load(self, path: str) -> bytes:
        return self._resolve(path).read_bytes()

    def exists(self, path: str) -> bool:
        return self._resolve(path).exists()

    def delete(self, path: str) -> None:
        self._resolve(path).unlink(missing_ok=True)

    def list(self, prefix: str = ""):
        base = self._resolve(prefix)
        if not base.exists():
            return []
        return [
            str(p.relative_to(self.base_dir))
            for p in base.rglob("*")
            if p.is_file()
        ]
