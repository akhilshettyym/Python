f = open("Chapter 10/write.txt")

l1 = f.readline() 
print(l1, type(l1))

l2 = f.readline() 
print(l2, type(l2))

l3 = f.readline() 
print(l3, type(l3))

l4 = f.readline() 
print(l4, type(l4))

f.close()