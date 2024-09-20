# Tuple Unpacking with *args in Function Definitions

def print_all(*args):
    # args is a tuple containing all the arguments passed to the function
    for arg in args:
        print(arg)


# Calling the function with multiple arguments
print_all(1, 2, 3, 4)
# Outputs:
# 1
# 2
# 3
# 4

# Calling the function with a single tuple argument
print_all((5, 6))
# Outputs:
# (5, 6)
