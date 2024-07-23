#!/usr/bin/python3
"""FIFO caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO"""
    def __init__(self):
        """Inherits from BaseCaching and is a caching system"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """put item in a cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        self.cache_data[key] = item
        self.order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

    def get(self, key):
        """to get the item"""
        return self.cache_data.get(key, None)
