# Pyby

[![Python package](https://github.com/DevL/pyby/actions/workflows/python-package.yml/badge.svg)](https://github.com/DevL/pyby/actions/workflows/python-package.yml)

Lecture material for implementing certain Ruby-like behaviours in Python.

The links in the list of available modules, classes, methods, and functions below link to the corresponding Ruby documentation.

---

## [`RObject`](https://ruby-doc.org/core-3.1.1/Object.html) (object.py)

A base class to enrich Python objects with additional functionality.

### [`respond_to`](https://ruby-doc.org/core-3.1.1/Object.html#method-i-respond_to-3F)

Determines whether an object has a certain callable property or not.
Also available as a standalone function, rather than a method.

---

## [`Enumerable`](https://ruby-doc.org/core-3.1.1/Enumerable.html) (enumerable.py)

A base class meant to be subclassed by an iterable.
The iterable must implement `__each__`, `__into__`, and `to_enum` in order to unlock the rest of the functionality.

### `__each__` (internal)

Must be implemented by the subclass.
Returns an iterator to be used internally.

### `__into__` (internal)

Must be implemented by the subclass.
Returns a constructor that accepts an iterable for the given method name.

### `as_enum` (internal)

A decorator used internally to enable the return type of a method to be configured by the
collection class inheriting from Enumerable. Relys on `__into__`.

### [`collect`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-collect), [`map`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-map)

Returns the result of mapping a function over the elements.
The mapping function takes a single argument for sequences and two arguments for mappings.

### [`compact`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-compact)

Returns an enumerable of the elements with None values removed.

### [`each`](https://ruby-doc.org/core-3.1.1/Enumerable.html#module-Enumerable-label-Enumerable+in+Ruby+Core+Classes)

Given a function, calls the function once for each item in the enumerable.
For sequences this will typically be the same as iterating over the elements,
whereas for mappings this will be same as iterating over the items.

Without a function, returns an enumerator by calling `to_enum`.

### [`first`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-first)

Returns the first element or a given number of elements.
With no argument, returns the first element, or `None` if there is none.
With a number of elements requested, returns as many elements as possible.

### [`take`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-take)

Returns the number of elements requested or as many elements as possible.

### [`to_enum`](https://ruby-doc.org/core-3.1.1/Object.html#method-i-to_enum)

Returns an `Enumerator` for the enumerable.
Must be implemented by the subclass due to cyclical dependencies.

---

## [`Enumerator`](https://ruby-doc.org/core-3.1.1/Enumerator.html) (enumerator.py)

A class which allows both internal and external iteration.
An enumerator is in turn an enumerable.

### [`next`](https://ruby-doc.org/core-3.1.1/Enumerator.html#method-i-next)

Returns the next object in the enumeration sequence.
If going beyond the enumeration, `StopIteration` is raised.

### [`peek`](https://ruby-doc.org/core-3.1.1/Enumerator.html#method-i-peek)

Returns the current object in the enumeration sequence without advancing the enumeration.
If going beyond the enumeration, `StopIteration` is raised.

### [`rewind`](https://ruby-doc.org/core-3.1.1/Enumerator.html#method-i-rewind)

Rewinds the enumeration sequence to the beginning.

_Note that this may not be possible to do for underlying iterables that can be exhausted._
