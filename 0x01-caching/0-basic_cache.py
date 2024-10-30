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
        """
         Adds an item to the cache data with the specified key
        """
    
        if not key or not item:
            return
        else:
            self.cache_data[key] = item


    def get(self, key):
        """
        Retrieves the item from the cache data associated with the specified key.

        """
        return self.cache_data.get(key)