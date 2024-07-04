#!/usr/bin/env python3
""" type-annotated function """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns their sum as a float """

    sum: float = 0.0

    for num in mxd_lst:
        sum += num
    return sum
