class RObject:
    def respond_to(self, name):
        return respond_to(self, name)


def respond_to(obj, name):
    """
    Returns True if the object has a callable property with the given name.

    Inspired by Ruby's respond_to method.

    >>> respond_to(dict(), "get")
    True

    >>> respond_to(1, "get")
    False
    """
    return callable(getattr(obj, name, False))
