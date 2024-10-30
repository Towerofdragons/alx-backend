#!/usr/bin/env python3

from base_caching import BaseCaching

"""

"""


class FIFOCache(BaseCaching):
    """

    """
    def __init__(self):
        super().__init__()
        self.key_queue = []

    def put(self, key, item):
        if not key or not item:
            return
        
        if key in self.cache_data:
            # Update the existing item; no need to adjust the order
            self.cache_data[key] = item
      
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            cleared_key = self.key_queue.pop(0)
            del self.cache_data[cleared_key]
            print(f"DISCARD: {cleared_key}")

          
        self.key_queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key)