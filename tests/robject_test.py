from pyby import RObject


class SomeObject(RObject):
    def __init__(self):
        self.a_number = 1
        self.a_lambda = lambda x: x

    def a_method(self):
        self


OBJECT = SomeObject()


def test_respond_to_with_a_callable_property():
    assert OBJECT.respond_to("a_lambda") is True


def test_respond_to_with_a_method():
    assert OBJECT.respond_to("a_method") is True


def test_respond_to_with_a_non_callable_property():
    assert OBJECT.respond_to("a_number") is False


def test_respond_to_with_a_missing_property():
    assert OBJECT.respond_to("missing") is False
