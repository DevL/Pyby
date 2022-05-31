import re
from pyby import EnumerableDict, EnumerableList


def test_one(empty_list, numbers, empty_dict, enumerable_dict):
    assert not numbers.one()
    assert not empty_list.one()
    assert not empty_dict.one()
    assert not enumerable_dict.one()
    assert not EnumerableList([False]).one()
    assert EnumerableList([True]).one()
    assert EnumerableDict({"key": "value"}).one()
    assert EnumerableDict({"key": False}).one()


def test_one_with_an_object(numbers, enumerable_dict):
    assert numbers.one(3)
    assert not numbers.one(4)
    assert enumerable_dict.one(("a", 1))
    assert not enumerable_dict.one(("d", 4))


def test_one_with_a_predicate(empty_list, numbers, empty_dict, enumerable_dict):
    assert EnumerableList([0]).one(is_zero)
    assert not empty_list.one(is_zero)
    assert not numbers.one(is_zero)
    assert EnumerableDict({"key": 0}).one(value_is_zero)
    assert not empty_dict.one(value_is_zero)
    assert not enumerable_dict.one(value_is_zero)


def test_one_with_a_regex_pattern(numbers, enumerable_dict):
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

    assert not enumerable_dict.one(string_pattern)
    assert not enumerable_dict.one(bytes_pattern)


def test_one_with_a_class(numbers, enumerable_dict):
    assert not numbers.one(int)
    numbers.append(1.23)
    assert numbers.one(float)
    assert EnumerableDict({"some": "value"}).one(tuple)
    assert not enumerable_dict.one(tuple)


def is_zero(element):
    return element == 0


def value_is_zero(key, value):
    return value == 0
