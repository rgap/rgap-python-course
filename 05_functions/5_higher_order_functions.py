# Higher-order functions are functions that take other functions as
# arguments and/or return functions.

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


# The following function is a higher-order function because it takes
# another function as an argument.

def apply_operation(a, b, operation):
    # This function takes another function as an argument (operation)
    # and applies it to the given arguments a and b.
    return operation(a, b)


# Using the apply_operation function with different operations
result_add = apply_operation(3, 4, add)
print(result_add)  # Output: 7

result_multiply = apply_operation(5, 6, multiply)
print(result_multiply)  # Output: 30


###############################################


# Higher-order functions can also return other functions.
# Here's an example of a higher-order function that returns a function.

def create_multiplier(n):
    # This function returns a new function that multiplies its input by n.
    def multiplier(x):
        return x * n
    return multiplier


# Using the higher-order function to create new functions
double = create_multiplier(2)
triple = create_multiplier(3)

# The functions double and triple are created by the higher-order function
# create_multiplier and can be used independently.

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
