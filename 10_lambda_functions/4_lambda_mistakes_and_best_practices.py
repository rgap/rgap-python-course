# Common Mistakes and Best Practices with Lambda Functions

# Mistake 1: Assuming lambda has an implicit return
# While lambdas do return the result of the expression, it's important to remember that this expression is the only thing they can return.

no_return = lambda x: x + 1
print(f"No return lambda with 4: {no_return(4)}")

##########################################################

# Mistake 2: Trying to use multi-line statements in a lambda
# Lambdas in Python can only contain one expression, so attempting to include multi-line logic will result in an error.

# Uncommenting the following code will raise a syntax error
# multi_line = lambda x: (y = x + 1; z = y + 2)

##########################################################

# Mistake 3: Using lambdas for complex logic
# Lambdas are best suited for simple operations. For complex logic or multi-step processes,
# it's better to define a regular function for clarity and maintainability.

# Handling exceptions in lambdas (best practice is to avoid complex logic)
safe_divide = lambda x, y: x / y if y != 0 else "Undefined"
print(f"Safe division: {safe_divide(10, 2)} and {safe_divide(10, 0)}")

##########################################################

# Best Practice: Use lambdas for simple, inline operations only.
# If your lambda function starts becoming too complex, it's a sign that you should use a regular function instead.
