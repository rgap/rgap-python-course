# Python Version: List comprehensions were introduced in Python 2.0 (October 2000).

# List comprehension is a concise way to create lists. 
# It allows you to generate a new list by applying an expression to each item in an existing list or iterable.

# Creating a list of numbers from 1 to 10
numbers = list(range(1, 11))
print(f"Original numbers: {numbers}")  # Outputs: Original numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creating a list of squares using list comprehension
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")  # Outputs: Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

##################################

# Example 1: Filtering Even Numbers

# This list comprehension creates a new list containing only the even numbers from the original list.

# The order is:
# 1. `for x in numbers`: Iterates over each number in the list `numbers`.
# 2. `if x % 2 == 0`: Checks if the current number `x` is even.
# 3. `x`: Includes the number `x` in the new list `evens` if the condition is True.
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")  # Outputs: Evens: [2, 4, 6, 8, 10]


# Example 2: Filtering Even Numbers with Explicit Variable

# This list comprehension creates a new list of even numbers.

# The order is:
# 1. `for number in numbers`: Iterates over each number in the list `numbers`.
# 2. `if number % 2 == 0`: Checks if the current number `number` is even.
# 3. `number`: Includes the number `number` in the new list `evens` if the condition is True.
evens = [number for number in numbers if number % 2 == 0]
print(f"Evens: {evens}")  # Outputs: Evens: [2, 4, 6, 8, 10]



##################################

# New Examples with if and else inside list comprehensions

# Example 3: Creating a list of even and odd labels

# This list comprehension creates a new list where even numbers are labeled 'Even' 
# and odd numbers are labeled 'Odd'.

# The order is:
# 1. for x in numbers: Iterates over each number in the list numbers.
# 2. if x % 2 == 0: Checks if the current number x is even.
# 3. 'Even' if the condition is True, otherwise 'Odd': Includes the appropriate label in the new list.
labels = ['Even' if x % 2 == 0 else 'Odd' for x in numbers]
print(f"Labels: {labels}")  # Outputs: Labels: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

# Example 4: Doubling Even Numbers, Halving Odd Numbers

# This list comprehension creates a new list where even numbers are doubled,
# and odd numbers are halved.

# The order is:
# 1. for x in numbers: Iterates over each number in the list numbers.
# 2. if x % 2 == 0: Checks if the current number x is even.
# 3. x * 2 if the condition is True, otherwise x / 2: Performs the appropriate operation on x and includes it in the new list.
modified_numbers = [x * 2 if x % 2 == 0 else x / 2 for x in numbers]
print(f"Modified numbers: {modified_numbers}")  # Outputs: Modified numbers: [0.5, 4, 1.5, 8, 2.5, 12, 3.5, 16, 4.5, 20]

# Example 5: Categorizing Numbers

# This list comprehension creates a new list that categorizes numbers into 'Small', 'Medium', or 'Large'.

# The order is:
# 1. for x in numbers: Iterates over each number in the list numbers.
# 2. if x <= 3: Checks if the current number x is less than or equal to 3.
# 3. if x <= 7: Checks if the current number x is less than or equal to 7.
# 4. 'Small', 'Medium', or 'Large': Includes the appropriate label in the new list.
categories = ['Small' if x <= 3 else 'Medium' if x <= 7 else 'Large' for x in numbers]
print(f"Categories: {categories}")  # Outputs: Categories: ['Small', 'Small', 'Small', 'Medium', 'Medium', 'Medium', 'Medium', 'Large', 'Large', 'Large']
