from functools import wraps
from itertools import islice
from .object import RObject


class Enumerable(RObject):
    """
    Base class for collection classes mimicing some of Ruby's Enumerable module.
    """

    def adaptive(method):
        """
        Decorator enabling the return type of a method, as well as the number of arguments
        predicate and mapping functions are to be called with, to be configured by the
        collection class inheriting from Enumerable.

        Relys on `__into__` and `__to_tuple__`.
        """

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            into = self.__into__(method.__name__)
            to_tuple = self.__to_tuple__
            return method(self, into, to_tuple, *args, **kwargs)

        return wrapper

    def enumerator_without_func(method):
        """
        Decorator that skips calling the decorated method if no arguments have been passed
        and instead returns an Enumerator based on the enumerable.
        """

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            if args or kwargs:
                return method(self, *args, **kwargs)
            else:
                return self.to_enum()

        return wrapper

    @enumerator_without_func
    def each(self, func):
        """
        Given a function, calls the function once for each item in the enumerable.
        Without a function, returns an enumerator by calling to_enum.
        """
        for item in self.__each__():
            func(item)

    @adaptive
    def compact(self, into, to_tuple):
        """
        Returns an enumerable of the elements with None values removed.
        """
        return into(item for item in self.__each__() if to_tuple(item)[-1] is not None)

    @enumerator_without_func
    @adaptive
    def select(self, into, to_tuple, func):
        """
        Returns the elements for which the function is truthy.
        Without a function, returns an enumerator by calling to_enum.

        Also available as the alias `filter`.
        """
        return into(item for item in self.__each__() if func(*to_tuple(item)))

    filter = select  # Alias for the select method

    @adaptive
    def first(self, into, to_tuple, number=None):
        """
        Returns the first element or a given number of elements.
        With no argument, returns the first element, or `None` if there is none.
        With an number of elements requested, returns as many elements as possible.
        """
        if number is None:
            return next(self.__each__(), None)
        else:
            return into(islice(self.__each__(), number))

    @enumerator_without_func
    @adaptive
    def map(self, into, to_tuple, func):
        """
        Returns the result of mapping a function over the elements.
        The mapping function takes a single argument for sequences and two arguments for mappings.

        Also available as the alias `collect`.
        """
        return into(func(*to_tuple(item)) for item in self.__each__())

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
        Used by the adaptive decorator internally.
        Must be implemented by a subclass.
        """
        raise NotImplementedError("'__into__' must be implemented by a subclass")

    def __to_tuple__(self, item):
        """
        Transforms a single element of an enumerable to a tuple.
        Used internally by the adaptive decorator to uniformly handle predicate and mapping
        functions with a higher arity than one.
        May be overriden by a subclass.
        """
        return (item,)
