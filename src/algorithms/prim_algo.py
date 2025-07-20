"""Prim's Algorithm Barebones Python Implementation"""

from src.algorithms.utils import EdgesIndex
from src.data_structures.graph import GraphBuild, sample_graph


def find_min_edge(edges: list, visited: set) -> tuple[int, str, str] | None:
    """Finds the minimum edge from the list of edges that connects to an unvisited node."""
    min_edge = None
    min_weight = float("inf")

    for weight, from_node, to_node in edges:
        if to_node not in visited and weight < min_weight:
            min_weight = weight
            min_edge = (weight, from_node, to_node)

    return min_edge


def prim_algorithm(
    graph: dict[str, list[tuple[str, int]]], start_node: str
) -> list[tuple[int, str, str]]:
    """Barebones implementation of Prim's algorithm to find the min. spanning tree of a graph."""
    min_span_tree: list[tuple[int, str, str]] = []
    visited = set([start_node])
    edges = [(weight, start_node, to_node) for to_node, weight in graph[start_node]]

    while edges:
        min_edge = find_min_edge(edges, visited)

        if min_edge is None:
            break

        weight, _, to_node = min_edge

        min_span_tree.append(min_edge)
        visited.add(to_node)

        for next_to_node, next_weight in graph[to_node]:
            if next_to_node not in visited:
                edges.append((next_weight, to_node, next_to_node))
            edges = [
                edge
                for edge in edges
                if edge[EdgesIndex.TO_NODE.value] != to_node
                or edge[EdgesIndex.WEIGHT.value] != weight
            ]

    return min_span_tree


class PrimGraphBuild(GraphBuild):
    """Graph class to build and represent the minimum spanning tree using Prim's algorithm."""

    def __init__(self, min_span_tree: list[tuple[int, str, str]]):
        super().__init__()
        self.min_span_tree = min_span_tree

        for edge in min_span_tree:
            weight, from_node, to_node = edge
            self.add_edge(from_node, to_node, weight)

    def print_visited_nodes(self):
        """Prints the nodes visited in the minimum spanning tree."""
        print("Visited nodes in the Minimum Spanning Tree:")
        for weight, from_node, to_node in self.min_span_tree:
            print(f"{from_node} -- {to_node} == {weight}")


def main():
    """Main function"""
    graph = sample_graph()
    graph.print_graph()
    print(f"\nTotal weight of the graph: {graph.get_weight_sum()}\n")

    prim_algorithm_result = prim_algorithm(graph.get_graph(), "A")

    prim_graph = PrimGraphBuild(prim_algorithm_result)
    prim_graph.print_graph()
    prim_graph.print_visited_nodes()
    print(f"\nTotal weight of the graph: {prim_graph.get_weight_sum()}\n")


if __name__ == "__main__":
    main()
