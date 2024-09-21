# The `for` loop is used to iterate over an iterable (such as a list, tuple, string, dictionary, or set).
# It allows you to execute a block of code multiple times, once for each item in the iterable.
# Syntax:
#     for <variable> in <iterable>:
#         <code to execute>
# The loop will stop after the last item in the iterable has been processed.

# Example 1: Processing a list of prices and applying a discount to each
prices = [100, 200, 300, 400]
discounted_prices = []
for price in prices:
    discounted_price = price * 0.9  # Apply 10% discount
    discounted_prices.append(discounted_price)
print("Discounted Prices:", discounted_prices)


###############################################


# Example 2: Collecting valid ages from a list (age must be >= 18)
ages = [15, 22, 17, 19, 34]
valid_ages = []
for age in ages:
    if age >= 18:
        valid_ages.append(age)
print("Valid Ages:", valid_ages)
