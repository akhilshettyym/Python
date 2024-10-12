# Sometimes we want to play PUBG on our phone if the day is Sunday.
# Sometimes we order Ice Cream online if the day is sunny.
# Sometimes we go hiking if our parents allow.
# All these are decisions which depend on a condition being met.
# In python programming too, we must be able to execute instructions on a condition(s)
# being met.
# This is what conditionals are for!

# IF ELSE AND ELIF IN PYTHON
# If else and elif statements are a multiway decision taken by our program due to certain
# conditions in our code.


# SYNTAX
# if (condition1): # if condition1 is True
#     print ("yes")
# elif(condition2): # if condition2 is True
#     print("no")
# else: # otherwise
#     print("maybe")

# If elif else ladder

a = int(input("Enter your age :"))
if (a>18):
    print("You are above the age of consent")

else:
    print("You are below the age of consent")

print("End of the program")