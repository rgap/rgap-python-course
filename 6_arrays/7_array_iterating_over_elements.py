# Python Version: Iterating over lists has been supported since Python 1.0 (January 1994).

# Iterating Over Elements in an Array (List)
# Python allows you to iterate over the elements of a list using a for loop.

# Example list
colors = ["red", "green", "blue"]

# 1. Iterating using a for loop
# This is the most straightforward way to iterate over the elements of a list.
for color in colors:
    print(f"Color: {color}")  # Outputs: Color: red, Color: green, Color: blue

# 2. Iterating with index using enumerate()
# The enumerate() function adds a counter to the iteration, allowing you to access both the index and the value.
for index, color in enumerate(colors):
    print(
        f"Index {index}: {color}"
    )  # Outputs: Index 0: red, Index 1: green, Index 2: blue

# Note: Python's for loop is a powerful tool for iterating over lists.
# The enumerate() function adds a counter to the iteration, allowing you to access both the index and the value.

# 3. Iterating Using a `while` Loop (Less Common)
# A `while` loop can be used to iterate over a list if you need more control over the loop's flow.
index = 0
while index < len(colors):
    print(f"Index {index}: {colors[index]}")
    index += 1  # Outputs: Index 0: red, Index 1: green, Index 2: blue

# 4. Iterating Over Multiple Lists Simultaneously with `zip()`
# `zip()` pairs elements from each list together, allowing parallel iteration.
shades = ["light", "dark", "medium"]
for color, shade in zip(colors, shades):
    print(
        f"{shade.capitalize()} {color}"
    )  # Outputs: Light red, Dark green, Medium blue

# 5. Iterating in Reverse Order Using `reversed()`
# The `reversed()` function allows you to iterate over the list in reverse order.
for color in reversed(colors):
    print(f"Color: {color}")  # Outputs: Color: blue, Color: green, Color: red
