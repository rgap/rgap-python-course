# Combining *args and **kwargs in Function Definitions

def process_data(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"Additional positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")


# Calling the function with both positional and keyword arguments
process_data(1, 2, 3, 4, x=10, y=20)
# Outputs:
# a: 1, b: 2
# Additional positional arguments: (3, 4)
# Keyword arguments: {'x': 10, 'y': 20}

# Note: This function can handle both fixed arguments, additional positional arguments (*args),
# and keyword arguments (**kwargs) simultaneously.
