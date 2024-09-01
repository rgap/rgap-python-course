# This script corrects the naming convention issues from naming_conventions_incorrect.py
# by using descriptive, consistent names that follow PEP 8 guidelines.

user_name = "Alice"
user_age = 30


def get_user_info(name, age):
    """Return a formatted string with user information."""
    return f"{name} is {age} years old."


class UserProfile:
    def __init__(self, name, age):
        self.name = name
        self.age = age
