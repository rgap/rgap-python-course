# Python Version: Finding elements in lists has been supported since Python 1.0 (January 1994).

# Finding Elements in an Array (List)
# Python provides methods to search for elements within a list.

# Example list
animals = ["dog", "cat", "bird", "fish"]

# Checking if an element exists using 'in'
is_dog_present = "dog" in animals
print(f"Is 'dog' present: {is_dog_present}")  # Outputs: Is 'dog' present: True

# Finding the index of an element using index()
cat_index = animals.index("cat")
print(f"Index of 'cat': {cat_index}")  # Outputs: Index of 'cat': 1

# Finding the count of an element using count()
fish_count = animals.count("fish")
print(f"Count of 'fish': {fish_count}")  # Outputs: Count of 'fish': 1

# Note: The 'in' keyword is used to check for the existence of an element in a list.
# The index() method returns the index of the first occurrence of a value.
# The count() method returns the number of occurrences of a value in the list.
