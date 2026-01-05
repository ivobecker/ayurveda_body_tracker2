class GraphitiClient:
    def __init__(self, backend):
        self.backend = backend  # postgres / sqlite / neo4j_facts

    def get_facts(self, filter: dict):
        return self.backend.query(filter)

    def store_fact(self, fact: dict):
        self.backend.append(fact)
