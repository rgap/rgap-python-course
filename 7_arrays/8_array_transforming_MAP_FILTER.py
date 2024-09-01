# Python Version: Transforming lists using map() and filter() has been supported since Python 2.0 (October 2000).

# Transforming Elements in an Array (List) with map() and filter()
# Python provides built-in functions like map() and filter() for transforming lists.
# These functions are part of Python's functional programming tools, allowing you to apply transformations
# or filtering operations over sequences like lists.

numbers = [1, 2, 3, 4, 5]

# 1. Using map() to apply a transformation to each element in the list
# The map() function takes two arguments: a function and an iterable (like a list).
# It applies the function to each element in the iterable, returning a map object (an iterator).

# In this example, we use map() to square each element of the list 'numbers'.
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")  # Outputs: Squared numbers: [1, 4, 9, 16, 25]

# Explanation:
# - `lambda x: x**2` is an anonymous function (lambda function) that takes one argument `x` and returns its square.
# - `map(lambda x: x**2, numbers)` applies this function to each element in `numbers`.
# - The result is a map object, which we convert to a list using `list()`.

# 2. Using filter() to select elements based on a condition
# The filter() function also takes two arguments: a function and an iterable.
# It applies the function to each element in the iterable and returns a filter object (an iterator) containing only the elements for which the function returns True.

# In this example, we use filter() to get only the even numbers from the list 'numbers'.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Outputs: Even numbers: [2, 4]

# Explanation:
# - `lambda x: x % 2 == 0` is a lambda function that returns True if `x` is even, False otherwise.
# - `filter(lambda x: x % 2 == 0, numbers)` applies this function to each element in `numbers`.
# - The result is a filter object, which we convert to a list using `list()`.

# 3. Combining map() and filter() for more complex transformations
# Sometimes, you might need to perform both filtering and transformation operations on a list.
# You can combine map() and filter() to first filter the elements and then transform the filtered results.

# For example, let's first filter out even numbers and then square the remaining odd numbers.
odd_squared_numbers = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))
print(f"Odd squared numbers: {odd_squared_numbers}")  # Outputs: Odd squared numbers: [1, 9, 25]

# Explanation:
# - `filter(lambda x: x % 2 != 0, numbers)` filters out the odd numbers from `numbers`.
# - `map(lambda x: x**2, ...)` then squares the filtered odd numbers.
# - The combined result is a list of squared odd numbers.

# 4. Using list comprehensions as an alternative to map() and filter()
# Python list comprehensions provide a more Pythonic and often more readable way to achieve the same results
# as map() and filter(), particularly when both filtering and transforming elements.

# Example using list comprehension to achieve the same result as the combined map() and filter() example above.
odd_squared_numbers_lc = [x**2 for x in numbers if x % 2 != 0]
print(f"Odd squared numbers (list comprehension): {odd_squared_numbers_lc}")  # Outputs: Odd squared numbers (list comprehension): [1, 9, 25]

# Explanation:
# - `[x**2 for x in numbers if x % 2 != 0]` iterates over `numbers`, filters out the odd numbers,
#   and squares them, all within a single, readable line.
