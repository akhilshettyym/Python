# 7. If the names of 2 friends are same; what will happen to the program in problem 6?

d = {}

name = input("Enter friends name :")
lang = input("Enter lang name :")
d.update({name :lang})

name = input("Enter friends name :")
lang = input("Enter lang name :")
d.update({name :lang})

name = input("Enter friends name :")
lang = input("Enter lang name :")
d.update({name :lang})

name = input("Enter friends name :")
lang = input("Enter lang name :")
d.update({name :lang})

print(d)

print("The 2 friends with same names the latest name will be returned")