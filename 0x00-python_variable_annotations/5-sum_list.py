#!/usr/bin/env python3
""" type-annotated function """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns their sum as a float """
    sum: int = 0

    for num in input_list:
        sum += num
    return sum
