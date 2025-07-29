#!/usr/bin/env python3
from typing import Union, Tuple
"""Return a tuple containing a string and the square of a number."""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:

    """
    k: The string key.
    v: The integer or floating-point value.
    Return: A tuple containing the key and the square of the value.
    """
    return (k, float(v ** 2))
