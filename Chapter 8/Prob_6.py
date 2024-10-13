# 6. Write a program to calculate the factorial of a given number using for loop.


n = int(input("Enter a number: "))
f = 1
for i in range(1, n + 1):
    f = f * i
print("Factorial of", n, "is:", f)  


n = int(input("Enter a number: "))
f = 1
for i in range(1, n+1):
    f = f * i
print(f"Factorial of {n} is {f}")