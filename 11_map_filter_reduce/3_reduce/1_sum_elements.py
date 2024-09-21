# Example: Using reduce to sum all elements in a list
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda x, y: x + y, numbers)
print(f"Sum of all elements: {total_sum}")
