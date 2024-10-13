'''7. Write a program to print the following star pattern.
  
for n = 3
          *
         ***
        ***** 


for n = 5
          *
         ***
        *****
       *******
      ********* 

'''

# Here for n = 3 we start the first * with two spaces, Same way for n = 4 we start from 3 spaces

n = int(input("Enter a number :"))
for i in range (1, n+1):                    # for loop that iterates from i = 1 to i = n (inclusive)
    print(" " * (n-i), end="")              # This line prints the spaces before each row of asterisks. 
    print("*" * (2*i-1), end="")            # This line prints the asterisks (*) for the current row.
    print("")                               # This line ensures that after each row of asterisks is printed, the cursor moves to the next line for the next iteration of the loop.


    # end="" ensures no newline is added yet, allowing the full row to be printed before moving to the next line.