#!/usr/bin/env python3
""" a nested type-annotated function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """  returns a function that multiplies a float by multiplier """
    return lambda value: value * multiplier
