from collections import UserList
from .enumerable import Enumerable


class EnumerableList(Enumerable, UserList):
    def each(self, func=None):
        if func:
            for item in self:
                func(item)
        else:
            return iter(self)

    def map(self, func=None):
        if func:
            return EnumerableList(func(item) for item in self.each())
        else:
            return iter(self)
