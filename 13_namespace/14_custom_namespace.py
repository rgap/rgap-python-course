# Python's `types.SimpleNamespace` allows you to create a simple object with dynamic attributes.
# This can be used to simulate a custom namespace for organizing related data.

from types import SimpleNamespace

# Create a custom namespace to hold related data.
custom_ns = SimpleNamespace()
custom_ns.name = "Alice"
custom_ns.age = 30

# Accessing and modifying attributes in the custom namespace.
print("Name:", custom_ns.name)  # Outputs 'Alice'.
print("Age:", custom_ns.age)    # Outputs 30.

# Modify attributes dynamically.
custom_ns.age = 31
print("Updated Age:", custom_ns.age)  # Outputs 31.

# Adding new attributes dynamically.
custom_ns.occupation = "Engineer"
print("Occupation:", custom_ns.occupation)  # Outputs 'Engineer'.
