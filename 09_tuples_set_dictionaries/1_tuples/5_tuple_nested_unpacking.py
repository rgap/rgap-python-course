# Nested Tuple Unpacking

nested_tuple = ((1, 2), (3, 4), (5, 6))

# Unpacking nested tuples
(first_a, first_b), (second_a, second_b), (third_a, third_b) = nested_tuple
print(f"First pair: {first_a}, {first_b}")  # Outputs: First pair: 1, 2
print(f"Second pair: {second_a}, {second_b}")  # Outputs: Second pair: 3, 4
print(f"Third pair: {third_a}, {third_b}")  # Outputs: Third pair: 5, 6
