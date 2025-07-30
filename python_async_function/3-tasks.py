#!/usr/bin/env python3
"""Create an asyncio task that waits for a random delay."""
from basic_async_syntax import wait_random
import asyncio


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    max_delay: The maximum delay in seconds.
    Return: An asyncio Task that waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
