# For Loops in Python
# Python Version: The for loop has been part of Python since version 1.0 (January 1994).

# The for loop is used to iterate over a sequence (such as a list, tuple, string, or range).
# It is one of the most common control structures in Python, enabling iteration through elements of a collection.

# Example: Iterating over a list
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(f"Number: {number}")  # Outputs each number in the list

# Example: Iterating over a string
for char in "Python":
    print(f"Character: {char}")  # Outputs each character in the string

# Using the range() function with for loops
# The range() function generates a sequence of numbers.
for i in range(5):  # Iterates from 0 to 4 (5 is not included)
    print(f"Index: {i}")

# Using for loop with enumerate() to get index and value
for index, value in enumerate(numbers):
    print(f"Index {index}: Value {value}")

# Nested for loops
# You can nest for loops to iterate over multiple dimensions, such as in a matrix.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(f"Item: {item}")  # Outputs each item in the matrix

# Note: For loops in Python are powerful and flexible, supporting iteration over any iterable object.
