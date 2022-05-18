import pytest
import re
from operator import add
from pyby import EnumerableList
from .test_helpers import assert_enumerable_list, assert_enumerator, pass_through


@pytest.fixture
def letters():
    return EnumerableList(["a", "b", "c"])


@pytest.fixture
def list_with_a_tuple():
    return EnumerableList(["a", ("b", None), "c"])


@pytest.fixture
def numbers_with_duplicates():
    return EnumerableList([1, 2, 3, 3, 2])


def test_repr(letters):
    assert repr(letters) == "EnumerableList(['a', 'b', 'c'])"


def test_any(empty_list, numbers):
    assert numbers.any()
    assert not empty_list.any()
    assert not EnumerableList([False, None]).any()


def test_any_with_an_object(numbers):
    assert numbers.any(3)
    assert not numbers.any(4)


def test_any_with_a_predicate(empty_list, numbers):
    assert EnumerableList([0]).any(is_zero)
    assert not empty_list.any(is_zero)
    assert not numbers.any(is_zero)


def test_any_with_a_regex_pattern(numbers):
    string_pattern = re.compile(r"\d")
    assert not numbers.any(string_pattern)
    numbers.append("the number 69")
    assert numbers.any(string_pattern)
    bytes_pattern = re.compile(r"\d".encode())
    assert not numbers.any(bytes_pattern)
    numbers.append(b"binary 420")
    assert numbers.any(bytes_pattern)


def test_any_with_a_class(numbers):
    assert numbers.any(int)
    assert not numbers.any(str)


def test_all(empty_list, numbers):
    assert numbers.all()
    assert empty_list.all()
    assert not EnumerableList([False, None]).all()


def test_all_with_an_object(numbers):
    assert not numbers.all(3)
    assert EnumerableList([4, 4, 4]).all(4)


def test_all_with_a_predicate(empty_list, numbers):
    assert empty_list.all(is_zero)
    assert EnumerableList([0]).all(is_zero)
    assert not numbers.all(larger_than_one)


# def test_all_with_a_regex_pattern(empty_list, numbers):
#     string_pattern = re.compile(r"\d")

#     assert not numbers.all(string_pattern)
#     assert numbers.all(string_pattern)

#     bytes_pattern = re.compile(r"\d".encode())
#     assert not numbers.any(bytes_pattern)
#     numbers.append(b"420")
#     assert numbers.any(bytes_pattern)


def test_all_with_a_class(numbers, list_with_a_tuple):
    assert numbers.all(int)
    assert not numbers.all(str)
    assert not list_with_a_tuple.all(int)


def test_collect_with_a_function_maps_over_the_items_and_returns_an_enumerable_list(numbers):
    assert_enumerable_list(numbers.collect(increment), [2, 3, 4])


def test_collect_with_a_sequence_containing_a_tuple(list_with_a_tuple):
    assert_enumerable_list(list_with_a_tuple.collect(not_none), [True, True, True])


def test_collect_without_a_function_returns_an_enumerator(letters):
    assert_enumerator(letters.collect(), ["a", "b", "c"])


def test_compact():
    enumerable_list = EnumerableList([None, "a", None, "b", "c", None])
    assert_enumerable_list(enumerable_list.compact(), ["a", "b", "c"])


def test_compact_when_empty(empty_list):
    assert_enumerable_list(empty_list.compact(), [])


def test_compact_when_not_containing_any_None_values(letters):
    assert_enumerable_list(letters.compact(), ["a", "b", "c"])


def test_compact_with_a_sequence_containing_a_tuple(list_with_a_tuple):
    assert_enumerable_list(list_with_a_tuple.compact(), ["a", ("b", None), "c"])


def test_count(numbers):
    assert numbers.count() == 3


def test_count_with_a_non_callable_argument(numbers):
    assert numbers.count(2) == 1


def test_count_with_a_callable_argument(numbers):
    assert numbers.count(larger_than_one) == 2


def test_each_with_a_function_calls_it_once_for_each_item(letters, seen):
    letters.each(seen)
    assert seen == ["a", "b", "c"]


