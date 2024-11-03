''' You are given a Function , Write the code for the Fibonacci numbers,  commonly denoted F(n) form a sequence, called the Fibonacci  sequence, such that each number is the sum of the two preceding  ones, starting from 0and 1. That is,  
Input: n = 2  
Output: 1  '''

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1 
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

n = int(input("Enter the number :"))
print("The fibonacci number is :", fibonacci(n))