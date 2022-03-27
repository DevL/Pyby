from collections import UserDict
from .enumerable import Enumerable
from .enumerable_list import EnumerableList


class EnumerableDict(Enumerable, UserDict):
    """
    A dict behaving like an Enumerable.
    """

    def each(self, func=None):
        if func:
            for item in self.items():
                func(item)
        else:
            return iter(self.items())

    def __into__(self, method_name):
        return {"compact": __class__}.get(method_name, EnumerableList)
