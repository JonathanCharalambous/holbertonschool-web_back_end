#!/usr/bin/env python3
from typing import Callable

"""Return a function that multiplies a number by the given multiplier."""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplier: The number to multiply by.
    Return: A function that takes a float and returns the
      product of that float and multiplier.
    """
    def mul(n: float) -> float:
        """
        n: The float to multiply.
        Return: The product of n and multiplier.
        """
        return n * multiplier
    return mul
