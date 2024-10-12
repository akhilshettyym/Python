#  Dictionary with Nested Dictionaries
# A more complex example where each key in the outer dictionary contains a nested dictionary.

company = {
    "Employee1": {
        "name": "Alice",
        "position": "Manager",
        "salary": 90000
    },
    "Employee2": {
        "name": "Bob",
        "position": "Developer",
        "salary": 75000
    },
    "Employee3": {
        "name": "Charlie",
        "position": "Designer",
        "salary": 70000
    }
}

# Access Employee2's salary
print(company["Employee2"]["salary"])  # Output: 75000