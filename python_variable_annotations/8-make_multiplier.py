#!/usr/bin/env python3
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a number by the given multiplier."""
    def mul(n: float) -> float:
        """Multiply a number by the multiplier."""
        return n * multiplier
    return mul
