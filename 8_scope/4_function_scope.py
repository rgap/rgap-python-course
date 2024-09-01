# Python Version: Function scope has been supported since Python 1.0 (January 1994).

# Function Scope in Python
# Variables defined inside a function are in the local scope and can only be accessed within that function.


def my_function():
    local_var = "I am a local variable"
    print(local_var)


my_function()  # Outputs: I am a local variable

# Attempting to access a local variable outside its function will result in an error
# print(local_var)  # Uncommenting this line will cause an error: NameError: name 'local_var' is not defined

# Note: Function scope ensures that variables defined within a function are isolated from the rest of the code.
# This isolation prevents unintended interactions between different parts of the program.
# Local variables are destroyed once the function execution is complete, freeing up memory.
