from core.models.graph_node import GraphNode

def record_to_graph_node(record) -> GraphNode:
    node = record["n"]
    return GraphNode(
        id=str(node.id),
        label=list(node.labels)[0],
        properties=dict(node),
    )
