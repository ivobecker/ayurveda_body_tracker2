from neo4j import GraphDatabase

class Neo4jDriver:

    def __init__(self, uri: str, user: str, password: str, database: str = "neo4j"):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), database=database)

    def session(self):
        return self._driver.session()
