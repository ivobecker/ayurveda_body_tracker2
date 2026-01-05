# app/bootstrap.py

# # TEMPORARY 
# from pathlib import Path
# import sys

# # When running this file directly (e.g. `python app/bootstrap.py`) ensure
# # repository root is on sys.path so top-level packages like `infrastructure`
# # are importable. Prefer running as a module: `python -m app.bootstrap`.
# ROOT = Path(__file__).resolve().parents[1]
# if str(ROOT) not in sys.path:
#     sys.path.insert(0, str(ROOT))

# # END TEMPORARY    

# bootstrap.py is your composition root.

# It: creates concrete implementations
#     wires interfaces → implementations
#     returns fully-wired services

# It does NOT:
# handle requests
# contain business logic
# get imported everywhere

# The Mental Model (Important)

# - bootstrap.py → Creates objects
# - entrypoint → Calls bootstrap + starts app
        # Common entrypoints:
        # main.py (CLI / script)
        # uvicorn main:app (FastAPI)
        # Azure Function handler
        # Celery worker
# - services / use cases → Use injected dependencies

# Nothing imports bootstrap.py except the entrypoint

#from infrastructure.logging.config import configure_logging
#from infrastructure.logging.structured_logger import StructuredLogger
from infrastructure.storage.azure_blob import AzureBlobStorage
from infrastructure.tools.storage_tools import SaveTextTool, LoadTextTool
from infrastructure.tools.web_tools import FetchUrlTool
from infrastructure.tools.file_tools import ReadFileTool

#NEO4J / GRAPHITI
from infrastructure.neo4j.driver import Neo4jDriver
from infrastructure.neo4j.repositories import Neo4jGraphRepository
#from infrastructure.neo4j.neo4j_for_adk import graphdb

#from infrastructure.graphiti.connector import GraphitiEpisodeStore
#from graphiti_core import GraphitiClient

#from graphiti_core import Graphiti # check was client before




#from core.interfaces.tool_registry import ToolRegistry
#from app.services.llm_service import LLMService
#from infrastructure.llm.openai_llm import OpenAILLM
from config import settings

#
#from app.agents.constitution_agent.agent import tools

def bootstrap():
    # 1. logging (first!)
    # configure_logging()
    # logger = StructuredLogger(service_name="llm-app")

    # 2. storage
    storage = AzureBlobStorage(
        connection_string=settings.AZURE_BLOB_CONNECTION_STRING,
        container_name=settings.AZURE_BLOB_CONTAINER,
        prefix="llm-artifacts"
    )

    # 3. tools
    # tool_registry = ToolRegistry()
    # tool_registry.register(SaveTextTool(storage, logger))
    # tool_registry.register(LoadTextTool(storage, logger))
    # tool_registry.register(FetchUrlTool(logger))
    # tool_registry.register(ReadFileTool(logger))    

    # 4. LLM
    # llm = OpenAILLM(
    #     api_key=settings.OPENAI_API_KEY,
    #     model="gpt-4.1"
    # )

    # # 5. services
    # llm_service = LLMService(
    #     llm=llm,
    #     tool_registry=tool_registry,
    #     logger=logger
    # )

    # 6. NEO4J 

    neo4j_driver = Neo4jDriver(
        uri=settings.NEO4J_URI,
        user=settings.NEO4J_USER,
        password=settings.NEO4J_PASSWORD,
        database=settings.NEO4J_DB
    )
    graph_repo = Neo4jGraphRepository(neo4j_driver)

    # NEO4J ADK
    #graphdb.

    # Inject dependencies into tools
   # tools.graph_repo = graph_repo


    # 7. GRAPHITI

    # graphiti_client = Graphiti(
    #      uri=settings.NEO4J_URI,
    #      user=settings.NEO4J_USER,
    #      password=settings.NEO4J_PASSWORD
    # )
      
    # episode_store = GraphitiEpisodeStore(graphiti_client)


    # Inject dependencies into tools
   # tools.graph_repo = graph_repo
   # tools.episode_store = episode_store

    #return llm_service  







