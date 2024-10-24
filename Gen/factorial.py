num = int(input("Enter a number: "))
factorial = 1

# Calculate factorial
for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")
