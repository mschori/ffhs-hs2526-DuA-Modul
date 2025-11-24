import math
from typing import Dict, Optional

from gewichteter_gerichteter_graph import DirectedWeightedGraph


def floyd_warshall(graph: DirectedWeightedGraph):
    # List of all node IDs
    nodes = list(graph.nodes.keys())

    # Initialize distance-matrix, that looks like:
    # dist = {
    #   'A': {'A': inf, 'B': inf},
    #   'B': {'A': inf, 'B': inf},
    #   ...
    # }
    dist: Dict[str, Dict[str, float]] = {
        u: {v: math.inf for v in nodes} for u in nodes
    }

    # Next-Matrix for path-costs, that looks like:
    # next_node = {
    #   'A': {'A': None, 'B': None},
    #   'B': {'A': None, 'B': None},
    #   ...
    # }
    next_node: Dict[str, Dict[str, Optional[str]]] = {
        u: {v: None for v in nodes} for u in nodes
    }

    # Fille direct distances
    for u in nodes:
        dist[u][u] = 0

    # Get all edges and set their weights and next nodes
    for edge in graph.edges:
        dist[edge.source.id][edge.target.id] = edge.weight
        next_node[edge.source.id][edge.target.id] = edge.target.id

    # Floyd-Warshall
    for k in nodes:
        for i in nodes:
            for j in nodes:
                # If a shorter path is found over k, update distance and next_node
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node


def reconstruct_fw_path(next_node, start: str, ziel: str):
    if next_node[start][ziel] is None:
        return []  # No Path

    path = [start]
    while start != ziel:
        start = next_node[start][ziel]
        path.append(start)

    return path


if __name__ == "__main__":
    g = DirectedWeightedGraph()

    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "D", 1)
    g.add_edge("C", "D", 7)
    g.add_edge("C", "E", 4)
    g.add_edge("D", "E", 1)

    dist, nxt = floyd_warshall(g)

    print("Distanzmatrix:")
    for u in dist:
        print(u, dist[u])

    pfad = reconstruct_fw_path(nxt, "A", "E")
    print("\nKürzester Weg A→E:", pfad)
    print("Distanz:", dist["A"]["E"])
