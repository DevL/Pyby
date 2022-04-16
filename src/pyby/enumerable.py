import functools
from importlib import import_module
from itertools import islice
from .object import RObject

EMPTY_REDUCE_ERRORS = [
    "reduce() of empty iterable with no initial value",
    "reduce() of empty sequence with no initial value",
]
NOT_USED = object()


def always_true(*args):
    """
    A predicate function that is always truthy.
    """
    return True


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

    @configure()
    def collect(self, into, to_tuple, func):
        """
        Returns the result of mapping a function over the elements.
        The mapping function takes a single argument for sequences and two arguments for mappings.

        Also available as the alias `map`.
        """
        return into(func(*to_tuple(item)) for item in self.__each__())

    def compact(self):
        """
        Returns an enumerable of the elements with None values removed.
        """
        return self.select(lambda *args: args[-1] is not None)

    def count(self, compare_to=always_true):
        """
        Returns the number of elements in the enumerable.

        Optionally accepts an argument.
        Given a non-callable argument, counts the number of equivalent elements.
        Given a callable predicate, counts the elements for which the predicate is truthy.
        """
        if callable(compare_to):
            return len(self.select(compare_to))
        else:
            return list(self.__each__()).count(compare_to)

    @configure(use_into=False, use_to_tuple=False)
    def each(self, func):
        """
        Given a function, calls the function once for each item in the enumerable.
        Without a function, returns an enumerator by calling to_enum.
        """
        for item in self.__each__():
            func(item)

    @configure(use_into=False)
    def find(self, to_tuple, func_or_not_found, func=NOT_USED):
        predicate = func_or_not_found if func is NOT_USED else func
        try:
            return next(self.__select__(predicate, to_tuple))
        except StopIteration:
            return None if func == NOT_USED else func_or_not_found()

    @configure(use_to_tuple=False, enumerator_without_func=False)
    def first(self, into, number=NOT_USED):
        """
        Returns the first element or a given number of elements.
        With no argument, returns the first element, or `None` if there is none.
        With a number of elements requested, returns as many elements as possible.
        """
        if number is NOT_USED:
            return next(self.__each__(), None)
        else:
            return into(islice(self.__each__(), number))

    def inject(self, func_or_initial, func=NOT_USED):
        """
        Performs a reduction operation much like `functools.reduce`.
        If called with a single argument, treats it as the reduction function.
        If called with two arguments, the first is treated as the initial value
        for the reduction and the second argument acts as the reduction function.

        Also available as the alias `reduce`.
        """
        try:
            if func is NOT_USED:
                return functools.reduce(func_or_initial, self.__each__())
            else:
                return functools.reduce(func, self.__each__(), func_or_initial)
        except TypeError as error:
            if error.args[0] in EMPTY_REDUCE_ERRORS:
                return None
            else:
                raise

    @configure(use_into=False, use_to_tuple=False)
    def reject(self, predicate):
        """
        Returns the elements for which the function is falsy.
        Without a function, returns an enumerator by calling to_enum.
        """
        return self.select(inverse(predicate))

    @configure()
    def select(self, into, to_tuple, predicate):
        """
        Returns the elements for which the function is truthy.
        Without a function, returns an enumerator by calling to_enum.

        Also available as the alias `filter`.
        """
        return into(self.__select__(predicate, to_tuple))

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
    map = collect
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

    def __select__(self, predicate, to_tuple):
        """
        Used internally by find, select et al.
        """
        return (item for item in self.__each__() if predicate(*to_tuple(item)))

    def __to_tuple__(self, item):
        """
        Transforms a single element of an enumerable to a tuple.
        Used internally by the configure decorator to uniformly handle
        predicate and mapping functions with a higher arity than one.
        May be overridden by a subclass.
        """
        return (item,)


def inverse(predicate):
    """
    Reverses the logic of a predicate function.

    >>> inverse(bool)(True)
    False

    >>> inverse(lambda x, y: x > y)(0, 1)
    True
    """
    return lambda *args: not predicate(*args)
