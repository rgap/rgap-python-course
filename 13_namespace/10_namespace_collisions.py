# Namespace collisions occur when a variable in one scope has the same name as a variable in another scope.
# Python resolves these collisions based on the LEGB rule (Local, Enclosing, Global, Built-in).

x = "global x"  # Global variable.

def outer_function():
    x = "enclosing x"  # Enclosing variable (shadows the global variable within this function).

    def inner_function():
        x = "local x"  # Local variable (shadows the enclosing variable).
        print("Inner function:", x)  # Prints the local 'x': 'local x'.

    inner_function()
    print("Outer function:", x)  # Prints the enclosing 'x': 'enclosing x'.

outer_function()
print("Global scope:", x)  # Prints the global 'x': 'global x'.
