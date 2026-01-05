from neo4j import GraphDatabase

class AyurvedaKGClient:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def query(self, cypher: str, params: dict):
        with self.driver.session(database="ayurveda_kg") as session:
            return session.run(cypher, params).data()