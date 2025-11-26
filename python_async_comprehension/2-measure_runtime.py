#!/usr/bin/env python3
"""
2-measure_runtime
coroutine that will execute
four times in parallel using asyncio.gather.
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.time()

    return (end - start)
