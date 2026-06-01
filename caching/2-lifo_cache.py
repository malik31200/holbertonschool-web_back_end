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

        prev_last = self.last_key
        self.cache_data[key] = item
        self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[prev_last]
            print(f"DISCARD: {prev_last}")

    def get(self, key):
        """Return value linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
