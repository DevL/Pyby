import re
from pyby import EnumerableList


def test_none(empty_list, numbers):
    assert not numbers.none()
    assert empty_list.none()
    assert EnumerableList([False, None]).none()


def test_none_with_an_object(numbers):
    assert not numbers.none(3)
    assert numbers.none(4)


def test_none_with_a_predicate(empty_list, numbers):
    assert not EnumerableList([0]).none(is_zero)
    assert empty_list.none(is_zero)
    assert numbers.none(is_zero)


def test_none_with_a_regex_pattern(numbers):
    string_pattern = re.compile(r"\d")
    assert numbers.none(string_pattern)
    numbers.append("the number 69")
    assert not numbers.none(string_pattern)

    bytes_pattern = re.compile(r"\d".encode())
    assert numbers.none(bytes_pattern)
    numbers.append(b"binary 420")
    assert not numbers.none(bytes_pattern)


def test_none_with_a_class(numbers):
    assert not numbers.none(int)
    assert numbers.none(str)


def is_zero(element):
    return element == 0
