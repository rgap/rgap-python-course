# Example: Using filter to get even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")


# Example: Using filter with a named function to filter positive numbers
def is_positive(x):
    return x > 0

numbers = [-5, 3, -1, 101, 0]
positive_numbers = list(filter(is_positive, numbers))
print(f"Positive numbers: {positive_numbers}")
