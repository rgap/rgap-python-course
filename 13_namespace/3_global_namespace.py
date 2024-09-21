# The global namespace contains variables and functions defined at the top level of a module or script.
# This namespace is created when a module is loaded and remains in existence until the script ends.

x = "global variable"  # A variable in the global namespace.

def global_function():
    pass  # A function in the global namespace.

# The `dir()` function without arguments shows the global namespace.
print(dir())  # Lists all global variables and functions.
