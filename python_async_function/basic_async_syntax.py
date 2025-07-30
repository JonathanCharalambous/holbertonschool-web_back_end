#!/usr/bin/env python3
"""Return a random floating-point number after a delay."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    max_delay: The maximum delay in seconds.
    Return: A random floating-point number after a delay.
    """
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
