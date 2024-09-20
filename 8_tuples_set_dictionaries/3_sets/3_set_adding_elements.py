# Adding Elements to a Set

fruits_set = {"apple", "banana"}

# Adding a single element using add()
fruits_set.add("cherry")
print(f"Set after adding 'cherry': {fruits_set}")  # Outputs: Set after adding 'cherry': {'apple', 'banana', 'cherry'}

# Adding multiple elements using update()
fruits_set.update(["orange", "grape"])
print(f"Set after adding multiple elements: {fruits_set}")  # Outputs: Set after adding multiple elements: {'apple', 'banana', 'cherry', 'orange', 'grape'}

# Note: The add() method adds a single element to the set.
# The update() method adds multiple elements from a list, tuple, or another set.
