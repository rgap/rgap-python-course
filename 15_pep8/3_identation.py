# ===============================
# MAXIMUM LINE LENGTH AND LINE BREAKING
# ===============================

# PEP 8 recommends keeping lines to a maximum length of 79 characters.
# When a line exceeds this limit, use line breaks to maintain readability.
# It also recommends breaking lines before binary operators to enhance readability.

# ===============================
# IMPORTS
# ===============================

# When importing multiple items from a module, it’s recommended to use
# parentheses to clearly show the list of imports and keep lines under 79 characters.

from turtle import (
    Turtle,
    color,
    shape
)

# ===============================
# FUNCTION DEFINITIONS
# ===============================

# Function definitions with many arguments should break across multiple lines.
# Align arguments under the first argument or use a hanging indent.

def long_function(argument_one, argument_two,
                  argument_one_three, argument_four):
    return argument_one

# Alternative method using a hanging indent:
def long_function_two(argument_one,
                      argument_two,
                      argument_one_three,
                      argument_four):
    return argument_one


# ===============================
# FUNCTION CALLS
# ===============================

# Recommended way to call a function when arguments exceed the line length limit:
result_1 = long_function(arg_one, arg_two,
                         arg_three, arg_four)

# Another recommended approach is to place each argument on a new line:
result_2 = long_function(
    arg_one, arg_two, arg_three, arg_four
)

# Not Recommended: Arguments should not be broken across multiple lines 
# with inconsistent indentation, as it decreases readability.
result_3 = long_function(arg_one, arg_two,
                         arg_three, arg_four)


# ===============================
# BINARY OPERATORS
# ===============================

# PEP 8 recommends breaking lines before binary operators to keep lines 
# under the maximum length and maintain readability.

first_variable, second_variable, third_variable = (1, 2, 3)
total = (first_variable
         + second_variable
         - third_variable)


# ===============================
# LISTS
# ===============================

# Lists with many items should also be broken across multiple lines for readability.
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]


# ===============================
# LONG STRINGS
# ===============================

# For long strings, especially those used for comments or documentation,
# consider using triple-quoted strings. This allows for multi-line strings
# that can be broken across multiple lines without needing backslashes.

long_string = """
Use block comments to document a small section of code.
They are useful when you have to write several lines of
code to perform a single action, such as importing data
from a file or updating a database entry. They are important
as they help others understand the purpose and functionality
of a given code block.

PEP 8 provides the following rules for writing block comments:

    Indent block comments to the same level as the code they describe.
    Start each line with a # followed by a single space.
    Separate paragraphs by a line containing a single #.
"""