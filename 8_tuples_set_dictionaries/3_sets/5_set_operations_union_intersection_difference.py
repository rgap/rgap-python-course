# Set Operations: Union, Intersection, and Difference

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: Elements in either set
union_set = set_a | set_b
print(f"Union: {union_set}")  # Outputs: Union: {1, 2, 3, 4, 5, 6}

# Intersection: Elements in both sets
intersection_set = set_a & set_b
print(f"Intersection: {intersection_set}")  # Outputs: Intersection: {3, 4}

# Difference: Elements in set_a but not in set_b
difference_set = set_a - set_b
print(f"Difference: {difference_set}")  # Outputs: Difference: {1, 2}

# Symmetric Difference: Elements in either set, but not in both
symmetric_difference_set = set_a ^ set_b
print(f"Symmetric Difference: {symmetric_difference_set}")  # Outputs: Symmetric Difference: {1, 2, 5, 6}
