# Python Version: Adding elements to lists has been supported since Python 1.0 (January 1994).

# Adding Elements to an Array (List)
# Python provides several ways to add elements to a list.

# Example list
numbers = [1, 2, 3]

# Adding an element at the end using append()
numbers.append(4)
print(f"After append: {numbers}")  # Outputs: After append: [1, 2, 3, 4]

# Adding multiple elements at the end using extend()
numbers.extend([5, 6])
print(f"After extend: {numbers}")  # Outputs: After extend: [1, 2, 3, 4, 5, 6]

# Adding an element at a specific index using insert()
numbers.insert(2, "two-and-a-half")
print(
    f"After insert: {numbers}"
)  # Outputs: After insert: [1, 2, 'two-and-a-half', 3, 4, 5, 6]

# Note: The append() method adds a single element to the end of the list.
# The extend() method adds multiple elements to the end of the list.
# The insert() method allows you to add an element at a specific index.
