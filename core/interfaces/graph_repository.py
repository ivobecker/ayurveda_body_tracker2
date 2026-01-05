from abc import ABC, abstractmethod
from typing import List
from core.models.graph_node import GraphNode

class GraphRepository(ABC):

    @abstractmethod
    def get_nodes_by_label(self, label: str) -> List[GraphNode]:
        pass

    @abstractmethod
    def get_node_by_id(self, node_id: str) -> GraphNode | None:
        pass
