# Python Enhancement Proposal (PEP): PEP 8 (2001) introduced conventions for naming constants.

# Constants are variables that should not change once set.
# Python does not have a true constant type, but naming conventions can be used to indicate that a variable should be treated as a constant.

# Example of a constant
PI = 3.14159  # By convention, constants are written in uppercase letters.


def calculate_circumference(radius):
    return 2 * PI * radius


circumference = calculate_circumference(5)
print(
    f"The circumference of a circle with radius 5 is: {circumference}"
)  # Outputs: The circumference of a circle with radius 5 is: 31.4159

# Note: Python allows you to modify 'constants', but doing so goes against convention and should be avoided.
