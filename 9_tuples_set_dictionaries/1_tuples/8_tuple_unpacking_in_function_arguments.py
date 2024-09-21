# Tuple Unpacking in Function Arguments

def calculate_sum(a, b, c):
    return a + b + c


# Tuple to be unpacked
values = (1, 2, 3)

# Unpacking tuple into function arguments
result = calculate_sum(*values)
print(f"Sum: {result}")  # Outputs: Sum: 6
