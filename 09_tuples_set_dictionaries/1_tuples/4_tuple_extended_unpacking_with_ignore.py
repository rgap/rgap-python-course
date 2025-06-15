
# Extended Unpacking with Ignore (using *_)

numbers_tuple = (1, 2, 3, 4, 5)

# Extended unpacking with ignore - ignoring all elements between b and last
a, b, *_, last = numbers_tuple
print(f"a: {a}, b: {b}, last: {last}")  # Outputs: a: 1, b: 2, last: 5

# Note: *_ captures all intermediate elements, effectively ignoring them.
