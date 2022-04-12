from collections import UserList
from .enumerable import Enumerable


class EnumerableList(Enumerable, UserList):
    """
    A list behaving like an Enumerable.
    """

    def __each__(self):
        return iter(self)

    def __into__(self, method_name):
        return self.__class__

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"
