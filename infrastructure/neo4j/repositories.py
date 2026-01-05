from core.interfaces.graph_repository import GraphRepository
from core.models.graph_node import GraphNode
from infrastructure.neo4j.driver import Neo4jDriver
from infrastructure.neo4j.mappers import record_to_graph_node

class Neo4jGraphRepository(GraphRepository):

    def __init__(self, driver: Neo4jDriver):
        self._driver = driver

    def get_nodes_by_label(self, label: str):
        query = f"MATCH (n:{label}) RETURN n"
        with self._driver.session() as session:
            result = session.run(query)
            return [record_to_graph_node(r) for r in result]

    def get_node_by_id(self, node_id: str):
        query = "MATCH (n) WHERE id(n) = $id RETURN n"
        with self._driver.session() as session:
            record = session.run(query, id=int(node_id)).single()
            return record_to_graph_node(record) if record else None