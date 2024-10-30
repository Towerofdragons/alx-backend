#!/usr/bin/env python3
"""
    Implements a caching system using a Least Recently Used (LRU) strategy.
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        Adds an item to the cache data with
        the specified key using LRU replacement policy.
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
            with the LRU policy.
        """
        if not key or not item:
            return

        if key in self.cache_data:
            # Update the existing item; no need to adjust the order
            self.cache_data[key] = item
            self.key_queue.remove(key)
            self.key_queue.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            LRU_key = self.key_queue.pop(0)
            del self.cache_data[LRU_key]
            print(f"DISCARD: {LRU_key}")

        self.key_queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
             Retrieves the item from the cache
             data associated with the specified key.
             Re-adds the key to the queue once accessed
        """
        # Attach use recency value
        if self.cache_data.get(key, None):
            self.key_queue.remove(key)
            self.key_queue.append(key)
        else:
            return None

        return self.cache_data.get(key)
