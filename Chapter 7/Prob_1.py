# 1. Write a program to find the greatest of four numbers entered by the user.

a1 = int(input("Enter the first number :"))
a2 = int(input("Enter the second number :"))
a3 = int(input("Enter the third number :"))
a4 = int(input("Enter the fourth number :"))

if (a1>a2>a3>a4):
    print(f"{a1} is greater than {a2} {a3} {a4}")
    print(f"The greatest number is {a1}")
elif (a2>a1>a3>a4):
    print(f"{a2} is greater than {a1} {a3} {a4}")
    print(f"The greatest number is {a2}")
elif (a3>a1>a2>a4):
    print(f"{a3} is greater than {a1} {a2} {a4}")
    print(f"The greatest number is {a3}")
else:
    print(f"{a4} is greater than {a1} {a2} {a3}")
    print(f"The greatest number is {a4}")


