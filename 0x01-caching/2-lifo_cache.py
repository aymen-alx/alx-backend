#!/usr/bin/env python3
""" FLIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the
        key key.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key.
        """

        return self.cache_data.get(key, None)
