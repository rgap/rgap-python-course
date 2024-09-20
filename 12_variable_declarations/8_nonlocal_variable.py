# Nonlocal variables
# Nonlocal variables allow you to assign values to variables in the nearest enclosing scope that is not global.

def outer_function():
    x = "local"

    def inner_function():
        nonlocal x
        x = "nonlocal"
        print(f"Inner function x: {x}")  # Outputs: Inner function x: nonlocal

    inner_function()
    print(f"Outer function x: {x}")  # Outputs: Outer function x: nonlocal

outer_function()
