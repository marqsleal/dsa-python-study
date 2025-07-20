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
