#!/usr/bin/env python3
""" an asynchronous coroutine """

import asyncio
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values)
    in ascending order without using sort()
    """

    task = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]
    task = asyncio.as_completed(task)
    results = await asyncio.gather(*task)
    return results