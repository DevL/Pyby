from pyby import EnumerableDict
from .test_helpers import (
    assert_enumerable_dict,
    assert_enumerable_list,
    assert_enumerator,
    pass_through,
)


def test_repr(enumerable_dict):
    assert repr(enumerable_dict) == "EnumerableDict({'a': 1, 'b': 2, 'c': 3})"


def test_collect_with_a_function_returns_an_enumerable_list(enumerable_dict):
    result = enumerable_dict.collect(lambda key, value: (key.upper(), value + 1))
    assert_enumerable_list(result, [("A", 2), ("B", 3), ("C", 4)])


def test_collect_without_a_function_returns_an_enumerator(enumerable_dict):
    assert_enumerator(enumerable_dict.collect(), [("a", 1), ("b", 2), ("c", 3)])


def test_compact():
    enumerable_dict = EnumerableDict(a=1, b=2, c=3, d=None)
    assert_enumerable_dict(enumerable_dict.compact(), {"a": 1, "b": 2, "c": 3})


def test_compact_when_empty(empty_dict):
    assert_enumerable_dict(empty_dict.compact(), {})


def test_compact_when_not_containing_any_None_values(enumerable_dict):
    assert_enumerable_dict(enumerable_dict.compact(), {"a": 1, "b": 2, "c": 3})


def test_count(enumerable_dict):
    assert enumerable_dict.count() == 3


def test_count_with_a_non_callable_argument(enumerable_dict):
    assert enumerable_dict.count(("b", 2)) == 1


def test_count_with_a_callable_argument(enumerable_dict):
    assert enumerable_dict.count(value_larger_than_one) == 2


def test_each_with_a_function_calls_it_once_for_each_item(enumerable_dict, seen):
    enumerable_dict.each(seen)
    assert seen == [("a", 1), ("b", 2), ("c", 3)]


def test_each_without_a_function_returns_an_enumerator(enumerable_dict):
    assert_enumerator(enumerable_dict.each(), [("a", 1), ("b", 2), ("c", 3)])


def test_find(enumerable_dict):
    assert enumerable_dict.find(value_larger_than_one) == ("b", 2)


def test_find_when_not_found(enumerable_dict):
    assert enumerable_dict.find(value_is_zero) is None


def test_find_when_not_found_with_default(enumerable_dict):
    assert enumerable_dict.find(lambda: 69, value_is_zero) == 69


def test_find_whitout_predicate_returns_an_enumerator(enumerable_dict):
    assert_enumerator(enumerable_dict.find(), [("a", 1), ("b", 2), ("c", 3)])


def test_first(enumerable_dict):
    assert enumerable_dict.first() == ("a", 1)


def test_first_with_number_of_elements_specified(enumerable_dict):
    assert_enumerable_list(enumerable_dict.first(2), [("a", 1), ("b", 2)])


def test_first_with_fewer_elements_than_asked_for(enumerable_dict):
    assert_enumerable_list(enumerable_dict.first(5), [("a", 1), ("b", 2), ("c", 3)])


def test_first_when_empty(empty_dict):
    assert empty_dict.first() is None


def test_first_when_empty_when_asked_for_a_number_of_elements(empty_dict):
    assert_enumerable_list(empty_dict.first(5), [])


def test_flat_map_without_a_function_returns_an_enumerator(enumerable_dict):
    assert_enumerator(enumerable_dict.flat_map(), [("a", 1), ("b", 2), ("c", 3)])


def test_flat_map_with_nested_iterables(enumerable_dict):
    assert_enumerable_list(enumerable_dict.flat_map(pass_through), ["a", 1, "b", 2, "c", 3])


def test_include(enumerable_dict):
    assert enumerable_dict.include("a")
    assert not enumerable_dict.include(1)


def test_inject(enumerable_dict):
    assert enumerable_dict.inject(lambda acc, kv_pair: ("sum", acc[1] + kv_pair[1])) == ("sum", 6)


def test_inject_with_initial_value(enumerable_dict):
    assert enumerable_dict.inject(4, lambda acc, kv_pair: acc + kv_pair[1]) == 10


def test_inject_when_empty(empty_dict):
    assert empty_dict.inject(lambda acc, kv_pair: acc + kv_pair[1]) is None


def test_inject_when_empty_with_initial_value(empty_dict):
    assert empty_dict.inject(0, lambda acc, kv_pair: acc + kv_pair[1]) == 0


def test_reject_returns_the_elements_for_which_the_function_is_falsy(enumerable_dict):
    assert_enumerable_dict(enumerable_dict.reject(value_larger_than_one), {"a": 1})


def test_reject_without_a_function_returns_an_enumerator(enumerable_dict):
    assert_enumerator(enumerable_dict.reject(), [("a", 1), ("b", 2), ("c", 3)])


def test_select_returns_the_elements_for_which_the_function_is_truthy(enumerable_dict):
    assert_enumerable_dict(enumerable_dict.select(value_larger_than_one), {"b": 2, "c": 3})


def test_select_without_a_function_returns_an_enumerator(enumerable_dict):
    assert_enumerator(enumerable_dict.select(), [("a", 1), ("b", 2), ("c", 3)])


def test_take(enumerable_dict):
    assert_enumerable_list(enumerable_dict.take(2), [("a", 1), ("b", 2)])


def test_take_with_fewer_elements_than_asked_for(enumerable_dict):
    assert_enumerable_list(enumerable_dict.take(5), [("a", 1), ("b", 2), ("c", 3)])


def test_take_when_empty(empty_dict):
    assert_enumerable_list(empty_dict.take(5), [])


def test_uniq(enumerable_dict):
    assert_enumerable_list(enumerable_dict.uniq(), [("a", 1), ("b", 2), ("c", 3)])


def test_uniq_with_predicate(enumerable_dict):
    assert_enumerable_list(enumerable_dict.uniq(value_larger_than_one), [("a", 1), ("b", 2)])


def value_is_zero(key, value):
    return value == 0


def value_larger_than_one(key, value):
    return value > 1
