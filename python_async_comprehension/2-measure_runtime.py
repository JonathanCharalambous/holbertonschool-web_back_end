#!/usr/bin/env python3
"""Measure the runtime of async_comprehension."""
from async_comprehension import async_comprehension
import time
import asyncio


async def measure_runtime() -> float:
    """Measures the total runtime of async_comprehension."""
   
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    return end_time - start_time
