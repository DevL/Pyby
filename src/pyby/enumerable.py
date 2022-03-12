from itertools import islice
from functools import wraps
from .object import RObject


class Enumerable(RObject):
    def as_enum(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            into = self._return_type()
            result = func(self, *args, into=into, **kwargs)
            return result

        return wrapper

    def each(self, func=None):
        """
        The basis for all the functionality of any enumerable.
        Must be implemented by a subclass.
        """
        raise NotImplementedError("'each' must be implemented by a subclass")

    @as_enum
    def compact(self, into=None):
        """
        Returns an enumerable of the elements with None values removed.
        """
        return into(item for item in self.each() if _to_tuple(item)[-1] is not None)

    @as_enum
    def first(self, number=None, into=None):
        """
        Returns the first element or a given number of elements.
        With no argument, returns the first element, or `None` if there is none.
        With an number of elements requested, returns as many elements as possible.
        """
        if number is None:
            return next(self.each(), None)
        else:
            return into(islice(self.each(), number))

    @as_enum
    def map(self, func=None, into=None):
        """
        Returns the result of mapping a function over the elements.
        The mapping function takes a single argument for sequences and two arguments for mappings.

        Also available as the alias `collect`.
        """
        if func:
            return into(func(*_to_tuple(item)) for item in self.each())
        else:
            return self.each()

    collect = map

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
