a = int(input("Enter your age :"))

# If statement 1
if(a%2 == 0):
    print("Your age is even")
# End of If statement 1

# If statement 2
if (a>18):
    print("You are above the age of consent")

elif(a<0):
    print("You are entering an invalid age which is not appropriate")


else:
    print("You are below the age of consent")
# End of If statement 2

print("End of the program")