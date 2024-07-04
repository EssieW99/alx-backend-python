#!/usr/bin/env python3
""" type-annotated function """

from typing import Any, Dict, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """ returns a value of type V or None """

    if key in dct:
        return dct[key]
    else:
        return default
