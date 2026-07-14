#!/usr/bin/env python3
"""
Redis cache
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable] = None):
        """
        Get data in Redis  and optionnaly convert it
        """
        data = self._redis.get(key)

        if data is None:
            return None

        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> str:
        """
        Get string value from Redis
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: int) -> int:
        """
        Get integer value from Redis
        """
        return self.get(key, fn=int)
