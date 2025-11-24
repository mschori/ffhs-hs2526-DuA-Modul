import heapq
import math
from typing import Dict, Tuple, Optional

from gewichteter_gerichteter_graph import DirectedWeightedGraph


def dijkstra(graph: DirectedWeightedGraph, start_id: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    """
    Dijkstra-Algorithmus für einen gerichteten, gewichteten Graphen mit NICHT-negativen Gewichten.

    Liefert zwei Dictionaries zurück:
      - dist:  kürzeste Distanzen von start_id zu jeder Knoten-ID
      - prev: Vorgänger jeder Knoten-ID auf dem kürzesten Pfad (oder None)
    """
    if start_id not in graph.nodes:
        raise ValueError(f"Startknoten {start_id} existiert nicht im Graphen.")

    # Distanz- und Vorgänger-Maps vorbereiten
    dist: Dict[str, float] = {}
    prev: Dict[str, Optional[str]] = {}

    for node_id in graph.nodes:
        dist[node_id] = math.inf
        prev[node_id] = None

    dist[start_id] = 0.0

    # Priority Queue: (distanz, node_id)
    heap: list[Tuple[float, str]] = []
    heapq.heappush(heap, (0.0, start_id))

    visited = set()

    while heap:
        current_dist, current_id = heapq.heappop(heap)

        # Schon verarbeitet?
        if current_id in visited:
            continue

        visited.add(current_id)
        current_node = graph.nodes[current_id]

        # Falls die Distanz nicht mehr aktuell ist, überspringen
        if current_dist > dist[current_id]:
            continue

        # Nachbarn durchsuchen
        for edge in graph.get_neighbors(current_node):
            neighbor_id = edge.target.id
            weight = edge.weight

            if weight < 0:
                raise ValueError("Dijkstra funktioniert nur mit nicht-negativen Gewichten!")

            new_dist = dist[current_id] + weight

            if new_dist < dist[neighbor_id]:
                dist[neighbor_id] = new_dist
                prev[neighbor_id] = current_id
                heapq.heappush(heap, (new_dist, neighbor_id))

    return dist, prev


from typing import List


def reconstruct_path(prev: Dict[str, Optional[str]], start_id: str, target_id: str) -> List[str]:
    """
    Rekonstruiert den kürzesten Pfad von start_id nach target_id
    anhand des prev-Dictionaries aus Dijkstra.
    Gibt eine Liste von Knoten-IDs zurück.
    """
    path: List[str] = []
    current: Optional[str] = target_id

    while current is not None:
        path.append(current)
        if current == start_id:
            break
        current = prev[current]

    path.reverse()

    # Falls der Startknoten nicht erreicht wurde
    if not path or path[0] != start_id:
        return []  # kein Pfad vorhanden

    return path


if __name__ == "__main__":
    g = DirectedWeightedGraph()

    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 3)
    g.add_edge("C", "D", 7)
    g.add_edge("C", "E", 4)
    g.add_edge("D", "E", 1)

    dist, prev = dijkstra(g, "A")

    print("Kürzeste Distanzen von A:")
    for node_id, d in dist.items():
        print(f"  A -> {node_id}: {d}")

    ziel = "E"
    pfad = reconstruct_path(prev, "A", ziel)

    print(f"Kürzester Pfad von A nach {ziel}: {pfad}")
    print(f"Distanz: {dist[ziel]}")

