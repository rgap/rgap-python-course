# In this script, the `dir()` function is called without arguments, which lists all the names in the current (global) namespace.
# The global namespace contains variables, functions, and other objects defined at the top level of your script or module.

# Example of what's in the global namespace:
x = "global variable"  # A string variable defined at the top level.
def global_function():  # A function also defined at the top level.
    pass  # The function doesn't do anything.

# The following line lists all names defined globally in this script.
print(dir())  # Lists the names of all objects available in the current global namespace.


# The output:
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'global_function', 'x']

# Key items in the output:
# 1. `__annotations__`: A dictionary storing type annotations for variables or functions, if any are defined.
# 2. `__builtins__`: The built-in module containing all Python's built-in objects, similar to what is listed by `dir(__builtins__)`.
# 3. `__cached__`: The path to the compiled bytecode file (.pyc) of the module if it exists.
# 4. `__doc__`: The docstring of the current module, which is either `None` or the string if you’ve defined documentation for the module.
# 5. `__file__`: The path to the script or module file.
# 6. `__loader__`: The loader used to load the module.
# 7. `__name__`: The name of the module (usually `__main__` when you run the script directly).
# 8. `__package__`: The package name of the module, or `None` if it’s not part of a package.
# 9. `__spec__`: The import specification of the module.
# 10. `global_function`: The user-defined function `global_function` declared in the global namespace.
# 11. `x`: The variable `x` defined in the global namespace, holding the value "global variable".

# The `dir()` function, when used without arguments, shows these names that are present in the global namespace.