#!/usr/bin/env python3
"""Asynchronous comprehension to collect random floating-point numbers."""
from async_generator import async_generator
from typing import List

async def async_comprehension() -> List[float]:
    """Collects 10 random floating-point numbers from async_generator."""
    result = []
    async for num in async_generator():
        result.append(num)
    return result
