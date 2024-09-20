# First-order functions are functions that do NOT take other functions as
# arguments or return functions.

def add(a, b):
    return a + b


# This function is a first-order function because it operates directly on
# its arguments without involving any other functions.
print(add(3, 4))  # Output: 7


# In contrast, the following function is not a first-order function because
# it takes another function as an argument.
def apply(func, a, b):
    return func(a, b)
