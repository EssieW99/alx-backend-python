#!/usr/bin/env python3
""" a coroutine function """

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    will execute async_comprehension four times in parallel
    using asyncio.gather
    """

    start_time = time.perf_counter()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    results = await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return end_time - start_time
