#!/usr/bin/env python3
""" FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value
            for the key key
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key.
        """

        return self.cache_data.get(key, None)
