from collections import UserDict
from .enumerable import Enumerable
from .enumerable_list import EnumerableList


class EnumerableDict(Enumerable, UserDict):
    """
    A dict behaving like an Enumerable.
    """

    def to_enum(self):
        return self.__each__()

    def __each__(self):
        return iter(self.items())

    def __into__(self, method_name):
        return {"compact": __class__}.get(method_name, EnumerableList)
