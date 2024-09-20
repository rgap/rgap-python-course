# In Python, lambda functions are restricted to a single expression,
# which means that traditional multi-line 'for' loops cannot be directly used.
# However, you can use list comprehensions or generator expressions
# within lambda functions to achieve similar behavior.

# Example 1: Filter even numbers using a lambda function with list comprehension
# List comprehensions provide a way to include loops within lambda expressions.
# Here, we filter even numbers from a list.

filter_evens = lambda lst: [x for x in lst if x % 2 == 0]
print(f"Even numbers in [1, 2, 3, 4, 5, 6]: {filter_evens([1, 2, 3, 4, 5, 6])}")

##########################################################

# Example 2: Create a list of squares
# Similarly, list comprehensions can be used to transform a list within a lambda.
# This lambda generates the square of each number in a list.

square_numbers = lambda lst: [x**2 for x in lst]
print(f"Squares of [1, 2, 3, 4]: {square_numbers([1, 2, 3, 4])}")
