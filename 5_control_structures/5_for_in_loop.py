# For-In Loop in Python
# Python Version: The for-in loop has been part of Python since version 1.0 (January 1994).

# The for-in loop is used to iterate over the items of a collection (like a list, tuple, or dictionary).

# Example: Iterating over a dictionary's keys
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

for key in my_dict:
    print(
        f"Key: {key}, Value: {my_dict[key]}"
    )  # Outputs each key-value pair in the dictionary

# Example: Iterating over a range of numbers
for i in range(1, 6):  # range(start, stop) generates numbers from start to stop-1
    print(f"Number: {i}")

# Iterating over a list with the for-in loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"Fruit: {fruit}")  # Outputs each fruit in the list

# Using for-in loop with tuples
coordinates = [(0, 0), (1, 2), (3, 4)]

for x, y in coordinates:
    print(f"X: {x}, Y: {y}")  # Outputs each coordinate pair

# Note: The for-in loop is a versatile tool in Python, allowing iteration over a wide range of collections and iterable objects.
