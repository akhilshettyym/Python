marks = {
    "Akhil" : 100,
    "Lochan" : 85,
    "Atin" : 85,
    "Lipika" : 90,
    0 : "AKH"
}


print(marks.keys())                     # Returns a list containing dictionary's keys.
marks.update({"Akhil" : 99})     # Updates the dictionary with supplied key-value pairs.
marks.update({"Lishika" : 95}) 
print(marks.get("Akhil"))
print(marks["Akhil"])   # Returns the value of the specified keys (and value is returned eg."harry" is returned here).
print(marks.keys())

print(marks.items())    # Returns a list of (key,value)tuples.


# print(marks["Akhil5"])     # This will return error.
# print(marks.get("Akhil5")) # This will return NONE.

student = {
    "name": "Akhil",
    "age": 21,
    "course": "Computer Science",
    "marks": [88, 100, 92]
}
print(student)


# Dictionary with Different Data Types
# Dictionaries can contain different data types, such as integers, lists, and even other dictionaries.
employee = {
    "name": "John Doe",
    "age": 30,
    "department": "HR",
    "skills": ["communication", "management"],
    "salary": 50000,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "postal_code": "10001"
    }
}
print(employee)


# dict.clear()
# Removes all items from the dictionary.
my_dict = {"name": "Akhil", "age": 21, "course": "CS"}
my_dict.clear()
print(my_dict)  # Output: {}


# dict.copy()
# Returns a shallow copy of the dictionary.
a = {
    "name": "Akhil", 
    "age": 21
    }
b = a.copy()
print(b)  # Output: {'name': 'Akhil', 'age': 21}


# dict.pop(key, default=None)
# Removes the key and returns the corresponding value. If the key is not found, it returns the default value (or raises a KeyError if no default is provided).
a = {"name": "Akhil", "age": 21}
age = a.pop("age")
print(age)  # Output: 21
print(a)  # Output: {'name': 'Akhil'}


# dict.popitem()
# Removes and returns the last key-value pair inserted in the dictionary as a tuple. Raises a KeyError if the dictionary is empty.
a = {
    "name": "Akhil", 
    "age": 21
    }
b = a.popitem()
print(b)  # Output: ('age', 21)
print(a)  # Output: {'name': 'Akhil'}