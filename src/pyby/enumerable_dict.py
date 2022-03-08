from collections import UserDict
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
            return EnumerableList(func(key, value) for key, value in self.each())
        else:
            return iter(self.items())
