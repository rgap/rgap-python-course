# Immutability in Python
# Python Version: Immutability of certain data types has been inherent since Python's early versions.

# In Python, some data types are immutable, meaning their values cannot be changed after they are created.
# The most common immutable types are integers, floats, strings, and tuples.

# Integer example
a = 10
print(f"Original value of a: {a}")

# Attempting to modify the integer (actually creates a new object)
a = a + 5
print(f"New value of a: {a}")
# Here, a new integer object is created and 'a' is reassigned to this new object.

# String example
greeting = "Hello"
print(f"Original greeting: {greeting}")

# Strings are immutable, so any modification creates a new string
greeting += ", World!"
print(f"Modified greeting: {greeting}")

# Tuple example
my_tuple = (1, 2, 3)
print(f"Original tuple: {my_tuple}")

# Attempting to modify a tuple results in an error
# Uncommenting the line below will raise a TypeError
# my_tuple[0] = 4  # TypeError: 'tuple' object does not support item assignment

# Note: Immutability helps ensure the integrity of data, making it easier to reason about code behavior.
