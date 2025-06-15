# The `break` statement is used to exit the loop prematurely, stopping further iterations.
# When `break` is encountered inside a loop, the loop is immediately terminated.
# Syntax:
#     for <variable> in <iterable>:
#         if <condition>:
#             break
#         <code to execute>

# Example 1: Searching for a specific product and stopping when it's found
products = ["laptop", "tablet", "smartphone", "monitor"]
for product in products:
    if product == "smartphone":
        print(f"{product} found in stock!")
        break  # Stop once product is found
    print(f"Still checking: {product}")


###############################################


# Example 2: Looking for the first large number in a list
numbers = [10, 15, 25, 35, 50]
for num in numbers:
    if num > 30:
        print(f"Found a large number: {num}")
        break
    print(f"{num} is not large enough.")
