# Match Statement in Python
# Python Version: The match statement was introduced in Python 3.10 (October 2021).

# The match statement provides pattern matching, allowing more readable control over complex conditions.

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

# Example usage of match
print(http_status(200))  # Outputs: OK
print(http_status(404))  # Outputs: Not Found
print(http_status(999))  # Outputs: Unknown Status

# Match with complex patterns
def describe_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On the X axis at {x}"
        case (0, y):
            return f"On the Y axis at {y}"
        case (x, y) if x == y:
            return "On the line y = x"
        case _:
            return "Somewhere else"

# Example usage of matching tuples
print(describe_point((0, 0)))  # Outputs: Origin
print(describe_point((3, 0)))  # Outputs: On the X axis at 3
print(describe_point((2, 2)))  # Outputs: On the line y = x

# Note: The match statement allows for more expressive pattern matching, 
# making it ideal for handling complex conditions, such as data structures or enums.
