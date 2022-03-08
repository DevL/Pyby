# Pyby

[![Python package](https://github.com/DevL/pyby/actions/workflows/python-package.yml/badge.svg)](https://github.com/DevL/pyby/actions/workflows/python-package.yml)

Lecture material for implementing certain Ruby-like behaviours in Python.

## [Object](https://ruby-doc.org/core-3.1.1/Object.html) (object.py)

### [respond_to](https://ruby-doc.org/core-3.1.1/Object.html#method-i-respond_to-3F)

Determines whether an object has a certain callable property or not.

## [Enumerable](https://ruby-doc.org/core-3.1.1/Enumerable.html) (enumerable.py)

A class meant to be subclassed by a collection implementing `each` in order to unlock the rest of the functionality.

### [each](https://ruby-doc.org/core-3.1.1/Enumerable.html#module-Enumerable-label-Enumerable+in+Ruby+Core+Classes)

Must be implmented by the subclass.
For sequences this will typically be the same as iterating over the elements,
whereas for mappings this will be same as iterating over the items.

# Candidates

- [x] collect/map
- [ ] compact
- [ ] count (no args, non-callable arg, and callable arg)
- [ ] find
- [x] first
- [ ] inject/reduce
- [ ] reject
- [ ] select/filter
