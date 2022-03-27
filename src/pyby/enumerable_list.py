from collections import UserList
from .enumerable import Enumerable
from .enumerator import Enumerator


class EnumerableList(Enumerable, UserList):
    """
    A list behaving like an Enumerable.
    """

    def to_enum(self):
        return Enumerator(self)

    def __each__(self):
        return iter(self)

    def __into__(self, method_name):
        return __class__

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"
