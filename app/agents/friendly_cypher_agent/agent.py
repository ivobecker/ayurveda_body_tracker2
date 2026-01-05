# Import necessary libraries
import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm # For OpenAI support
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types # For creating message Content/Parts
from typing import Optional, Dict, Any
#NEO4J / GRAPHITI from BOOTSRAP INJECTION
from infrastructure.neo4j.driver import Neo4jDriver
# Convenience libraries for working with Neo4j inside of Google ADK
from infrastructure.neo4j.neo4j_for_adk import graphdb
from config import settings

import warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.CRITICAL)

print("Libraries imported.")

# # Define Model Constants for easier use 
# MODEL_GPT = "openai/gpt-4o"

# llm = LiteLlm(model=MODEL_GPT)

# # Test LLM with a direct call
# print(llm.llm_client.completion(model=llm.model, 
#                                 messages=[{"role": "user", 
#                                            "content": "Are you ready?"}], 
#                                 tools=[]))

# print("\nOpenAI is ready for use.")



# Sending a simple query to the database
neo4j_is_ready = graphdb.send_query("RETURN 'Neo4j is Ready!' as message")

print(neo4j_is_ready)