#!/usr/bin/env python3
"""Measure the runtime of an asynchronous function."""
from concurrent_coroutines import wait_n
import time
import asyncio


async def measure_time(n: int, max_delay: int = 10) -> float:
    """
    n: The number of times to wait.
    max_delay: The maximum delay to wait for each call.
    """
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    total_time = time.perf_counter() - start_time
    return total_time / n
