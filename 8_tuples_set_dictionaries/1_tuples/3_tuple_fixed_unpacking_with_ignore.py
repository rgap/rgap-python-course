# Fixed Unpacking with Ignore (using _)

numbers_tuple = (1, 2, 3, 4)

# Fixed unpacking with ignore - ignoring the third element
a, b, _, d = numbers_tuple
print(f"a: {a}, b: {b}, d: {d}")  # Outputs: a: 1, b: 2, d: 4

# Note: Only a single element (in this case, the third) is ignored.
