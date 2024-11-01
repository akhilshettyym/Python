"""
FILE INPUT OUTPUT OPERATION
The random-access memory is volatile, and all its contents are lost once a program
terminates. In order to persist the data forever, we use files.
Files are used to store data in a non-volatile manner. We can read data from a file.

A file is data stored in a storage device. A python program can talk to the file by reading
content from it and writing content to it.


TYPE OF FILES.
There are 2 types of files:

1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .dat, etc)

Python has a lot of functions for reading, updating, and deleting files.


OPENING A FILE
Python has an open() function for opening files. It takes 2 parameters: filename and
mode.
# open("filename", "mode


"""

f = open("README.md")
data = f.read()
print(data)
f.close()