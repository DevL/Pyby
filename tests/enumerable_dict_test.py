from collections import UserList
from inspect import isgenerator
from pyby import EnumerableDict, EnumerableList


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


def test_map_with_a_function_calls_it_once_for_each_item_and_returns_an_enumerable_list():
    enumerable_dict = EnumerableDict(a=1, b=2, c=3)
    result = enumerable_dict.map(lambda key, value: (key.upper(), value + 1))
    assert isinstance(result, EnumerableList)
    assert result == [("A", 2), ("B", 3), ("C", 4)]


def test_map_without_a_function_yields_each_item():
    enumerable_dict = EnumerableDict(a=1, b=2, c=3)
    enumerator = enumerable_dict.map()
    assert isgenerator(enumerator)
    assert list(enumerator) == [("a", 1), ("b", 2), ("c", 3)]


def test_first():
    enumerable_dict = EnumerableDict(a=1, b=2, c=3)
    assert enumerable_dict.first() == ("a", 1)


def test_first_with_number_of_elements_specified():
    enumerable_dict = EnumerableDict(a=1, b=2, c=3)
    result = enumerable_dict.first(2)
    assert isinstance(result, EnumerableList)
    assert result == [("a", 1), ("b", 2)]


def test_first_with_fewer_elements_than_asked_for():
    enumerable_dict = EnumerableDict(a=1, b=2, c=3)
    result = enumerable_dict.first(5)
    assert isinstance(result, EnumerableList)
    assert result == [("a", 1), ("b", 2), ("c", 3)]


def test_first_when_empty():
    enumerable_dict = EnumerableDict()
    assert enumerable_dict.first() is None


def test_first_when_empty_when_asked_for_a_number_of_elements():
    enumerable_dict = EnumerableDict()
    result = enumerable_dict.first(5)
    assert isinstance(result, EnumerableList)
    assert result == []


class Seen(UserList):
    def __bool__(self):
        return True

    def __call__(self, element):
        self.data.append(element)
