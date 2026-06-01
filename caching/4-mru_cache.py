# !/usr/bin/env python3
"""MRU module cache"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""
    def __init__(self):
        """ Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add item to cache using MRU rule"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)
            self.order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru = self.order.pop()
            del self.cache_data[mru]
            print(f"DISCARD: {mru}")

         # add normal
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Return value linked to key"""
        if key is None:
            return None

        if key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
