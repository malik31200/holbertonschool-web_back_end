#!/usr/bin/env python3
"""
Measure the average runtime of wait_n
"""
import asyncio
import random
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measure the total execution time of wait_n(n, max_delay)
    and returns the average time per task (total_time/n)
    """
    start: float = time.time()

    asyncio.run(wait_n(n, max_delay))

    end: float = time.time()

    total_time: float = end - start

    return (total_time / n)
