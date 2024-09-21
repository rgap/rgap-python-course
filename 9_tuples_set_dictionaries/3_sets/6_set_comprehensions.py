# Set Comprehensions

# Creating a set of squares
squares_set = {x ** 2 for x in range(6)}
print(f"Squares set: {squares_set}")  # Outputs: Squares set: {0, 1, 4, 9, 16, 25}

# Creating a set of unique characters
unique_chars_set = {char for char in "hello world"}
print(f"Unique characters set: {unique_chars_set}")  # Outputs: Unique characters set: {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

# Note: Set comprehensions provide a concise way to create sets, similar to list comprehensions.
