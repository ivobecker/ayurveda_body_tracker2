
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "evil-pilate-roughly")
)

def setup_ayurveda_graph(tx):
    tx.run("""
        MERGE (:Dosha {name:"Vata"})
        MERGE (:Dosha {name:"Pitta"})
        MERGE (:Dosha {name:"Kapha"})
    """)

with driver.session() as session:
    session.execute_write(setup_ayurveda_graph)

driver.close()
print("Doshas created successfully")
