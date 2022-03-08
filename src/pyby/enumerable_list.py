from collections import UserList
from .enumerable import Enumerable


class EnumerableList(Enumerable, UserList):
    def each(self, func=None):
        if func:
            for item in self:
                func(item)
        else:
            return iter(self)

    def _return_type(self):
        return __class__
