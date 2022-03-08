# Pyby

[![Python package](https://github.com/DevL/pyby/actions/workflows/python-package.yml/badge.svg)](https://github.com/DevL/pyby/actions/workflows/python-package.yml)

Lecture material for implementing certain Ruby-like behaviours in Python.

## [Object](https://ruby-doc.org/core-3.1.1/Object.html) (object.py)

### [respond_to](https://ruby-doc.org/core-3.1.1/Object.html#method-i-respond_to-3F)

Determines whether an object has a certain callable property or not.

## [Enumerable](https://ruby-doc.org/core-3.1.1/Enumerable.html) (enumerable.py)

A class meant to be subclassed by a collection implementing `each` in order to unlock the rest of the functionality.

### [each](https://ruby-doc.org/core-3.1.1/Enumerable.html#module-Enumerable-label-Enumerable+in+Ruby+Core+Classes)

Must be implemented by the subclass.
For sequences this will typically be the same as iterating over the elements,
whereas for mappings this will be same as iterating over the items.

### [first](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-first)

Returns the first element or a given number of elements.
With no argument, returns the first element, or `None` if there is none.
With an number of elements requested, returns as many elements as possible.

### [map](https://ruby-doc.org/core-3.1.1/Enumerable.html#method-i-map)

Returns the result of mapping a function over the elements.
The mapping function takes a single argument for sequences and two arguments for mappings.

Also available as the alias `collect`.

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
