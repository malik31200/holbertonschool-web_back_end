#!/usr/bin/env python3
"""
Module contains a coroutine that takes no arguments.
The coroutine will loop 10 times, each time asynchronously wait 1 second.
"""
import random
import asyncio
from typing import Generator, List


async def async_generator() -> Generator[float, None, None]:
    """
    Yields a random number between 0 and 10 for 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
