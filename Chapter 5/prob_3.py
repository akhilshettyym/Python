# 3. Check that a tuple type cannot be changed in python.

a = (1,4,9, "Akhil")
a[3] = "Khushi"
print(a)

a = [1,4,9, "Akhil"]
a[3] = "Khushi"
print(a)