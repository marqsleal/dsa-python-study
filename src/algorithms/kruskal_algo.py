from enum import Enum
from src.data_structures.graph import GraphBuild, sample_graph


class EdgesIndex(Enum):
    """Enum to represent the index of edges in a tuple."""
    WEIGHT = 0
    FROM_NODE = 1
    TO_NODE = 2


def merge_sort_edges_by_weight(edges: list) -> list:
    if len(edges) <= 1:
        return edges

    middle_node = len(edges) // 2

    edges_left_half = merge_sort_edges_by_weight(edges[:middle_node])
    edges_right_half = merge_sort_edges_by_weight(edges[middle_node:])

    return merge_lists(edges_left_half, edges_right_half)


def merge_lists(edges_left_half: list, edges_right_half: list) -> list:
    sorted_list = []
    i, j = 0, 0

    while i < len(edges_left_half) and j < len(edges_right_half):
        if edges_left_half[i][EdgesIndex.WEIGHT.value] < edges_right_half[j][EdgesIndex.WEIGHT.value]:
            sorted_list.append(edges_left_half[i])
            i += 1
        else:
            sorted_list.append(edges_right_half[j])
            j += 1
    
    sorted_list.extend(edges_left_half[i:])
    sorted_list.extend(edges_right_half[j:])

    return sorted_list


def find_node_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_node_parent(parent, parent[node])
    return parent[node]


def union_nodes(parent, rank, node1, node2):
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


def kruskal_algorithm(graph: dict):
    edges = []
    seen = set()

    for from_node in graph:
        for to_node, weight in graph[from_node]:
            if (to_node, from_node) not in seen:
                edges.append((weight, from_node, to_node))
                seen.add((from_node, to_node))
    
    sorted_edges = merge_sort_edges_by_weight(edges)


def main():
    graph = sample_graph()
    graph.print_graph()


if __name__ == "__main__":
    main()