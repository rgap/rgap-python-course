# Python Version: Python does not have "arrow functions" like JavaScript, but lambda functions serve a similar purpose.

# Python's Equivalent of Arrow Functions (Lambdas)
# Lambda functions in Python are used to create small, anonymous functions on the fly.
# They are particularly useful in contexts where a simple function is needed temporarily.

# Basic lambda function for addition
add = lambda x, y: x + y
print(f"Addition using lambda: {add(5, 10)}")  # Outputs: Addition using lambda: 15

# Lambda functions are often used with higher-order functions that operate on iterables.

# Example: Using lambda with sorted() to sort a list of tuples by the second element
points = [(1, 2), (3, 1), (5, 4)]
points_sorted = sorted(points, key=lambda point: point[1])
# The lambda function here returns the second element of each tuple for sorting.
print(
    f"Points sorted by second element: {points_sorted}"
)  # Outputs: Points sorted by second element: [(3, 1), (1, 2), (5, 4)]

# Lambda functions as a key in min() and max() functions
# Example: Finding the maximum number by treating it as a negative value
numbers = [4, 2, 9, 1]
max_number = max(numbers, key=lambda x: -x)
# The lambda function negates the numbers, effectively finding the smallest absolute value.
print(
    f"Maximum number using negation: {max_number}"
)  # Outputs: Maximum number using negation: 1

# Note: While Python's lambda functions are similar to JavaScript's arrow functions, they have some limitations.
# Lambdas in Python are restricted to a single expression and are typically used for short, simple tasks.
# For more complex operations, full function definitions are recommended for clarity and maintainability.
