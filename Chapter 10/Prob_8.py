# Write a program to make a copy of a text file “this. txt”

with open("Chapter 10/this.txt") as f:
    content = f.read()

with open("Chapter 10/this_copy.txt", "w") as f:
    f.write(content)