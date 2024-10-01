friends = ["Akhil", 5, 10, 0.4124, "Grapes", "Khushi", True ]
print(friends)

friends.append("Shetty")
print(friends)

# Unlike Strings the list itself will be changed instead creating a new one. That is str is immutable and list is 

# SORT - Sort method will sort the whole list
l = [1, 3, 1.5, 9, 9.75, 6, 4, 9, 11]
l.sort()
print(l)           

# APPEND - Adds 13 at the end of the list
l.append(13)
print(l)

# REVERSE - updates the list
l.reverse()
print(l)

# INSERT 
l.insert(5,13.1)    # This will add 13.1 at 5 index
print(l)

# REMOVE
l.remove(13.1)
print(l)

# POP - Will delete element at index 2 and return its value.
l.pop(2)
print(l)