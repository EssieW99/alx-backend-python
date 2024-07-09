#!/usr/bin/env python3
""" an asynchronous coroutine """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values)
    in ascending order without using sort()
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    tasks = asyncio.as_completed(tasks)
    results = await asyncio.gather(*tasks)
    return results
