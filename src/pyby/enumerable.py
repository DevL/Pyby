from itertools import islice
from .object import RObject


class Enumerable(RObject):
    def each(self, func=None):
        """
        The basis for all the functionality of any enumerable.
        Must be implemented by a subclass.
        """
        raise NotImplementedError("'each' must be implemented by a subclass")

    def compact(self):
        """
        Returns an enumerable of the elements with None values removed.
        """
        return self._as_enumerable(
            (item for item in self.each() if _to_tuple(item)[-1] is not None)
        )

    def first(self, number=None):
        """
        Returns the first element or a given number of elements.
        With no argument, returns the first element, or `None` if there is none.
        With an number of elements requested, returns as many elements as possible.
        """
        if number is None:
            return next(self.each(), None)
        else:
            return self._as_enumerable(islice(self.each(), number))

    def map(self, func=None):
        """
        Returns the result of mapping a function over the elements.
        The mapping function takes a single argument for sequences and two arguments for mappings.

        Also available as the alias `collect`.
        """
        if func:
            return self._as_enumerable(func(*_to_tuple(item)) for item in self.each())
        else:
            return self.each()

    collect = map

    def _as_enumerable(self, iterable):
        return self._return_type()(iterable)

    def _return_type(self):
        """
        Returns a constructor that accepts an iterable.
        Must be implemented by a subclass.
        """
        raise NotImplementedError("'_return_type' must be implemented by a subclass")


def _to_tuple(item):
    """
    >>> _to_tuple(1)
    (1,)

    >>> _to_tuple(("key", "value"))
    ('key', 'value')
    """
    return item if isinstance(item, tuple) else (item,)
