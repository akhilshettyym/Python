# LIST - Python lists are containers to store a set of values of any data type.
friends = ["Akhil", 5, 10, 0.4124, "Grapes", "Khushi", True ]
print(friends)
print(friends[0])
friends[0] = "Shetty"
print(friends[0])
friends[0:2]

print(friends)

# LISTS ARE MUTABLE
# Here unlike strings we can change the elements in the the list and that gets updated in the list

l1 = [7,9,"Akhil"]
l1[0] # 7
l1[1] # 9
# l1[70] # error
l1[0:2] # [7,9] #list slicing