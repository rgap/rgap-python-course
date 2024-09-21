# Using `from <module> import *` imports all the names from a module into the global namespace.
# This can lead to namespace collisions and is generally discouraged in large programs.

# Import everything from the math module into the global namespace.
from math import *

# Now all functions and variables from math are part of the global namespace.
print("Accessing math.pi:", pi)  # No need to use 'math.' prefix.

# Defining a function that shadows the imported `sqrt` function.
def sqrt(x):
    return "This shadows the imported sqrt"

print("Shadowing example:", sqrt(16))  # Outputs the local sqrt function, shadowing math.sqrt.

# If we need the original sqrt, it's harder to access now since it was imported directly.
# We lose clarity by importing all names from the math module this way.
