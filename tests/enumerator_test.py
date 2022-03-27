import pytest
from pyby import Enumerator


@pytest.fixture
def enumerated_list():
    return Enumerator([1, 2, 3])


@pytest.fixture
def enumerated_dict():
    return Enumerator({"a": 1, "b": 2, "c": 3})


def test_an_enumerator_responds_to_next():
    assert Enumerator([]).respond_to("next")


def test_repr(enumerated_list):
    assert repr(enumerated_list) == "Enumerator([1, 2, 3])"


def test_an_enumerated_list_can_be_iterated(enumerated_list):
    assert enumerated_list.next() == 1
    assert enumerated_list.next() == 2
    assert enumerated_list.next() == 3


def test_an_enumerated_list_can_be_rewound(enumerated_list):
    assert enumerated_list.next() == 1
    assert enumerated_list.next() == 2
    assert enumerated_list.rewind() == enumerated_list
    assert enumerated_list.next() == 1


def test_an_enumerated_dict_can_be_iterated(enumerated_dict):
    assert enumerated_dict.next() == "a"
    assert enumerated_dict.next() == "b"
    assert enumerated_dict.next() == "c"


def test_an_enumerated_dict_can_be_rewound(enumerated_dict):
    assert enumerated_dict.next() == "a"
    assert enumerated_dict.next() == "b"
    assert enumerated_dict.rewind() == enumerated_dict
    assert enumerated_dict.next() == "a"








