# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry","Soham","Sachin","Rahul","Rahul"]

l = ["Harry","Soham","Sachin","Rahul","Rahul"]
for name in l:
    if (name.startswith("S")):
        print("Hello", name)            # print(f"hello {name}")
print("Greetings to the persons whose names starts with S")

l = ["Harry","Soham","Sachin","Rahul","Rahul"]
for name in l:
    if (name.startswith("R")):
        print("Hello", name)
print("Greetings to the persons whose names starts with R")
