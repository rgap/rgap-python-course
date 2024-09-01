# Python Version: Accessing elements in lists has been supported since Python 1.0 (January 1994).

# Accessing Elements in an Array (List)
# Elements in a list can be accessed by their index, with the first element at index 0.

# Example list
fruits = ["apple", "banana", "cherry"]

# Accessing the first element
first_fruit = fruits[0]
print(f"First fruit: {first_fruit}")  # Outputs: First fruit: apple

# Accessing the last element using negative indexing
last_fruit = fruits[-1]
print(f"Last fruit: {last_fruit}")  # Outputs: Last fruit: cherry

# Accessing a range of elements (slicing)
some_fruits = fruits[0:2]  # Gets elements from index 0 to 1 (2 is not included)
print(f"Some fruits: {some_fruits}")  # Outputs: Some fruits: ['apple', 'banana']

# Note: Python supports both positive and negative indexing. Negative indices count from the end of the list.
# Slicing allows you to access a subset of the list by specifying a start and stop index.
