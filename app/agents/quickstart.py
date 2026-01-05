import asyncio
from datetime import datetime, timezone
from turtle import clear

from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType
from graphiti_core.driver.neo4j_driver import Neo4jDriver
from graphiti_core.search.search_filters import SearchFilters


from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Custom Entity Types
class Person(BaseModel):
    """A person entity with biographical information."""
    age: Optional[int] = Field(None, description="Age of the person")
    occupation: Optional[str] = Field(None, description="Current occupation")
    location: Optional[str] = Field(None, description="Current location")
    birth_date: Optional[datetime] = Field(None, description="Date of birth")

class Company(BaseModel):
    """A business organization."""
    industry: Optional[str] = Field(None, description="Primary industry")
    founded_year: Optional[int] = Field(None, description="Year company was founded")
    headquarters: Optional[str] = Field(None, description="Location of headquarters")
    employee_count: Optional[int] = Field(None, description="Number of employees")

class Product(BaseModel):
    """A product or service."""
    category: Optional[str] = Field(None, description="Product category")
    price: Optional[float] = Field(None, description="Price in USD")
    release_date: Optional[datetime] = Field(None, description="Product release date")

# Custom Edge Types
class Employment(BaseModel):
    """Employment relationship between a person and company."""
    position: Optional[str] = Field(None, description="Job title or position")
    start_date: Optional[datetime] = Field(None, description="Employment start date")
    end_date: Optional[datetime] = Field(None, description="Employment end date")
    salary: Optional[float] = Field(None, description="Annual salary in USD")
    is_current: Optional[bool] = Field(None, description="Whether employment is current")

class Investment(BaseModel):
    """Investment relationship between entities."""
    amount: Optional[float] = Field(None, description="Investment amount in USD")
    investment_type: Optional[str] = Field(None, description="Type of investment (equity, debt, etc.)")
    stake_percentage: Optional[float] = Field(None, description="Percentage ownership")
    investment_date: Optional[datetime] = Field(None, description="Date of investment")

class Partnership(BaseModel):
    """Partnership relationship between companies."""
    partnership_type: Optional[str] = Field(None, description="Type of partnership")
    duration: Optional[str] = Field(None, description="Expected duration")
    deal_value: Optional[float] = Field(None, description="Financial value of partnership")

entity_types = {
    "Person": Person,
    "Company": Company,
    "Product": Product
}

edge_types = {
    "Employment": Employment,
    "Investment": Investment,
    "Partnership": Partnership
}

edge_type_map = {
    ("Person", "Company"): ["Employment"],
    ("Company", "Company"): ["Partnership", "Investment"],
    ("Person", "Person"): ["Partnership"],
    ("Entity", "Entity"): ["Investment"],  # Apply to any entity type
}

# Create a Neo4j driver with custom database name
    
graphiti = Graphiti(
uri="bolt://localhost:7687",
user="neo4j",
password="neo4jneo4j"
)



