# This script corrects the commenting and docstring issues from comments_and_docstrings_incorrect.py
# by adding clear and appropriate docstrings and using inline comments sparingly.

def add_numbers(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of the two numbers.
    """
    return a + b


# Example usage
result = add_numbers(10, 20)
print(result)
