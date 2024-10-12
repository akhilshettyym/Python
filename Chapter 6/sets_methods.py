# PROPERTIES OF SETS
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.


s = {99, 1, 3, 54, 6, 7, 7, 7, 100, "Akhil"}
print(s, type(s)) 

# add()
# Adds an element to the set.
s.add(566)
print(s, type(s)) 

# remove()
# Removes the specified element from the set. Raises KeyError if the element is not found.
s.remove(566)
print(s)

# discard()
# Removes the specified element from the set, but does not raise an error if the element is not found.
s.discard(3)  # Now s is {1, 3}
s.discard(5)  # No error, s is still {1, 3}
print(s)

# clear()
# Removes all elements from the set.
s.clear() # Now s is an empty set {}
print(s)


# union()
# Returns a new set with all elements from both sets (also works with multiple sets). This is equivalent to the | operator.
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)  # s3 is {1, 2, 3, 4, 5}
print(s3)


# intersection()
# Returns a new set with only the elements that are common between the sets. This is equivalent to the & operator.
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.intersection(s2)  # s3 is {2, 3}
print(s3)

# difference()
# Returns a new set with elements
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.difference(s2)  # s3 is {1}
print(s3)

# pop()
# Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.
s = {1, 2, 3}
elem = s.pop()  # Removes and returns an element (random)
print(s)


print({1,2}.issubset(s1))
print({1,2}.issuperset(s1))
print({1,2}.isdisjoint(s1))
print(s1.issuperset({1,2}))