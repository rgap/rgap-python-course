# Impure functions may produce different results even with the same inputs
# and can modify external state or produce side effects.

# Classic Random Example
# The use of random number generation is a common example of an impure function,
# because it produces different outputs for the same input.

import random


def generate_random_number():
    # This function generates a random number between 1 and 10.
    # The output varies each time it is called, making it an impure function.
    return random.randint(1, 10)


# Call the function multiple times
random_result_1 = generate_random_number()
random_result_2 = generate_random_number()

# The outputs will likely be different, demonstrating the impurity of the
# function.
print(f"Random Number 1: {random_result_1}")
print(f"Random Number 2: {random_result_2}")
