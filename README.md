# Pyby

[![Python package](https://github.com/DevL/pyby/actions/workflows/python-package.yml/badge.svg)](https://github.com/DevL/pyby/actions/workflows/python-package.yml)

Lecture material for implementing certain Ruby-like behaviours in Python.

The links in the list of available modules, classes, methods, and functions below link to the corresponding Ruby documentation.

## [`RObject`](https://ruby-doc.org/core-3.1.1/Object.html) (object.py)

A base class to enrich Python objects with additional functionality.

### [`respond_to`](https://ruby-doc.org/core-3.1.1/Object.html#method-i-respond_to-3F)

Determines whether an object has a certain callable property or not.
Also available as a standalone function, rather than a method.

## [`Enumerable`](https://ruby-doc.org/core-3.1.1/Enumerable.html) (enumerable.py)

A base class meant to be subclassed by an iterable.
The iterable must implement `each` and `__into__` in order to unlock the rest of the functionality.

### `as_enum` (internal)

A decorator used internally to enable the return type of a method to be configured by the
collection class inheriting from Enumerable. Relys on `__into__`.

### `__into__` (internal)

Must be implemented by the subclass.
Returns a constructor that accepts an iterable for the given method name.

### [`each`](https://ruby-doc.org/core-3.1.1/Enumerable.html#module-Enumerable-label-Enumerable+in+Ruby+Core+Classes)

Must be implemented by the subclass.
For sequences this will typically be the same as iterating over the elements,
whereas for mappings this will be same as iterating over the items.

### [`compact`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-compact)

Returns an enumerable of the elements with None values removed.

### [`first`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-first)

Returns the first element or a given number of elements.
With no argument, returns the first element, or `None` if there is none.
With an number of elements requested, returns as many elements as possible.

### [`collect`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-collect), [`map`](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-map)

Returns the result of mapping a function over the elements.
The mapping function takes a single argument for sequences and two arguments for mappings.

# Candidates

- [x] collect/map
- [x] compact
- [ ] count (no args)
- [ ] count (non-callable arg)
- [ ] count (callable arg)
- [ ] find
- [x] first (no args)
- [x] first (n elements)
- [ ] inject/reduce
- [ ] reject
- [ ] select/filter
- [ ] uniq
