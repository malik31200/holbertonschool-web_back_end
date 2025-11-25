#!/usr/bin/env python3
"""
modul contains a fuction who called task_wait_random
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    fuction who called task_wait_random
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
