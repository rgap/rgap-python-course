# Python Version: Removing elements from lists has been supported since Python 1.0 (January 1994).

# Removing Elements from an Array (List)
# Python provides several ways to remove elements from a list.

# Example list
fruits = ["apple", "banana", "cherry", "date"]

# Removing an element by value using remove()
fruits.remove("banana")
print(f"After remove: {fruits}")  # Outputs: After remove: ['apple', 'cherry', 'date']

# Removing an element by index using pop()
popped_fruit = fruits.pop(1)
print(
    f"After pop: {fruits}, Popped fruit: {popped_fruit}"
)  # Outputs: After pop: ['apple', 'date'], Popped fruit: cherry

# Removing the last element using pop() without an index
last_fruit = fruits.pop()
print(
    f"After pop without index: {fruits}, Last fruit: {last_fruit}"
)  # Outputs: After pop without index: ['apple'], Last fruit: date

# Clearing all elements from the list using clear()
fruits.clear()
print(f"After clear: {fruits}")  # Outputs: After clear: []

# Note: The remove() method removes the first occurrence of a value.
# The pop() method removes and returns the element at the specified index, or the last element if no index is provided.
# The clear() method removes all elements from the list.
