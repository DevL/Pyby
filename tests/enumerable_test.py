import pytest
from pyby import Enumerable
from .test_helpers import pass_through


@pytest.fixture
def enumerable():
    return Enumerable()


@pytest.mark.parametrize(
    "method_name",
    [
        "each",
        "collect",
        "compact",
        "filter",
        "first",
        "inject",
        "map",
        "reduce",
        "reject",
        "select",
        "take",
        "to_enum",
    ],
)
def test_public_interface(enumerable, method_name):
    assert enumerable.respond_to(method_name)


@pytest.mark.parametrize(
    "alias, method_name",
    [
        ("collect", "map"),
        ("filter", "select"),
        ("reduce", "inject"),
    ],
)
def test_aliases(enumerable, alias, method_name):
    assert getattr(enumerable, alias) == getattr(enumerable, method_name)


def test_each_with_function_requires___each___to_be_implemented_by_a_subclass(enumerable):
    with pytest.raises(NotImplementedError, match="'__each__' must be implemented by a subclass"):
        enumerable.each(pass_through)


def test_each_without_a_function_requires_to_enum_to_be_implemented_by_a_subclass(enumerable):
    with pytest.raises(NotImplementedError, match="'to_enum' must be implemented by a subclass"):
        enumerable.each()


def test_requires___into___to_be_implemented_by_a_subclass(enumerable):
    with pytest.raises(NotImplementedError, match="'__into__' must be implemented by a subclass"):
        enumerable.first(1)
