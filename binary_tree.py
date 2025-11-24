from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Generic, Iterator, List, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    value: T
    children: List["Node[T]"] = field(default_factory=list)

    def add(self, child: "Node[T] | T") -> "Node[T]":
        """Bequemes Anhängen; akzeptiert Node oder Wert."""
        if isinstance(child, Node):
            self.children.append(child)
        else:
            self.children.append(Node(child))
        return self


class Tree(Generic[T]):
    def __init__(self, root: Node[T] | None):
        self.root = root

    # ------------------------------------------------------------
    # 1) Rekursive Traversierungen (DFS)
    # ------------------------------------------------------------
    def preorder_recursive(self) -> List[T]:
        out: List[T] = []

        def rec(n: Node[T] | None) -> None:
            if n is None:
                return
            out.append(n.value)
            for c in n.children:
                rec(c)

        rec(self.root)
        return out

    def postorder_recursive(self) -> List[T]:
        out: List[T] = []

        def rec(n: Node[T] | None) -> None:
            if n is None:
                return
            for c in n.children:
                rec(c)
            out.append(n.value)

        rec(self.root)
        return out

    # ------------------------------------------------------------
    # 2) Nicht-rekursiv: Pre-Order als Iterator (Stack)
    # ------------------------------------------------------------
    def iter_preorder(self) -> Iterator[T]:
        """Pre-Order ohne Rekursion (depth-first)."""
        if self.root is None:
            return
        stack: List[Node[T]] = [self.root]
        while stack:
            node = stack.pop()
            yield node.value
            # wichtig: Kinder rückwärts pushen
            for c in reversed(node.children):
                stack.append(c)

    # ------------------------------------------------------------
    # 3) Breitensuche (Level-Order) als Iterator (Queue)
    # ------------------------------------------------------------
    def iter_bfs(self) -> Iterator[T]:
        if self.root is None:
            return
        q: deque[Node[T]] = deque([self.root])
        while q:
            node = q.popleft()
            yield node.value
            for c in node.children:
                q.append(c)


# ------------------------------------------------------------
# Demo
# ------------------------------------------------------------
if __name__ == "__main__":
    #          A
    #       /  |  \
    #      B   C   D
    #         / \   \
    #        E   F   G
    A = Node("A")
    B, C, D = Node("B"), Node("C"), Node("D")
    E, F, G = Node("E"), Node("F"), Node("G")
    A.add(B).add(C).add(D)
    C.add(E).add(F)
    D.add(G)

    tree = Tree(A)

    print("Pre-Order (rekursiv): ", tree.preorder_recursive())
    print("Post-Order (rekursiv):", tree.postorder_recursive())
    print("Pre-Order (iterativ): ", list(tree.iter_preorder()))
    print("BFS / Level-Order:    ", list(tree.iter_bfs()))
