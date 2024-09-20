# Merging Two Dictionaries

dict_a = {"name": "Alice", "age": 31}
dict_b = {"profession": "Engineer", "salary": 70000}

# Merging two dictionaries (Python 3.9+)
merged_dict = dict_a | dict_b
# Outputs: Merged dictionary: {'name': 'Alice', 'age': 31, 'profession':
# 'Engineer', 'salary': 70000}
print(f"Merged dictionary: {merged_dict}")
