from functools import wraps
from itertools import islice
from .object import RObject


class Enumerable(RObject):
    """
    Base class for collection classes mimicing some of Ruby's Enumerable module.
    """

    def as_enum(func):
        """
        Decorator enabling the return type of a method to be configured by the
        collection class inheriting from Enumerable. Relys on `__into__`.
        """

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            into = self.__into__(func.__name__)
            result = func(self, into, *args, **kwargs)
            return result

        return wrapper

    def each(self, func=None):
        """
        Given a function, calls the function once for each item in the enumerable.
        Without a function, returns an enumerator by calling to_enum.
        """
        if func:
            for item in self.__each__():
                func(item)
        else:
            return self.to_enum()

    @as_enum
    def compact(self, into):
        """
        Returns an enumerable of the elements with None values removed.
        """
        return into(item for item in self.__each__() if self.__to_tuple__(item)[-1] is not None)

    @as_enum
    def select(self, into, func=None):
        """
        Returns the elements for which the function is truthy.
        Without a function, returns an enumerator by calling to_enum.

        Also available as the alias `filter`.
        """
        if func:
            return into(item for item in self.__each__() if func(*self.__to_tuple__(item)))
        else:
            return self.to_enum()

    filter = select  # Alias for the select method

    @as_enum
    def first(self, into, number=None):
        """
        Returns the first element or a given number of elements.
        With no argument, returns the first element, or `None` if there is none.
        With an number of elements requested, returns as many elements as possible.
        """
        if number is None:
            return next(self.__each__(), None)
        else:
            return into(islice(self.__each__(), number))

    @as_enum
    def map(self, into, func=None):
        """
        Returns the result of mapping a function over the elements.
        The mapping function takes a single argument for sequences and two arguments for mappings.

        Also available as the alias `collect`.
        """
        if func:
            return into(func(*self.__to_tuple__(item)) for item in self.__each__())
        else:
            return self.to_enum()

    collect = map  # Alias for the map method

    def take(self, number):
        """
        Returns the number of elements requested or as many elements as possible.
        """
        return self.first(number)

    def to_enum(self):
        """
        Returns an enumerator for the enumerable.
        Must be implemented by a subclass.
        """
        raise NotImplementedError("'to_enum' must be implemented by a subclass")

    def __each__(self):
        """
        The basis for all the functionality of any enumerable.
        Must be implemented by a subclass.
        """
        raise NotImplementedError("'__each__' must be implemented by a subclass")

    def __into__(self, method_name):
        """
        Returns a constructor that accepts an iterable for the given method name.
        Used by the as_enum decorator internally.
        Must be implemented by a subclass.
        """
        raise NotImplementedError("'__into__' must be implemented by a subclass")

    def __to_tuple__(self, item):
        """
        Transforms a single element of an enumerable to a tuple.
        Used internally to uniformly handle predicate and mapping functions with a higher arity
        than one.
        May be overriden by a subclass.
        """
        return (item,)
