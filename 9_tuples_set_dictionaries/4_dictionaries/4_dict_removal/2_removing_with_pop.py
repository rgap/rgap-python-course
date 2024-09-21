# Removing a Key-Value Pair with pop()

person = {"name": "Alice", "age": 31, "city": "New York"}

# Removing a key-value pair using pop()
city = person.pop("city")
print(f"Updated dictionary: {person}")  # Outputs: Updated dictionary: {'name': 'Alice', 'age': 31}
print(f"Removed city: {city}")  # Outputs: Removed city: New York
