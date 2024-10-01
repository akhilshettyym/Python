# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.
# f-strings (formatted string literals) provide a concise and efficient way to embed expressions inside string literals. Introduced in Python 3.6, f-strings make string formatting more readable and intuitive.
# To create an f-string, prefix your string with the letter f or F, and use curly braces {} to insert expressions, variables, or even Python code directly into the string.


name = input("Enter your name :")
print(f"Good Afternoon {name}")
print("Good Afternoon " +name+ "!")

age = 21
print(f"My name is {name} and I am {age} years old.")