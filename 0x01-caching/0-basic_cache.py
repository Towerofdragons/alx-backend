#!/usr/bin/env python3

from base_caching import BaseCaching

"""
 BasicCache that inherits from BaseCaching and is a caching system:
"""

class BasicCache(BaseCaching):
    """
        BasicCache class that inherits from BaseCaching.
        Implements a basic caching system with no limit on the cache size.
    """

    def put(self, key, item):
        if not key or not item:
            return
        else:
            self.cache_data[key] = item


    def get(self, key):
        return self.cache_data.get(key)