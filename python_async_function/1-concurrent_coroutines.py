#!/usr/bin/env python3
"""
Module contains an async routine hat takes in 2 int arguments.
"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Returns the list of all the delays.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
