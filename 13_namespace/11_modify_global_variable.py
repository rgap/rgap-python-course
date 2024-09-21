# In Python, the `global` keyword allows you to modify a global variable inside a function.
# Without the `global` keyword, any assignment to a variable inside a function creates a local variable by default.

x = "global x"  # Global variable.

def modify_global():
    global x  # Declare that we want to modify the global 'x'.
    x = "modified global x"  # Modify the global variable.
    print(x)  # Outputs 'modified global x'.

modify_global()
print(x)  # Outputs 'modified global x', showing that the global variable has been changed.
