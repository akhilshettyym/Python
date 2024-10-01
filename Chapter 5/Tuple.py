# TUPLES IN PYTHON
# A tuple in Python is an immutable sequence type that can store a collection of items. Like lists, tuples can hold different types of data, but once a tuple is created, you cannot change (mutate) its elements. This immutability makes tuples useful for representing fixed collections of items.

# TUPLE IS IMMUTABLE

# Ordered: Tuples maintain the order of elements as they were defined.
# Immutable: Once created, you cannot modify, add, or remove elements from a tuple.
# Allows Mixed Data Types: Tuples can contain elements of different data types (e.g., integers, strings, lists).
# Indexable: You can access elements of a tuple using indexing, just like lists.

# You can create a tuple by enclosing elements in parentheses () and separating them by commas.

tuple = (1, 2, 3)
print(tuple)  # Output: (1, 2, 3)
a = () # empty tuple
a = (1,) # tuple with only one element needs a comma
a = (1,7,2) # tuple with more than one element
print(a)
print(type(tuple))


