# Example: Filtering out None values from a list
mixed_list = [1, None, "hello", 0, None, 5]
filtered_list = list(filter(None, mixed_list))
print(f"List after removing None values: {filtered_list}")
