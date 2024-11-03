''' Implement the following Function : def differenceofSum(n,m)  
• The function accepts two integers n, m as arguments Find the sum of  all numbers in range from 1 to m(both inclusive) that are not divisible  by n.
Return difference between sum of integers not divisible by n  with sum of numbers divisible by n.  

n : 4
m : 20

Output : 90

'''

def difference_sum(n, m):
    sum_divisible = 0
    sum_not_divisible = 0

    for i in range(m+1):
        if i % n == 0:
            sum_divisible += i
        else:
            sum_not_divisible += i
    return sum_not_divisible - sum_divisible 

n = 4
m = 20

print("The difference between the sum are :", difference_sum(n, m))