# DSA Study with Python

[Prim Algorithm](https://www.youtube.com/watch?v=cplfcGZmX7I) - Prim's Algorithm is a greedy algorithm used to find a Minimum Spanning Tree (MST) of a connected, weighted, and undirected graph. It starts with an arbitrary vertex and, at each step, adds the smallest edge that connects a vertex already in the MST to a vertex outside it. This process continues until all vertices are included in the MST.  
    - Final Time Complexity (Linear Search): $O(V * E)$.  
    - $V$ = total nodes in `graph.get_graph.keys()`.  
    - $E$ = total tuples `(to_node, weight)`.   
    - **Ways to improve**: Priority Queue + Min-Heap: $O(E \log E)$

[Kruskal's Algorithm](https://www.youtube.com/watch?v=71UQH7Pr9kU) - Kruskal's Algorithm is a greedy algorithm used to find a Minimum Spanning Tree (MST) of a connected, weighted, and undirected graph. Unlike Prim's Algorithm, which grows the MST from a single starting vertex, Kruskal's Algorithm begins by sorting all edges by their weights and adds them one by one, starting from the smallest, as long as they do not form a cycle. This process continues until the MST spans all vertices, typically managed with a Union-Find data structure to detect cycles efficiently.  
    - Final Time Complexity (Sorting Edges + Union-Find Operations): $O(E \log E + E \alpha(V)) \approx O(E \log E)$.  
    - $V$ = total nodes in `graph.get_graph.keys()`.  
    - $E$ = total tuples `(to_node, weight)`.   
