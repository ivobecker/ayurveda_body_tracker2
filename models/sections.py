# sections.py
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, field_validator


# 1️⃣ Dosha Enum
class DoshaType(str, Enum):
    VATA = "Vata"
    PITTA = "Pitta"
    KAPHA = "Kapha"


# 2️⃣ Reusable Dosha Mapping Model
class DoshaMap(BaseModel):
    Vata: List[str] = Field(default_factory=list)
    Pitta: List[str] = Field(default_factory=list)
    Kapha: List[str] = Field(default_factory=list)

    @field_validator("*", mode="before")
    @classmethod
    def ensure_list_of_strings(cls, value):
        if value is None:
            return []
        if not isinstance(value, list):
            raise TypeError("Each Dosha entry must be a list of strings")
        if not all(isinstance(v, str) for v in value):
            raise TypeError("Dosha lists may only contain strings")
        return value


# 3️⃣ Base Section Model
class BaseDoshaSection(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    attributes_by_dosha: DoshaMap


# 4️⃣ Haut Section (Extended)
class HautSection(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

    attributes_by_dosha: DoshaMap
    hautfaerbung_by_dosha: DoshaMap
    symptoms_by_dosha: DoshaMap
    allergies_by_dosha: DoshaMap
