def pass_through(value, *values):
    """
    >>> pass_through(2)
    2

    >>> pass_through(1, 2)
    (1, 2)
    """
    if values:
        return value, *values
    else:
        return value


class Seen(list):
    def __bool__(self):
        """
        >>> bool(Seen())
        True
        """
        return True

    def __call__(self, element):
        """
        >>> seen = Seen([1, 2])
        >>> seen(3)
        >>> seen
        Seen([1, 2, 3])
        """
        self.append(element)

    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"
