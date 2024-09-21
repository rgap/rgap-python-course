# Example: Using reduce to concatenate a list of strings
from functools import reduce

strings = ["apple", "banana", "cherry"]
concatenated_string = reduce(lambda x, y: x + y, strings)
print(f"Concatenated string: {concatenated_string}")
