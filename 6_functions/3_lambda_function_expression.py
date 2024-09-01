# Python Version: Python has supported function expressions (lambda) since its early versions.

# Function Expressions in Python (Lambda Functions)
# Lambda functions are small anonymous functions defined using the 'lambda' keyword.
# They are typically used for short operations that don't require a full function definition.

# Example: A simple lambda function for addition
add = lambda a, b: a + b

result = add(10, 5)
print(f"Lambda function result: {result}")  # Outputs: Lambda function result: 15

# Lambda functions are commonly used with higher-order functions like map(), filter(), and reduce().

# Lambda functions with map()
# The map() function applies a function to all items in an iterable (like a list).
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x**2, numbers))
# The lambda function here squares each element in the list 'numbers'.
print(f"Squared numbers: {squared_numbers}")  # Outputs: Squared numbers: [1, 4, 9, 16]

# Lambda functions with filter()
# The filter() function filters items in an iterable based on a condition.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# The lambda function here filters out the even numbers from the list 'numbers'.
print(f"Even numbers: {even_numbers}")  # Outputs: Even numbers: [2, 4]

# Lambda functions with reduce()
# The reduce() function applies a function cumulatively to the items of an iterable.
from functools import reduce

product = reduce(lambda x, y: x * y, numbers)
# The lambda function here multiplies all the numbers in the list together.
print(f"Product of numbers: {product}")  # Outputs: Product of numbers: 24

# Note: Lambda functions are useful for quick, one-off tasks that don't require a full function definition.
# However, they should be used judiciously, as they can make code less readable if overused.
# For more complex operations, traditional function definitions with 'def' are generally preferred.
