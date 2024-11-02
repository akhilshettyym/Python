# An automobile company manufactures both a two wheeler (TW) and a four wheeler  (FW). 
# A company manager wants to make the production of both types of vehicle  according to the given data below:  
# •⁠  ⁠Ist data, Total number of vehicle (two-wheeler + four-wheeler)=v  
# •  2nd data, Total number of wheels = W  
# The task is to find how many two-wheeler as well as four-wheeler need to manufacture  as per the given data

"""
Constraints :
2<=w
w%2 = 0
v<w
print "INVALID INPUT" if inputs did not meet the constraints

Input format for testing:
The candidate has to write acode that accepts two positive numbers seperated by a new line.
- First Input Line - Accept value v
- Second Input Line - Accept value w

Input :
200 -> Value of v
540 -> Value of w

Output:
TW = 130
FW = 70

Explaination :
130 + 70 = 200 vehicles
(70*4) + (130*2) = 540 wheels

"""

v = int(input("Enter the number of Vehicles: "))
w = int(input("Enter the number of Wheels: "))
if (w<2 or w % 2 != 0 or v >= w):
    print("INVALID INPUT")
else:
    TW = (4 * v - w) // 2
    FW = v - TW

    if (TW >= 0 and FW >= 0):
        print(f"Number of two wheelers : {TW}")
        print(f"Number of four wheelers : {FW}")  
    else:
        print("INVALID INPUT")


# Time complexity of the above will be - O(1)