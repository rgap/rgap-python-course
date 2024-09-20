# Tuple Unpacking in Loops

pairs = [(1, 2), (3, 4), (5, 6)]

# Unpacking in a for loop
for a, b in pairs:
    print(f"a: {a}, b: {b}")  # Outputs: a: 1, b: 2 (and so on for each pair)

# Nested Unpacking in Loops
nested_pairs = [((1, 2), (3, 4)), ((5, 6), (7, 8))]
for (a, b), (c, d) in nested_pairs:
    # Outputs: a: 1, b: 2, c: 3, d: 4 (and so on)
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
