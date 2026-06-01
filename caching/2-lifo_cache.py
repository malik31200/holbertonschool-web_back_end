#!/usr/bin/env python3
"""Module LIFO caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add item to cache using LIFO rule"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print(f"DISCARD: {self.last_key}")
            del self.cache_data[self.last_key]

        self.last_key = key
            

    def get(self, key):
        """Return value linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
