# Introduction to Lambda Functions

# Example 1: Lambda function with no parameters
# Lambdas can be defined without parameters, and they always return the same value.
# This is useful for creating simple, reusable functions for constant values.

no_param = lambda: "Hello, World!"
print(f"Message from no_param lambda: {no_param()}")

##########################################################

# Example 2: Lambda function with a single parameter
# Lambdas can take a single parameter, making them useful for quick transformations.
# Here, we define a lambda function to square a number.

square = lambda x: x ** 2
print(f"Square of 4 using lambda: {square(4)}")

##########################################################

# Example 3: Lambda function with multiple parameters
# Lambdas can take multiple parameters to perform operations on them.
# This example shows a lambda that multiplies two numbers.

multiply = lambda x, y: x * y
print(f"Result of multiplying 3 and 4 using lambda: {multiply(3, 4)}")

##########################################################

# Example 4: Lambda function returning multiple outputs
# Although lambdas are limited to a single expression, they can still return multiple
# values using tuples or lists. This makes them versatile even in simple scenarios.

multiple_outputs = lambda x: (x, x**2, x**3)
print(f"Multiple outputs from lambda: {multiple_outputs(2)}")
