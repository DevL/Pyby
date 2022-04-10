import pytest
import re
from pyby import respond_to, RObject


class SomeObject(RObject):
    def __init__(self):
        self.a_number = 1
        self.a_lambda = lambda name: f"Hello {name}"

    def a_method(self, *args, **kwargs):
        return args, kwargs

    def a_method_without_args(self):
        return "No arguments here"

    def echo(self, arg):
        return arg


OBJECT = SomeObject()


def test_respond_to_with_a_callable_property():
    assert OBJECT.respond_to("a_lambda") is True
    assert respond_to(OBJECT, "a_lambda") is True


def test_respond_to_with_a_method():
    assert OBJECT.respond_to("a_method") is True
    assert respond_to(OBJECT, "a_method") is True


def test_respond_to_with_a_non_callable_property():
    assert OBJECT.respond_to("a_number") is False
    assert respond_to(OBJECT, "a_number") is False


def test_respond_to_with_a_missing_property():
    assert OBJECT.respond_to("missing") is False
    assert respond_to(OBJECT, "missing") is False


def test_send_with_a_non_callable_property_without_arguments_returns_the_property():
    assert OBJECT.send("a_number") == 1


def test_send_with_a_non_callable_property_with_arguments():
    with pytest.raises(TypeError, match="'int' object is not callable"):
        OBJECT.send("a_number", "an unexpected argument")


def test_send_with_a_callable_property_with_arguments():
    assert OBJECT.send("a_method", 1, 2, 3, key="value") == ((1, 2, 3), {"key": "value"})


def test_send_without_arguments_calls_an_arity_0_callable_property():
    assert OBJECT.send("a_method_without_args") == "No arguments here"


def test_send_with_a_callable_property_without_required_arguments():
    with pytest.raises(
        TypeError, match=re.escape("<lambda>() missing 1 required positional argument: 'name'")
    ):
        OBJECT.send("a_lambda")


def test_send_with_a_callable_property_with_too_many_arguments():
    with pytest.raises(
        TypeError,
        match=re.escape("a_method_without_args() takes 1 positional argument but 2 were given"),
    ):
        OBJECT.send("a_method_without_args", "an unexpected argument")


def test_send_with_a_missing_property():
    with pytest.raises(AttributeError, match="'SomeObject' object has no attribute 'missing'"):
        OBJECT.send("missing")
