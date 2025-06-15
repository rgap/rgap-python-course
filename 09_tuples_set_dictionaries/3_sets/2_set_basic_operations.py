# Basic Set Operations: Membership and Length

# Example set
fruits_set = {"apple", "banana", "cherry"}

# Checking for membership
is_apple_in_set = "apple" in fruits_set
print(f"Is 'apple' in set: {is_apple_in_set}")  # Outputs: Is 'apple' in set: True

# Checking for non-membership
is_grape_in_set = "grape" not in fruits_set
print(f"Is 'grape' not in set: {is_grape_in_set}")  # Outputs: Is 'grape' not in set: True

# Getting the length of a set
set_length = len(fruits_set)
print(f"Number of elements in set: {set_length}")  # Outputs: Number of elements in set: 3
