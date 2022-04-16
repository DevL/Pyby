import pytest
from pyby import EnumerableList, Enumerator
from .test_helpers import pass_through


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
    result = numbers.collect(increment)
    assert isinstance(result, EnumerableList)
    assert result == [2, 3, 4]


def test_collect_with_a_sequence_containing_a_tuple(list_with_a_tuple):
    result = list_with_a_tuple.collect(not_none)
    assert isinstance(result, EnumerableList)
    assert result == [True, True, True]


def test_collect_without_a_function_returns_an_enumerator(letters):
    enumerator = letters.collect()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(pass_through) == ["a", "b", "c"]


def test_compact():
    enumerable_list = EnumerableList([None, "a", None, "b", "c", None])
    result = enumerable_list.compact()
    assert isinstance(result, EnumerableList)
    assert result == ["a", "b", "c"]


def test_compact_when_empty(empty_list):
    result = empty_list.compact()
    assert isinstance(result, EnumerableList)
    assert result == []


def test_compact_when_not_containing_any_None_values(letters):
    result = letters.compact()
    assert isinstance(result, EnumerableList)
    assert result == ["a", "b", "c"]


def test_compact_with_a_sequence_containing_a_tuple(list_with_a_tuple):
    result = list_with_a_tuple.compact()
    assert isinstance(result, EnumerableList)
    assert result == ["a", ("b", None), "c"]


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
    enumerator = letters.each()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(pass_through) == ["a", "b", "c"]


def test_find(numbers):
    assert numbers.find(larger_than_one) == 2


def test_find_when_not_found(numbers):
    assert numbers.find(is_zero) is None


def test_find_when_not_found_with_default(numbers):
    assert numbers.find(lambda: 69, is_zero) == 69


def test_find_whitout_predicate_returns_an_enumerator(letters):
    enumerator = letters.find()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(pass_through) == ["a", "b", "c"]


def test_first(numbers):
    assert numbers.first() == 1


def test_first_when_empty(empty_list):
    assert empty_list.first() is None


def test_first_with_number_of_elements_specified(letters):
    result = letters.first(2)
    assert isinstance(result, EnumerableList)
    assert result == ["a", "b"]


def test_first_with_fewer_elements_than_asked_for(letters):
    result = letters.first(5)
    assert isinstance(result, EnumerableList)
    assert result == ["a", "b", "c"]


def test_first_when_empty_when_asked_for_a_number_of_elements(empty_list):
    result = empty_list.first(5)
    assert isinstance(result, EnumerableList)
    assert result == []


def test_inject(numbers):
    assert numbers.inject(lambda acc, element: acc + element) == 6


def test_inject_with_initial_value(numbers):
    assert numbers.inject(4, lambda acc, element: acc + element) == 10


def test_inject_when_empty(empty_list):
    assert empty_list.inject(lambda acc, element: acc + element) is None


def test_inject_when_empty_with_initial_value(empty_list):
    assert empty_list.inject(0, lambda acc, element: acc + element) == 0


def test_reject_returns_the_elements_for_which_the_function_is_falsy(numbers):
    result = numbers.reject(larger_than_one)
    assert isinstance(result, EnumerableList)
    assert result == [1]


def test_reject_without_a_function_returns_an_enumerator(letters):
    enumerator = letters.reject()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(pass_through) == ["a", "b", "c"]


def test_reject_with_a_sequence_containing_a_tuple(list_with_a_tuple):
    result = list_with_a_tuple.reject(not_none)
    assert isinstance(result, EnumerableList)
    assert result == []


def test_select_returns_the_elements_for_which_the_function_is_truthy(numbers):
    result = numbers.select(larger_than_one)
    assert isinstance(result, EnumerableList)
    assert result == [2, 3]


def test_select_without_a_function_returns_an_enumerator(letters):
    enumerator = letters.select()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(pass_through) == ["a", "b", "c"]


def test_select_with_a_sequence_containing_a_tuple(list_with_a_tuple):
    result = list_with_a_tuple.select(not_none)
    assert isinstance(result, EnumerableList)
    assert result == ["a", ("b", None), "c"]


def test_take(letters):
    result = letters.take(2)
    assert isinstance(result, EnumerableList)
    assert result == ["a", "b"]


def test_take_with_fewer_elements_than_asked_for(letters):
    result = letters.take(5)
    assert isinstance(result, EnumerableList)
    assert result == ["a", "b", "c"]


def test_take_when_empty(empty_list):
    result = empty_list.take(5)
    assert isinstance(result, EnumerableList)
    assert result == []


def increment(element):
    return element + 1


def is_zero(element):
    return element == 0


def larger_than_one(element):
    return element > 1


def not_none(element):
    return element is not None
