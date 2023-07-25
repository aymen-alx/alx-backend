#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache
    """
    def put(self, key, item):
        """put
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get
        """

        return self.cache_data.get(key, None)
