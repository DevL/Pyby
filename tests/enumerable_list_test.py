import pytest
from pyby import EnumerableList, Enumerator


@pytest.fixture
def empty_list():
    return EnumerableList()


@pytest.fixture
def letters():
    return EnumerableList(["a", "b", "c"])


@pytest.fixture
def numbers():
    return EnumerableList([1, 2, 3])


def test_each_with_a_function_calls_it_once_for_each_item(letters, seen):
    letters.each(seen)
    assert seen == ["a", "b", "c"]


def test_each_without_a_function_yields_each_item(letters):
    enumerator = letters.each()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(lambda x: x) == ["a", "b", "c"]


def test_map_with_a_function_calls_it_ince_for_each_item_and_returns_an_enumerable_list(numbers):
    result = numbers.map(lambda element: element + 1)
    assert isinstance(result, EnumerableList)
    assert result == [2, 3, 4]


def test_map_without_a_function_returns_an_enumerator(letters):
    enumerator = letters.map()
    assert isinstance(enumerator, Enumerator)
    assert enumerator.map(lambda x: x) == ["a", "b", "c"]


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


def test_repr(letters):
    assert repr(letters) == "EnumerableList(['a', 'b', 'c'])"
