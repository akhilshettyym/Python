# THE BREAK STATEMENT
# ‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now.

for i in range(50):
    if i == 25:
        break   # Exit the loop right now
    print(i)
print("End of one !")

for i in range (0,80):
    print(i) # this will print 0,1,2 and 3
    if i==3:
        break
print("End of second !")


# THE CONTINUE STATEMENT
# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.
for i in range(50):
    if i == 25:
        continue    # Skip this iteration
    print(i)
print("End of third !")

for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
    print(i)
print("End of fourth !")