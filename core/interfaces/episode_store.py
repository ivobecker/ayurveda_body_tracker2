from abc import ABC, abstractmethod
from core.models.episode import Episode

class EpisodeStore(ABC):

    @abstractmethod
    def store_episode(self, episode: Episode) -> None:
        pass
