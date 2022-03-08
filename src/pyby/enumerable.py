from itertools import islice
from .object import RObject


class Enumerable(RObject):
    def each(self, func=None):
        """
        The basis for all the functionality of any enumerable.
        Must be implemented by a subclass.
        """
        raise NotImplementedError("'each' must be implemented by a subclass")

    def first(self, elements=None):
        if elements is None:
            return next(self.each(), None)
        else:
            return self._return_type()(islice(self.each(), elements))

    def map(self, func=None):
        if func:
            return self._return_type()(func(*_to_tuple(item)) for item in self.each())
        else:
            return self.each()

    collect = map

    def _return_type(self):
        raise NotImplementedError("'_return_type' must be implemented by a subclass")


def _to_tuple(item):
    """
    >>> _to_tuple(1)
    (1,)

    >>> _to_tuple(("key", "value"))
    ('key', 'value')
    """
    return item if isinstance(item, tuple) else (item,)
