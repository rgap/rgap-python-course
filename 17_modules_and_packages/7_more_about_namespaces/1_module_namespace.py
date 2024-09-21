# When you import a module in Python, it creates a namespace for the module.
# Variables, functions, and classes in the module are stored in that module's namespace.

# Let's import the math module and inspect its namespace.
import math

# The `dir()` function can be used to list all the names in the math module's namespace.
print("Math module namespace:", dir(math))

# Accessing specific attributes in the module's namespace.
print("Accessing math.pi:", math.pi)  # Accesses the value of pi in the math module.

# Defining a function that shadows an imported function.
def sqrt(x):
    return "This shadows math.sqrt"

print("Shadowing example:", sqrt(16))  # Outputs the local sqrt function.

# Use the module's sqrt function explicitly.
print("Using math.sqrt:", math.sqrt(16))  # Outputs the actual square root calculation.
