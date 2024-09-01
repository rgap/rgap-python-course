# This script demonstrates improper code formatting, violating PEP 8 guidelines.
# Issues include lines exceeding 79 characters and improper spacing around operators.
# It will show erros with the format: E501 line too long (80 > 79 characters)

def CalculateArea(Radius):return 3.14159 * Radius**2

def DescribeCircle(Radius):
    Area=CalculateArea(Radius)
    # This line exceeds 79 characters, which is against PEP 8 guidelines.
    return f"A circle with radius {Radius} has an area of {Area:.2f}. Circles are interesting shapes due to their symmetry."
