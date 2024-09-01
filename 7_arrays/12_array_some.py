# Python Version: Checking if any elements meet a condition has been supported since Python 1.0 (January 1994).

# Checking if Some Elements in an Array (List) Meet a Condition
# Python allows you to check if any elements in a list meet a certain condition using a loop or comprehension.

# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Checking if any number is greater than 3 using a loop
any_greater_than_3 = any(x > 3 for x in numbers)
print(f"Any number greater than 3: {any_greater_than_3}")  # Outputs: Any number greater than 3: True

# Checking if all numbers are positive
all_positive = all(x > 0 for x in numbers)
print(f"All numbers are positive: {all_positive}")  # Outputs: All numbers are positive: True

# Note: The any() function returns True if at least one element meets the condition.
# The all() function returns True only if all elements meet the condition.
