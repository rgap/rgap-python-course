# Python Version: Checking for inclusion in lists has been supported since Python 1.0 (January 1994).

# Checking Inclusion in Arrays (Lists)
# Python provides the 'in' keyword to check if a list contains an element.

# Example list
fruits = ["apple", "banana", "cherry"]

# Checking if an element exists using 'in'
is_apple_present = "apple" in fruits
print(f"Is 'apple' present: {is_apple_present}")  # Outputs: Is 'apple' present: True

# Checking if an element does not exist using 'not in'
is_mango_present = "mango" not in fruits
print(
    f"Is 'mango' not present: {is_mango_present}"
)  # Outputs: Is 'mango' not present: True

# Note: The 'in' keyword is a simple and efficient way to check for the existence of an element in a list.
# It returns True if the element is found, otherwise False.
