from collections import UserDict
from inspect import signature
from .enumerable import Enumerable
from .enumerable_list import EnumerableList


class EnumerableDict(Enumerable, UserDict):
    def each(self, func=None):
        if func:
            for item in self.items():
                func(item)
        else:
            return iter(self.items())

    def map(self, func=None):
        if func:
            return EnumerableList(func(*kv) for kv in self.each())
            # return EnumerableList(func(key, value) for key, value in self.each())
        else:
            return iter(self.items())


def _safe_arity(func):
    """
    Makes a wild-ass guess that builtin functions without a signature have an arity of 1.

    >>> _safe_arity(dict)
    1
    """
    try:
        return _arity(func)
    except ValueError:
        return 1


def _arity(func):
    """
    >>> _arity("abc".upper)
    0

    >>> _arity(str.upper)
    1

    >>> _arity(lambda x, y: x + y)
    2

    Note that this cannot be used with certain builtin types such as dict.
    """
    return len(signature(func).parameters.keys())
