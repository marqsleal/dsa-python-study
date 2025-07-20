"""Kruskal's Algorithm Barebones Python Implementation"""

from src.algorithms.utils import EdgesIndex
from src.data_structures.ds_sample import sample_graph
from src.data_structures.graph import GraphBuild


def merge_sort_edges_by_weight(
    edges: list[tuple[int, str, str]],
) -> list[tuple[int, str, str]]:
    """Sorts edges by weight using merge sort."""
    if len(edges) <= 1:
        return edges

    middle_node = len(edges) // 2

    edges_left_half = merge_sort_edges_by_weight(edges[:middle_node])
    edges_right_half = merge_sort_edges_by_weight(edges[middle_node:])

    return merge_lists(edges_left_half, edges_right_half)


def merge_lists(
    edges_left_half: list[tuple[int, str, str]],
    edges_right_half: list[tuple[int, str, str]],
) -> list[tuple[int, str, str]]:
    """Merges two sorted lists of edges by weight."""
    sorted_list = []
    i, j = 0, 0

    while i < len(edges_left_half) and j < len(edges_right_half):
        if (
            edges_left_half[i][EdgesIndex.WEIGHT.value]
            < edges_right_half[j][EdgesIndex.WEIGHT.value]
        ):
            sorted_list.append(edges_left_half[i])
            i += 1
        else:
            sorted_list.append(edges_right_half[j])
            j += 1

    sorted_list.extend(edges_left_half[i:])
    sorted_list.extend(edges_right_half[j:])

    return sorted_list


def find_node_parent(parent: dict, node: str) -> str:
    """Finds the parent of a node in the disjoint set."""
    if parent[node] != node:
        parent[node] = find_node_parent(parent, parent[node])
    return parent[node]


def union_nodes(parent: dict[str, str], rank: dict[str, int], node1: str, node2: str):
    """Unites two nodes in the disjoint set."""
    root1 = find_node_parent(parent, node1)
    root2 = find_node_parent(parent, node2)

    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2

        elif rank[root1] > rank[root2]:
            parent[root2] = root1

        else:
            parent[root2] = root1
            rank[root1] += 1


def kruskal_algorithm(
    graph: dict[str, list[tuple[str, int]]],
) -> list[tuple[int, str, str]]:
    """Barebones implementation of Kruskal's algorithm to find the min. spanning tree of a graph."""
    edges: list[tuple[int, str, str]] = []
    seen: set[tuple[str, str]] = set()

    for from_node in graph:
        for to_node, weight in graph[from_node]:
            if (to_node, from_node) not in seen:
                edges.append((weight, from_node, to_node))
                seen.add((from_node, to_node))

    sorted_edges = merge_sort_edges_by_weight(edges)

    parent: dict[str, str] = {}
    rank: dict[str, int] = {}
    min_span_tree: list[tuple[int, str, str]] = []

    for node in graph:
        parent[node] = node
        rank[node] = 0

    for weight, from_node, to_node in sorted_edges:
        if find_node_parent(parent, from_node) != find_node_parent(parent, to_node):
            union_nodes(parent, rank, from_node, to_node)
            min_span_tree.append((weight, from_node, to_node))

    return min_span_tree


class KruskalGraphBuild(GraphBuild):
    """Graph class to build and represent the minimum spanning tree using Kruskal's algorithm."""

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
    """Main function to demonstrate Kruskal's algorithm."""
    graph = sample_graph()
    graph.print_graph()
    print(f"\nTotal weight of the graph: {graph.get_weight_sum()}\n")

    kruskal_algorithm_result = kruskal_algorithm(graph.get_graph())

    kruskal_graph = KruskalGraphBuild(kruskal_algorithm_result)
    kruskal_graph.print_graph()
    kruskal_graph.print_visited_nodes()
    print(f"\nTotal weight of the graph: {kruskal_graph.get_weight_sum()}\n")


if __name__ == "__main__":
    main()
