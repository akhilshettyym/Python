d = {}  # Empty dictionary
print(type(d))

s = {1, 2, 3}   # this is a set
print(type(s))

e = set()
print(type(s))  # Don't use s = {} (this will create a dict) to create an empty set, instead use s = set() to create a set. 

s = {99, 1, 3, 54, 6, 7, 7, 7, 100}     # Will not return repetitive numbers also here the order won't be maintained
print(s)