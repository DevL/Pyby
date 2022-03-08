from collections import UserDict, UserList
from inspect import isgenerator
from pyby import Enumerable


class EnumerableDict(Enumerable, UserDict):
    def each(self, func=None):
        if func:
            for item in self.items():
                func(item)
        else:
            return iter(self.items())


def test_each_with_a_function_calls_it_once_for_each_item():
    seen = []
    enumerable_dict = EnumerableDict(a=1, b=2, c=3)
    enumerable_dict.each(lambda key_value_pair: seen.append(key_value_pair))
    assert seen == [("a", 1), ("b", 2), ("c", 3)]


def test_each_without_a_function_yields_each_item():
    enumerable_dict = EnumerableDict(a=1, b=2, c=3)
    enumerator = enumerable_dict.each()
    assert isgenerator(enumerator)
    assert list(enumerator) == [("a", 1), ("b", 2), ("c", 3)]
