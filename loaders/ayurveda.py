from core.models.sections import AyurvedaConfig
from .json_loader import load_model_from_json


def load_ayurveda_config(path: str) -> AyurvedaConfig:
    return load_model_from_json(path, AyurvedaConfig)
