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

    left_half = merge_sort_edges_by_weight(edges[:middle_node])
    right_half = merge_sort_edges_by_weight(edges[middle_node:])

    return merge_lists(left_half, right_half)


def merge_lists(left_half: list, right_half: list) -> list:
    sorted_list = []
    i, j = 0, 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i][EdgesIndex.WEIGHT.value] < right_half[j][EdgesIndex.WEIGHT.value]:
            sorted_list.append(left_half[i])
            i += 1
        else:
            sorted_list.append(right_half[j])
            j += 1
    
    sorted_list.extend(left_half[i:])
    sorted_list.extend(right_half[j:])

    return sorted_list


def kruskal_algorithm(graph: dict):
    pass


def main():
    graph = sample_graph()
    graph.print_graph()


if __name__ == "__main__":
    main()