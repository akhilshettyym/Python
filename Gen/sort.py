# Function to implement bubble sort
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted, so ignore them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Input: Array elements
array = [64, 34, 25, 12, 22, 11, 90]

# Display original array
print("Original array:", array)

# Sorting the array
bubble_sort(array)

# Display sorted array
print("Sorted array:", array)