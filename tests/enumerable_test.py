import pytest
from pyby import Enumerable


def test_each_with_function_requires___each___to_be_implemented_by_a_subclass():
    with pytest.raises(NotImplementedError, match="'__each__' must be implemented by a subclass"):
        Enumerable().each(lambda x: x)


def test_each_without_a_function_requires_to_enum_to_be_implemented_by_a_subclass():
    with pytest.raises(NotImplementedError, match="'to_enum' must be implemented by a subclass"):
        Enumerable().each()


def test_an_enumerable_responds_to_each():
    assert Enumerable().respond_to("each")


def test_an_enumerable_responds_to_to_enum():
    assert Enumerable().respond_to("to_enum")


def test_collect_is_an_alias_to_map():
    assert Enumerable.collect == Enumerable.map
