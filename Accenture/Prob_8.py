# Give an array mums containing n distinct numbers in the range [0,n], return the only number in the range that is missing from the array
# Input: nums = [3,0,1]
# Output: 2

def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n+1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

nums = [3,0,1]
print("The missing number is :", missing_number(nums))