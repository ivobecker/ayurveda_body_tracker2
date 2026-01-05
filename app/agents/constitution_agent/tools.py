from google.adk.tools import tool
from core.interfaces.graph_repository import GraphRepository
from core.interfaces.episode_store import EpisodeStore
from core.models.episode import Episode
from datetime import datetime
import uuid

# These will be injected via bootstrap
graph_repo: GraphRepository | None = None
episode_store: EpisodeStore | None = None


# Define a basic tool -- send a parameterized cypher query
def say_hello(person_name: str) -> dict:
    """Formats a welcome message to a named person. 

    Args:
        person_name (str): the name of the person saying hello

    Returns:
        dict: A dictionary containing the results of the query.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'query_result' key with an array of result rows.
              If 'error', includes an 'error_message' key.
    """
    return graphdb.send_query("RETURN 'Hello to you, ' + $person_name AS reply",
    {
        "person_name": person_name
    })


@tool
def query_constitution_tool(label: str):
    """Query constitutional nodes from Neo4j."""
    assert graph_repo is not None
    nodes = graph_repo.get_nodes_by_label(label)
    return [n.model_dump() for n in nodes]


@tool
def store_episode_tool(content: str):
    """Store an episode into Graphiti."""
    assert episode_store is not None

    episode = Episode(
        id=str(uuid.uuid4()),
        agent_name="constitution-agent",
        content=content,
        created_at=datetime.utcnow(),
    )
    episode_store.store_episode(episode)
    return {"status": "stored"}