from inspect import isgenerator
from pyby import EnumerableList


def test_each_with_a_function_calls_it_once_for_each_item():
    seen = []
    enumerable_list = EnumerableList(["a", "b", "c"])
    enumerable_list.each(lambda element: seen.append(element))
    assert seen == ["a", "b", "c"]


def test_each_without_a_function_yields_each_item():
    enumerable_list = EnumerableList(["a", "b", "c"])
    enumerator = enumerable_list.each()
    assert isgenerator(enumerator)
    assert list(enumerator) == ["a", "b", "c"]


def test_map_with_a_function_calls_it_ince_for_each_item_and_returns_an_enumerable_list():
    enumerable_list = EnumerableList([1, 2, 3])
    result = enumerable_list.map(lambda element: element + 1)
    assert isinstance(result, EnumerableList)
    assert result == [2, 3, 4]


def test_map_without_a_function_yields_each_item():
    enumerable_list = EnumerableList(["a", "b", "c"])
    enumerator = enumerable_list.map()
    assert isgenerator(enumerator)
    assert list(enumerator) == ["a", "b", "c"]


def test_first():
    enumerable_list = EnumerableList([1, 2, 3])
    assert enumerable_list.first() == 1


def test_first_when_empty():
    enumerable_list = EnumerableList()
    assert enumerable_list.first() is None
