#!/usr/bin/env python3
"""
    Implements a caching system using a Least Recently Used (MRU) strategy.
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
        Adds an item to the cache data with
        the specified key using MRU replacement policy.
    """
    def __init__(self):
        """
             Calls the parent class (BaseCaching) initializer
             and sets up additional attributes.
        """
        super().__init__()
        self.key_queue = []
        self.frequency = {}

    def put(self, key, item):
        """
            Adds an item to the cache data
            with the MRU policy.
        """
        if not key or not item:
            return

        if key in self.cache_data:
            # Update the existing item; no need to adjust the order
            self.cache_data[key] = item
            # self.key_queue.remove(key)
            # self.key_queue.append(key)
            self.frequency[key] += 1
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_frequency = min(self.frequency.values())
            lfu_keys = [k for k, freq
                        in self.key_frequency.items() if freq == min_frequency]

            LFU_key = self.lfu_keys[0]
            del self.cache_data[LFU_key]
            del self.frequency[LFU_key]
            print(f"DISCARD: {LFU_key}")

        self.cache_data[key] = item
        self.frequency[key] = 1

    def get(self, key):
        """
             Retrieves the item from the cache
             data associated with the specified key.
             Re-adds the key to the queue once accessed
        """
        # Attach use recency value
        if self.cache_data.get(key, None):
            self.key_frequency[key] += 1
        else:
            return None

        return self.cache_data.get(key)
