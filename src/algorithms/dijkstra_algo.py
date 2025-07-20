"""Dijkstra's Algorithm Barebones Python Implementation"""

from src.data_structures.ds_sample import sample_graph_dijkstra
from src.data_structures.graph import GraphBuild


def update_neighbor_node_distances(
    graph: dict[str, list[tuple[str, int]]],
    current_node: str,
    unvisited_nodes: set[str],
    distances: dict[str, float | int]
):
    """Attempts to update the distances of neighboring nodes from the current node."""
    for neighbor_node, weight in graph.get(current_node, []):
        if neighbor_node in unvisited_nodes:
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor_node]:
                distances[neighbor_node] = new_distance


def dijkstra_algorithm(
    graph: dict[str, list[tuple[str, int]]],
    start_node: str
) -> dict[str, float | int]:
    """Barebones implementation of Dijkstra's algo to find the shortest path from a start node."""

    distances = {
        node: 0 if node == start_node else float('inf')
        for node in graph.keys()
    }

    unvisited_nodes = set(graph.keys())

    while unvisited_nodes:
        current_node = min(
            (node for node in unvisited_nodes),
            key=lambda node: distances[node]
        )

        update_neighbor_node_distances(
            graph,
            current_node,
            unvisited_nodes,
            distances
        )

        unvisited_nodes.remove(current_node)

    return distances


class DijkstraGraphBuild(GraphBuild):
    """Graph class to build and represent the minimum spanning tree using Dijkstra's algorithm."""

    def __init__(
        self,
        distances: dict[str, float | int],
        start_node: str
    ):
        super().__init__()
        self.distances = distances
        self.start_node = start_node

        for node, distance in distances.items():
            self.add_edge(self.start_node, node, int(distance))


def main():
    """Main function"""
    graph = sample_graph_dijkstra()
    graph.print_graph()

    start_node = "A"
    shortest_paths = dijkstra_algorithm(graph.get_graph(), start_node)

    print(f"\nShortest paths from node {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"Distance to {node}: {distance}")

    dijkstra_graph = DijkstraGraphBuild(shortest_paths, start_node)
    dijkstra_graph.print_graph()

if __name__ == "__main__":
    main()
