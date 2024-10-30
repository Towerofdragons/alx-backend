#!/usr/bin/env python3
"""
    Implements a caching system using a First-In-First-Out (FIFO) strategy.
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        Adds an item to the cache data with
        the specified key using FIFO replacement policy.
    """
    def __init__(self):
        """
             Calls the parent class (BaseCaching) initializer
             and sets up additional attributes.
        """
        super().__init__()
        self.key_queue = []

    def put(self, key, item):
        """
            Adds an item to the cache data
            with the specified key using FIFO replacement policy.
        """
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
        """
             Retrieves the item from the cache
             data associated with the specified key.
        """
        return self.cache_data.get(key)
