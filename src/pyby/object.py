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

    def send(self, name, *args, **kwargs):
        """
        Calls the property identified by name, passing it any arguments specified.
        If the property is not callable and no arguments are specified, the property is returned.
        """
        property_or_method = getattr(self, name)
        if args or kwargs or callable(property_or_method):
            return property_or_method(*args, **kwargs)
        else:
            return property_or_method


respond_to = RObject.respond_to
