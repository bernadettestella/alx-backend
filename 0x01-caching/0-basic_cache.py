#!/usr/bin/env python3
"""
BaseCaching Module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    defines a class for caching information in key-value pairs
    Methods used:
            put - stores a key-value pair
            get - retrieves the value associated with a key
    """

    def __init__(self):
        """
        Initializes the class using the parent class __init__
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Stores a key value pair passing the key and Item arguments
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns value linked to key.
        If Key is none or does not exist return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
