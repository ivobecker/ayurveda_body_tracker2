# config.py
from pydantic import BaseModel, ValidationError
from .sections import BaseDoshaSection, HautSection


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