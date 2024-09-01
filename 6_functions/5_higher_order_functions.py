# Python Version: Higher-order functions have been a core part of Python since version 1.0.

# Higher-Order Functions in Python
# Higher-order functions either take other functions as arguments or return them as results.
# They enable more abstract, flexible, and reusable code by treating functions as first-class objects.


# Example: A function that takes another function as an argument
def apply_operation(func, x, y):
    # This higher-order function applies the passed 'func' to 'x' and 'y'.
    return func(x, y)


# Using apply_operation with a lambda function
result = apply_operation(lambda a, b: a * b, 10, 3)
print(f"Result of apply_operation: {result}")  # Outputs: Result of apply_operation: 30


# Example: A function that returns another function
def create_multiplier(n):
    # This higher-order function returns a lambda that multiplies its input by 'n'.
    return lambda x: x * n


# Using create_multiplier to create a doubling function
doubler = create_multiplier(2)
print(
    f"Doubling 5 using doubler: {doubler(5)}"
)  # Outputs: Doubling 5 using doubler: 10

# Built-in higher-order functions: map(), filter(), reduce()

# map() applies a function to all elements in an iterable
numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers))
# The lambda function here doubles each element in the list 'numbers'.
print(
    f"Doubled numbers using map: {doubled}"
)  # Outputs: Doubled numbers using map: [2, 4, 6]

# filter() filters elements based on a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(
    f"Even numbers using filter: {even_numbers}"
)  # Outputs: Even numbers using filter: [2]

# reduce() applies a function cumulatively to the items of an iterable, from left to right
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
print(
    f"Product of numbers using reduce: {product}"
)  # Outputs: Product of numbers using reduce: 6

# Note: Higher-order functions are powerful tools that enable functional programming techniques in Python.
# They allow you to write more abstract, reusable code by treating functions as first-class objects,
# which can be passed around and composed in various ways.
# Understanding higher-order functions is key to leveraging Python's full functional programming capabilities.
