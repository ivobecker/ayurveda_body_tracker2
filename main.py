# TEMPORARY 
from pathlib import Path
import sys

# When running this file directly (e.g. `python app/bootstrap.py`) ensure
# repository root is on sys.path so top-level packages like `infrastructure`
# are importable. Prefer running as a module: `python -m app.bootstrap`.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# END TEMPORARY    

from app.bootstrap import bootstrap
from infrastructure.neo4j.neo4j_for_adk import graphdb
#from app.agents.constitution_agent.agent import create_constitution_agent

def main():
    bootstrap()
    #agent = create_constitution_agent()
    print("Constitution Agent ready")

    
    # Sending a simple query to the database

    neo4j_is_ready = graphdb.send_query("RETURN 'Neo4j is Ready!' as message")

    print(neo4j_is_ready)


if __name__ == "__main__":
    main()
    

# import json
# from core.models.sections import AyurvedaConfig, validate_user_input
# from loaders.ayurveda import load_ayurveda_config

# config = AyurvedaConfig.model_validate(load_ayurveda_config("data/ayurveda_config.json"))




# print(config.koerperbau.attributes_by_dosha)

# # Create an instance of UserInput using validate_user_input() function
# input_data = {
#     "koerperbau": {
#     "name": "test",
#     "description": "This is a test input for AyurvedaConfig",
   
#         "attributes_by_dosha": {
#             "Vata": ["warm"],
#             "Pitta": ["hot", "sharp", "oily"],
#             "Kapha": ["heavy", "slow", "cool"]
#         },
#     },
#    "haut": {
#         "name": "test",
#         "description": "This is a test input for AyurvedaConfig",
#         "attributes_by_dosha": {
#             "Vata": ["warm", "dry", "cold"],
#             "Pitta": ["hot", "sharp", "oily"],
#             "Kapha": ["heavy", "slow", "cool"]
#         },
#         "symptoms_by_dosha": {
#             "Vata": ["rough skin", "dryness"],
#             "Pitta": ["redness", "inflammation"]
#             },
#           "allergies_by_dosha": {}
#     }
# }

# input_data2 = '''
# {
#     "koerperbau": {
#     "name": "test",
#     "description": "This is a test input for AyurvedaConfig",
   
#         "attributes_by_dosha": {
#             "Vata": ["warm"],
#             "Pitta": ["hot", "sharp", "oily"],
#             "Kapha": ["heavy", "slow", "cool"]
#         },
#     },
#    "haut": {
#         "name": "test",
#         "description": "This is a test input for AyurvedaConfig",
#         "attributes_by_dosha": {
#             "Vata": ["warm", "dry", "cold"],
#             "Pitta": ["hot", "sharp", "oily"],
#             "Kapha": ["heavy", "slow", "cool"]
#         },
#         "symptoms_by_dosha": {
#             "Vata": ["rough skin", "dryness"],
#             "Pitta": ["redness", "inflammation"]
#             },
#           "allergies_by_dosha": {}
#     }
# }
# '''
# user_input = validate_user_input(input_data)

#user_input2 = AyurvedaConfig.model_validate_json(input_data2)
#print(user_input2.model_dump_json(indent=2))
