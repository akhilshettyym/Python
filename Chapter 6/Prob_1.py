# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

words = {
    "Namaste": "Hello",
    "Dhanyawad": "Thank you",
    "Kaise ho": "How are you",
    "Mein teek hun": "I am fine",
    "Aapka swaagat hai": "Welcome"
}

word = input(" Enter the word you want meaning of :")
print(words[word])