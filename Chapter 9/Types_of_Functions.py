'''TYPES OF FUNCTIONS IN PYTHON
There are two types of functions in python:
• Built in functions (Already present in python)
• User defined functions (Defined by the user)
Examples of built in functions includes len(), print(), range() etc.
The func1() function we defined is an example of user defined function.'''

# FUNCTIONS WITH ARGUMENTS
# A function can accept some value it can work with. We can put these values in the
# parentheses.
# A function can also return value as shown below:

def goodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
goodDay("Akhil", "Thank you")


def greet(name, ending):            # name and endings are arguments
    print("Good day, " + name)
    print(ending)
    return "Done"
a = greet ("Akhil", "Thank you")
print(a)