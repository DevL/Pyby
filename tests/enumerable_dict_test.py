import pytest
from pyby import EnumerableDict, EnumerableList, Enumerator
from .test_helpers import pass_through


@pytest.fixture
def enumerable_dict():
    return EnumerableDict(a=1, b=2, c=3)


@pytest.fixture
def empty_dict():
    return EnumerableDict()


def test_repr(enumerable_dict):
    assert repr(enumerable_dict) == "EnumerableDict({'a': 1, 'b': 2, 'c': 3})"


def test_each_with_a_function_calls_it_once_for_each_item(enumerable_dict, seen):
    enumerable_dict.each(seen)
    assert seen == [("a", 1), ("b", 2), ("c", 3)]


def test_each_without_a_function_returns_an_enumerator(enumerable_dict):
    enumerator = enumerable_dict.each()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(lambda x, y: (x, y)) == [("a", 1), ("b", 2), ("c", 3)]


def test_compact():
    enumerable_dict = EnumerableDict(a=1, b=2, c=3, d=None)
    result = enumerable_dict.compact()
    assert isinstance(result, EnumerableDict)
    assert result == {"a": 1, "b": 2, "c": 3}


def test_compact_when_empty(empty_dict):
    result = empty_dict.compact()
    assert isinstance(result, EnumerableDict)
    assert result == {}


def test_compact_when_not_containing_any_None_values(enumerable_dict):
    result = enumerable_dict.compact()
    assert isinstance(result, EnumerableDict)
    assert result == {"a": 1, "b": 2, "c": 3}


def test_first(enumerable_dict):
    assert enumerable_dict.first() == ("a", 1)


def test_first_with_number_of_elements_specified(enumerable_dict):
    result = enumerable_dict.first(2)
    assert isinstance(result, EnumerableList)
    assert result == [("a", 1), ("b", 2)]


def test_first_with_fewer_elements_than_asked_for(enumerable_dict):
    result = enumerable_dict.first(5)
    assert isinstance(result, EnumerableList)
    assert result == [("a", 1), ("b", 2), ("c", 3)]


def test_first_when_empty(empty_dict):
    assert empty_dict.first() is None


def test_first_when_empty_when_asked_for_a_number_of_elements(empty_dict):
    result = empty_dict.first(5)
    assert isinstance(result, EnumerableList)
    assert result == []


def test_inject(enumerable_dict):
    assert enumerable_dict.inject(lambda acc, kv_pair: ("sum", acc[1] + kv_pair[1])) == ("sum", 6)


def test_inject_with_initial_value(enumerable_dict):
    assert enumerable_dict.inject(4, lambda acc, kv_pair: acc + kv_pair[1]) == 10


def test_inject_when_empty(empty_dict):
    assert empty_dict.inject(lambda acc, kv_pair: acc + kv_pair[1]) is None


def test_inject_when_empty_with_initial_value(empty_dict):
    assert empty_dict.inject(0, lambda acc, kv_pair: acc + kv_pair[1]) == 0


def test_map_with_a_function_returns_an_enumerable_list(enumerable_dict):
    result = enumerable_dict.map(lambda key, value: (key.upper(), value + 1))
    assert isinstance(result, EnumerableList)
    assert result == [("A", 2), ("B", 3), ("C", 4)]


def test_map_without_a_function_returns_an_enumerator(enumerable_dict):
    enumerator = enumerable_dict.map()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(lambda x, y: (x, y)) == [("a", 1), ("b", 2), ("c", 3)]


def test_reject_returns_the_elements_for_which_the_function_is_falsy(enumerable_dict):
    result = enumerable_dict.reject(value_larger_than_one)
    assert isinstance(result, EnumerableDict)
    assert result == {"a": 1}


def test_reject_without_a_function_returns_an_enumerator(enumerable_dict):
    enumerator = enumerable_dict.reject()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(pass_through) == [("a", 1), ("b", 2), ("c", 3)]


def test_select_returns_the_elements_for_which_the_function_is_truthy(enumerable_dict):
    result = enumerable_dict.select(value_larger_than_one)
    assert isinstance(result, EnumerableDict)
    assert result == {"b": 2, "c": 3}


def test_select_without_a_function_returns_an_enumerator(enumerable_dict):
    enumerator = enumerable_dict.select()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(pass_through) == [("a", 1), ("b", 2), ("c", 3)]


def test_take(enumerable_dict):
    result = enumerable_dict.take(2)
    assert isinstance(result, EnumerableList)
    assert result == [("a", 1), ("b", 2)]


def test_take_with_fewer_elements_than_asked_for(enumerable_dict):
    result = enumerable_dict.take(5)
    assert isinstance(result, EnumerableList)
    assert result == [("a", 1), ("b", 2), ("c", 3)]


def test_take_when_empty(empty_dict):
    result = empty_dict.take(5)
    assert isinstance(result, EnumerableList)
    assert result == []


def value_larger_than_one(key, value):
    return value > 1
