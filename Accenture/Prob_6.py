# You are given a function and you need to reverse a number
# input : 12345
# output :54321

def reverse_number(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num

num = int(input("Enter numbers to be reversed :"))
print("Reversed number :", reverse_number(num))


num_str = "12345"
print(num_str[1:4])     # Output: '234' (from index 1 up to, but not including, 4)
print(num_str[:3])      # Output: '123' (from start up to, but not including, 3)
print(num_str[2:])      # Output: '345' (from index 2 to the end)
print(num_str[::2])     # Output: '135' (every second element)
print(num_str[::-1])    # Output: '54321' (reverses the string)