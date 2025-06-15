# Introduction to different methods of string formatting in Python
# Historical Context:
# - Old-style formatting with '%' has been part of Python since early versions (Python 1.x).
# - The str.format() method was introduced in Python 2.7 (July 2010) and Python 3.0 (December 2008).
# - f-strings were introduced in Python 3.6 (December 2016).


# 1. Old-style string formatting using the '%' operator

# This method is similar to the printf-style formatting in C.
# '%s' is used as a placeholder for strings, and '%d' is used for integers.
name = "Alice"
age = 30
print(
    "Hello, %s. You are %d years old." % (name, age)
)  # Outputs: Hello, Alice. You are 30 years old.

# 2. The 'str.format()' method

# This method is more powerful and flexible than the '%' operator.
# It uses curly braces {} as placeholders, which are replaced by the arguments passed to the format() method.
print(
    "Hello, {}. You are {} years old.".format(name, age)
)  # Outputs: Hello, Alice. You are 30 years old.

# 3. f-strings (formatted string literals)

# F-strings provide a concise and readable way to embed expressions inside string literals.
# You prefix the string with an 'f' and place expressions in curly braces {}.
# F-strings are evaluated at runtime and can include any valid Python expression.
print(
    f"Hello, {name}. You are {age} years old."
)  # Outputs: Hello, Alice. You are 30 years old.

# Note: F-strings are preferred in modern Python code for their readability and efficiency.
