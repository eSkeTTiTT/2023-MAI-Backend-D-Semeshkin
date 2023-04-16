from typing import Any

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.counter = 0

    def get(self, key: str) -> str | None:
        if key in self.cache:
            self.cache[key][1] = self.counter
            self.counter += 1
            return self.cache[key][0]
        else:
            return None

    def set(self, key: str, value: str) -> None:
        if len(self.cache) >= self.capacity:
            oldest = min(self.cache, key=lambda k: self.cache[k][1])
            del self.cache[oldest]
        self.cache[key] = [value, self.counter]
        self.counter += 1

    def rem(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]