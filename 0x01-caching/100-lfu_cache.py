#!/usr/bin/python3
"""LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching System"""

    def __init__(self):
        """Initialize the class with the parent class's init method"""
        super().__init__()
        self.frequency = {}
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.frequency[key] += 1
            self.order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                """ Find the key with the minimum frequency"""
                min_freq = min(self.frequency.values())
                min_freq_keys = [k for k, v in self.frequency.items()
                                 if v == min_freq]
                lru_key = next(k for k in self.order if k in min_freq_keys)
                self.order.remove(lru_key)
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print(f"DISCARD: {lru_key}")
            self.frequency[key] = 1
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
