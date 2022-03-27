from pyby import Enumerable, EnumerableList


class Enumerator(Enumerable):
    """
    A class which allows both internal and external iteration.
    """

    def __init__(self, iterable):
        self.iterable = iterable
        self.enumeration = iter(iterable)

    def each(self, func=None):
        if func:
            for item in self.__each__():
                func(item)
        else:
            return self.to_enum()

    def next(self):
        """
        Returns the next object in the enumeration sequence.
        If going beyond the enumeration, `StopIteration` is raised.
        """
        return next(self.enumeration)

    def rewind(self):
        """
        Rewinds the enumeration sequence to the beginning.
        Note that this may not be possible to do for underlying iterables that can be exhausted.
        """
        self.enumeration = iter(self.iterable)
        return self

    def to_enum(self):
        return self.__class__(self.iterable)

    def __each__(self):
        return iter(self.iterable)

    def __into__(self, method_name):
        return EnumerableList

    def __iter__(self):
        return iter(self.iterable)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.iterable})"
