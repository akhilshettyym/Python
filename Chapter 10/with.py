# WITH STATEMENT
# The best way to open and close the file automatically is the with statement.

f = open("Chapter 10/write.txt")
print(f.read())
f.close()
print("Without WITH statement")

# The same can be written using WITH statement like this :
with open("Chapter 10/write.txt") as f:
    print(f.read())
    print("With WITH statement")

# Need't close the file explicitly