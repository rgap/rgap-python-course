# Python Version: Combining and slicing lists has been supported since Python 1.0 (January 1994).

# Combining and Slicing Arrays (Lists)
# Python allows you to combine and slice lists easily.

# Example lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Combining lists using concatenation (+)
combined_list = list1 + list2
print(f"Combined list: {combined_list}")  # Outputs: Combined list: [1, 2, 3, 4, 5, 6]

# Slicing a list to get a subset
subset_list = combined_list[2:5]  # Gets elements from index 2 to 4 (5 is not included)
print(f"Sliced list: {subset_list}")  # Outputs: Sliced list: [3, 4, 5]

# Note: The + operator concatenates two lists.
# Slicing allows you to extract a portion of the list by specifying a start and stop index.
