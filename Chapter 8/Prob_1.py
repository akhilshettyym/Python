# 1. Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter a number :"))
for i in range(1,11):
    mul = i*n
    print(n,"*",i,"=",mul)


m = int(input("Enter a number :"))
for i in range(1,11):
    print(f"{m} X {i} = {m*i}")