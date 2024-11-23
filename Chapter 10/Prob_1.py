# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

f = open("Chapter 10/poem.txt")
content = f.read()
if ("Twinkle" in content):
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is not present in the file.")
f.close()

# Using with statement

with open("Chapter 10/poem.txt") as f:
    content = f.read()
    if ("Twinkle" in content):
        print("The word 'twinkle' is present in the file.")
    else:
        print("The word 'twinkle' is not present in the file.")

print("End of the program")
