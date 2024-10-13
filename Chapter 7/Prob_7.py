# 7. Write a program to find out whether a given post is talking about “Akhil” or not.

# post = " Hey Akhil bhai is good, Akhil bhai is very good, Akhil is great"

post = input("Enter the post :")
if ("Akhil".lower() in post.lower()):
    print("The post is talking about Akhil")
else:
    print("The post is not talking about Akhil")