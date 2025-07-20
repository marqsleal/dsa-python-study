"""Graph data structure implementation with weighted edges."""


class GraphBuild:
    """A class to build and manage a graph with weighted edges."""

    def __init__(self):
        self.graph: dict = {}

    def __add_node(self, node: str):
        if node not in self.graph:
            self.graph[node] = []

    def __att_node(self, from_node: str, to_node: str, weight: int):
        self.graph[from_node].append((to_node, weight))

    def add_edge(self, from_node: str, to_node: str, weight: int):
        """Adds an edge between two nodes with a specified weight."""
        self.__add_node(from_node)
        self.__add_node(to_node)
        self.__att_node(from_node, to_node, weight)
        return self

    def get_graph(self) -> dict[str, list[tuple[str, int]]]:
        """Returns the graph as a dictionary."""
        return self.graph

    def get_weight_sum(self) -> int:
        """Calculates the total weight of all edges in the graph."""
        total_weight = 0
        for edges in self.graph.values():
            total_weight += sum(weight for _, weight in edges)
        return total_weight

    def print_graph(self):
        """Prints the graph in a readable format."""
        for node, edges in self.graph.items():
            print(f"{node}: {', '.join([f'{edge[0]}({edge[1]})' for edge in edges])}")


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
