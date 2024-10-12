# If elif else ladder

a = int(input("Enter your age :"))
if (a>18):
    print("You are above the age of consent")

elif(a<0):
    print("You are entering an invalid age which is not appropriate")

elif(a==0):
    print("Enter an appropriate age")

else:
    print("You are below the age of consent")

print("End of the program")