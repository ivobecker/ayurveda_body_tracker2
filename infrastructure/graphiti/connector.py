from core.interfaces.episode_store import EpisodeStore
from core.models.episode import Episode
#from graphiti_core import GraphitiClient


class GraphitiEpisodeStore(EpisodeStore):

    def __init__(self, client: GraphitiClient):
        self._client = client

    def store_episode(self, episode: Episode) -> None:
        self._client.store_episode(
            episode_id=episode.id,
            content=episode.content,
            metadata={
                "agent": episode.agent_name,
                "created_at": episode.created_at.isoformat(),
            },
        )