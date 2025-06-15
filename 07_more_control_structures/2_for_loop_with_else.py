# A `for` loop can optionally include an `else` block.
# The `else` block will execute after the loop completes, unless the loop is terminated with a `break`.
# Syntax:
#     for <variable> in <iterable>:
#         <code>
#     else:
#         <code to execute if loop completes without break>

# Example 1: Checking for the availability of a product in a list
products = ["laptop", "tablet", "smartphone", "monitor"]
for product in products:
    print(f"Checking {product} availability...")
else:
    print("All products are checked.")


###############################################


# Example 2: Stopping the search once a specific product is found
search_item = "tablet"
for product in products:
    if product == search_item:
        print(f"{search_item} found!")
        break  # Stop searching when item is found
else:
    print(f"{search_item} not found.")
