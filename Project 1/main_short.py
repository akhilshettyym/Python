import random
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
    if ((computer - you) == 1 or (computer -you) == -2) :
        print("You win")






    """
    if (computer == 1 and you == -1):        2 comp
        print("Computer wins")
    elif (computer == 1 and you == 0):       1 you
        print("You win")

    elif (computer == -1 and you == 1):      -2 you
        print("You win")        
    elif (computer == -1 and you == 0):      -1 comp
        print("Computer wins")

    elif (computer == 0 and you == -1):      1 you
        print("You win")
    elif (computer == 0 and you == 1):       -1 comp
        print("Computer wins")
    else:
        print("Something went wrong")   
        """