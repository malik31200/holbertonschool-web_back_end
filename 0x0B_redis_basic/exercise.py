#!/usr/bin/env python3
"""
Redis cache
"""
import redis
import uuid
from typing import Union


class Cache():
    """
    CAche class
    """
    def __init__(self):
        """
        Initialize redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
