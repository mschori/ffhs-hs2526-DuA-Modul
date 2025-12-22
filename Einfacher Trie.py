# implement a simple Trie (prefix tree) data structure in Python
from typing import Dict


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Example usage:
trie = Trie()
trie.insert("hello")
print(trie.search("hello"))  # Output: True
print(trie.search("hell"))  # Output: False
print(trie.starts_with("hell"))  # Output: True
print(trie.starts_with("world"))  # Output: False
