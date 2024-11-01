"""
Snake water gun game :
1 for snake
-1 for water
0 for gun
"""
import random
# computer = -1
computer = random.choice([1,-1,0])
youstr = input("Enter your choice :")
youDict = {'s':1, 'w':-1, 'g':0}
reverseDict = {1:'Snake', -1:'Water', 0:'Gun'}

you = youDict[youstr]

# By now we have two numbers you and computer

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if (computer == you ):
    print("Its a draw !!!")
else: 
    if (computer == 1 and you == -1):
        print("Computer wins")
    elif (computer == 1 and you == 0):
        print("You win")

    elif (computer == -1 and you == 1):
        print("You win")
    elif (computer == -1 and you == 0):
        print("Computer wins")

    elif (computer == 0 and you == -1):
        print("You win")
    elif (computer == 0 and you == 1):
        print("Computer wins")
    else:
        print("Something went wrong")