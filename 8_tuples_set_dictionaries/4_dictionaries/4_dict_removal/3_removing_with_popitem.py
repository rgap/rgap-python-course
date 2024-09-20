# Removing the Last Inserted Key-Value Pair with popitem()

person = {"name": "Alice", "age": 31, "city": "New York"}

# Removing the last inserted key-value pair using popitem()
last_item = person.popitem()
print(f"Updated dictionary: {person}")  # Outputs: Updated dictionary: {'name': 'Alice', 'age': 31}
print(f"Removed item: {last_item}")  # Outputs: Removed item: ('city', 'New York')
