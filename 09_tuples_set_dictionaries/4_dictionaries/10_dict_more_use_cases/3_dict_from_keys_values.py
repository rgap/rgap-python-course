# Creating a Dictionary from Keys and Values

keys = ["name", "age", "salary"]
values = ["Alice", 31, 70000]

# Creating the dictionary using zip
person_dict = dict(zip(keys, values))
# Outputs: Dictionary from keys and values: {'name': 'Alice', 'age': 31,
# 'salary': 70000}
print(f"Dictionary from keys and values: {person_dict}")
