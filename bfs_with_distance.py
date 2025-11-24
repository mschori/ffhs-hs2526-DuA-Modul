from collections import deque
from typing import Dict

from gewichteter_gerichteter_graph import DirectedWeightedGraph, Node


def bfs_with_distance(graph: DirectedWeightedGraph, start_id: str) -> Dict[str, int]:
    """
    Breitensuche, die die minimale Anzahl Kanten vom Startknoten zu jedem
    erreichbaren Knoten liefert.
    """
    if start_id not in graph.nodes:
        raise ValueError(f"Startknoten {start_id} existiert nicht im Graphen.")

    start_node = graph.nodes[start_id]

    distances: Dict[Node, int] = {}
    queue: deque[Node] = deque()

    distances[start_node] = 0
    queue.append(start_node)

    while queue:
        current = queue.popleft()
        current_dist = distances[current]

        for edge in graph.get_neighbors(current):
            neighbor = edge.target
            if neighbor not in distances:
                distances[neighbor] = current_dist + 1
                queue.append(neighbor)

    return {node.id: dist for node, dist in distances.items()}


if __name__ == "__main__":
    g = DirectedWeightedGraph()
    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "D", 1)
    g.add_edge("C", "D", 3)
    g.add_edge("D", "E", 4)

    result = bfs_with_distance(g, "A")
    print("BFS-Besuchsreihenfolge:", result)
