#!/usr/bin/env python3
"""Module FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system"""
    def __init__(self):
        """"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add item to cache using FIFO rule"""
        if key is None or item is None:
            return

        # if key already exist, we only update
        if key in self.cache_data:
            self.cache_data[key] = item
            return

        # add normal
        self.cache_data[key] = item
        self.order.append(key)

        # if capacity is exceded
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            firstInput = self.order.pop(0)
            del self.cache_data[firstInput]
            print(f"DISCARD: {firstInput}")

    def get(self, key):
        """Return value linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)
