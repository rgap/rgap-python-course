# Dictionary Comprehension with Conditions

person = {"name": "Alice", "age": 31, "city": "New York"}

# Creating a new dictionary by filtering items
filtered_dict = {k: v for k, v in person.items() if k != "city"}
print(f"Filtered dictionary: {filtered_dict}")  # Outputs: Filtered dictionary: {'name': 'Alice', 'age': 31}
