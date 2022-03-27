from collections import UserList
from .enumerable import Enumerable


class EnumerableList(Enumerable, UserList):
    """
    A list behaving like an Enumerable.
    """

    def to_enum(self):
        return self.__each__()

    def __each__(self):
        return iter(self)

    def __into__(self, method_name):
        return __class__
