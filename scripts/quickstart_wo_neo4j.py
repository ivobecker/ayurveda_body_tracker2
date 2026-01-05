# Install first (in your terminal, not in Python):
# pip install graphiti-core

from graphiti_core.graphiti import Graph, Node, Edge

def main():
    # Create a new in-memory graph
    graph = Graph()

    # Create some nodes
    alice = Node(id="1", label="Person", properties={"name": "Alice", "age": 30})
    bob = Node(id="2", label="Person", properties={"name": "Bob", "age": 25})
    company = Node(id="3", label="Company", properties={"name": "Acme Corp"})

    # Add nodes to the graph
    graph.add_node(alice)
    graph.add_node(bob)
    graph.add_node(company)

    # Create relationships (edges)
    works_for = Edge(source="1", target="3", label="WORKS_FOR")
    friends_with = Edge(source="1", target="2", label="FRIENDS_WITH")

    # Add edges to the graph
    graph.add_edge(works_for)
    graph.add_edge(friends_with)

    # Query: Find all people Alice is connected to
    connections = graph.get_neighbors("1")
    print("Alice's connections:")
    for conn in connections:
        print(f"- {conn.label}: {conn.properties}")

    # Query: Find all edges from Alice
    edges = graph.get_edges("1")
    print("\nRelationships from Alice:")
    for e in edges:
        print(f"- {e.label} -> Node {e.target}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
