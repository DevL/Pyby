from collections import UserList
from .enumerable import Enumerable


class EnumerableList(Enumerable, UserList):
    """
    A list behaving like an Enumerable.
    """

    def each(self, func=None):
        if func:
            for item in self:
                func(item)
        else:
            return iter(self)

    def __into__(self, method_name):
        return __class__
