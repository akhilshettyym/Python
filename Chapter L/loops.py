# Loops in Python allow you to execute a block of code repeatedly. Python has two main types of loops: for loops and while loops.

# Sometimes we want to repeat a set of statements in our program. For instance: Print 1
# to 1000.
# Loops make it easy for a programmer to tell the computer which set of instructions to
# repeat and how!

# TYPES OF LOOPS IN PYTHON
# Primarily there are two types of loops in python.
# • while loops
# • for loops

# for loop have the potential to iterate over the items present in the sequence such as lists, tuples, dictionaries and strings
# for loop uses range() to iterate for a specific amount of time

s = "Akhil Shetty M" #The variable s is assigned the string "Akhil Shetty M". Strings in Python are sequences of characters, meaning each character in the string can be accessed individually.
for i in s:     # This statement means "for each character i in the string s."
    print(i)


s = "Akhil Shetty M"
for i in s:
    print(i, end="*")
    # print(i, start="*") not used


# Use of for loop in a list
programming = ["Java", "Python", "Ruby", "HTML", "C"]
for i in programming:
    print(i)

