# Copying a Dictionary with copy()

person = {"name": "Alice", "age": 31, "city": "New York"}

# First, let's assign the original dictionary to a new variable without using copy()
person_copy = person

# At this point, both 'person' and 'person_copy' reference the same dictionary object in memory.
# Modifying one will affect the other because they are not independent of each other.

# Let's modify 'person_copy'
person_copy["age"] = 32

# Now, let's check both dictionaries
print(f"Original dictionary after modification: {person}")  # Outputs: Original dictionary after modification: {'name': 'Alice', 'age': 32, 'city': 'New York'}
print(f"Modified 'person_copy' dictionary: {person_copy}")  # Outputs: Modified 'person_copy' dictionary: {'name': 'Alice', 'age': 32, 'city': 'New York'}

# Notice that both 'person' and 'person_copy' have been modified.
# This is because they both point to the same dictionary object.

# Now, let's see how using the copy() method prevents this issue.

# Reset the 'person' dictionary
person = {"name": "Alice", "age": 31, "city": "New York"}

# Create a true copy of the dictionary using the copy() method
person_copy = person.copy()

# With copy(), 'person_copy' now references a different dictionary object.
# Modifying 'person_copy' will not affect the original 'person' dictionary.

# Modify the copied dictionary
person_copy["age"] = 32

# Check both dictionaries again
print(f"Original dictionary after using copy(): {person}")  # Outputs: Original dictionary after using copy(): {'name': 'Alice', 'age': 31, 'city': 'New York'}
print(f"Copied and modified dictionary: {person_copy}")  # Outputs: Copied and modified dictionary: {'name': 'Alice', 'age': 32, 'city': 'New York'}

# Now, the original dictionary remains unchanged because 'person_copy' is an independent copy.
