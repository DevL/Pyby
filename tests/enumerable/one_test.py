import re
from pyby import EnumerableList


def test_one(empty_list, numbers):
    assert not numbers.one()
    assert not empty_list.one()
    assert not EnumerableList([False]).one()
    assert EnumerableList([True]).one()


def test_one_with_an_object(numbers):
    assert numbers.one(3)
    assert not numbers.one(4)


def test_one_with_a_predicate(empty_list, numbers):
    assert EnumerableList([0]).one(is_zero)
    assert not empty_list.one(is_zero)
    assert not numbers.one(is_zero)


def test_one_with_a_regex_pattern(numbers):
    string_pattern = re.compile(r"\d")
    assert not numbers.one(string_pattern)
    numbers.append("the number 69")
    assert numbers.one(string_pattern)
    numbers.append("another number 69")
    assert not numbers.one(string_pattern)
    bytes_pattern = re.compile(r"\d".encode())
    assert not numbers.one(bytes_pattern)
    numbers.append(b"binary 420")
    assert numbers.one(bytes_pattern)


def test_one_with_a_class(numbers):
    assert not numbers.one(int)
    numbers.append(1.23)
    assert numbers.one(float)


def is_zero(element):
    return element == 0
