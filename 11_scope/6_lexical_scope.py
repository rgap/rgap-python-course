# Python Version: Lexical scope (or static scope) has been a part of Python since version 1.0 (January 1994).

# Lexical Scope in Python
# Lexical scope means that the scope of a variable is determined by its location in the source code.
# In Python, functions create a new scope, but they can access variables from their containing scope.


def outer_function():
    outer_var = "I am outside"

    def inner_function():
        # Inner function can access the outer function's variable due to lexical scope
        print(outer_var)

    inner_function()


outer_function()  # Outputs: I am outside

# Attempting to access inner function's variable from the outer function will result in an error
# print(inner_var)  # Uncommenting this line will cause an error: NameError: name 'inner_var' is not defined

# Note: Lexical scope allows inner functions to access variables from their enclosing functions.
# This concept is foundational for understanding closures in Python, where inner functions retain access to the outer function's variables even after the outer function has finished executing.
