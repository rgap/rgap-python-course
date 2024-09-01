# All Primitive and Built-In Data Types in Python
# Python Version: These types have been part of Python since version 1.0 (January 1994), with some additions in later versions.

# Python includes a variety of primitive and built-in types that are fundamental to the language.
# These include integers, floats, booleans, strings, complex numbers, NoneType, and other built-in collections.

# Integer (int): Whole numbers, both positive and negative
x = 10  # Integer
print(f"x is an integer: {x} (type: {type(x)})\n")

# Float (float): Numbers with a decimal point
y = 10.5  # Float
print(f"y is a float: {y} (type: {type(y)})\n")

# String (str): A sequence of characters
name = "Alice"  # String
print(f"name is a string: {name} (type: {type(name)})\n")

# Boolean (bool): Represents truth values: True or False
is_python_fun = True  # Boolean
print(f"is_python_fun is a boolean: {is_python_fun} (type: {type(is_python_fun)})\n")

# List (list): A mutable sequence of items
mutable_sequence = [1, 2, 3]  # List
print(
    f"mutable_sequence is a list: {mutable_sequence} (type: {type(mutable_sequence)})\n"
)

# Tuple (tuple): An immutable sequence of items
immutable_sequence = (1, 2, 3)  # Tuple
print(
    f"immutable_sequence is a tuple: {immutable_sequence} (type: {type(immutable_sequence)})\n"
)

# Dictionary (dict): A mutable collection of key-value pairs
key_value_pairs = {"key": "value"}  # Dictionary
print(f"key_value_pairs is a dict: {key_value_pairs} (type: {type(key_value_pairs)})\n")

# Set (set): A mutable, unordered collection of unique items
unique_items = {1, 2, 3}  # Set
print(f"unique_items is a set: {unique_items} (type: {type(unique_items)})\n")

# Bytes (bytes): An immutable sequence of bytes
byte_data = b"hello"  # Bytes
print(f"byte_data is bytes: {byte_data} (type: {type(byte_data)})\n")

# Bytearray (bytearray): A mutable sequence of bytes
mutable_byte_data = bytearray(b"hello")  # Bytearray
print(
    f"mutable_byte_data is bytearray: {mutable_byte_data} (type: {type(mutable_byte_data)})\n"
)

# NoneType (None): Represents the absence of a value or a null value
nothing = None  # NoneType
print(f"nothing is NoneType: {nothing} (type: {type(nothing)})\n")

# Range (range): Represents an immutable sequence of numbers, typically used in loops
num_range = range(0, 10)  # Range
print(f"num_range is range: {list(num_range)} (type: {type(num_range)})\n")

# Frozenset (frozenset): An immutable set
immutable_set = frozenset([1, 2, 3])  # Frozenset
print(f"immutable_set is frozenset: {immutable_set} (type: {type(immutable_set)})\n")

# Complex (complex): Numbers with a real and an imaginary part
z = 3 + 4j  # Complex number
print(f"z is a complex number: {z} (type: {type(z)})\n")

# Memoryview (memoryview): Allows viewing the memory of other binary objects without copying
memory_view = memoryview(b"hello")  # Memoryview
print(f"memory_view is memoryview: {memory_view} (type: {type(memory_view)})\n")
