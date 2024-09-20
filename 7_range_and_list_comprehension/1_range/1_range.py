# Python Version: The range() function was introduced in Python 1.0 (January 1994).
# It was modified in Python 3.0 (December 2008) to behave like the
# xrange() from Python 2.

# Introduction to range() in Python
# ---------------------------------
# The range() function in Python is a built-in function that generates a sequence of numbers.
# In earlier versions of Python (2.x), there were two functions: range() and xrange().
# - range() would generate a list of numbers all at once in memory.
# - xrange() would generate numbers one at a time as needed, without storing the entire sequence in memory.

# Starting from Python 3.0, the range() function was updated to combine the benefits of both:
# - It now behaves like the old xrange() by generating numbers on demand.
# - This makes it much more memory-efficient, especially for large sequences.

# The range() function returns an immutable sequence type called a "range object."
# This range object behaves like a sequence (similar to lists or tuples) but does not actually create a list of numbers.
# Instead, it generates each number on-the-fly as you iterate over it,
# which saves memory.

# Characteristics of the range object:
# - Immutable: Once created, the sequence cannot be modified.
# - Efficient: Generates numbers only when needed, making it suitable for large ranges.
# - Indexable: You can access elements in the range using indexing, just like with lists.
# - Supports slicing: You can slice the range to create a new range object with a subset of the original sequence.

# The range() function is commonly used in for-loops to iterate over a
# sequence of numbers.

# Example 1: Using range() to generate a sequence of numbers from 0 to 4
sequence = range(5)
# Outputs: Sequence from 0 to 4: [0, 1, 2, 3, 4]
print(f"Sequence from 0 to 4: {list(sequence)}")

# Example 2: Using range() with a start and stop parameter
# Generates a sequence from 1 to 5 (the stop value is not included)
sequence = range(1, 6)
# Outputs: Sequence from 1 to 5: [1, 2, 3, 4, 5]
print(f"Sequence from 1 to 5: {list(sequence)}")

# Example 3: Using range() with a step parameter
# Generates a sequence from 0 to 10 with a step of 2
sequence = range(0, 11, 2)
# Outputs: Sequence from 0 to 10 with a step of 2: [0, 2, 4, 6, 8, 10]
print(f"Sequence from 0 to 10 with a step of 2: {list(sequence)}")

# Example 4: Using a negative step parameter to generate a sequence in reverse
# Generates a sequence from 10 down to 1
sequence = range(10, 0, -1)
# Outputs: Sequence from 10 to 1: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Sequence from 10 to 1: {list(sequence)}")

# Example 5: Looping through a range in a for-loop
# Print each number from 0 to 4
for i in range(5):
    print(f"Number: {i}")
# Outputs:
# Number: 0
# Number: 1
# Number: 2
# Number: 3
# Number: 4

# Note: range() in Python 3 does not create a list in memory, but an immutable sequence type,
# which means it is memory-efficient even for large ranges.

# Example 6: Converting a range to a list explicitly
# Generates a list of numbers from 1 to 10
numbers_list = list(range(1, 11))
# Outputs: List of numbers from 1 to 10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List of numbers from 1 to 10: {numbers_list}")

# Summary:
# - range() in Python 3.x is a powerful and memory-efficient way to generate sequences of numbers.
# - It behaves similarly to the old xrange() from Python 2.x, but with the additional benefits of a more unified and consistent interface.
# - It is commonly used in loops and is especially useful when working with large sequences of numbers.
