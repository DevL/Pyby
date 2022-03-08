import pytest
from pyby import Enumerable


def test_each_must_be_implemented_by_a_subclass():
    with pytest.raises(NotImplementedError, match="'each' must be implemented by a subclass"):
        Enumerable().each()


def test_an_enumerable_behaves_like_a_robject():
    assert Enumerable().respond_to("each") is True
