# TUPLE METHODS
# a.count (1): a count (1) will return number of times 1 occurs in a.
# a.index (1) will return the index of first occurrence of 1 in a. If 1 is not found, it will raise an error.

friends = ("Akhil", 5, 10, 0.4124, "Grapes", "Khushi", True, 5, 5)
print(type(friends))

no = friends.count(5)  # a.count (1): a count (1) will return number of times 1 occurs in a.
print(no)

# a.index (1) will return the index of first occurrence of 1 in a.
no = friends.index(True)    # no = friends.index(5)
print(no)

# Indexing - You can access tuple elements using their index (just like lists). Indexing starts at 0
my_tuple = (10, 20, 30, 40)
print(my_tuple[0])  # Output: 10
print(my_tuple[-1]) # Output: 40 (negative index refers to the last element)


# Slicing - You can retrieve a part (or slice) of a tuple using the slicing syntax start:end:step
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple[1:4])   # Output: (1, 2, 3) (elements from index 1 to 3)
print(my_tuple[::2])   # Output: (0, 2, 4) (every second element)

# Concatenation - You can combine two or more tuples using the + operator.
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4)

# Repetition - You can repeat the elements in a tuple a specified number of times using the * operator.
my_tuple = ('A', 'B')
print(my_tuple * 3)  # Output: ('A', 'B', 'A', 'B', 'A', 'B')

# Checking Membership - You can check whether an element exists in a tuple using the in or not in keywords.
my_tuple = (10, 20, 30, 40)
print(20 in my_tuple)   # Output: True
print(50 not in my_tuple)  # Output: True

# Length of a Tuple - You can find out how many elements are in a tuple using the len() function.
my_tuple = (1, 2, 3, 4)
print(len(my_tuple))  # Output: 4

print(min(my_tuple))
print(max(my_tuple))


# Packing
my_tuple = 1, 2, "apple"

# Unpacking
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: apple
# Unpacking with default values