from collections import UserDict
from .enumerable import Enumerable
from .enumerable_list import EnumerableList


class EnumerableDict(Enumerable, UserDict):
    """
    A dict behaving like an Enumerable.
    """

    def include(self, candidate):
        return candidate in self.keys()

    def __each__(self):
        return iter(self.items())

    def __into__(self, method_name):
        return {
            "select": self.__class__,
        }.get(method_name, EnumerableList)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.data})"

    def __to_tuple__(self, item):
        return item

    def _item_equals(self, compare_to):
        return lambda pair: pair == compare_to

    def _item_is_a(self, compare_to):
        return lambda *pair: isinstance(pair, compare_to)

    def _item_matches(self, compare_to):
        return lambda *pair: isinstance(*pair, type(compare_to.pattern)) and bool(
            compare_to.search(*pair)
        )
