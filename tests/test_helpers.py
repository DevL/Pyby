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
        return True

    def __call__(self, element):
        self.append(element)
