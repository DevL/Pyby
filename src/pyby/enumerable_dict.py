from collections import UserDict
from .enumerable import Enumerable
from .enumerable_list import EnumerableList


class EnumerableDict(Enumerable, UserDict):
    """
    A dict behaving like an Enumerable.
    """

    def __each__(self):
        return iter(self.items())

    def __into__(self, method_name):
        return {
            "compact": self.__class__,
            "reject": self.__class__,
            "select": self.__class__,
        }.get(method_name, EnumerableList)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"

    def __to_tuple__(self, item):
        return item
