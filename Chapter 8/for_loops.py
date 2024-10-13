# FOR LOOP
# A for loop is used to iterate through a sequence like list, tuple, or string [iterables]
    
for i in range(5): # 0 to 4
    print(i)
print("Program 1 ends")

l = [1, 7, 8]
for item in l:
    print(item) # prints 1, 7 and 8
print("Program 2 ends")


# RANGE FUNCTION IN PYTHON
# The range() function in python is used to generate a sequence of number.
# We can also specify the start, stop and step-size as follows:
# range(start, stop, step_size)
# # step_size is usually not used with range()

for i in range(0, 50, 10):
    print(i)