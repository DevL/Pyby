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