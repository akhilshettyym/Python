# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Akhil", [1,2]}
print(s)
s.add([3,4])

print(s)


# No, you cannot change the values inside a list that is contained in a set in Python. In fact, the code you have provided will raise an error because sets in Python cannot contain mutable objects like lists.

# Sets in Python only allow immutable (unchangeable) objects as elements, such as integers, strings, and tuples. Lists are mutable, meaning they can be changed (items can be added, removed, or modified), so they are not allowed in sets.