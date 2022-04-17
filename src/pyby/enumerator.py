from .enumerable import Enumerable
from .enumerable_list import EnumerableList

NO_HEAD = object()


class Enumerator(Enumerable):
    """
    A class which allows both internal and external iteration.
    """

    def __init__(self, iterable):
        self.iterable = iterable
        self.enumeration = iter(iterable)
        self.head = NO_HEAD
        self.delegate = isinstance(self.iterable, Enumerable)

    def next(self):
        """
        Returns the next object in the enumeration sequence.
        If going beyond the enumeration, `StopIteration` is raised.
        """
        head = self.head
        if head is NO_HEAD:
            return next(self.enumeration)
        else:
            self.head = NO_HEAD
            return head

    def peek(self):
        """
        Returns the current object in the enumeration sequence without advancing the enumeration.
        If going beyond the enumeration, `StopIteration` is raised.
        """
        if self.head is NO_HEAD:
            self.head = next(self.enumeration)
        return self.head

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
        if self.delegate:
            return self.iterable.__each__()
        else:
            return iter(self.iterable)

    def __into__(self, method_name):
        if self.delegate:
            return self.iterable.__into__(method_name)
        else:
            return EnumerableList

    def __iter__(self):
        return self.__each__()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.iterable})"

    def __to_tuple__(self, item):
        if self.delegate:
            return self.iterable.__to_tuple__(item)
        else:
            return (item,)
