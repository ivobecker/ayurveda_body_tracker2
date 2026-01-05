tools = [
  query_neo4j,
  get_graphiti_facts,
  store_graphiti_fact
]


User Input
   ↓
Constitution Agent
   ↓
Vikriti Agent
   ↓
Therapy Planning Agent
   ↓
Monitoring Agent
   ↓
Learning Agent


Python Application
Requirements:
Core Layers should contain business model (pydantic entities) and interfaces.
In agents i like to setup google-adk and wiring via bootstrap. i need to have tools for my first agent called constituion agent (tool to query neo4j and tool store an episode of graphiti)
In infrastructure i like to have the classes/utils for connecting to neo4j (crud operations) inline with core data model.
in infrastructure i need to have the graphiti-core connecter.
can you propose the layout, files, and examples.

core knows nothing about Neo4j, Graphiti, or Google ADK
agents depend only on core interfaces
infrastructure implements those interfaces
bootstrap assembles the system

root/
├── agents/
│   ├── __init__.py
│   ├── constitution_agent/
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── tools.py
│   │   └── prompts.py
│   │
│   └── bootstrap.py
├── services/
│   ├── __init__.py
│   │
│   └── bootstrap.py
├── core/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── constitution.py
│   │   ├── episode.py
│   │   └── graph_node.py
│   │
│   ├── interfaces/
│   │   ├── __init__.py
│   │   ├── graph_repository.py
│   │   └── episode_store.py
│   │
│   └── exceptions.py
│

│
├── infrastructure/
│   ├── __init__.py
│   ├── neo4j/
│   │   ├── __init__.py
│   │   ├── driver.py
│   │   ├── repositories.py
│   │   └── mappers.py
│   │
│   ├── graphiti/
│   │   ├── __init__.py
│   │   └── connector.py
│   │
│   └── settings.py
│
├── main.py
└── pyproject.toml