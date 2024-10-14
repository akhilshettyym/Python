# DEFAULT PARAMETER VALUE
# We can have a value as default as default argument in a function.
# If we specify name = “stranger” in the line containing def, this value is used when no
# argument is passed.

# def greet(name = "stranger"):
# # function body
# greet() # name will be "stranger" in function body (default)
# greet("harry") # name will be "harry" in function body (passed)

def goodDay(name, ending="Thank you"):
    print(f"Good day, {name} {ending}.")
goodDay("Akhil")
goodDay("Akhi", "Thanks")