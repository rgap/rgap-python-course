# Tuple Creation and Basic Unpacking

# Creating a simple tuple
numbers_tuple = (1, 2, 3)
print(f"Numbers tuple: {numbers_tuple}")  # Outputs: Numbers tuple: (1, 2, 3)

# Basic unpacking
a, b, c = numbers_tuple
print(f"a: {a}, b: {b}, c: {c}")  # Outputs: a: 1, b: 2, c: 3

# Unpacking with Mismatched Elements
# Uncommenting the following line will raise a ValueError
# a, b = numbers_tuple  # ValueError: too many values to unpack (expected 2)
