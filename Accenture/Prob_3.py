'''
Rob has gone to Mars to collect some stones. The bag he carries can hold a maximum  weight of M. There are M stones weighing from 1 to M on Mars. There are N stones on  Mars that are similar to the ones on Earth. Find the number of stones he can bring from  Mars such that none are similar to any stone on Èarth.  
Input Specification:  
• Input 1: M is the size of the bag and the number of different stone weights present on Mars.  
• Input 2: N is the number of common stones on Earth and Mars.  
• Input 3: An N elements array containing the list of the weights of the common stones.

example:
input 1: 10 bag size
input 2: 3 common stones
input 3: [1, 6, 8]

[2,3,4,5,7,9,10]

2,3,4   2,3,5

output - 3

'''


def get_unique_stones(M, N, common_stones):

    mars_weights = list(range(1, M+1))      # non inclusive so +1

    earth_weights = common_stones

    mars_set = set(mars_weights)
    earth_set = set(earth_weights)

    unique_mars_weights = list(mars_set - earth_set)

    unique_mars_weights.sort()

    total_weight = 0
    num_stones_selected = 0

    for weight in unique_mars_weights:
        if total_weight + weight <= M:
            total_weight += weight
            num_stones_selected += 1
        else:
            break
    return num_stones_selected

input1 = int(input("Enter the capacity of Robs bag :"))
input2 = int(input("Enter the number of common stones on earth :"))
input3 = list(map(int, input("List of stones from earth :").split()))

output = get_unique_stones(input1, input2, input3)
print(output)