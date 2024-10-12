# Dictionary of Lists :
# We can store lists as values in a dictionary, which is useful for grouping similar data.

classes = {
    "math": ["Alice", "Bob", "Charlie"],
    "science": ["David", "Eve", "Frank"],
    "history": ["Grace", "Heidi", "Ivan"]
}

# Add a student to the math class
classes["math"].append("John")
print(classes["math"])  # Output: ['Alice', 'Bob', 'Charlie', 'John']