async def main():
    # Connect to Neo4j
    graphiti = Graphiti(
    uri="bolt://localhost:7687",
    user="neo4j",
    password="neo4jneo4j"
    )
    try:
        # Create indices & constraints (run once)

        
        #await clear_data(graphiti.driver)
        #await graphiti.build_indices_and_constraints()
        #print("Graph initialized")



        # # Add an episode — unstructured text
        # await graphiti.add_episode(
        #     name="meeting_1",
        #     episode_body="Alice met Bob at the AI conference in San Francisco in March 2024",
        #     source=EpisodeType.text,
        #     source_description="meeting note",
        #     reference_time=datetime.now(timezone.utc),
        # )
        # print("Episode added")

        # # Add a JSON episode
        # await graphiti.add_episode(
        #     name="alice_info",
        #     episode_body={
        #         "person": "Alice",
        #         "role": "Data Scientist",
        #         "city": "San Francisco"
        #     },
        #     source=EpisodeType.json,
        #     source_description="person metadata",
        #     reference_time=datetime.now(timezone.utc),
        # )
        # print("JSON episode added")



        # await graphiti.add_episode(
        #     name="Business Update",
        #     episode_body="Sarah joined TechCorp as CTO in January 2023 with a $200K salary. TechCorp partnered with DataCorp in a $5M deal.",
        #     source_description="Business news",
        #     reference_time=datetime.now(),
        #     entity_types=entity_types,
        #     edge_types=edge_types,
        #     edge_type_map=edge_type_map
        # )
        # print("Using Custom Entity and Edge Types a episode added")     

        # Search for only specific entity types
        # search_filter = SearchFilters(
        #     node_labels=["Person", "Company"]  # Only return Person and Company entities
        #  )
        # results = await graphiti.search_(
        #     query="Who works at tech companies?",
        #     search_filter=search_filter
        # )
        # print('\nSearch Results:Search for only specific entity types:')
        # for result in results:
        #     print(f'UUID: {result.uuid}')
        #     print(f'Fact: {result.fact}')
        #     if hasattr(result, 'valid_at') and result.valid_at:
        #         print(f'Valid from: {result.valid_at}')
        #     if hasattr(result, 'invalid_at') and result.invalid_at:
        #         print(f'Valid until: {result.invalid_at}')
        #     print('---')

        # # Search for only specific edge types
        # search_filter = SearchFilters(
        #     edge_types=["Employment", "Partnership"]  # Only return Employment and Partnership edges
        # )
        # results = await graphiti.search_(
        #     query="Tell me about business relationships",
        #     search_filter=search_filter
        # )
        # print('\nSearch Results: Search for only specific edge types')
        # for result in results:
        #     print(f'UUID: {result.uuid}')
        #     print(f'Fact: {result.fact}')
        #     if hasattr(result, 'valid_at') and result.valid_at:
        #         print(f'Valid from: {result.valid_at}')
        #     if hasattr(result, 'invalid_at') and result.invalid_at:
        #         print(f'Valid until: {result.invalid_at}')
        #     print('---')



        # A basic search over stored episodes
        # results = await graphiti.search("Alice San Francisco", num_results=5)
        # print("Search results:")
        # for r in results:
        #     print(f"- {r.fact} (score {r.score})")


        # Perform a hybrid search combining semantic similarity and BM25 retrieval
        print("\nSearching for: 'Alice San Francisco'")
        search_filter = SearchFilters(
           node_labels=["Person", "Company"]  # Only return Person and Company entities
        )
        results = await graphiti.search(query='Alice San Francisco',search_filter=search_filter)
        # Print search results
        print('\nSearch Results:')
        for result in results:
            print(f'UUID: {result.uuid}')
            print(f'Fact: {result.fact}')
            if hasattr(result, 'valid_at') and result.valid_at:
                print(f'Valid from: {result.valid_at}')
            if hasattr(result, 'invalid_at') and result.invalid_at:
                print(f'Valid until: {result.invalid_at}')
            print('---')


        # print("Perform a hybrid search combining semantic similarity and BM25 retrieval")
        # # Use the top search result's UUID as the center node for reranking
        # if results and len(results) > 0:
        #     # Get the source node UUID from the top result
        #     center_node_uuid = results[0].source_node_uuid
        #     print('\nReranking search results based on graph distance:')
        #     print(f'Using center node UUID: {center_node_uuid}')
        #     reranked_results = await graphiti.search(
        #         'Who was the California Attorney General?', center_node_uuid=center_node_uuid
        #     )
        #     # Print reranked search results
        #     print('\nReranked Search Results:')
        #     for result in reranked_results:
        #         print(f'UUID: {result.uuid}')
        #         print(f'Fact: {result.fact}')
        #         if hasattr(result, 'valid_at') and result.valid_at:
        #             print(f'Valid from: {result.valid_at}')
        #         if hasattr(result, 'invalid_at') and result.invalid_at:
        #             print(f'Valid until: {result.invalid_at}')
        #         print('---')
        # else:
        #     print('No results found in the initial search to use as center node.')



    finally:
        # Cleanly close connection
        await graphiti.close()

async def serch_with_filter():
    # Connect to Neo4j
    graphiti = Graphiti(
    uri="bolt://localhost:7687",
    user="neo4j",
    password="neo4jneo4j"
    )
    try:        
      # Perform a hybrid search combining semantic similarity and BM25 retrieval
        print("Perform a hybrid search combining semantic similarity and BM25 retrieval")
        print("\nSearching for: 'Alice San Francisco'")
        search_filter = SearchFilters(
           node_labels=["Person", "Company"]  # Only return Person and Company entities
        )
        results = await graphiti.search(query='Alice San Francisco',search_filter=search_filter)
        # Print search results
        print('\nSearch Results:')
        for result in results:
            print(f'UUID: {result.uuid}')
            print(f'Fact: {result.fact}')
            if hasattr(result, 'valid_at') and result.valid_at:
                print(f'Valid from: {result.valid_at}')
            if hasattr(result, 'invalid_at') and result.invalid_at:
                print(f'Valid until: {result.invalid_at}')
            print('---')
    finally:
        # Cleanly close connection
        await graphiti.close()

if __name__ == "__main__":
    print(__name__)
    asyncio.run(main())
    asyncio.run(serch_with_filter())
