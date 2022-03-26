from .object import RObject


class Enumerator(RObject):
    """
    A class which allows both internal and external iteration.
    """

    def __init__(self, iterable):
        self.iterable = iterable
        self.enumeration = iter(iterable)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.iterable})"

    def next(self):
        return self.enumeration.__next__()

    def rewind(self):
        self.enumeration = iter(self.iterable)
