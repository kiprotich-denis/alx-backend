#!/usr/bin/python3
"""inherits from BaseCaching and is a caching system"""
import queue
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """subclass LIFOCache"""

    def __init__(self):
        """initialize"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the
        key key"""
        if key is not None and item is not None and len(self.cache_data) <= 4:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            for key, item in list(self.cache_data.items()):
                self.cache_data.popitem()
                print("DISCARD: {}".format(list(self.cache_data.keys())[-1]))
                break

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key not in self.cache_data or key is None:
            return (None)
        return (self.cache_data[key])
