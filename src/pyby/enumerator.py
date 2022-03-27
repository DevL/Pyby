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
            for item in self.iterable:
                func(item)
        else:
            return self.__class__(self.iterable)

    def next(self):
        return next(self.enumeration)

    def rewind(self):
        self.enumeration = iter(self.iterable)
        return self

    def __iter__(self):
        return iter(self.iterable)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.iterable})"

    def _return_type_for(self, method_name):
        return EnumerableList
