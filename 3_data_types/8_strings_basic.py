# Basic String Operations in Python
# Python Version: Strings have been part of Python since version 1.0, and have evolved with enhancements like Unicode support in Python 3.0 (December 2008).

# Strings in Python are sequences of characters used to store text.

# Concatenation
str1 = "Hello"
str2 = "World"
combined_str = str1 + " " + str2  # Combining strings using the '+' operator
print(combined_str)  # Outputs: Hello World

# Repetition
repeat_str = "Python! " * 3  # Repeating strings using the '*' operator
print(repeat_str)  # Outputs: Python! Python! Python!

# Accessing characters
first_char = str1[0]  # Strings are indexed starting from 0
print(f"First character of str1: {first_char}")  # Outputs: H

# Slicing
slice_str = str1[1:4]  # Slicing a substring from the string
print(f"Sliced substring: {slice_str}")  # Outputs: ell

# Note: Python strings are immutable, meaning they cannot be changed after they are created.
