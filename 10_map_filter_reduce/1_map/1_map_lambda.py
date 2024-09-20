# Example: Using map to add 1 to each element in a list
numbers = [1, 2, 3, 4, 5]
add_one = list(map(lambda x: x + 1, numbers))
print(f"Adding 1 to each element: {add_one}")


# Example: Using map with a named function to square each element in a list
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(f"Squaring each element: {squared_numbers}")
