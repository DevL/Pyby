import functools
from importlib import import_module
from itertools import islice
from .object import RObject

EMPTY_REDUCE_ERRORS = [
    "reduce() of empty iterable with no initial value",
    "reduce() of empty sequence with no initial value",
]


class Enumerable(RObject):
    """
    Base class for collection classes mimicing some of Ruby's Enumerable module.
    """

    def configure(use_into=True, use_to_tuple=True, enumerator_without_func=True):
        """
        Decorator enabling the return type of a method, as well as the number of arguments
        predicate and mapping functions are to be called with, to be configured by the
        collection class inheriting from Enumerable. If enumerator_without_func is set,
        the decorator skips calling the decorated method if no arguments have been passed
        and instead returns an Enumerator based on the enumerable.

        Relys on the enumerable's implementation of `__into__` and `__to_tuple__`.
        """

        def decorator(method):
            @functools.wraps(method)
            def wrapper(self, *args, **kwargs):
                if enumerator_without_func and not (args or kwargs):
                    return self.to_enum()
                else:
                    config = []
                    if use_into:
                        config.append(self.__into__(method.__name__))
                    if use_to_tuple:
                        config.append(self.__to_tuple__)
                    return method(self, *config, *args, **kwargs)

            return wrapper

        return decorator

    @configure(use_into=False, use_to_tuple=False)
    def each(self, func):
        """
        Given a function, calls the function once for each item in the enumerable.
        Without a function, returns an enumerator by calling to_enum.
        """
        for item in self.__each__():
            func(item)

    @configure(enumerator_without_func=False)
    def compact(self, into, to_tuple):
        """
        Returns an enumerable of the elements with None values removed.
        """
        return into(item for item in self.__each__() if to_tuple(item)[-1] is not None)

    @configure(use_to_tuple=False, enumerator_without_func=False)
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

    @configure()
    def map(self, into, to_tuple, func):
        """
        Returns the result of mapping a function over the elements.
        The mapping function takes a single argument for sequences and two arguments for mappings.

        Also available as the alias `collect`.
        """
        return into(func(*to_tuple(item)) for item in self.__each__())

    def inject(self, *args):
        """
        Performs a reduction operation much like `functools.reduce`.
        If called with a single argument, treats it as the reduction function.
        If called with two arguments, the first is treated as the initial value
        for the reduction and the second argument acts as the reduction function.

        Also available as the alias `reduce`.
        """
        try:
            if len(args) == 1:
                return functools.reduce(args[0], self.__each__())
            else:
                return functools.reduce(args[1], self.__each__(), args[0])
        except TypeError as error:
            if error.args[0] in EMPTY_REDUCE_ERRORS:
                return None
            else:
                raise

    @configure()
    def reject(self, into, to_tuple, func):
        """
        Returns the elements for which the function is falsy.
        Without a function, returns an enumerator by calling to_enum.
        """
        return into(item for item in self.__each__() if not func(*to_tuple(item)))

    @configure()
    def select(self, into, to_tuple, func):
        """
        Returns the elements for which the function is truthy.
        Without a function, returns an enumerator by calling to_enum.

        Also available as the alias `filter`.
        """
        return into(item for item in self.__each__() if func(*to_tuple(item)))

    def take(self, number):
        """
        Returns the number of elements requested or as many elements as possible.
        """
        return self.first(number)

    def to_enum(self):
        """
        Returns an enumerator for the enumerable.
        Must be implemented by an iterable subclass.
        """
        return import_module("pyby.enumerator").Enumerator(self)

    # Method aliases
    collect = map
    filter = select
    reduce = inject

    def __each__(self):
        """
        The basis for all the functionality of any enumerable.
        Must be implemented by a subclass.
        """
        raise NotImplementedError("'__each__' must be implemented by a subclass")

    def __into__(self, method_name):
        """
        Returns a constructor that accepts an iterable for the given method name.
        Used by the configure decorator internally.
        May be overridden by a subclass.
        """
        return import_module("pyby.enumerable_list").EnumerableList

    def __to_tuple__(self, item):
        """
        Transforms a single element of an enumerable to a tuple.
        Used internally by the configure decorator to uniformly handle
        predicate and mapping functions with a higher arity than one.
        May be overridden by a subclass.
        """
        return (item,)
