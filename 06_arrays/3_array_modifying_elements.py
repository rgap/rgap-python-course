# Python Version: Modifying elements in lists has been supported since Python 1.0 (January 1994).

# Modifying Elements in an Array (List)
# Lists in Python are mutable, meaning their elements can be changed after creation.

# Example list
colors = ["red", "green", "blue"]

# Modifying an element by index
colors[1] = "yellow"
print(
    f"Modified colors: {colors}"
)  # Outputs: Modified colors: ['red', 'yellow', 'blue']

# Modifying a range of elements (slicing)
colors[0:2] = ["purple", "orange"]
print(
    f"Modified colors with slicing: {colors}"
)  # Outputs: Modified colors with slicing: ['purple', 'orange', 'blue']

# Note: Since lists are mutable, you can directly change their elements using indexing.
# Slicing allows for bulk modification of several elements at once.
