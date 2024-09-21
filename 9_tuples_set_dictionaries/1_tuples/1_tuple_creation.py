# Python Version: Tuples have been a part of Python since version 1.0
# (January 1994).

# Tuple Creation in Python
# Tuples are immutable sequences, typically used to store collections of
# heterogeneous data.

# Creating a simple tuple
numbers_tuple = (1, 2, 3, 4, 5)
# Outputs: Numbers tuple: (1, 2, 3, 4, 5)
print(f"Numbers tuple: {numbers_tuple}")

# Tuples can contain different data types
mixed_tuple = (1, "two", 3.0, True)
# Outputs: Mixed tuple: (1, 'two', 3.0, True)
print(f"Mixed tuple: {mixed_tuple}")

# Creating a tuple without parentheses
implicit_tuple = 1, 2, 3
# Outputs: Implicit tuple: (1, 2, 3)
print(f"Implicit tuple: {implicit_tuple}")

# Creating a tuple using the tuple() function
tuple_from_list = tuple([1, 2, 3, 4])
# Outputs: Tuple from list using tuple(): (1, 2, 3, 4)
print(f"Tuple from list using tuple(): {tuple_from_list}")

# Note: Tuples are immutable, meaning their elements cannot be changed
# after creation.
