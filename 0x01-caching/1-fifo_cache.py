#!/usr/bin/env python3
"""
FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """put"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """get"""

        return self.cache_data.get(key, None)
