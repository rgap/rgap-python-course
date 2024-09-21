# The local namespace exists within functions or methods.
# Variables defined inside a function are part of the local namespace.
# This namespace is created when the function is called and is destroyed when the function finishes.

def my_local_function():
    local_var = "local variable"  # A local variable inside the function.
    
    # Using `dir()` inside the function lists all local names.
    print(dir())  # Lists local variables in this function.

my_local_function()
