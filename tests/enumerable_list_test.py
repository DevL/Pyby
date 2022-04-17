import pytest
from operator import add
from pyby import EnumerableList
from .test_helpers import assert_enumerable_list, assert_enumerator


@pytest.fixture
def empty_list():
    return EnumerableList()


@pytest.fixture
def letters():
    return EnumerableList(["a", "b", "c"])


@pytest.fixture
def list_with_a_tuple():
    return EnumerableList(["a", ("b", None), "c"])


@pytest.fixture
def numbers():
    return EnumerableList([1, 2, 3])


def test_repr(letters):
    assert repr(letters) == "EnumerableList(['a', 'b', 'c'])"


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


def increment(element):
    return element + 1


def is_zero(element):
    return element == 0


def larger_than_one(element):
    return element > 1


def not_none(element):
    return element is not None
