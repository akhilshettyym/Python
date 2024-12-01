# Repeat program 4 for a list of such words to be censored.word = "Donkey"

words = ["Donkey", "bad", "ganda"]
with open("Chapter 10/donkey.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("Chapter 10/donkey.txt", "w") as f:
    f.write(content)