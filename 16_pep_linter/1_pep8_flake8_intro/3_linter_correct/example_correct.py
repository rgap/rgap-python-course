# This script corrects the formatting issues from code_formatting_incorrect.py
# by following PEP 8 guidelines, including proper line length and spacing.

def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    pi = 3.14159
    return pi * radius ** 2


def describe_circle(radius):
    """Return a description of a circle."""
    area = calculate_area(radius)
    return f"A circle with radius {radius} has an area of {area:.2f}."
