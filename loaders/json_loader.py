import json
from pathlib import Path
from typing import Type, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


def load_model_from_json(file_path: str | Path, model: Type[T]) -> T:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    return model.model_validate(data)
