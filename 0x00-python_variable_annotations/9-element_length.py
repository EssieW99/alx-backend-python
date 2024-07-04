#!/usr/bin/env python3
""" type-annotated function """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns a list of tuples containing a a sequence and an integer
    (the length of that sequence)
    """
    return [(i, len(i)) for i in lst]
