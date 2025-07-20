from src.data_structures.graph import GraphBuild


def sample_graph() -> GraphBuild:
    """Creates a sample graph with edges and weights."""
    graph = GraphBuild()

    # Node A
    graph.add_edge("A", "B", 2).add_edge("A", "C", 3).add_edge("A", "D", 3)

    # Node B
    graph.add_edge("B", "A", 2).add_edge("B", "C", 4).add_edge("B", "E", 3)

    # Node C
    graph.add_edge("C", "D", 5).add_edge("C", "F", 6).add_edge("C", "E", 1)
    graph.add_edge("C", "A", 3).add_edge("C", "B", 4)

    # Node D
    graph.add_edge("D", "F", 7).add_edge("D", "A", 3).add_edge("D", "C", 5)

    # Node E
    graph.add_edge("E", "F", 8).add_edge("E", "B", 3).add_edge("E", "C", 1)

    # Node F
    graph.add_edge("F", "D", 7).add_edge("F", "C", 6).add_edge("F", "E", 8)
    graph.add_edge("F", "G", 9)

    # Node G
    graph.add_edge("G", "F", 9)

    return graph

def sample_graph_dijkstra() -> GraphBuild:
    """Creates a sample graph with edges and weights."""
    graph = GraphBuild()

    # Node A
    graph.add_edge("A", "B", 4).add_edge("A", "C", 2)

    # Node B
    graph.add_edge("B", "C", 3).add_edge("B", "D", 2).add_edge("B", "E", 3)

    # Node C
    graph.add_edge("C", "B", 1).add_edge("C", "D", 4).add_edge("C", "E", 5)

    # Node D

    # Node E
    graph.add_edge("E", "D", 1)

    return graph