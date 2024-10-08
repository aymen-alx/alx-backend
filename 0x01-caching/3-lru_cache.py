#!/usr/bin/env python3
""" LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache
    """
    def __init__(self):
        super().__init__()
        self.used_key = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value
            for the key key.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.used_key:
                self.used_key.append(key)
            else:
                self.used_key.append(
                    self.used_key.pop(self.used_key.index(key)))
            if len(self.used_key) > BaseCaching.MAX_ITEMS:
                discard = self.used_key.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """Return the value in self.cache_data linked to key.
        """
        if key is not None and key in self.cache_data.keys():
            self.used_key.append(self.used_key.pop(self.used_key.index(key)))
        return self.cache_data.get(key, None)