def test_each_without_a_function_returns_an_enumerator(letters):
    assert_enumerator(letters.each(), ["a", "b", "c"])


def test_find(numbers):
    assert numbers.find(larger_than_one) == 2


def test_find_when_not_found(numbers):
    assert numbers.find(is_zero) is None


def test_find_when_not_found_with_default(numbers):
    assert numbers.find(lambda: 69, is_zero) == 69


def test_find_whitout_predicate_returns_an_enumerator(letters):
    assert_enumerator(letters.find(), ["a", "b", "c"])


def test_first(numbers):
    assert numbers.first() == 1


def test_first_when_empty(empty_list):
    assert empty_list.first() is None


def test_first_with_number_of_elements_specified(letters):
    assert_enumerable_list(letters.first(2), ["a", "b"])


def test_first_with_fewer_elements_than_asked_for(letters):
    assert_enumerable_list(letters.first(5), ["a", "b", "c"])


def test_first_when_empty_when_asked_for_a_number_of_elements(empty_list):
    assert_enumerable_list(empty_list.first(5), [])


def test_flat_map_without_a_function_returns_an_enumerator(letters):
    assert_enumerator(letters.flat_map(), ["a", "b", "c"])


def test_flat_map_with_nested_iterables(letters, numbers):
    enumerable_list = EnumerableList([letters, numbers, 4])
    assert_enumerable_list(enumerable_list.flat_map(pass_through), ["a", "b", "c", 1, 2, 3, 4])


def test_flat_map_does_not_treat_strings_as_nested_iterables():
    enumerable_list = EnumerableList(["abc", "def"])
    assert_enumerable_list(enumerable_list.flat_map(pass_through), ["abc", "def"])


def test_include(numbers):
    assert numbers.include(3)
    assert not numbers.include(4)


def test_inject(numbers):
    assert numbers.inject(add) == 6


def test_inject_with_initial_value(numbers):
    assert numbers.inject(4, add) == 10


def test_inject_when_empty(empty_list):
    assert empty_list.inject(add) is None


def test_inject_when_empty_with_initial_value(empty_list):
    assert empty_list.inject(0, add) == 0


def test_reject_returns_the_elements_for_which_the_function_is_falsy(numbers):
    assert_enumerable_list(numbers.reject(larger_than_one), [1])


def test_reject_without_a_function_returns_an_enumerator(letters):
    assert_enumerator(letters.reject(), ["a", "b", "c"])


def test_reject_with_a_sequence_containing_a_tuple(list_with_a_tuple):
    assert_enumerable_list(list_with_a_tuple.reject(not_none), [])


def test_select_returns_the_elements_for_which_the_function_is_truthy(numbers):
    assert_enumerable_list(numbers.select(larger_than_one), [2, 3])


def test_select_without_a_function_returns_an_enumerator(letters):
    assert_enumerator(letters.select(), ["a", "b", "c"])


def test_select_with_a_sequence_containing_a_tuple(list_with_a_tuple):
    assert_enumerable_list(list_with_a_tuple.select(not_none), ["a", ("b", None), "c"])


def test_take(letters):
    assert_enumerable_list(letters.take(2), ["a", "b"])


def test_take_with_fewer_elements_than_asked_for(letters):
    assert_enumerable_list(letters.take(5), ["a", "b", "c"])


def test_take_when_empty(empty_list):
    assert_enumerable_list(empty_list.take(5), [])


def test_uniq(numbers_with_duplicates):
    assert_enumerable_list(numbers_with_duplicates.uniq(), [1, 2, 3])


def test_uniq_with_predicate(numbers_with_duplicates):
    assert_enumerable_list(numbers_with_duplicates.uniq(larger_than_one), [1, 2])


def test_uniq_with_no_hashable_elements():
    enumerable_list = EnumerableList([1, 2, [1], [2], [1, 2]])
    assert_enumerable_list(enumerable_list.uniq(), [1, 2, [1], [2], [1, 2]])


def increment(element):
    return element + 1


def is_zero(element):
    return element == 0


def larger_than_one(element):
    return element > 1


def not_none(element):
    return element is not None
