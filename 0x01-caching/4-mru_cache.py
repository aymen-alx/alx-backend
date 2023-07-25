#!/usr/bin/env python3
""" LRU Caching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache"""
    def __init__(self):
        super().__init__()
        self.used_key = []

    def put(self, key, item):
        """put"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.used_key:
                self.used_key.append(key)
            else:
                self.used_key.append(
                    self.used_key.pop(self.used_key.index(key)))
            if len(self.used_key) > BaseCaching.MAX_ITEMS:
                discard = self.used_key.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """get"""
        if key is not None and key in self.cache_data.keys():
            self.used_key.append(self.used_key.pop(self.used_key.index(key)))
        return self.cache_data.get(key, None)
