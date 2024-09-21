# Removing Elements from a Set

fruits_set = {"apple", "banana", "cherry", "date"}

# Removing an element using remove()
fruits_set.remove("banana")
print(f"Set after removing 'banana': {fruits_set}")  # Outputs: Set after removing 'banana': {'apple', 'cherry', 'date'}

# Removing an element using discard() (no error if the element doesn't exist)
fruits_set.discard("grape")
print(f"Set after discarding 'grape': {fruits_set}")  # Outputs: Set after discarding 'grape': {'apple', 'cherry', 'date'}

# Removing and returning the last element using pop()
last_fruit = fruits_set.pop()
print(f"Set after popping an element: {fruits_set}, Popped element: {last_fruit}")  # Outputs: Set after popping an element: {...}, Popped element: {...}

# Clearing all elements from the set using clear()
fruits_set.clear()
print(f"Set after clearing: {fruits_set}")  # Outputs: Set after clearing: set()

# Note: The remove() method raises an error if the element is not found.
# The discard() method does not raise an error if the element is not found.
# The pop() method removes and returns an arbitrary element from the set.
# The clear() method removes all elements from the set.
