# Tuple Unpacking with **kwargs in Function Definitions

def print_details(**kwargs):
    # kwargs is a dictionary containing all keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Calling the function with keyword arguments
print_details(name="Alice", age=30, profession="Engineer")
# Outputs:
# name: Alice
# age: 30
# profession: Engineer

# Note: The **kwargs syntax allows the function to accept an arbitrary
# number of keyword arguments.
