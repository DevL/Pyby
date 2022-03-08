from pyby import respond_to


class SomeObject:
    def __init__(self):
        self.a_number = 1
        self.a_lambda = lambda x: x

    def a_method(self):
        self


def test_respond_to_with_a_callable_property():
    assert respond_to(SomeObject(), "a_lambda") is True


def test_respond_to_with_a_method():
    assert respond_to(SomeObject(), "a_method") is True


def test_respond_to_with_a_non_callable_property():
    assert respond_to(SomeObject(), "a_number") is False


def test_respond_to_with_a_missing_property():
    assert respond_to(SomeObject(), "missing") is False
