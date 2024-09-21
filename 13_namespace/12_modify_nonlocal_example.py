# The `nonlocal` keyword allows you to modify a variable in an enclosing (outer) function's scope,
# but it does not affect global variables. It's useful in nested functions.

def outer_function():
    x = "outer x"  # Variable in the enclosing scope.

    def inner_function():
        nonlocal x  # Refers to the 'x' in the enclosing (outer) function's scope.
        x = "modified outer x"  # Modify the enclosing 'x'.
        print("Inner:", x)  # Outputs 'modified outer x'.

    inner_function()
    print("Outer:", x)  # Outputs 'modified outer x' because the inner function changed it.

outer_function()
