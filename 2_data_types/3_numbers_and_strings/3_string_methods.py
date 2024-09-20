# Common String Methods in Python
# Python Version: String methods have been enhanced over time, with many useful methods being part of Python since version 1.0.

# Python provides a wide range of methods to manipulate and analyze strings.

text = "Hello, Python!"

# Converting to uppercase
uppercase_text = text.upper()
print(f"Uppercase: {uppercase_text}")  # Outputs: HELLO, PYTHON!

# Converting to lowercase
lowercase_text = text.lower()
print(f"Lowercase: {lowercase_text}")  # Outputs: hello, python!

# Splitting into a list of words
words = text.split()  # Default split is by whitespace
print(f"Words: {words}")  # Outputs: ['Hello,', 'Python!']

# Finding a substring
position = text.find("Python")
print(f"Position of 'Python': {position}")  # Outputs: 7

# Replacing a substring
new_text = text.replace("Python", "World")
print(f"Replaced text: {new_text}")  # Outputs: Hello, World!

# Note: String methods in Python are numerous and allow for comprehensive string manipulation.
