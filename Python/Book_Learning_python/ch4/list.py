# This program play with list.
# List is a mutable object, operation on a list object could change itself.

L = [1, 2, 3]

# >>> Add Elements here <<<
# Extend List by iterable elements
L.extend([13, 43, 54])

# insert(at, element)
L.insert(2, -1)

# Add an element to the end of the list. Equivlant to L.insert(-1, e)
L.append(123)

# >>> Operation on list here <<<
# Reverse L
L.reverse()

# L is sorted here
L.sort()

# shallow copy of the list
L.copy()

# count the para in the list
L.count(999)

# >>> Remove elements here <<<
# L.pop(at), remove the element at at.
L.pop(-1)

print(L)

# Remove all elements from list
L.clear()