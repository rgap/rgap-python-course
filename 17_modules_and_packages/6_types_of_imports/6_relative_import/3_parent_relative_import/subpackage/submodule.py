# submodule.py

# Relative import from the parent directory's module_a.py
from ..module_a import greet_a


# A function that combines a message from Module A and Submodule.
def greet_combined():
    return f"{greet_a()} and Hello from the Submodule!"
