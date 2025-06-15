# Example 1: Multiple for Loops in List Comprehension

# This list comprehension creates a list of tuples representing pairs (x, y)
# where x is from the first list and y is from the second list.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# The order is:
# 1. for x in list1: Iterates over each item in list1.
# 2. for y in list2: Iterates over each item in list2 for every item in list1.
# 3. (x, y): Includes the tuple (x, y) in the new list.
pairs = [(x, y) for x in list1 for y in list2]
print(f"Pairs: {pairs}")  # Outputs: Pairs: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]


# Example 2: Multiple for Loops with Conditions

# This list comprehension creates a list of tuples representing pairs (x, y)
# where x is even, and y is a vowel.

list1 = [1, 2, 3, 4]
list2 = ['a', 'e', 'i', 'o', 'u']

# The order is:
# 1. for x in list1: Iterates over each item in list1.
# 2. if x % 2 == 0: Checks if x is even.
# 3. for y in list2: Iterates over each item in list2 if x is even.
# 4. (x, y): Includes the tuple (x, y) in the new list.
pairs = [(x, y) for x in list1 if x % 2 == 0 for y in list2]
print(f"Pairs: {pairs}")  # Outputs: Pairs: [(2, 'a'), (2, 'e'), (2, 'i'), (2, 'o'), (2, 'u'), (4, 'a'), (4, 'e'), (4, 'i'), (4, 'o'), (4, 'u')]
