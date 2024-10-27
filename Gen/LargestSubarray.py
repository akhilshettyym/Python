#Write a function that, given an integer array, returns the length of the longest subarray with a sum equal to zero.
array = (15, -2, 2, -8, 1, 7, 10)
print(len(array))
def longest_subarray_with_zero_sum(array):
    prefix_sum_dict = {0: -1}
    current_sum = 0
    max_length = 0
    for i, num in enumerate(array):
        current_sum += num
        if current_sum in prefix_sum_dict:
            max_length = max(max_length, i - prefix_sum_dict[current_sum])
        else:
            prefix_sum_dict[current_sum] = i
        return max_length
print(longest_subarray_with_zero_sum(array)) 



