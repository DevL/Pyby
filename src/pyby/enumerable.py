from .object import RObject


class Enumerable(RObject):
    def each(self, func=None):
        """
        The basis for all the functionality of any enumerable.
        Must be implemented by a subclass.
        """
        raise NotImplementedError("'each' must be implemented by a subclass")
