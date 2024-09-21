# This block of code calculates the factorial of a given number.
# The factorial is the product of all positive integers less than or equal to the number.


def factorial(n):
    if n == 0:
        return 1  # The factorial of 0 is defined as 1
    else:
        return n * factorial(n - 1)  # Recursive call to calculate the factorial


# Print the factorial of 5, which should be 120
print(factorial(5))
