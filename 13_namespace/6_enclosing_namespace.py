# The enclosing namespace exists when we have nested functions.
# It refers to the scope of an outer function that wraps an inner function.

def outer_function():
    outer_var = "outer variable"  # A variable in the enclosing (outer) namespace.

    def inner_function():
        # This is a local variable within the inner function, but it can access the outer variable.
        inner_var = "inner variable"
        print(dir())  # Lists local and enclosing variables (outer_var will be accessible here).

    inner_function()

outer_function()
