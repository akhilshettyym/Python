# A function is a group of statements performing a specific task.
# When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!
# A function can be reused by the programmer in a given program any number of

# FUNCTION CALL
# Whenever we want to call a function, we put the name of the function followed by parentheses as follows:
# func1() # This is called function call.

# FUNCTION DEFINITION
# The part containing the exact set of instructions which are executed during the function call.

# def func1():
#     print('hello')
# func1()
# This function can be called any number of times, anywhere in the program.

# a = 12
# b = 45
# c = 56
# avg = (a+b+c)/3
# print(avg)


# a = int(input("Enter a number :"))
# b = int(input("Enter a number :"))
# c = int(input("Enter a number :"))
# avg = (a+b+c)/3
# print(avg)

# Function defination
def avg():
    a = int(input("Enter a number :"))
    b = int(input("Enter a number :"))
    c = int(input("Enter a number :"))

    avg = (a+b+c)/3
    print(avg)

avg()                   
print("Thank you")