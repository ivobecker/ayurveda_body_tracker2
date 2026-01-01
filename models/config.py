# config.py
from pydantic import BaseModel
from .sections import BaseDoshaSection, HautSection


class AyurvedaConfig(BaseModel):
    koerperbau: BaseDoshaSection
    haut: HautSection
