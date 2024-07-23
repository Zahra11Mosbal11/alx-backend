#!/usr/bin/python3
"""FIFO caching"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """FIFO cache """
    def __init__(self):
        """Inherits from BaseCaching and is a caching system"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put item in a cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """to get the item"""
        return self.cache_data.get(key, None)
