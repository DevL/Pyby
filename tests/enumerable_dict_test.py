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
    seen = Seen()
    enumerable_dict = EnumerableDict(a=1, b=2, c=3)
    enumerable_dict.each(seen)
    assert seen == [("a", 1), ("b", 2), ("c", 3)]


def test_each_without_a_function_yields_each_item():
    enumerable_dict = EnumerableDict(a=1, b=2, c=3)
    enumerator = enumerable_dict.each()
    assert isgenerator(enumerator)
    assert list(enumerator) == [("a", 1), ("b", 2), ("c", 3)]


class Seen(UserList):
    def __bool__(self):
        return True

    def __call__(self, element):
        self.data.append(element)
