# Enumerable Candidates

## Methods for Querying

- [ ] all? (no args)
- [ ] all? (non-callable arg)
- [ ] all? (callable arg)
- [ ] any? (no args)
- [ ] any? (non-callable arg)
- [ ] any? (callable arg)
- [x] count (no args)
- [x] count (non-callable arg)
- [x] count (callable arg)
- [ ] none? (no args)
- [ ] none? (non-callable arg)
- [ ] none? (callable arg)
- [ ] one? (no args)
- [ ] one? (non-callable arg)
- [ ] one? (callable arg)
- [x] include?/member?

## Methods for Fetching

- [x] first (no args)
- [x] first (n elements)
- [x] take

## Methods for Searching and Filtering

- [x] find/detect
- [x] find/detect (if_non_proc)
- [x] reject
- [x] select/filter/find_all
- [x] uniq (no args)
- [x] uniq (predicate to determine uniqueness)

## Other Methods

- [x] collect/map (no args)
- [x] collect/map (callable args)
- [x] compact
- [ ] cycle (positive number)
- [ ] cycle (zero or negative number)
- [ ] cycle (no number)
- [ ] cycle (no arg)
- [x] each (no args)
- [x] each (callable arg)
- [x] flat_map / collect_concat (no args)
- [x] flat_map / collect_concat (callable arg)
- [x] inject/reduce
- [ ] zip (no args)
- [ ] zip (callable arg)
---

# Enumerator Candidates

- [x] next
- [x] peek
- [x] rewind

---

# Object Candidates

- [ ] public_send
- [x] respond_to
- [x] send

---

# Additional Candidates

- [ ] [OpenStruct](https://ruby-doc.org/stdlib-3.1.1/libdoc/ostruct/rdoc/OpenStruct.html)
- [ ] [Set](https://ruby-doc.org/stdlib-3.1.1/libdoc/set/rdoc/Set.html)
- [ ] [Struct](https://ruby-doc.org/core-3.1.1/Struct.html)
