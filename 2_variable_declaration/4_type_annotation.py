# Type Annotations in Python
# Python Version: Type annotations were introduced in Python 3.5 (September 2015) via PEP 484.
# This feature allows you to specify the expected data types of variables, function parameters, and return values.

# Type annotations DO NOT ENFORCE TYPES AT RUNTIME, but they help with code readability and can be used by static type checkers.


# Example of type annotations in function parameters and return type
def add_numbers(a: int, b: int) -> int:
    return a + b


result = add_numbers(10, 20)
print(
    f"The result of adding 10 and 20 is: {result}"
)  # Outputs: The result of adding 10 and 20 is: 30

# Type annotations for variables (Python 3.6+)
# You can also annotate the types of variables.
age: int = 25
name: str = "Alice"

print(f"Name: {name}, Age: {age}")  # Outputs: Name: Alice, Age: 25

# Note: Type annotations improve code clarity and help tools like linters and IDEs provide better support.
