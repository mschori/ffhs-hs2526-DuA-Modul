import mmh3
from bitarray import bitarray


class BloomFilter:
    def __init__(self, size: int, hash_count: int):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item: str):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            self.bit_array[digest] = 1

    def check(self, item: str) -> bool:
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == 0:
                return False
        return True

# Example usage:
bloom = BloomFilter(size=1000, hash_count=10)
bloom.add("hello")
print(bloom.check("hello"))  # Output: True
print(bloom.check("world"))  # Output: False
