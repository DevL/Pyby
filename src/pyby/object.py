class RObject:
    """
    A base class to enrich Python objects with additional functionality.
    """

    def respond_to(self, name):
        """
        Returns True if the object has a callable property with the given name.

        Inspired by Ruby's respond_to method.

        >>> respond_to(dict(), "get")
        True

        >>> respond_to(1, "get")
        False
        """
        return callable(getattr(self, name, False))


respond_to = RObject.respond_to
