from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict


@dataclass(eq=True, frozen=True)
class Node:
    """Repräsentiert einen Knoten im Graphen."""
    id: str

    def __str__(self) -> str:
        return self.id


@dataclass
class Edge:
    """Repräsentiert eine gerichtete, gewichtete Kante."""
    source: Node
    target: Node
    weight: float

    def __str__(self) -> str:
        return f"{self.source} --{self.weight}--> {self.target}"


class DirectedWeightedGraph:
    """Ein gerichteter, gewichteter Graph."""

    def __init__(self) -> None:
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []
        self.adjacency: Dict[Node, List[Edge]] = {}

    def add_node(self, node_id: str) -> Node:
        if node_id not in self.nodes:
            node = Node(node_id)
            self.nodes[node_id] = node
            self.adjacency[node] = []
        return self.nodes[node_id]

    def add_edge(self, source_id: str, target_id: str, weight: float) -> Edge:
        source = self.add_node(source_id)
        target = self.add_node(target_id)

        edge = Edge(source, target, weight)
        self.edges.append(edge)
        self.adjacency[source].append(edge)
        return edge

    def get_neighbors(self, node: Node) -> List[Edge]:
        return self.adjacency.get(node, [])

    def __str__(self) -> str:
        result = ["DirectedWeightedGraph:"]
        for edge in self.edges:
            result.append(f"  {edge}")
        return "\n".join(result)


# Beispiel verwenden
if __name__ == "__main__":
    g = DirectedWeightedGraph()

    g.add_edge("A", "B", 5)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 1)
    g.add_edge("C", "A", 4)

    print(g)

    print("\nNachbarn von A:")
    for edge in g.get_neighbors(Node("A")):  # Node is frozen=True → hashable
        print(" ", edge)
