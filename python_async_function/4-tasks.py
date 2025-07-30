#!/usr/bin/env python3
"""Return a list of floating-point numbers in ascending order after waiting."""
import asyncio
from basic_async_syntax import wait_random
from typing import List


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    n: The number of times to wait.
    max_delay: The maximum delay to wait for each call.
    """
    times = []
    ordered_times = []
    for _ in range(n):
        time = wait_random(max_delay)
        times.append(time)

    for procedure in asyncio.as_completed(times):
        ordered_time = await procedure
        ordered_times.append(ordered_time)

    return ordered_times