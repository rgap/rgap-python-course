# Python Version: reduce() function has been available since Python 2.0 (October 2000), initially in the built-in namespace and moved to functools in Python 3.0.

# Counting or Reducing Elements in an Array (List) with reduce()
# The reduce() function applies a rolling computation to sequential pairs of elements in a list.

from functools import reduce

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce() to sum all elements
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(f"Sum of numbers: {sum_of_numbers}")  # Outputs: Sum of numbers: 15

# Using reduce() to find the product of all elements
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print(f"Product of numbers: {product_of_numbers}")  # Outputs: Product of numbers: 120

# Note: The reduce() function is powerful for performing cumulative operations on lists.
# It is commonly used for summing, multiplying, or otherwise combining all elements of a list.
