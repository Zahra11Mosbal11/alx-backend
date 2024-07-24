#!/usr/bin/python3
""" LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ least-recently used """
    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ puts an item in the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
