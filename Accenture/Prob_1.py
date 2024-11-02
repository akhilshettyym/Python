# Write a function that accepts three parameters: two positive integers r and unit, and a  positive integer array arr of size n.  
# •⁠  ⁠r represents the number of rats present in an area.  • unit is the amount of food each rat consumes.  • Each element of the array arr represents the amount of food present in each house,  where the index of the array corresponds to the house number.  
# The function should determine the minimum number of houses required to provide  enough food for all the rats.

def calculate(r, unit, arr, n):
    if arr is None or n == 0:
        return -1
    
    totalFoodRequired = r * unit
    foodTillNow = 0

    for house in range(n):
        foodTillNow += arr[house]
        if foodTillNow >= totalFoodRequired:
            return house + 1
    return 0

r = int(input("Enter number of rats: "))
unit = int(input("Enter the value of units: "))
n = int(input("Number of elements in the array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))

print(calculate(r, unit, arr, n))

# Time complexity for this problem will be -  O(n)
# As we have to visit each of the houses and that can be n number of houses


"""
arr = list(map(int, input("Enter the elements of the array: ").split()))

input("Enter the elements of the array: "):
This will allow user to enter multiple numbers in a single line. For example, the user might enter 4 2 5 1.
The input is taken as a single string, such as "4 2 5 1"

.split() is a string method that splits the input string into a list of substrings (words) based on spaces.
For example, if the user enters "4 2 5 1", .split() converts this into a list of strings: ["4", "2", "5", "1"].

map(int, ...):
map(int, ...) applies the int function to each element in the list, converting each string into an integer.
In our example, map(int, ["4", "2", "5", "1"]) would convert this to 4, 2, 5, 1 as integers.

list(...) takes the output of map and converts it into a list.
This gives the final result: arr = [4, 2, 5, 1], where arr is a list of integers.

"""