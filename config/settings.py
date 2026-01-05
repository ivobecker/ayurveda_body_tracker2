# config/settings.py
import os
from dotenv import load_dotenv

# Load environment variables from a .env file (optional)
load_dotenv(override=True) # with override throug no python restart process needed

# Read values from environment variables
AZURE_BLOB_CONNECTION_STRING = os.getenv("AZURE_BLOB_CONNECTION_STRING")
AZURE_BLOB_CONTAINER = os.getenv("AZURE_BLOB_CONTAINER")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_DB = os.getenv("NEO4J_DB")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# Validate required settings
missing = [
    name for name, value in {
        "AZURE_BLOB_CONNECTION_STRING": AZURE_BLOB_CONNECTION_STRING,
        "AZURE_BLOB_CONTAINER": AZURE_BLOB_CONTAINER,
        "OPENAI_API_KEY": OPENAI_API_KEY,
        "NEO4J_URI": NEO4J_URI,
        "NEO4J_DB": NEO4J_DB,
        "NEO4J_USER": NEO4J_USER,
        "NEO4J_PASSWORD": NEO4J_PASSWORD
    }.items() if not value
]

if missing:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")
