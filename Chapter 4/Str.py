# String is a data type in python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways.
# string is immutable

a ='Akhil'               # Single quoted string
b = "Akhil"              # Double quoted string
c = '''Akhil'''          # Triple quoted string

print(len(a))            # Prints the length of the string

# String Slicing :A string in python can be sliced for getting a part of the strings.
# The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, we use the following syntax:
# string[start:stop:step]
name = print(a[0:3])    # Starts from index 0 and goes all the way till 3 excluding 3

# Negative slicing
name_2 = print(a[-4:-1])
name_3 = print(a[1:4])      # Conversion of negative to positive

name_4 = print(a[:4])   # Is same as name_4 = print(a[0:4])
name_5 = print(a[1:])   # Is same as name_5 = print(a[1:5])

# Negative Indices: Negative indices can also be used as shown in the figure above. -1 corresponds to the (length - 1) index, -2 to (length - 2).


# SLICING WITH SKIP VALUE
# We can provide a skip value as a part of our slice like this:\
a = "0123456789"
print(a[1:8:2])    # Takes the start from index 1 to 8 and gets the number after each two numbers

b = "abcdefghijklmnopqrstuvwxyz"
print(b[0:25:2])

# Other advanced slicing techniques:
Word = "amazing"
Word = Word[:7] # word [0:7] – 'amazing'
Word = Word[0:] # word [0:7] – 'amazing'
