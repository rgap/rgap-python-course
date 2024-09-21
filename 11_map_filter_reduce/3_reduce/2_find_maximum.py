# Example: Using reduce to find the maximum element in a list
from functools import reduce

numbers = [1, 2, 3, 4, 5]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum value: {max_value}")
