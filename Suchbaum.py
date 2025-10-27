class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_rec(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_rec(root.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_rec(root.left, key)
        return self._search_rec(root.right, key)
