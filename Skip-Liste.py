import random


class Node:
    def __init__(self, key, level: int):
        """
        Initialize a node with a given key and level.
        :param key: The key of the node.
        :param level: The level of the node.
        """
        self.key = key
        self.forward = [None] * (level + 1)


class SkipList:
    def __init__(self, max_level: int, p: float):
        """
        Initialize the skip list.
        :param max_level: Maximum level for this skip list.
        :param p: Probability for the random level generator.
        :return: None
        """
        self.max_level = max_level
        self.p = p
        self.header = Node(-1, max_level)
        self.level = 0

    def random_level(self):
        """
        Generate a random level for a new node.
        :return: The level for the new node.
        """
        level = 0
        while random.random() < self.p and level < self.max_level:  # random() returns a random floating number between 0 and 1
            level += 1
        return level

    def insert(self, key):
        """
        Insert a new key into the skip list.
        :param key: The key to insert.
        :return: None
        """
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is None or current.key != key:
            new_level = self.random_level()
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level

            new_node = Node(key, new_level)
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]

        return current is not None and current.key == key

    def delete(self, key):
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is not None and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1


# Example usage:
skip_list = SkipList(max_level=3, p=0.5)
skip_list.insert(3)
skip_list.insert(6)
skip_list.insert(7)
skip_list.insert(9)
skip_list.insert(12)
skip_list.insert(19)
