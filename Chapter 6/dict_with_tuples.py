# Dictionary with Tuple Keys
# A dictionary where the keys are tuples, which is useful for storing multi-dimensional data.

coordinates = {
    (0, 0): "Origin",
    (1, 2): "Point A",
    (3, 5): "Point B"
}

# Access value using tuple as key
print(coordinates[(1, 2)])  # Output: Point A
