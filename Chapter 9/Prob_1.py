# 1. Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
a = int(input("Enter a number for a :"))   
b = int(input("Enter a number for b :"))    
c = int(input("Enter a number for c :"))
print("The greatest number is:",greatest(a,b,c))
