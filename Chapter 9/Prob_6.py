# 6. Write a python function which converts inches to cms.
def inch_to_cm(n):
    return n * 2.54
n = int(input("Enter a value in inches :"))
print(inch_to_cm(n))


# Program to convert cm to inches
def cm_to_inch(n):
    return n / 2.54
n = int(input("Enter a value in cm :"))
print(cm_to_inch(n))