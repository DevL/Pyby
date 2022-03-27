from collections import UserDict
from .enumerable import Enumerable
from .enumerable_list import EnumerableList
from .enumerator import Enumerator


class EnumerableDict(Enumerable, UserDict):
    """
    A dict behaving like an Enumerable.
    """

    def to_enum(self):
        return Enumerator(self)

    def __each__(self):
        return iter(self.items())

    def __into__(self, method_name):
        return {"compact": __class__}.get(method_name, EnumerableList)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"
