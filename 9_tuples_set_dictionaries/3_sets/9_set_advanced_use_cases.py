# Advanced Set Operations and Use Cases

# Set Membership Testing with Subsets
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

# Checking if set_a is a subset of set_b
is_subset = set_a.issubset(set_b)
print(f"Is set_a a subset of set_b? {is_subset}")  # Outputs: Is set_a a subset of set_b? True

# Checking if set_b is a superset of set_a
is_superset = set_b.issuperset(set_a)
print(f"Is set_b a superset of set_a? {is_superset}")  # Outputs: Is set_b a superset of set_a? True

# Disjoint Sets: No common elements
set_c = {6, 7, 8}
are_disjoint = set_a.isdisjoint(set_c)
print(f"Are set_a and set_c disjoint? {are_disjoint}")  # Outputs: Are set_a and set_c disjoint? True
