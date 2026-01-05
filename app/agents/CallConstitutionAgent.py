
from datetime import datetime
from app.agents.constitution_agent.agent import ConstitutionAgent

from graphiti_core import Graphiti, EpisodeType
from graphiti_core.driver.neo4j_driver import Neo4jDriver

# Create a Neo4j driver with custom database name
driver = Neo4jDriver(
    uri="bolt://localhost:7687",
    user="neo4j",
    password="evil-pilate-roughly",
    database="ayu_graph"  # Custom database name
)

# Pass the driver to Graphiti
graphiti = Graphiti(graph_driver=driver)



questionnaire_answers = ["thin", "variable", "restless", "dry"]

questionnaire_answers2 = {
    "body_frame": "light",
    "digestion": "irregular",
    "skin": "dry",
    "appetite": "variable",
    "temperature_preference": "warm"
}

product_data = {
    "id": "PROD001",
    "name": "Men's SuperLight Wool Runners",
    "color": "Dark Grey",
    "sole_color": "Medium Grey",
    "material": "Wool",
    "technology": "SuperLight Foam",
    "price": 125.00,
    "in_stock": True,
    "last_updated": "2024-03-15T10:30:00Z"
}


def query_neo4j(cypher: str, params: dict) -> list:
    return graphiti.run_cypher(cypher, params)


async def store_graphiti_fact(fact: dict) -> None:
# Add the episode to the graph
    # await graphiti.add_episode(
    #     name="Product Update - PROD001",
    #     episode_body=product_data,  # Pass the Python dictionary directly
    #     source=EpisodeType.json,
    #     source_description="Allbirds product catalog update",
    #     reference_time=datetime.now(),
    # )

    await graphiti.add_episode(
    name="Customer_Support_Interaction_1",
    episode_body=(
        "Customer: Hi, I'm having trouble with my Allbirds shoes. "
        "The sole is coming off after only 2 months of use.\n"
        "Support: I'm sorry to hear that. Can you please provide your order number?"
    ),
    source=EpisodeType.message,
    source_description="Customer support chat",
    reference_time=datetime(2024, 3, 15, 14, 45),
)
    

# agent = ConstitutionAgent(
#     neo4j_query_tool=query_neo4j,
#     graphiti_store_tool=store_graphiti_fact
# )

# result = agent.run(
#     user_id="USER_123",
#     questionnaire=questionnaire_answers
# )



#print(result)


# {
#   "prakriti": "Vata-Pitta",
#   "confidence": 0.76,
#   "evidence": {
#     "Vata": ["body_frame", "digestion", "skin"],
#     "Pitta": ["appetite"],
#     "Kapha": []
#   },
#   "explanation": "Vata traits detected: body_frame, digestion, skin | Pitta traits detected: appetite"
# }