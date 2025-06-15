# Frozenset: An Immutable Set

# Creating a frozenset
immutable_set = frozenset([1, 2, 3, 3, 4])
print(f"Immutable set: {immutable_set}")  # Outputs: Immutable set: frozenset({1, 2, 3, 4})

# Using a frozenset as a dictionary key (since it is immutable)
my_dict = {frozenset([1, 2, 3]): "first"}
print(f"Dictionary with frozenset key: {my_dict}")  # Outputs: Dictionary with frozenset key: {frozenset({1, 2, 3}): 'first'}

# Note: Frozensets are like sets but immutable, meaning their elements cannot be modified after creation.
