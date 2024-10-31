# 4. Write a recursive function to calculate the sum of first n natural numbers.
"""
sum(1) = 1
sum(2) = 1 + 2 
sum(3) = 1 + 2 + 3 
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4 + 5 + ... + n-1 + n

sum(n) = sum(n-1) + n
"""

def Sum_of_Nat(n):
    if n == 1:
        return 1
    else:
        return n + Sum_of_Nat(n-1)
    
n = int(input("Enter a Natural number :"))
print(f"The sum of first n natural number is : {Sum_of_Nat(n)}")


# Simple form
def sum(n):
    if n == 1:
        return 1
    else:
        return sum(n-1) + n
print(f"Sum of first n natural number is : {sum(5)}")