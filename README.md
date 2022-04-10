# Pyby

![PyPI](https://img.shields.io/pypi/v/pyby)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyby)
![PyPI - Status](https://img.shields.io/pypi/status/pyby)
![PyPI - License](https://img.shields.io/pypi/l/pyby)
![based on Ruby](https://img.shields.io/badge/based%20on%20Ruby-3.1.1-red)
[![Python package](https://github.com/DevL/pyby/actions/workflows/python-package.yml/badge.svg)](https://github.com/DevL/pyby/actions/workflows/python-package.yml)


A library implementing certain Ruby-like behaviours in Python.

**NB:** This is heavily under development and subject to change. Expect breaking changes until the 1.0.0 release.

## Current Functionality

The links in the list of available modules, classes, methods, and functions below link to the corresponding Ruby documentation.  
Currently, Ruby version 3.1.1 is used as a basis for the mimiced functionality.

### [`RObject`](https://ruby-doc.org/core-3.1.1/Object.html) (object.py)

A base class to enrich Python objects with additional functionality.

#### [`respond_to`](https://ruby-doc.org/core-3.1.1/Object.html#method-i-respond_to-3F)

Determines whether an object has a certain callable property or not.  
Also available as a standalone function, rather than a method.

#### [`send`](https://ruby-doc.org/core-3.1.1/Object.html#method-i-send)

Calls the property identified by name, passing it any arguments specified.
If the property is not callable, and no arguments are specified, the property is instead returned.

---

### [`Enumerable`](https://ruby-doc.org/core-3.1.1/Enumerable.html) (enumerable.py)

A base class meant to be subclassed by an iterable.  
The iterable must implement `__each__`, `__into__`, and `to_enum` in order to unlock the rest of the functionality.
In addition, the iterable may implement `__to_tuple__` in order to support predicate and mapping functions with a higher arity than one. A prime example would be `EnumerableDict` in combination with `select` where the 

#### `__each__` (internal)

Returns an iterator to be used internally.  
Must be implemented by the subclass.

#### `__into__` (internal)

Returns a constructor that accepts an iterable for the given method name.  
Must be implemented by the subclass.

#### `__to_tuple__` (internal)

Transforms a single element of an enumerable to a tuple.  
Used internally to uniformly handle predicate and mapping functions with a higher arity than one.  
May be implemented by the subclass.

#### `configure` (internal)

A decorator enabling the return type of a method, as well as the number of arguments predicate and mapping functions are to be called with, to be configured by the collection class inheriting from Enumerable.  
If `enumerator_without_func` is set, the decorator skips calling the decorated method if no arguments have been passed and instead returns an Enumerator based on the enumerable.

Relys on the enumerable's implementation of `__into__` and `__to_tuple__`.

#### [`collect`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-collect), [`map`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-map)

Returns the result of mapping a function over the elements.  
The mapping function takes a single argument for sequences and two arguments for mappings.

#### [`compact`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-compact)

Returns an enumerable of the elements with None values removed.

#### [`each`](https://ruby-doc.org/core-3.1.1/Enumerable.html#module-Enumerable-label-Enumerable+in+Ruby+Core+Classes)

Given a function, calls the function once for each item in the enumerable.  
For sequences this will typically be the same as iterating over the elements,
whereas for mappings this will be same as iterating over the items.

Without a function, returns an enumerator by calling `to_enum`.

#### [`filter`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-filter), [`select`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-select)

Returns the elements for which the predicate function is truthy.  
Without a function, returns an enumerator by calling to_enum.

The predicate function takes a single argument for sequences and two arguments for mappings.

#### [`first`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-first)

Returns the first element or a given number of elements.  
With no argument, returns the first element, or `None` if there is none.  
With a number of elements requested, returns as many elements as possible.

#### [`take`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-take)

Returns the number of elements requested or as many elements as possible.

#### [`to_enum`](https://ruby-doc.org/core-3.1.1/Object.html#method-i-to_enum)

Returns an `Enumerator` for the enumerable.  
Must be implemented by the subclass due to cyclical dependencies.

---

### [`EnumerableDict`](https://ruby-doc.org/core-3.1.1/Hash.html) (enumerable_dict.py)

A subclass of `Enumerable` that mimics some of Ruby's `Hash` while still behaving like a Python `dict`.

---

### [`EnumerableList`](https://ruby-doc.org/core-3.1.1/Array.html) (enumerable_list.py)

A subclass of `Enumerable` that mimics some of Ruby's `Array` while still behaving like a Python `list`.

---

### [`Enumerator`](https://ruby-doc.org/core-3.1.1/Enumerator.html) (enumerator.py)

A class which allows both internal and external iteration.  
An enumerator is in turn an enumerable.

#### [`next`](https://ruby-doc.org/core-3.1.1/Enumerator.html#method-i-next)

Returns the next object in the enumeration sequence.  
If going beyond the enumeration, `StopIteration` is raised.

#### [`peek`](https://ruby-doc.org/core-3.1.1/Enumerator.html#method-i-peek)

Returns the current object in the enumeration sequence without advancing the enumeration.  
If going beyond the enumeration, `StopIteration` is raised.

#### [`rewind`](https://ruby-doc.org/core-3.1.1/Enumerator.html#method-i-rewind)

Rewinds the enumeration sequence to the beginning.

_Note that this may not be possible to do for underlying iterables that can be exhausted._
