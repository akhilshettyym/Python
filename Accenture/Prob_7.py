# You are given a function and write the program to count the total number of characters in a string 
# Input = "Accenture coding round"
# Output = 20

def count_characters(str):
    return len(str)
str = "Accenture coding round"
print("The total number of characters in a string is :", count_characters(str))


def count_characters_without_spaces(str1):
    return len(str1.replace(" ", ""))
str1 = "Accenture coding round"
print("The total number of characters in a string wo counting blank soaces is :", count_characters_without_spaces(str1))