# Pure and Impure Functions in Python
# A pure function is one where the output depends only on its inputs and
# it has no side effects. Impure functions, however, can modify external
# states or produce side effects.


##########################################################


# Pure Function Example
# Pure functions always return the same result for the same input
# and do not modify any external state.

def pure_add(a, b):
    # This function adds two numbers and returns the result.
    # It does not modify any external state, making it a pure function.
    # Key point: For the same input values, the output will always be the same.
    return a + b


# Call the function
pure_result_1 = pure_add(5, 3)  # Outputs: 8
pure_result_2 = pure_add(5, 3)  # Outputs: 8

# Since the function is pure, pure_result_1 and pure_result_2 will always be the same.
print(f"Pure Function Result 1: {pure_result_1}")  # Outputs: Pure Function Result 1: 8
print(f"Pure Function Result 2: {pure_result_2}")  # Outputs: Pure Function Result 2: 8

# Advantages of Pure Functions:
# - Predictability: Always produce the same output for the same input, making them reliable and easy to understand.
# - No Side Effects: Do not alter external state, making them safer and easier to test.
# - Easier to Parallelize: Can be more easily parallelized or optimized due to their lack of side effects.

# Disadvantages of Pure Functions:
# - Limited Use: Cannot perform actions that require side effects (e.g., logging, database updates).
# - May Require Additional Code: Avoiding side effects may lead to more complex code.
