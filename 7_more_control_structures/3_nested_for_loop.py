# A `nested for loop` occurs when you place a `for` loop inside another `for` loop.
# This is useful for iterating over multiple iterables simultaneously or when you need to perform complex iterations.
# Syntax:
#     for <variable1> in <iterable1>:
#         for <variable2> in <iterable2>:
#             <code to execute>

# Example 1: Comparing two lists of products for common items
products_in_stock = ["laptop", "tablet", "monitor"]
requested_products = ["smartphone", "tablet", "laptop"]
for stock_product in products_in_stock:
    for requested_product in requested_products:
        if stock_product == requested_product:
            print(f"{requested_product} is available in stock.")


###############################################


# Example 2: Creating a list of combinations of two different iterables
# (e.g., colors and sizes)
colors = ["red", "blue", "green"]
sizes = ["small", "medium", "large"]
combinations = []
for color in colors:
    for size in sizes:
        combinations.append(f"{color} - {size}")
print("Available combinations:", combinations)
