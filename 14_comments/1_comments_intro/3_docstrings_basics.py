# This function adds two numbers together and returns the result.
# The function has a docstring that provides the following details:

# 1. A brief description of what the function does.
#    In this case, it mentions that the function adds two numbers together.

# 2. The 'Parameters' section:
#    - It lists each parameter the function takes, along with a brief description and its expected type.
#    - Here, 'a' and 'b' are the parameters, both expected to be integers.

# 3. The 'Returns' section:
#    - This part describes the type and purpose of the value that the function returns.
#    - In this function, the return value is an integer that represents the sum of 'a' and 'b'.

# 4. Additional Notes:
#    - The docstring might include extra information about the function's behavior.
#    - For example, it could mention if the function does not perform any error checking on the inputs.


def add(a, b):
    """
    Adds two numbers together and returns the result.

    Parameters:
    a (int): The first number to add.
    b (int): The second number to add.

    Returns:
    int: The sum of the two numbers.

    This function simply adds the two inputs without any error checking.
    """
    return a + b


# Example usage: add 2 and 3, and print the result (should be 5)
print(add(2, 3))
