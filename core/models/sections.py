# sections.py
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, field_validator, ValidationError


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


class DoshaScoring(BaseModel):
    Vata: int = Field(0, ge=0, le=3)
    Pitta: int = Field(0, ge=0, le=3)
    Kapha: int = Field(0, ge=0, le=3)


# 3️⃣ Base Section Model
class BaseDoshaSection(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    attributes_by_dosha: DoshaMap
    scoring_by_dosha: DoshaScoring

# 4️⃣ Haut Section (Extended)
class HautSection(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

    attributes_by_dosha: DoshaMap
    hautfaerbung_by_dosha: DoshaMap
    symptoms_by_dosha: DoshaMap
    allergies_by_dosha: DoshaMap



class AyurvedaConfig(BaseModel):
    koerperbau: BaseDoshaSection
    haut: HautSection




# Define a function to handle user input validation safely
def validate_user_input(input_data):
    try:
        # Attempt to create a AyurvedaConfig model instance from user input data
        ayurveda_input = AyurvedaConfig(**input_data)
        print("Valid ayurveda_input created:")
        print(f"{ayurveda_input.model_dump_json(indent=2)}")
        return ayurveda_input
    except ValidationError as e:
        # Capture and display validation errors in a readable format
        print("Validation error occurred:")
        missing_fields = []
        # Print non-missing errors immediately, collect missing fields
        for error in e.errors():
            loc = ".".join(str(p) for p in error.get("loc", []))
            msg = error.get("msg", "")
            err_type = error.get("type", "")
            if "field required" in msg.lower() or "missing" in err_type or "required" in err_type:
                missing_fields.append(loc or "<unknown>")
            else:
                print(f"  - {loc}: {msg}")
        if missing_fields:
            if len(missing_fields) == 1:
                print(f"  - Missing required field: {missing_fields[0]}")
            else:
                print(f"  - Missing required fields:")
                for f in missing_fields:
                    print(f"    - {f}")
        return None